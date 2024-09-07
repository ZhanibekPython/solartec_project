from whatsapp_chatbot_python import BaseStates

USER_ID = "7103112435"
API_TOKEN = "b9484b0671734f49bd3eb6568eecbda3bad279ce0b2f4bdbbf"

class States(BaseStates):
    INITIAL = "INITIAL"
    MENU = "MENU"
    SERVICE = "SERVICE"
    TOUCHDONW = "TOUCHDOWN"
    ADDITIONAL = "ADDITIONAL"