from rentals.methods.get_doc_name import get_customer
from rentals.classes.message_service_config import WhatsappServiceConfig, SmsServiceConfig 

class MessageFactory:
    @staticmethod
    def get_service(name, message, **kwargs):
        
        customer = get_customer(name)
        service_type = customer.service_type  
        
        if service_type == "Whatsapp":
            return WhatsappServiceConfig(name, message, kwargs.get("isGroup"),kwargs.get("isNewsletter"),kwargs.get("base64"))
        
        elif service_type == "SMS":
            return SmsServiceConfig(name, message, kwargs.get("orgName"),kwargs.get("userName"),kwargs.get("password"),kwargs.get("code"))
        else:
            raise ValueError("Invalid service type")