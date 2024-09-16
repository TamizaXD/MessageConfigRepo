import frappe, time
from rentals.methods.message_log import add_to_message_log_dt, add_to_frappe
from rentals.classes.message_service_config import  WhatsappServiceConfig, SmsServiceConfig
from rentals.methods.get_doc_name import get_customer
from rentals.methods.clean_number import remove_non_numeric

def add_to_message_dt(name, sender, message, message_time, message_service_type, message_type, message_status, base64):

    message_dt = frappe.get_doc({
        'doctype': 'Message',
        'sender': sender,
        'message': message,
        'timestamp': message_time,
        'message_service_type': message_service_type,                               
        'message_type': message_type,
        'status': message_status,
        'base64': base64
    })
    add_to_frappe(message_dt)

    getReceiverPhoneNumber = remove_non_numeric(get_customer(name).receiver_phone_number) 
    getSenderPhoneNumber = remove_non_numeric(get_customer(name).phone_number) #change it to the sender instead
    # time.sleep(10)

    if message_type == 'SMS':
        orgName = get_customer(name).organization
        userName = get_customer(name).provider_name
        # password = get_customer(name).password        
        sms = SmsServiceConfig(name, orgName=orgName, userName=userName, password='FinTechaSys@1777789' , code=2)
        message_status =  sms.send_message(getReceiverPhoneNumber, message)

    else:
        wam = WhatsappServiceConfig(name, isGroup = False, isNewsletter = False, base64 = base64)
        message_status = wam.send_message(getReceiverPhoneNumber, message)

    update_message_status(message_dt.name, message_status)
    add_to_message_log_dt(getSenderPhoneNumber, getReceiverPhoneNumber, frappe.utils.now(), message, message_status, message_dt.name, base64)

def update_message_status(name, status):
    frappe.db.set_value('Message', f'{name}','status', f'{status}')
    frappe.db.commit()