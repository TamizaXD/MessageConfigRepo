import frappe
from twilio.rest import Client 


def send_sms(to, body):
    twilio_setting = frappe.get_doc('Twilio Setting', 'TS-09')

    account_sid = twilio_setting.account_sid
    auth_token = twilio_setting.auth_token
    from_number = twilio_setting.from_phone_number

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = body,
        from_ = from_number,
        to = to
    )

    # frappe.msgprint(f"Message SID: {message.sid}")

    return message.sid
