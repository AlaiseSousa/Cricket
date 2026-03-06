# Copyright (c) 2026, . and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Lote(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		alimento: DF.Link
		data_entradacriação: DF.Date | None
		data_validade: DF.Date | None
		naming_series: DF.Literal["L-"]
		quantidade: DF.Data
	# end: auto-generated types

	pass
