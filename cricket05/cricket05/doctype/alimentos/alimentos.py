import frappe
import frappe.model.document

class Alimentos(frappe.model.document.Document):
    def validate(self):
        # Bloquear nomes duplicados
        if self.nome:
            existing = frappe.get_all("Alimentos", filters={"nome": self.nome}, limit=1)
            if existing and (not self.name or existing[0].name != self.name):
                frappe.throw(f"O alimento '{self.nome}' já existe!")

        # Validar unidade de medida
        unidades_validas = ["kg", "g", "L", "mL", "unidade"]
        if self.unidade_de_medida not in unidades_validas:
            frappe.throw(f"Unidade inválida. Escolha: {', '.join(unidades_validas)}")

        # Validar alteração de unidade se existirem lotes
        old_doc = self.get_doc_before_save()
        if old_doc and old_doc.unidade_de_medida != self.unidade_de_medida:
            if frappe.db.exists("Lote", {"alimento": self.name}):
                frappe.throw(
                    "Este alimento já possui lotes associados. "
                    "Não é possível alterar a unidade de medida."
                )

    def before_trash(self):
        # Bloqueia exclusão e sugere inativação
        if frappe.db.exists("Lote", {"alimento": self.name}):
            frappe.throw(
                f"Não é possível eliminar o alimento '{self.nome}' porque possui lotes associados. "
                "Deseja inativá-lo em vez de eliminar?"
            )