# Copyright (c) 2026, . and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Alimentos(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		descrição: DF.SmallText | None
		nome: DF.Data
		observações: DF.Text | None
		tipo_de_matéria_prima: DF.Data | None
		unidade_de_medida: DF.Literal["kg", "g", "L", "mL", "unidade"]
	# end: auto-generated types

	pass
