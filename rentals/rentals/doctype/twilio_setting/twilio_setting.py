# Copyright (c) 2024, MN and contributors
# For license information, please see license.txt

# import frappe
from rentals.twilio_integration import send_sms
from frappe.model.document import Document


class TwilioSetting(Document):
	def before_save(self):
		# pass
		send_sms('+967770871484', "you did it again!")

