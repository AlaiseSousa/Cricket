from frappe.model.document import Document
import frappe

class Fornecedor(Document):

    def validate(self):
        # Bloquear NIF duplicado
        if self.nif:
            existing = frappe.db.exists("Fornecedor", {"nif": self.nif})
            if existing and existing != self.name:
                frappe.throw(f"NIF {self.nif} já existe para outro fornecedor!")

        # Bloquear alteração do NIF após criação
        if not self.get("__islocal"):
            original = frappe.get_doc("Fornecedor", self.name)
            if self.nif != original.nif:
                frappe.throw("NIF não pode ser alterado após criação.")