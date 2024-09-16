import requests
import urllib.parse
from rentals.interfaces.message_service import MessageService
from rentals.methods.get_doc_name import get_customer, get_wppconnect_url
from rentals.data.wep_status_code import STATUS_CODE_MAP

class WhatsappServiceConfig(MessageService):
    def __init__(self, name, isGroup, isNewsletter, base64):

        self.name = name
        self.message_service_doc = get_customer(self.name)

        customer = self.message_service_doc

        self.isGroup = isGroup
        self.isNewsletter = isNewsletter
        self.base64 = base64
        # base64 Prefix = data:image/jpeg;base64,

        wppconnect_url = get_wppconnect_url()
        self.baseUrl = urllib.parse.urljoin(wppconnect_url, customer.session)
                                         # http://192.168.88.30:21444/api/m_noman
        self.status = 'Failed'

        self.headers = { 
            "Authorization": f"Bearer {customer.auth_token_wam}",
            "Content-Type": "application/json; charset=utf-8",
        }

    def send_message(self, phone_number, message_body):
        url = f"{self.baseUrl}/send-message"
        data = {
            "phone": phone_number,
            "isGroup": self.isGroup,
            "isNewsletter": self.isNewsletter,
            "message": message_body
        }
        if self.base64:
            url = f"{self.baseUrl}/send-image"
            data.update({"base64": self.base64})

        response = requests.post(url, json=data, headers=self.headers)
        self.status = STATUS_CODE_MAP.get(response.status_code, 'Failed')
        return self.status

class SmsServiceConfig(MessageService):
    def __init__(self, name, orgName, userName, password, code):

        self.name = name
        # self.message_service_doc = get_customer(self.name)
        self.orgName = orgName
        self.userName = userName
        self.password = password
        self.code = code

    def send_message(self, phone_number, message_body):
        url = 'https://sms.alawaeltec.com/MainServlet'
        data = {
           "orgName" : self.orgName,
           "userName" :  self.userName,
           "password" :  self.password,
           "mobileNo":  phone_number, 
           "text":  message_body,
           "coding":  self.code
        }
        response = requests.get(url, params=data)
        status = STATUS_CODE_MAP.get(response.status_code, 'Failed')
        return status