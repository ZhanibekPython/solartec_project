import logging
from whatsapp_chatbot_python import GreenAPIBot, Notification
from whatsapp_chatbot_python.filters import TEXT_TYPES
from log_config import my_logger
from config import (
    USER_ID, 
    API_TOKEN, 
    LANGUAGE_TO_CHOOSE, 
    WELCOME_MESSAGE, 
    States
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


@bot.router.message(type_message=TEXT_TYPES, state=States.INITIAL)
def language_choose_handler(notification: Notification) -> None:
    """Starting handler for newcomers"""
    
    state = notification.sender
    notification.state_manager.update_state(state)

    notification.answer(LANGUAGE_TO_CHOOSE)


@bot.router.message(type_message=TEXT_TYPES, regexp=r"^\s*[1-3]\s*$", state=States.MENU)
def services_handler(notification: Notification) -> None:
    """This handler sends a welcome message to the newcomer in the language he/she has chosen"""
    try:
        chosen_language = notification.message_text.strip()
        if isinstance(chosen_language, int) and 1<= chosen_language <=3:
            state = notification.sender
            notification.state_manager.update_state(state)

            notification.answer(WELCOME_MESSAGE[int(chosen_language)])
        else:
            notification.answer("Entered symbol is incorrect. Please try again")
    except KeyError:
        notification.answer("Entered symbol is incorrect. Please try again", link_preview=False)
        

@bot.router.message(command="menu")
def menu_page_handler(notification=Notification):
    """This handler returns menu page if sender tyoes in 'menu'"""

    sender = notification.sender

    state = notification.state_manager.get_state(sender=sender)

    if not state:
        return services_handler(notification)
    else:
        notification.state_manager.delete_state(sender=sender)


@bot.router.message(text_message=[])

bot.run_forever()
