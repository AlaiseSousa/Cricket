import frappe
from frappe.model.document import Document

class Alimentos(Document):
    def validate(self):
        # Bloquear nomes duplicados
        if self.nome:
            existing = frappe.get_all("Alimentos", filters={"nome": self.nome}, limit=1)
            if existing:
                if not self.name or existing[0].name != self.name:
                    frappe.throw(f"O alimento '{self.nome}' já existe!")

        # Validar unidade de medida
        unidades_validas = ["kg", "g", "L", "mL", "unidade"]
        if self.unidade_de_medida not in unidades_validas:
            frappe.throw(f"Unidade inválida. Escolha: {', '.join(unidades_validas)}")