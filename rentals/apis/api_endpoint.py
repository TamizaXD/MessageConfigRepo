from rentals.classes.message_factory import MessageFactory

def send_message(name, phone_number,message_body, **kwagrs):
    try:
        message_service = MessageFactory.get_service(name, message_body, **kwagrs)
        status = message_service.send_message(phone_number, message_body)
        return status
    
    except Exception as e:
        
        return {
            "Error: ": e
        }