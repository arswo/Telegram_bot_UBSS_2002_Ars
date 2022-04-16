from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Бот запущен. Нажмите Ctrl+C для завершения")


def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет! Хочешь узнать свежую информацию о МТУСИ?")

def on_help(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text='''Я бот созданный для ДЗ.
	/start - команда активации бота
	/go - просто команда
	/bmw - продажа X5
	Ну и доп слова \'хочу\',\'стишок\',\'пицца\'''')

def on_go(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Просто команда")	

def on_bmw(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="https://www.youtube.com/watch?v=aF0SDHz7d9I")

def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	if text == 'хочу':
		context.bot.send_message(chat_id=chat.id, text='Тогда тебе сюда - https://lms.mtuci.ru/')
	elif text == 'стишок':
			context.bot.send_message(chat_id=chat.id, text='''Внимание! Продаётся Х5ый 93его года. Карбюратор, инжектор, инспектор проректор, ИК-порт, блютуз, туз, козырь, валет, дама, румба, сальса, танго, манго, Мис Бахар, сеть магазинов "Сабина", сисле, Элвис Пресли, Джек Дэниелс, Уолт Дисней, Френсис Форд Коппола, акапелла, опера, хор, нейша хор, винзавод, Новый Год, Новруз Байрам, День Независимости, Праздник Св. Патрика.Дальше. Фул-салон, наверху-внизу люк, панорама, балкон, фасад, смотровая площадка, зеркало заднего вида, зеркало дисплея, зеркало фона, зеркало заставки, приставка, 10 к 1 ставка, пол-ставки, подставка, булавка, козявка.Пошли дальше. Затем - DVD, VCD, впереди, не перди, CD, и не рыпайся, MP3, MP4, М-пакет, М-торба, М-зембиль, changer, excange, I see no changes, California love, Two of America's most wanted, Hit'em Up, мемори-пакет, мемори-кард, мультимедиа-кард, флеш-карт, кард-ридер, сидер, гнойный пидер, Лидер, АНС, Аз-ТВ, Аз Саманд, Аз-Петрол, аста ла виста, Vista, XP, Windows.Затем сидение, вставание, лежание, функция Забеременеть, меню функции, настройки, браузер, Мои приложения, Игры, Контакты, SIM. Кондиционер Сплит, вентилятор, печка, автонагрев, греф, доля, посылка, доставка, отчёт переданных, входящие, исходящие, Мои папки, Шаблоны, СМС-сообщения, электронная почта.Тормоза: АБС, АТС, БАГЭС, собес, ММS, MSN, ICQ, АДИГО, чат, форум.Руль: гидравлика, биоравлика, Кравченко, Шевченко, чеченка, косынка, болонка, овчарка, air-bag, air-ballon, air-банка, air-бутылка, Turan Air.Сцепление, тормоз, газ, оксиген, Azeronline, «Азеррейл», Azercell, Аз-нефть, азеракшам, Азербайджан.Коробка передач: Стептроник, Типтроник, Электроник, автомат, пулемёт, самонаводящаяся ракета, пуля со смещённым центром тяжести.Цвет металлика, механика, аэробика, фитнесс, бодибилдинг, Empire State Building, пудинг, приёмник, стеклоподъёмник, разговорник, лётчик, переводчик, русско-английский переводчик, курсы повышения квалификации, компьютерные курсы, курс доллара, курс Северная широта, 3,4 курс, бакалавр, магистр, оркестр, министр, Мистер Твистер.Мотор 3.0, в пользу Франции, хозяева поля стали чемпионами.Мощность: 300 лошадиных сил, 250 ослиных сил, 4 пьяные макаки, 2 щучьих потроха и одно не твоё собачье дело.6 цилиндров, 4 кубика, 7 ромбиков, 16 кварталов, Clap Ur Hands, Shake That Ass, Tell me what you wanna all I dance.Расход топлива: 100 км - 30 л бензин, 20 л спирт, Cola, Fanta, Sprite, чай, лёля, балыкъ, хамча баы.Размер бензобака: 80 л, чистый етмиш алты, докъсан учь, докъсан беш, докъсан еди, Уиндоус докъсан секиз.Передние-задние колёса: AMG, Extasy, виагра, подагра, Сиалис, Виллес, герпес, Элвис, Гринпис.Круговая плёнка, клиёнка, скатерть, простыня, наволочка, занавеска, невестка, деверь, зять, тёща, двоюродный дядя.Сиденье: массаж, пассаж, форсаж, месаж, гагаш по имени Дадаш, номер ахаш, параша.Карбюратор, калькулятор, куратор, прокурор, государственный обвинитель, судебный исполнитель, адвокат, судья, сторона защиты, блок, оборона, противостояние, нападение, совпадение, академия, премия, Грэмми, Золотой глобус, Оскар, тостер, блендер, Enter, Caps Lock, Shift, Del, Alt, обновить, скопировать, перезагрузить, отжать, высушить, спустить.Кого интересует этот автомобиль, позвоните пожалуйста по номерам... или по буквам. Кому как удобно.Спасибо большое!Х5ый 93его года эксклюзивная модель Прощайте!''')
	elif text == 'пицца':
		context.bot.send_message(chat_id=chat.id, text='https://dodopizza.ru/balashiha')
	else:
		context.bot.send_message(chat_id=chat.id, text='Напиши слова - \'хочу\',\'стишок\',\'пицца\'')

token = '5367281943:AAFMNzAM2sgf3K_-CZVx6UmfErkq45JMUUg'

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(CommandHandler("help", on_help))
dispatcher.add_handler(CommandHandler("go", on_go))
dispatcher.add_handler(CommandHandler("bmw", on_bmw))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()