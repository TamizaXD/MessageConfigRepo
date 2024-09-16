import frappe 
from rentals.methods.get_doc_name import get_customer

@frappe.whitelist(allow_guest=False)
def send_message(name, message, base64 = None):
    
    getSender = get_customer(name).customer_detail
    getMessageServiceType = get_customer(name).service_type
    getMessageService =  get_customer(name).service_type
    method = 'rentals.methods.add_to_message.add_to_message_dt'

    print("TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    frappe.enqueue(method,    
                #    now = True,  # sending images thruogh whatsapp only works if this is True
                   name = name,
                   sender = getSender,
                   message = message,
                   message_time = frappe.utils.now(), 
                   message_service_type = getMessageServiceType, 
                   message_type = getMessageService,
                   message_status = 'Pending',
                   base64 = base64
                )
    return { 
        "status": "Message queued for sending",
        "Sender": getSender,
        "Message": message,
        "Message Service Type": getMessageServiceType
    }
# http://127.0.0.1:8001/api/method/rentals.apis.api.send_message