from whatsapp_chatbot_python import GreenAPIBot, Notification
from whatsapp_chatbot_python.filters import TEXT_TYPES
from log_config import my_logger
from user_data import (
    USER_ID, 
    API_TOKEN,
    States
)
from config import (
    LANGUAGE_TO_CHOOSE, 
    WELCOME_MESSAGE,
    SERVICE_TO_CHOOSE, 
)

logger = my_logger()

bot = GreenAPIBot(
    USER_ID, 
    API_TOKEN, 
    settings={
        "delaySendMessagesMilliseconds": 500,
        "markIncomingMessagesReaded": "yes",
        "incomingWebhook": "yes",
        "keepOnlineStatus": "yes",
        "pollMessageWebhook": "yes",
    }
)

CHOSEN_LANGUAGE = None

@bot.router.message(type_message=TEXT_TYPES, state=None)
def language_choose_handler(notification: Notification) -> None:
    """Starting handler for newcomers"""
    
    sender = notification.sender
    notification.state_manager.set_state(sender=sender, state_name=States.INITIAL)
    notification.answer(LANGUAGE_TO_CHOOSE)


@bot.router.message(type_message=TEXT_TYPES, state=States.INITIAL)
def available_services_handler(notification: Notification) -> None:
    """This handler sends a welcome message to the newcomer in the language he/she has chosen"""
    
    try:
        chosen_language = int(notification.message_text.strip())
        if 1<= chosen_language <=3:

            global CHOSEN_LANGUAGE
            CHOSEN_LANGUAGE = chosen_language

            sender = notification.sender
            notification.state_manager.update_state(sender=sender, state_name=States.MENU)

            notification.answer(WELCOME_MESSAGE[chosen_language])
        else:
            notification.answer("Entered symbol is incorrect. Please try again")
    except KeyError:
        notification.answer("Please try again")
        

@bot.router.message(type_message=TEXT_TYPES, state=States.MENU)
def service_handler(notification: Notification) -> None:
    """This handler sends a list of services available at Solartec Co."""
    
    try:
        chosen_service = int(notification.message_text.strip())
        if 1<= chosen_service <=5:
            sender = notification.sender
            notification.state_manager.update_state(sender=sender, state_name=States.SERVICE)

            notification.answer(SERVICE_TO_CHOOSE[chosen_service])

        elif 6 <= chosen_service <=7:
            chat_id = notification.chat

            match chosen_service:
                case 6:
                    notification.api.sending.sendFileByUrl(
                        chatId=chat_id,
                        urlFile="https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/gs.png",
                        fileName="Golden State Warriors logo",
                        caption="This is the best team!"
                        )
                case 7:
                    notification.api.sending.sendLocation(
                        chatId=chat_id,
                        latitude=37.773972,
                        longitude=-122.431297,
                        nameLocation='San-Francisco'
                    )
        else:
            notification.answer("Entered symbol is incorrect. Please try again")
    except KeyError:
        notification.answer("Please try again")


@bot.router.message(type_message=TEXT_TYPES, state=States.SERVICE)
def service_data(notification: Notification) -> None:
    """This handler sends full information about chosen service"""

    try:
        service = int(notification.message_text.strip())     
        notification.answer(SERVICE_TO_CHOOSE.get(service).get(CHOSEN_LANGUAGE))
    except Exception:
        notification.answer("Entered value not a number")


bot.run_forever()
