LANGUAGE_TO_CHOOSE = """Please choose the language for further communication\nby typing number [1-3]: \n1 - Қазақша,\n2 - Русский,\n3 - English"""


WELCOME_MESSAGE = {
    3: """Hello, welcome to Solartec!\nTo proceed to our services choose one of below by typing [1-5]\nor the service name you would like to get.\n
For example: '1' or 'Installation':\n1. Installation.\n2. Design.\n3. Commissioning.\n4. Tools supply.\n5. Servicing""",
    2: """Добро пожаловать в Solartec!\nВведите число соответсвующее услуге либо название услуги.\n
Например: '1' или 'Монтаж':\n1. Монтаж.\n2. Проектирование.\n3. Пусконаладка.\n4. Поставка инструментов.\n5. Сервисное обслуживание""",
    1: """Solartec компанияға қош келдіңіз!\nЖұмысты жалғастыру үшін сан немесе кызмет атын тандаңыз.
Мысалы: '1' немесе 'Монтаж'.\n1. Монтаж.\n2. Жобалау.\n3. Іске қосу және жөндеу.\n4. Құрал жеткізілуі.\n5. Сервистік қызмет көрсету"""
}


SERVICE_TO_CHOOSE = {
    1: {
        2: """Проектирование инженерных сетей - обязательный этап любого строительства.
Инженерные системы современных зданий и сооружений состоят из множества устройств и коммуникаций.
Доверившись специалистам компании «SOLARTEC», Вы решите даже самые сложные инженерные задачи!
Мы знаем, как проектируются инженерные системы, и сделаем все расчеты для того чтобы все элементы работали как единый слаженный механизм и на 100% выполняли свои функции с учетом особенностей объекта и пожеланий заказчика.
Также важно, чтобы на проектировании наша работа не заканчивалась - надежнее и выгоднее для Вас довериться компании полного цикла, способной создать инженерные системы под ключ!
Большой практический опыт позволяет нам создавать наиболее удачные инженерные решения с точки зрения эффективности, дизайна, бюджета и удобства обслуживания!""",
        1: """Инженерлік желілерді жобалау кез келген құрылыстың міндетті кезеңі болып табылады.
Қазіргі заманғы ғимараттар мен құрылыстардың инженерлік жүйелері көптеген құрылғылар мен коммуникациялардан тұрады.
SOLARTEC компаниясының мамандарына сену арқылы сіз тіпті ең күрделі инженерлік мәселелерді шешесіз!
Біз инженерлік жүйелердің қалай жобаланғанын білеміз және біз барлық элементтердің біртұтас, жақсы үйлестірілген механизм ретінде жұмыс істеуі және нысанның сипаттамалары мен тапсырыс берушінің тілектерін ескере отырып, өз функцияларын 100% орындауы үшін барлық есептеулерді жасаймыз. .
Сондай-ақ, біздің жұмысымыз дизайнмен аяқталмайтыны маңызды - сіз үшін кілтті тапсыру инженерлік жүйелерін жасай алатын толық циклді компанияға сену қауіпсіз және тиімдірек!
Үлкен практикалық тәжірибе тиімділік, дизайн, бюджет және техникалық қызмет көрсетудің қарапайымдылығы тұрғысынан ең сәтті инженерлік шешімдерді жасауға мүмкіндік береді!
""",
        3: """Design of utility networks is a mandatory stage of any construction.
Engineering systems of modern buildings and structures consist of many devices and communications.
By trusting the specialists of the SOLARTEC company, you will solve even the most complex engineering problems!
We know how engineering systems are designed, and we will do all the calculations to ensure that all elements work as a single, well-coordinated mechanism and 100% perform their functions, taking into account the characteristics of the facility and the wishes of the customer.
It is also important that our work does not end with design - it is safer and more profitable for you to trust a full-cycle company capable of creating turnkey engineering systems!
Extensive practical experience allows us to create the most successful engineering solutions in terms of efficiency, design, budget and ease of maintenance!"""    
    },
    2: {
        1: """Ғимараттар мен құрылыстардың инженерлік жүйелерін монтаждау бойынша жұмыстарды тиімді орындау процесінің маңызды кезеңі учаскеге жоғары сапалы материалдар мен жабдықтарды кешенді жеткізу болып табылады.
Сондықтан, біздің компания SOLARTEC уақтылы жеткізу туралы барлық уайымдарды өз мойнына алады!
Біздің инженерлер қажетті жабдықтың нақты есебін жасайды, содан кейін менеджерлер оған тапсырыс беріп, учаскеге немесе өздерінің қоймаларына жеткізуді ұйымдастырады.
Сонымен қатар, біздің компания көптеген отандық және шетелдік жеткізушілермен және инженерлік жабдықтарды өндірушілермен берік серіктестік байланыстарға ие, сондықтан біз инженерлік жабдықты сатып алу үшін ең жақсы бағаларды ұсына аламыз.
""",
        2: """Оперативные комплексные поставки качественных материалов и оборудования на объект – важный этап процесса эффективного исполнения работ по монтажу инженерных систем зданий и сооружений.
Поэтому все заботы о своевременном выполнении поставок наша компания «SOLARTEC» берет на себя!
Наши инженеры производят точный подсчет необходимого оборудования, далее менеджеры производят его заказ и организуют доставку до объекта или на собственные склады.
Кроме этого, наша компания имеет крепкие партнерские отношения с многочисленными отечествнными и иностранными поставщиками и производителями инженерного оборудования, поэтому мы можем предложить лучшие цены на закупку инженерного оборудования.
""",
        3: """Prompt comprehensive supplies of high-quality materials and equipment to the site is an important stage in the process of effective execution of work on the installation of engineering systems of buildings and structures.
Therefore, our company “SOLARTEC” takes on all the worries about timely delivery!
Our engineers make an accurate calculation of the required equipment, then managers order it and organize delivery to the site or to their own warehouses.
In addition, our company has strong partnerships with numerous domestic and foreign suppliers and manufacturers of engineering equipment, so we can offer the best prices for the purchase of engineering equipment."""
    },
    3: {
        1: """Кез келген құрылыс процесінде жабдықты орнату объектінің тиімді және сенімді жұмысының құрамдас бөліктерінің бірі болып саналады.
SOLARTEC компаниясы әртүрлі мақсаттарға арналған технологиялық жабдықтарды, машиналар мен агрегаттарды монтаждау мен құрастыруды қоса алғанда, құрылымдар мен ғимараттардың инженерлік жабдықтарын орнатуды ең кең ауқымда жүзеге асырады.
Жабдықты орнату және қосу барлық жобалық шешімдерді қатаң сақтай отырып жүзеге асырылады.
Біздің компания осы жұмыстың барлық спектрін минималды шығындармен орындаудың бірегей әдістемесін әзірледі және енгізді.
""",
        2: """В любом строительном процессе монтаж оборудования считается одним из составляющих компонентов эффективной и надежной работоспособности объекта.
Компания “SOLARTEC” осуществляет монтаж инженерного оборудования сооружений и зданий в самом широком спектре, в том числе установку и сборку технологического оборудования, машин и агрегатов различного предназначения.
Установка, а также подключение оборудования выполняется в четком следовании всем проектным решениям.
Нашей компанией разработана и внедрена уникальная методика выполнения всего спектра данной работы с минимальными затратами.
Если же проект носит временный характер, то мы не перекладываем заботы о его установке и ответственность за исправность на плечи заказчика. Монтаж и демонтаж оборудования на объекте полностью берем на себя!
""",
        3: """In any construction process, installation of equipment is considered one of the components of the effective and reliable operation of the facility.
The SOLARTEC company carries out installation of engineering equipment of structures and buildings in the widest range, including the installation and assembly of technological equipment, machines and units for various purposes.
Installation and connection of equipment is carried out in strict adherence to all design decisions.
Our company has developed and implemented a unique methodology for performing the entire range of this work at minimal cost.
"""
    },
    4: {
        1: """Учаскедегі кез келген инженерлік жабдық дұрыс іске қосылуы керек. Осы мақсатта арнайы іске қосу жұмыстары жүргізілуде.
Жұмыстың басты мақсаты – төтенше жағдайлардың туындау қаупінің алдын алып, жабдықты дұрыс іске қосу.
Іске қосу жұмыстарын орындау кезінде SOLARTEC мамандары ақауларға тез жауап бере алады және ақауларды шеше алады.
Инженерлік жүйелердің тұрақты белгіленген жұмыс параметрлерін алғаннан кейін іске қосу жұмыстары аяқталды деп саналады.
Біз тұтынушыларымызға инженерлік жүйелердің сапасы мен ұзақ мерзімділігіне, сондай-ақ жабдықтың бүкіл пайдалану кезеңінде оның жұмысы кезінде үздіксіз жұмыс істеуіне кепілдік береміз!
""",
        2: """Любое инженерное оборудование на объекте требуется правильно ввести в эксплуатацию. Для этого проводятся специальные пусконаладочные работы.
Основная цель работ – корректно запустить оборудование в работу, предупредив риск возникновения аварийных ситуаций.
При выполнении пусконаладочных работ специалисты «SOLARTEC» умеют оперативно отреагировать и устранить неполадки.
Пусконаладочные работы считаются выполненными после получения устойчивых заданных параметров работы инженерных систем.
Мы гарантируем своим заказчикам качество и долговечность инженерных систем, а также бесперебойную работу оборудования в ходе его эксплуатации в течение всего срока использования!
""",
        3: """Any engineering equipment at the site must be put into operation correctly. For this purpose, special commissioning work is carried out.
The main goal of the work is to put the equipment into operation correctly, preventing the risk of emergency situations.
When performing commissioning work, SOLARTEC specialists are able to quickly respond and troubleshoot problems.
Commissioning work is considered completed after obtaining stable specified operating parameters of engineering systems.
We guarantee our customers the quality and durability of engineering systems, as well as uninterrupted operation of the equipment during its operation throughout the entire period of use!
"""
    },
    5: {
        1: """Техникалық және сервистік аутсорсингті толыққанды қамтамасыз ететін тұрақты, сенімді компанияға техникалық қызмет көрсету жауапкершілігін тапсырсаңыз, инженерлік жабдық бірқалыпты жұмыс істейді!
Шұғыл жөндеу немесе жабдықты пайдалану бойынша практикалық кеңес алу үшін кез келген уақытта бізге хабарласуға болады.
SOLARTEC білікті мамандарының тобы сіздің сұранысыңызға мүмкіндігінше тез жауап береді және көрсетілген жұмыстардың жиынтығын тиісті деңгейде орындайды.
Компанияның барлық техникалық персоналында барлық стандартты мәселелерді шешу үшін дағдылар, нұсқаулар және тәжірибе бар.
Қызмет біздің тұтынушыларға тәулік бойы қол жетімді.
""",
        2: """Инженерное оборудование будет работать бесперебойно, если ответственность за его обслуживание Вы доверите стабильной, надежной компании, которая осуществляет полноценный технический и сервисный аутсорсинг!
В любой момент Вы сможете обратиться к нам за срочным ремонтом или практической рекомендацией по эксплуатации оборудования.
Команда квалифицированных специалистов «SOLARTEC» в кратчайшие сроки отреагирует на вашу заявку и на должном уровне выполнит комплекс обозначенных работ.
Весь технический персонал компании обладает навыками, инструкциями и опытом для решения всех стандартных проблем.
Для решения нестандартных задач технические специалисты «SOLARTEC» связываются напрямую со службами технической поддержки производителей оборудования.
Сервис доступен нашим заказчикам в режиме 24/7.
""",
        3: """Engineering equipment will operate smoothly if you entrust responsibility for its maintenance to a stable, reliable company that provides full-fledged technical and service outsourcing!
At any time, you can contact us for urgent repairs or practical advice on operating the equipment.
A team of qualified SOLARTEC specialists will respond to your request as soon as possible and will carry out the set of specified works at the proper level.
All technical personnel of the company have the skills, instructions and experience to solve all standard problems.
The service is available to our customers 24/7.
"""
    }
}