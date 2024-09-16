# Copyright (c) 2024, MN and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Dirver1(Document):
	def before_save(self):
		self.full_name = f"{self.frist_name} {self.last_name}"
		frappe.msgprint("TEST!")