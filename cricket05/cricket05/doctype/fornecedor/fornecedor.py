# noqa: E402
# type: ignore
# ===============================================
# Fornecedor DocType - Pap / Projeto de Estágio
# ===============================================

import frappe

# VS Code / PyLance podem reclamar do import, por isso usamos esta forma segura
try:
    from frappe.model.document import Document
except ImportError:
    class Document:
        pass  # stub para o editor, não afeta runtime

class Fornecedor(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        email: DF.Data | None
        estado: DF.Literal["Ativo", "Inativo"]
        localidade: DF.Data | None
        morada: DF.Data | None
        nif: DF.Data
        nome: DF.Data
        telefone: DF.Phone | None
        website: DF.Data | None
    # end: auto-generated types

    """
    Classe do DocType Fornecedor
    - Valida NIF único
    - Bloqueia alteração do NIF após criação
    """

    def validate(self):
        # Bloquear NIF duplicado
        if self.nif:
            existing = frappe.db.exists("Fornecedor", {"nif": self.nif})
            if existing and existing != self.name:
                frappe.throw(f"NIF {self.nif} já existe para outro fornecedor!")

        # Bloquear alteração do NIF após criação
        if not self.is_new():
            original_nif = frappe.db.get_value("Fornecedor", self.name, "nif")
            if self.nif != original_nif:
                frappe.throw("NIF não pode ser alterado após criação.")