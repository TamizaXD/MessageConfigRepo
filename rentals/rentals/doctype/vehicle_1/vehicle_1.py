# Copyright (c) 2024, MN and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class Vehicle1(Document):
    # pass
	def before_save(self):
		self.title = f"{self.make} {self.model}, {self.year}"
