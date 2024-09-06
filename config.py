from whatsapp_chatbot_python import BaseStates

USER_ID = "7103111896"
API_TOKEN = "1389cf92b66145ddb55785f5b09dedfedb9083b5850940bea7"

class States(BaseStates):
    INITIAL = "INITIAL"
    MENU = "MENU"
    SERVICE = "SERVICE"


LANGUAGE_TO_CHOOSE = """Please choose the language for further communication\nby typing number [1-3]: \n1 - Қазақша,\n2 - Русский,\n3 - English"""

WELCOME_MESSAGE = {
    3: """Hello, welcome to Solartec!\nTo proceed to our services choose one of below by typing [1-5]\nor the service name you would like to get.\n
For example: '1' or 'Installation':\n1. Installation.\n2. Design.\n3. Commissioning.\n4. Tools supply.\n5. Servicing""",
    2: """Добро пожаловать в Solartec!\nВведите число соответсвующее услуге либо название услуги.\n
Например: '1' или 'Монтаж':\n1. Монтаж.\n2. Проектирование.\n3. Пусконаладка.\n4. Поставка инструментов.\n5. Сервисное обслуживание""",
    1: """Solartec компанияға қош келдіңіз!\nЖұмысты жалғастыру үшін сан немесе кызмет атын тандаңыз.\n
Мысалы: '1' немесе 'Монтаж'.\n1. Монтаж.\n2. Жобалау.\т3. Іске қосу және жөндеу.\т4. Құрал жеткізілуі.\т5. Сервистік қызмет көрсету"""
}

SERVICE_TO_CHOOSE = {
    1 = {
    "russian": """Проектирование инженерных сетей - обязательный этап любого строительства.
Инженерные системы современных зданий и сооружений состоят из множества устройств и коммуникаций.
Доверившись специалистам компании «SOLARTEC», Вы решите даже самые сложные инженерные задачи!
Мы знаем, как проектируются инженерные системы, и сделаем все расчеты для того чтобы все элементы работали как единый слаженный механизм и на 100% выполняли свои функции с учетом особенностей объекта и пожеланий заказчика.
Также важно, чтобы на проектировании наша работа не заканчивалась - надежнее и выгоднее для Вас довериться компании полного цикла, способной создать инженерные системы под ключ!
Большой практический опыт позволяет нам создавать наиболее удачные инженерные решения с точки зрения эффективности, дизайна, бюджета и удобства обслуживания!""",
    "kazakh": """Инженерлік желілерді жобалау кез келген құрылыстың міндетті кезеңі болып табылады.
Қазіргі заманғы ғимараттар мен құрылыстардың инженерлік жүйелері көптеген құрылғылар мен коммуникациялардан тұрады.
SOLARTEC компаниясының мамандарына сену арқылы сіз тіпті ең күрделі инженерлік мәселелерді шешесіз!
Біз инженерлік жүйелердің қалай жобаланғанын білеміз және біз барлық элементтердің біртұтас, жақсы үйлестірілген механизм ретінде жұмыс істеуі және нысанның сипаттамалары мен тапсырыс берушінің тілектерін ескере отырып, өз функцияларын 100% орындауы үшін барлық есептеулерді жасаймыз. .
Сондай-ақ, біздің жұмысымыз дизайнмен аяқталмайтыны маңызды - сіз үшін кілтті тапсыру инженерлік жүйелерін жасай алатын толық циклді компанияға сену қауіпсіз және тиімдірек!
Үлкен практикалық тәжірибе тиімділік, дизайн, бюджет және техникалық қызмет көрсетудің қарапайымдылығы тұрғысынан ең сәтті инженерлік шешімдерді жасауға мүмкіндік береді!
""",
    "english": """Design of utility networks is a mandatory stage of any construction.
Engineering systems of modern buildings and structures consist of many devices and communications.
By trusting the specialists of the SOLARTEC company, you will solve even the most complex engineering problems!
We know how engineering systems are designed, and we will do all the calculations to ensure that all elements work as a single, well-coordinated mechanism and 100% perform their functions, taking into account the characteristics of the facility and the wishes of the customer.
It is also important that our work does not end with design - it is safer and more profitable for you to trust a full-cycle company capable of creating turnkey engineering systems!
Extensive practical experience allows us to create the most successful engineering solutions in terms of efficiency, design, budget and ease of maintenance!"""    
    }
}