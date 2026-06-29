import random
import json
import os
import time
from datetime import datetime, timedelta

# ============== ДАННЫЕ ==============

PRODUCTS = [
    {"name": "Хлеб", "hunger": 10, "energy": -5, "price": 50, "time": 5},
    {"name": "Багет", "hunger": 12, "energy": -5, "price": 70, "time": 5},
    {"name": "Булка", "hunger": 8, "energy": -3, "price": 40, "time": 5},
    {"name": "Круассан", "hunger": 10, "energy": 0, "price": 80, "time": 5},
    {"name": "Пирожок", "hunger": 12, "energy": -5, "price": 60, "time": 5},
    {"name": "Курица", "hunger": 20, "energy": 5, "price": 200, "time": 10},
    {"name": "Говядина", "hunger": 22, "energy": 5, "price": 300, "time": 10},
    {"name": "Свинина", "hunger": 20, "energy": 3, "price": 250, "time": 10},
    {"name": "Колбаса", "hunger": 15, "energy": 0, "price": 180, "time": 5},
    {"name": "Бекон", "hunger": 18, "energy": -5, "price": 220, "time": 5},
    {"name": "Лосось", "hunger": 15, "energy": 10, "price": 350, "time": 10},
    {"name": "Тунец", "hunger": 15, "energy": 8, "price": 300, "time": 10},
    {"name": "Скумбрия", "hunger": 14, "energy": 5, "price": 200, "time": 5},
    {"name": "Форель", "hunger": 16, "energy": 8, "price": 320, "time": 10},
    {"name": "Сардины", "hunger": 12, "energy": 5, "price": 150, "time": 5},
    {"name": "Молоко", "hunger": 10, "energy": 5, "price": 80, "time": 5},
    {"name": "Йогурт", "hunger": 10, "energy": 5, "price": 100, "time": 5},
    {"name": "Сыр", "hunger": 12, "energy": 5, "price": 150, "time": 5},
    {"name": "Масло", "hunger": 8, "energy": 5, "price": 120, "time": 5},
    {"name": "Кефир", "hunger": 10, "energy": 3, "price": 70, "time": 5},
    {"name": "Яблоко", "hunger": 8, "energy": 10, "price": 50, "time": 5},
    {"name": "Груша", "hunger": 8, "energy": 10, "price": 60, "time": 5},
    {"name": "Апельсин", "hunger": 8, "energy": 12, "price": 70, "time": 5},
    {"name": "Банан", "hunger": 10, "energy": 15, "price": 80, "time": 5},
    {"name": "Киви", "hunger": 6, "energy": 10, "price": 60, "time": 5},
    {"name": "Картошка", "hunger": 10, "energy": 5, "price": 40, "time": 5},
    {"name": "Помидор", "hunger": 8, "energy": 5, "price": 50, "time": 5},
    {"name": "Огурец", "hunger": 6, "energy": 3, "price": 30, "time": 5},
    {"name": "Морковь", "hunger": 8, "energy": 5, "price": 35, "time": 5},
    {"name": "Лук", "hunger": 6, "energy": 0, "price": 25, "time": 5},
    {"name": "Пицца", "hunger": 25, "energy": -10, "price": 400, "time": 20},
    {"name": "Бургер", "hunger": 22, "energy": -8, "price": 250, "time": 15},
    {"name": "Лапша", "hunger": 20, "energy": -5, "price": 200, "time": 15},
    {"name": "Суп", "hunger": 20, "energy": 5, "price": 180, "time": 15},
    {"name": "Пельмени", "hunger": 25, "energy": -5, "price": 280, "time": 20},
    {"name": "Шоколад", "hunger": 5, "energy": 15, "price": 120, "time": 5},
    {"name": "Печенье", "hunger": 5, "energy": 10, "price": 80, "time": 5},
    {"name": "Мармелад", "hunger": 3, "energy": 10, "price": 100, "time": 5},
    {"name": "Торт", "hunger": 10, "energy": 5, "price": 300, "time": 15},
    {"name": "Пряник", "hunger": 5, "energy": 8, "price": 60, "time": 5},
    {"name": "Кофе", "hunger": 0, "energy": 15, "price": 100, "time": 5},
    {"name": "Чай", "hunger": 0, "energy": 10, "price": 50, "time": 5},
    {"name": "Сок", "hunger": 5, "energy": 8, "price": 80, "time": 5},
    {"name": "Лимонад", "hunger": 3, "energy": 5, "price": 60, "time": 5},
    {"name": "Кола", "hunger": 3, "energy": 8, "price": 70, "time": 5},
    {"name": "Red Bull", "hunger": -5, "energy": 30, "price": 180, "time": 5},
    {"name": "Монстр", "hunger": -5, "energy": 28, "price": 200, "time": 5},
    {"name": "Flash", "hunger": -3, "energy": 25, "price": 150, "time": 5},
    {"name": "Adrenalin", "hunger": -5, "energy": 30, "price": 220, "time": 5},
    {"name": "Drive", "hunger": -3, "energy": 25, "price": 160, "time": 5},
    {"name": "Картошка фри", "hunger": 20, "energy": -15, "price": 150, "time": 10},
    {"name": "Наггетсы", "hunger": 18, "energy": -10, "price": 200, "time": 10},
    {"name": "Хот-дог", "hunger": 20, "energy": -10, "price": 120, "time": 10},
    {"name": "Сэндвич", "hunger": 18, "energy": -5, "price": 130, "time": 10},
    {"name": "Шаурма", "hunger": 25, "energy": -15, "price": 280, "time": 15},
    {"name": "Киноа", "hunger": 15, "energy": 20, "price": 350, "time": 10},
    {"name": "Чиа", "hunger": 10, "energy": 15, "price": 300, "time": 5},
    {"name": "Спирулина", "hunger": 5, "energy": 10, "price": 400, "time": 5},
    {"name": "Овес", "hunger": 15, "energy": 10, "price": 150, "time": 5},
    {"name": "Мюсли", "hunger": 15, "energy": 15, "price": 200, "time": 5},
    {"name": "Грецкий орех", "hunger": 10, "energy": 15, "price": 180, "time": 5},
    {"name": "Миндаль", "hunger": 10, "energy": 15, "price": 200, "time": 5},
    {"name": "Арахис", "hunger": 10, "energy": 10, "price": 120, "time": 5},
    {"name": "Кешью", "hunger": 10, "energy": 15, "price": 250, "time": 5},
    {"name": "Фисташки", "hunger": 10, "energy": 12, "price": 220, "time": 5},
    {"name": "Кетчуп", "hunger": 2, "energy": 0, "price": 30, "time": 0},
    {"name": "Майонез", "hunger": 2, "energy": 0, "price": 40, "time": 0},
    {"name": "Горчица", "hunger": 2, "energy": 0, "price": 30, "time": 0},
    {"name": "Соевый", "hunger": 2, "energy": 0, "price": 35, "time": 0},
    {"name": "Барбекю", "hunger": 2, "energy": 0, "price": 45, "time": 0},
    {"name": "Хлопья", "hunger": 15, "energy": 10, "price": 180, "time": 5},
    {"name": "Гранола", "hunger": 15, "energy": 15, "price": 220, "time": 5},
    {"name": "Каша", "hunger": 20, "energy": 10, "price": 120, "time": 10},
    {"name": "Панкейки", "hunger": 18, "energy": 5, "price": 200, "time": 15},
    {"name": "Омлет", "hunger": 20, "energy": 10, "price": 150, "time": 15},
    {"name": "Горошек", "hunger": 10, "energy": -5, "price": 80, "time": 5},
    {"name": "Кукуруза", "hunger": 10, "energy": -5, "price": 90, "time": 5},
    {"name": "Фасоль", "hunger": 12, "energy": -5, "price": 100, "time": 5},
    {"name": "Тушенка", "hunger": 18, "energy": -5, "price": 150, "time": 5},
    {"name": "Паштет", "hunger": 15, "energy": -3, "price": 120, "time": 5},
    {"name": "Соль", "hunger": 0, "energy": 0, "price": 20, "time": 0},
    {"name": "Перец", "hunger": 0, "energy": 0, "price": 25, "time": 0},
    {"name": "Корица", "hunger": 0, "energy": 0, "price": 30, "time": 0},
    {"name": "Ваниль", "hunger": 0, "energy": 0, "price": 40, "time": 0},
    {"name": "Паприка", "hunger": 0, "energy": 0, "price": 25, "time": 0},
    {"name": "Пиво", "hunger": 5, "energy": -30, "price": 150, "time": 10},
    {"name": "Вино", "hunger": 5, "energy": -30, "price": 400, "time": 15},
    {"name": "Водка", "hunger": 5, "energy": -40, "price": 300, "time": 10},
    {"name": "Ром", "hunger": 5, "energy": -35, "price": 500, "time": 10},
    {"name": "Виски", "hunger": 5, "energy": -35, "price": 600, "time": 10},
    {"name": "Протеин", "hunger": 5, "energy": 10, "price": 400, "time": 5},
    {"name": "Клетчатка", "hunger": 5, "energy": 5, "price": 300, "time": 5},
    {"name": "Омега-3", "hunger": 3, "energy": 8, "price": 350, "time": 5},
    {"name": "Коллаген", "hunger": 3, "energy": 5, "price": 500, "time": 5},
    {"name": "Витамины", "hunger": 3, "energy": 10, "price": 200, "time": 5},
    {"name": "Чипсы", "hunger": 3, "energy": 0, "price": 60, "time": 5},
    {"name": "Сухарики", "hunger": 3, "energy": 0, "price": 40, "time": 5},
    {"name": "Попкорн", "hunger": 3, "energy": 0, "price": 50, "time": 5},
    {"name": "Маршмеллоу", "hunger": 3, "energy": 5, "price": 80, "time": 5},
    {"name": "Жевачка", "hunger": 1, "energy": 0, "price": 20, "time": 0},
]

PC_PARTS = [
    {"name": "💻 Процессор", "price": 1000, "type": "cpu"},
    {"name": "💻 Видеокарта", "price": 1000, "type": "gpu"},
    {"name": "💻 Оперативная память", "price": 1000, "type": "ram"},
    {"name": "💻 Материнская плата", "price": 1000, "type": "mb"},
    {"name": "💻 Блок питания", "price": 1000, "type": "psu"},
    {"name": "🖱️ Мышь", "price": 1000, "type": "mouse"},
    {"name": "⌨️ Клавиатура", "price": 1000, "type": "keyboard"},
]

FIRST_NAMES_MALE = ["Александр", "Дмитрий", "Максим", "Иван", "Андрей", "Артем", "Михаил", "Сергей", "Николай", "Владимир",
                    "Алексей", "Егор", "Павел", "Роман", "Кирилл", "Виктор", "Олег", "Юрий", "Анатолий", "Григорий"]

FIRST_NAMES_FEMALE = ["Анна", "Екатерина", "Мария", "Ольга", "Татьяна", "Наталья", "Ирина", "Елена", "Светлана", "Юлия",
                      "Алиса", "Дарья", "Полина", "Виктория", "Ксения", "Евгения", "Валерия", "Анастасия", "Варвара", "Ульяна"]

LAST_NAMES_MALE = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Волков", "Козлов", "Морозов", "Новиков",
                   "Соколов", "Лебедев", "Ковалев", "Медведев", "Виноградов", "Белов", "Тарасов", "Крылов", "Орлов", "Мамонтов"]

LAST_NAMES_FEMALE = ["Иванова", "Петрова", "Сидорова", "Кузнецова", "Смирнова", "Попова", "Волкова", "Козлова", "Морозова", "Новикова",
                     "Соколова", "Лебедева", "Ковалева", "Медведева", "Виноградова", "Белова", "Тарасова", "Крылова", "Орлова", "Мамонтова"]

DEATH_METHODS = [
    "🫀 Остановка сердца", "🧠 Инсульт", "🚗 Сбит машиной", "🔥 Пожар", "💧 Утопление",
    "🔪 Ножевое ранение", "💊 Передозировка", "🏢 Падение с высоты", "⚡ Удар током",
    "🧊 Переохлаждение", "🌡️ Тепловой удар", "💨 Удушье", "💉 Отравление",
    "🏃 Сердечный приступ", "😴 Остановка дыхания", "💥 Взрыв", "🔫 Огнестрельное",
    "⚔️ Удар ножом", "🪦 Засыпание землёй", "🌊 Смерть в море", "🏔️ Сход лавины",
    "🌋 Извержение вулкана", "🌀 Торнадо", "⚡ Молния", "🌩️ Удар грома",
    "🔥 Самовозгорание", "💀 Смерть от страха", "🤮 Удушение рвотой", "🩸 Потеря крови",
    "🧬 Рак", "🫁 Пневмония", "🦠 Инфекция", "🤒 Лихорадка", "🧠 Аневризма",
    "💓 Тахикардия", "🫀 Инфаркт", "🧬 Генетическая болезнь", "🦷 Смерть от зуба",
    "👀 Ослепление", "👂 Потеря слуха", "🤧 Аллергия", "🧪 Эксперимент",
    "🤖 Убит роботом", "👾 Кибер-атака", "📱 Взрыв телефона", "💻 Поражение током от ПК",
    "🚀 Падение с космоса", "🌍 Изменение климата", "☢️ Радиация", "🧪 Химикаты",
    "🐍 Укус змеи", "🦂 Укус скорпиона", "🐅 Нападение тигра", "🦁 Нападение льва",
    "🐻 Нападение медведя", "🐊 Нападение крокодила", "🦈 Акула", "🐙 Осьминог",
    "🕷️ Укус паука", "🐝 Укус пчелы", "🦟 Малярия", "🐀 Крысиная лихорадка",
    "🍄 Отравление грибами", "🌿 Ядовитое растение", "🍷 Отравление алкоголем",
    "💊 Передозировка лекарств", "🧪 Химический ожог", "🔥 Ожог", "💧 Обморожение",
    "🌪️ Ураган", "🌊 Цунами", "🏚️ Обвал здания", "🚢 Кораблекрушение",
    "✈️ Авиакатастрофа", "🚂 Поезд", "🚌 Автобус", "🚲 Велосипед",
    "🏃 Сердечный приступ при беге", "🏊 Утопление в бассейне", "🎢 Аттракцион",
    "🎪 Цирк", "🎭 Театр", "🎮 Игровая зависимость", "📺 Телевизор",
    "📚 Книжная полка", "🖼️ Падение картины", "⚽ Футбольный мяч",
    "🎾 Теннис", "🏀 Баскетбол", "⚾ Бейсбол", "🎱 Бильярд",
    "🎯 Дартс", "🎳 Боулинг", "⛳ Гольф", "🏹 Стрела",
    "🗡️ Меч", "🛡️ Щит", "⚔️ Дуэль", "🏴‍☠️ Пираты",
    "👻 Привидение", "🧛 Вампир", "🧟 Зомби", "👽 Инопланетяне"
]

CARS = [
    {"name": "🚗 Жигули", "price": 5000, "time_reduce": 5, "energy_reduce": 2, "repair_cost": 500},
    {"name": "🚗 ВАЗ-2107", "price": 8000, "time_reduce": 10, "energy_reduce": 3, "repair_cost": 600},
    {"name": "🚗 Москвич", "price": 7000, "time_reduce": 8, "energy_reduce": 2, "repair_cost": 550},
    {"name": "🚗 Toyota Corolla", "price": 15000, "time_reduce": 15, "energy_reduce": 5, "repair_cost": 800},
    {"name": "🚗 Honda Civic", "price": 20000, "time_reduce": 20, "energy_reduce": 7, "repair_cost": 900},
    {"name": "🚗 Nissan Skyline", "price": 30000, "time_reduce": 25, "energy_reduce": 10, "repair_cost": 1200},
    {"name": "🚗 BMW M3", "price": 50000, "time_reduce": 30, "energy_reduce": 12, "repair_cost": 1500},
    {"name": "🚗 Mercedes-Benz C63", "price": 70000, "time_reduce": 35, "energy_reduce": 15, "repair_cost": 1800},
    {"name": "🚗 Audi R8", "price": 100000, "time_reduce": 40, "energy_reduce": 18, "repair_cost": 2000},
    {"name": "🚗 Porsche 911", "price": 120000, "time_reduce": 45, "energy_reduce": 20, "repair_cost": 2200},
    {"name": "🚗 Lamborghini Huracan", "price": 150000, "time_reduce": 50, "energy_reduce": 25, "repair_cost": 3000},
    {"name": "🚗 Ferrari F8", "price": 180000, "time_reduce": 55, "energy_reduce": 28, "repair_cost": 3500},
    {"name": "🚗 Bugatti Veyron", "price": 250000, "time_reduce": 60, "energy_reduce": 30, "repair_cost": 5000},
    {"name": "🚗 Tesla Model S", "price": 80000, "time_reduce": 35, "energy_reduce": 15, "repair_cost": 1500},
    {"name": "🚗 Rolls-Royce Phantom", "price": 200000, "time_reduce": 40, "energy_reduce": 20, "repair_cost": 4000},
    {"name": "🚗 Лада Веста", "price": 12000, "time_reduce": 12, "energy_reduce": 4, "repair_cost": 700},
    {"name": "🚗 Hyundai Solaris", "price": 18000, "time_reduce": 18, "energy_reduce": 6, "repair_cost": 850},
    {"name": "🚗 Kia Rio", "price": 20000, "time_reduce": 20, "energy_reduce": 7, "repair_cost": 900},
    {"name": "🚗 Volkswagen Golf", "price": 25000, "time_reduce": 22, "energy_reduce": 8, "repair_cost": 1000},
    {"name": "🚗 Subaru Impreza", "price": 35000, "time_reduce": 28, "energy_reduce": 11, "repair_cost": 1300},
    {"name": "🚗 Lexus RX", "price": 60000, "time_reduce": 32, "energy_reduce": 14, "repair_cost": 1600},
    {"name": "🚗 Jaguar F-Type", "price": 90000, "time_reduce": 38, "energy_reduce": 17, "repair_cost": 1900},
    {"name": "🚗 Maserati Ghibli", "price": 110000, "time_reduce": 42, "energy_reduce": 19, "repair_cost": 2100},
    {"name": "🚗 Aston Martin DB11", "price": 160000, "time_reduce": 48, "energy_reduce": 22, "repair_cost": 2800},
    {"name": "🚗 McLaren 720S", "price": 220000, "time_reduce": 58, "energy_reduce": 29, "repair_cost": 4500},
]

HOUSES = [
    {"name": "🏚️ Комната в общежитии", "price": 10000, "energy_bonus": 5},
    {"name": "🏚️ Маленькая квартира", "price": 30000, "energy_bonus": 10},
    {"name": "🏚️ Средняя квартира", "price": 60000, "energy_bonus": 15},
    {"name": "🏚️ Большая квартира", "price": 100000, "energy_bonus": 20},
    {"name": "🏚️ Квартира в центре", "price": 150000, "energy_bonus": 25},
    {"name": "🏚️ Пентхаус", "price": 300000, "energy_bonus": 35},
    {"name": "🏚️ Особняк", "price": 500000, "energy_bonus": 50},
    {"name": "🏚️ Студия в спальнике", "price": 8000, "energy_bonus": 3},
    {"name": "🏚️ Квартира-студия", "price": 20000, "energy_bonus": 7},
    {"name": "🏚️ Двушка в хрущёвке", "price": 45000, "energy_bonus": 12},
    {"name": "🏚️ Трёшка в панельке", "price": 70000, "energy_bonus": 17},
    {"name": "🏚️ Квартира в новостройке", "price": 120000, "energy_bonus": 22},
    {"name": "🏚️ Апартаменты с видом", "price": 180000, "energy_bonus": 28},
    {"name": "🏚️ Пентхаус в центре", "price": 350000, "energy_bonus": 40},
    {"name": "🏚️ Коттедж за городом", "price": 450000, "energy_bonus": 45},
    {"name": "🏚️ Особняк с бассейном", "price": 600000, "energy_bonus": 55},
    {"name": "🏚️ Замок в горах", "price": 1000000, "energy_bonus": 70},
]

BUSINESSES = [
    {"name": "🌯 Шаурмячная", "price": 15000, "income": 500, "tax": 100, "salary": 200},
    {"name": "🍕 Пиццерия", "price": 30000, "income": 900, "tax": 200, "salary": 350},
    {"name": "☕ Кофейня", "price": 50000, "income": 1200, "tax": 300, "salary": 500},
    {"name": "🍔 Бургерная", "price": 70000, "income": 1600, "tax": 400, "salary": 650},
    {"name": "🍣 Суши-бар", "price": 100000, "income": 2100, "tax": 500, "salary": 800},
    {"name": "🍷 Ресторан", "price": 150000, "income": 3000, "tax": 700, "salary": 1200},
    {"name": "🏋️ Фитнес-клуб", "price": 200000, "income": 3500, "tax": 800, "salary": 1400},
    {"name": "🎮 Игровой клуб", "price": 250000, "income": 4000, "tax": 900, "salary": 1600},
    {"name": "📚 Книжный магазин", "price": 300000, "income": 3000, "tax": 700, "salary": 1300},
    {"name": "🛒 Продуктовый магазин", "price": 350000, "income": 4500, "tax": 1000, "salary": 1800},
    {"name": "🏨 Отель", "price": 500000, "income": 7000, "tax": 1500, "salary": 2500},
    {"name": "🏦 Микрофинансовая контора", "price": 600000, "income": 9000, "tax": 2000, "salary": 3000},
    {"name": "🚗 Автосалон", "price": 800000, "income": 12000, "tax": 2500, "salary": 4000},
    {"name": "🏭 Завод", "price": 1000000, "income": 15000, "tax": 3000, "salary": 5000},
    {"name": "🏢 Торговый центр", "price": 2000000, "income": 25000, "tax": 5000, "salary": 8000},
]

CELEBRITIES = [
    "Освальд Мосли", "Владимир Путин", "Адольф Гитлер", "Чарли Чаплин",
    "Денис Жуков", "Алексей Навальный", "Александр Пушкин", "Иван Грозный",
    "Пётр I", "Екатерина II", "Владимир Ленин", "Иосиф Сталин",
    "Никита Хрущёв", "Леонид Брежнев", "Михаил Горбачёв"
]

EVENTS = [
    {"text": "Вы нашли 100 рублей на земле!", "money": 100, "hunger": 0, "energy": 0},
    {"text": "Вы выиграли в лотерею 500 рублей!", "money": 500, "hunger": 0, "energy": 0},
    {"text": "Вам вернули старый долг 300 рублей!", "money": 300, "hunger": 0, "energy": 0},
    {"text": "Вы нашли золотую цепочку!", "money": 1000, "hunger": 0, "energy": 0},
    {"text": "На вас напали грабители! -300 рублей", "money": -300, "hunger": 0, "energy": -10},
    {"text": "Вас чуть не сбила машина", "money": 0, "hunger": 0, "energy": -10},
    {"text": "Вы попали в драку", "money": 0, "hunger": 0, "energy": -20},
    {"text": "Вас остановила полиция для проверки", "money": -500, "hunger": 0, "energy": -10},
    {"text": "Вы простудились. Лекарства 100 рублей", "money": -100, "hunger": 0, "energy": -10},
    {"text": "Вы отравились едой", "money": 0, "hunger": -20, "energy": -20},
    {"text": "У вас аллергия. Таблетки 80 рублей", "money": -80, "hunger": 0, "energy": -5},
    {"text": "Вы заболели гриппом", "money": -200, "hunger": 0, "energy": -30},
    {"text": "Порвалась одежда. Новая 500 рублей", "money": -500, "hunger": 0, "energy": 0},
    {"text": "Сломался телефон. Ремонт 1000 рублей", "money": -1000, "hunger": 0, "energy": 0},
    {"text": "Потеряли ключи. Новые 300 рублей", "money": -300, "hunger": 0, "energy": 0},
    {"text": "Подарок на 400 рублей", "money": 400, "hunger": 0, "energy": 0},
    {"text": "Сильный дождь, промокли", "money": 0, "hunger": 0, "energy": -10},
    {"text": "Сильная жара. Вода 50 рублей", "money": -50, "hunger": 0, "energy": -5},
    {"text": "Тёплая погода подняла настроение", "money": 0, "hunger": 0, "energy": 15},
    {"text": "Пожар в соседнем доме", "money": -1000, "hunger": 0, "energy": -30},
    {"text": "Авария. Помогли пострадавшим -300", "money": -300, "hunger": 0, "energy": -10},
    {"text": "Спасли кошку. Вознаграждение 200", "money": 200, "hunger": 0, "energy": -10},
]

SEASONAL_EVENTS = {
    "winter": [
        {"text": "Сильный снегопад! Вы замёрзли", "money": -100, "hunger": 0, "energy": -10},
        {"text": "Слепили снеговика! + настроение", "money": 0, "hunger": 0, "energy": 5},
    ],
    "spring": [
        {"text": "Весеннее тепло! + энергия", "money": 0, "hunger": 0, "energy": 10},
        {"text": "Пошёл дождь, промокли", "money": 0, "hunger": 0, "energy": -5},
    ],
    "summer": [
        {"text": "Сильная жара! Мороженое 50р", "money": -50, "hunger": 5, "energy": 5},
        {"text": "Загорали и обгорели", "money": 0, "hunger": 0, "energy": -5},
    ],
    "autumn": [
        {"text": "Листопад! + настроение", "money": 0, "hunger": 0, "energy": 5},
        {"text": "Ветер сорвал шапку -200р", "money": -200, "hunger": 0, "energy": 0},
    ]
}

# ============== КЛАСС ИГРЫ ==============

class Game:
    def __init__(self):
        self.player_name = ""
        self.money = 5000
        self.hunger = 80
        self.energy = 70
        self.suspicion = 0
        self.fame = 0
        self.day = 1
        self.date = datetime(2010, 4, 23)
        self.time = datetime(2010, 4, 23, 8, 0, 0)
        self.fridge = []
        self.killed = []
        self.debt = 0
        self.debt_days = 0
        self.investigation = False
        self.running = True
        self.loaded = False
        self.active_contract = None
        self.known_people = []
        self.news_count = 0
        self.contracts_done = 0
        self.informant_met = False
        self.informant_paid = False
        self.l_name_known = False
        self.l_face_known = False
        self.l_killed = False
        self.pc_parts = {"cpu": 0, "gpu": 0, "ram": 0, "mb": 0, "psu": 0, "mouse": 0, "keyboard": 0}
        self.car = None
        self.house = 0
        self.story_index = 0
        self.story_done = False
        self.story_triggered = False
        self.contract_available = True
        self.ending = None
        self.game_over = False
        self.work_progress = 0
        self.businesses = []
        self.business_debt = 0
        self.business_days_left = 7
        self.island = False
        self.mafia_war = False
        self.mafia_killed = 0
        self.detective_hunt = False
        self.detective_count = 0
        self.girl_call_day = None
        self.girl_met = False
        self.girl_phone = False
        self.celebrity_contracts = False

    def get_season(self):
        month = self.date.month
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        else:
            return "autumn"

    def save(self):
        data = {
            "player_name": self.player_name,
            "money": self.money,
            "hunger": self.hunger,
            "energy": self.energy,
            "suspicion": self.suspicion,
            "fame": self.fame,
            "day": self.day,
            "date": self.date.isoformat(),
            "time": self.time.isoformat(),
            "fridge": self.fridge,
            "killed": self.killed,
            "debt": self.debt,
            "debt_days": self.debt_days,
            "investigation": self.investigation,
            "known_people": self.known_people,
            "news_count": self.news_count,
            "contracts_done": self.contracts_done,
            "informant_met": self.informant_met,
            "informant_paid": self.informant_paid,
            "l_name_known": self.l_name_known,
            "l_face_known": self.l_face_known,
            "l_killed": self.l_killed,
            "pc_parts": self.pc_parts,
            "car": self.car,
            "house": self.house,
            "story_index": self.story_index,
            "story_done": self.story_done,
            "story_triggered": self.story_triggered,
            "active_contract": self.active_contract,
            "contract_available": self.contract_available,
            "ending": self.ending,
            "game_over": self.game_over,
            "work_progress": self.work_progress,
            "businesses": self.businesses,
            "business_debt": self.business_debt,
            "business_days_left": self.business_days_left,
            "island": self.island,
            "mafia_war": self.mafia_war,
            "mafia_killed": self.mafia_killed,
            "detective_hunt": self.detective_hunt,
            "detective_count": self.detective_count,
            "girl_call_day": self.girl_call_day,
            "girl_met": self.girl_met,
            "girl_phone": self.girl_phone,
            "celebrity_contracts": self.celebrity_contracts
        }
        with open("save.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        if not os.path.exists("save.json"):
            return False
        with open("save.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.player_name = data["player_name"]
        self.money = data["money"]
        self.hunger = data["hunger"]
        self.energy = data["energy"]
        self.suspicion = data["suspicion"]
        self.fame = data.get("fame", 0)
        self.day = data["day"]
        self.date = datetime.fromisoformat(data["date"])
        self.time = datetime.fromisoformat(data.get("time", data["date"] + "T08:00:00"))
        self.fridge = data["fridge"]
        self.killed = data["killed"]
        self.debt = data["debt"]
        self.debt_days = data["debt_days"]
        self.investigation = data["investigation"]
        self.known_people = data.get("known_people", [])
        self.news_count = data.get("news_count", 0)
        self.contracts_done = data.get("contracts_done", 0)
        self.informant_met = data.get("informant_met", False)
        self.informant_paid = data.get("informant_paid", False)
        self.l_name_known = data.get("l_name_known", False)
        self.l_face_known = data.get("l_face_known", False)
        self.l_killed = data.get("l_killed", False)
        self.pc_parts = data.get("pc_parts", {"cpu": 0, "gpu": 0, "ram": 0, "mb": 0, "psu": 0, "mouse": 0, "keyboard": 0})
        self.car = data.get("car")
        self.house = data.get("house", 0)
        self.story_index = data.get("story_index", 0)
        self.story_done = data.get("story_done", False)
        self.story_triggered = data.get("story_triggered", False)
        self.active_contract = data.get("active_contract")
        self.contract_available = data.get("contract_available", True)
        self.ending = data.get("ending")
        self.game_over = data.get("game_over", False)
        self.work_progress = data.get("work_progress", 0)
        self.businesses = data.get("businesses", [])
        self.business_debt = data.get("business_debt", 0)
        self.business_days_left = data.get("business_days_left", 7)
        self.island = data.get("island", False)
        self.mafia_war = data.get("mafia_war", False)
        self.mafia_killed = data.get("mafia_killed", 0)
        self.detective_hunt = data.get("detective_hunt", False)
        self.detective_count = data.get("detective_count", 0)
        self.girl_call_day = data.get("girl_call_day")
        self.girl_met = data.get("girl_met", False)
        self.girl_phone = data.get("girl_phone", False)
        self.celebrity_contracts = data.get("celebrity_contracts", False)
        self.loaded = True
        return True

    def auto_save(self):
        self.save()

    def advance_time(self, minutes, energy_cost=0, hunger_cost=0):
        self.time += timedelta(minutes=minutes)
        self.energy -= energy_cost
        self.hunger -= hunger_cost
        if self.energy < 0:
            self.energy = 0
        if self.hunger < 0:
            self.hunger = 0
        if self.time.hour == 0 and self.time.minute == 0 and self.time.second == 0:
            self.new_day()

    def new_day(self):
        self.day += 1
        self.date += timedelta(days=1)
        self.hunger -= random.randint(5, 10)
        self.energy -= random.randint(5, 10)
        if self.hunger < 0:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0
        self.contract_available = True
        self.check_story()
        self.check_businesses()
        self.check_post_game()
        self.auto_save()

        if self.hunger <= 0:
            print("❌ ВЫ УПАЛИ В ГОЛОДНЫЙ ОБМОРОК!")
            cost = min(3000, self.money)
            self.money -= cost
            self.hunger = 50
            self.energy = 30
            self.time += timedelta(days=7)
            self.day += 7
            print(f"🏥 Больница: -{cost} ₽. Вы провели неделю в больнице.")

        if self.energy <= 0:
            print("💤 ВЫ РУХНУЛИ ОТ УСТАЛОСТИ! Спите 10 часов.")
            self.energy = 100
            self.time += timedelta(hours=10)

        if self.debt > 0:
            self.debt_days += 1
            if self.debt_days >= 5:
                self.suspicion += 10
                self.debt = 0
                self.debt_days = 0
                print("⚠️ Вы не вернули долг! Подозрение +10%")

        if self.suspicion >= 100:
            self.investigation = True

        self.active_contract = None

    def check_businesses(self):
        if not self.businesses:
            return

        total_income = 0
        total_tax = 0
        total_salary = 0

        for biz in self.businesses:
            total_income += biz["income"]
            total_tax += biz["tax"]
            total_salary += biz["salary"]

        self.money += total_income
        print(f"💰 Бизнесы принесли: +{total_income} ₽")

        if self.day % 30 == 0:
            total_cost = total_tax + total_salary
            if self.money >= total_cost:
                self.money -= total_cost
                print(f"💸 Оплачены налоги и зарплаты: -{total_cost} ₽")
            else:
                self.business_debt = total_cost
                self.business_days_left = 7
                print(f"⚠️ У вас недостаточно денег! Долг: {total_cost} ₽")
                print("📱 В телефоне появилась опция оплаты долга")

    def check_post_game(self):
        if self.day < 850 or not self.ending:
            return

        if self.day % 10 == 0 and self.detective_count < 10:
            self.detective_hunt = True
            self.detective_count += 1
            print(f"🔍 Детектив #{self.detective_count} начал расследование!")

        if self.day >= 1000 and not self.mafia_war and self.mafia_killed == 0:
            self.mafia_war = True
            print("🔫 Мафия объявила вам войну!")

        if self.day >= 2 and not self.girl_met and not self.girl_phone:
            if self.girl_call_day is None:
                self.girl_call_day = self.day + random.randint(1, 1)
            if self.day == self.girl_call_day:
                self.girl_phone = True
                print("📱 Вам позвонила девушка! Она хочет встретиться.")
                print("📞 В телефоне есть опция 'Свидание'")

    def check_story(self):
        if self.story_done or self.game_over:
            return
        story_events = [
            {"day": 1, "text": "📓 Вы нашли тетрадь смерти! Рюк появился перед вами.", "time": 10},
            {"day": 3, "text": "📰 Новости: 'Загадочная смерть криминального авторитета.'", "time": 5},
            {"day": 7, "text": "📰 Новости: 'В городе орудует убийца. Прозвище — Кира.'", "time": 5},
            {"day": 10, "text": "👤 На улице вы слышите разговор прохожих о Кире.", "time": 10},
            {"day": 15, "text": "📰 Новости: 'Детектив L вступает в игру.'", "time": 5},
            {"day": 22, "text": "📺 L по телевизору: 'Кира, я знаю, что ты смотришь меня.'", "time": 30},
            {"day": 30, "text": "💭 Прошёл месяц. L приближается.", "time": 5},
            {"day": 45, "text": "📰 Новости: 'L заявляет, что Кира — студент.'", "time": 5},
            {"day": 60, "text": "👤 Информатор: 'Я знаю, кто ты, Кира. Я хочу помочь.'", "time": 15},
            {"day": 75, "text": "📰 Новости: 'L даёт пресс-конференцию.'", "time": 5},
            {"day": 90, "text": "📰 Новости: 'L сузил круг подозреваемых.'", "time": 5},
            {"day": 100, "text": "👤 Информатор: 'Я знаю имя L. Но это стоит 100 000 ₽.'", "time": 15},
            {"day": 120, "text": "💭 L Lawliet... Теперь у тебя есть имя.", "time": 5},
            {"day": 150, "text": "📰 Новости: 'L объявляет награду за информацию о Кире.'", "time": 5},
            {"day": 180, "text": "👤 Информатор: 'Я знаю, где будет L завтра.'", "time": 15},
            {"day": 200, "text": "📰 Новости: 'L мёртв! Мир в шоке!'", "time": 5},
            {"day": 220, "text": "👤 Ниа: 'Ты думаешь, что победил, Кира? Это только начало.'", "time": 10},
            {"day": 250, "text": "📰 Новости: 'Новый детектив Ниа берётся за дело Киры.'", "time": 5},
            {"day": 280, "text": "👤 Миками: 'Вы... Вы Кира? Я хочу помочь вам.'", "time": 20},
            {"day": 300, "text": "👤 Миками: 'Ниа создал организацию СПК.'", "time": 15},
            {"day": 330, "text": "📰 Новости: 'Ниа: Я не L. Я хуже.'", "time": 5},
            {"day": 360, "text": "📰 Новости: 'Ниа приближается к разгадке.'", "time": 5},
            {"day": 400, "text": "👤 Миками: 'Я узнал, где находится Ниа.'", "time": 15},
            {"day": 420, "text": "👤 Миками: 'Ниа подозревает меня.'", "time": 15},
            {"day": 450, "text": "📰 Новости: 'Ниа заявляет, что Кира живёт в Японии.'", "time": 5},
            {"day": 480, "text": "👤 Миками: 'Ниа пригласил меня на встречу.'", "time": 20},
            {"day": 500, "text": "👤 Миками: 'Ниа ни о чём не догадывается.'", "time": 10},
            {"day": 550, "text": "👤 Миками: 'У меня есть план. Заменить тетрадь.'", "time": 20},
            {"day": 580, "text": "📰 Новости: 'Ниа уверен, что поймает Киру.'", "time": 5},
            {"day": 600, "text": "👤 Миками: 'Я заменил тетрадь. Настоящая у меня.'", "time": 15},
            {"day": 620, "text": "👤 Миками: 'Я готов. Я запишу имя Ниа в тетрадь.'", "time": 10},
            {"day": 650, "text": "👤 Миками: 'Он подменил тетрадь! Настоящая у него!'", "time": 15},
            {"day": 680, "text": "👤 Ниа вызывает тебя на встречу.", "time": 10},
            {"day": 700, "text": "👤 Ниа: 'Здравствуй, Кира.'", "time": 20},
            {"day": 720, "text": "👤 Миками: 'Я убью Ниа. Это последний шанс.'", "time": 15},
            {"day": 780, "text": "👤 Миками: 'Всё готово. Завтра я встречусь с Ниа.'", "time": 15},
            {"day": 800, "text": "👤 Встреча Миками и Ниа. Решающий момент.", "time": 30},
        ]

        for event in story_events:
            if event["day"] == self.day and self.story_index < len(story_events):
                self.story_index += 1
                print("=" * 50)
                print(f"📖 СОБЫТИЕ: День {self.day}")
                print("=" * 50)
                print(event["text"])
                print("=" * 50)
                if event["day"] == 1 and not self.story_triggered:
                    self.story_triggered = True
                    print("📓 'Это тетрадь смерти. Тот, чьё имя будет вписано, умрёт.'")
                    print("💭 Ты понимаешь: это шанс изменить мир.")
                self.advance_time(event.get("time", 15), 5, 3)
                input("Нажмите Enter...")

        if self.day >= 850 and self.ending is None:
            self.trigger_final()

    def trigger_final(self):
        print("=" * 50)
        print("💀 ФИНАЛ")
        print("=" * 50)
        print("Вы дошли до финала истории!")
        print("Ваши действия определили судьбу мира.")
        print("=" * 50)

        if self.l_killed or self.fame >= 100:
            self.ending = "good"
            print("🌟 ХОРОШАЯ КОНЦОВКА: Вы победили! Мир ваш!")
            print("=" * 50)
            print("💭 'Кажись, я победил, Ниа... 38... 39... 40 секунд! Я победил!'")
            print("=" * 50)
        elif self.suspicion >= 100 and self.fame < 100:
            self.ending = "neutral"
            print("😐 НЕЙТРАЛЬНАЯ КОНЦОВКА: Вы живы, но мир не ваш.")
            print("=" * 50)
            print("💭 'Я проиграл... Но я жив. Это ещё не конец.'")
            print("=" * 50)
        else:
            self.ending = "bad"
            print("⛓️ ПЛОХАЯ КОНЦОВКА: Вас поймали. Конец.")
            print("=" * 50)
            print("⛓️ 'Это конец... Я не смог стать богом...'")
            print("=" * 50)

        input("Нажмите Enter, чтобы продолжить игру...")
        self.game_over = True
        self.save()

    def show_stats(self):
        time_str = self.time.strftime("%H:%M:%S")
        months = ["января", "февраля", "марта", "апреля", "мая", "июня",
                  "июля", "августа", "сентября", "октября", "ноября", "декабря"]
        date_str = f"{self.day} {months[self.date.month-1]} {self.date.year}"
        print("=" * 50)
        print(f"        📓 ТЕТРАДЬ СМЕРТИ - СИМУЛЯТОР")
        print(f"        👤 {self.player_name}")
        print(f"        📅 {date_str}  ⏰ {time_str}")
        if self.ending:
            endings = {"good": "🌟 ПОБЕДА", "neutral": "😐 В БЕГАХ", "bad": "⛓️ ПОРАЖЕНИЕ"}
            print(f"        🏆 {endings.get(self.ending, '')}")
        if self.island:
            print("        🏝️ ВЛАДЕЛЕЦ ОСТРОВА")
        print("=" * 50)
        print(f" 🍔 Голод: {self.hunger}/100  |  ⚡ Энергия: {self.energy}/100")
        print(f" 💰 Деньги: {self.money} ₽")
        print(f" 🕵️ Подозрение: {self.suspicion}%  |  ⭐ Слава: {self.fame}%")
        if self.debt > 0:
            print(f" 💸 Долг: {self.debt} ₽ (осталось {5 - self.debt_days} дней)")
        if self.business_debt > 0:
            print(f" 💸 Долг бизнеса: {self.business_debt} ₽ (осталось дней: {self.business_days_left})")
        if self.fridge:
            print(f" 🧊 В холодильнике: {len(self.fridge)} продуктов")
        if self.active_contract:
            print(f" 📋 Активный контракт: {self.active_contract['name']} {self.active_contract['last']}")
        if self.car:
            print(f" 🚗 Машина: {self.car['name']}")
        if self.house > 0:
            print(f" 🏠 Жильё: {HOUSES[self.house-1]['name']}")
        if self.l_name_known:
            print(f" 📋 Имя L известно: L Lawliet")
        if self.l_face_known:
            print(f" 👤 Лицо L известно")
        if self.l_killed:
            print(f" 💀 L мёртв!")
        if self.businesses:
            print(f" 🏢 Бизнесов: {len(self.businesses)}")
        if self.mafia_war:
            print(f" 🔫 Война с мафией! Убито боссов: {self.mafia_killed}")
        if self.detective_hunt:
            print(f" 🔍 Охота на детективов: {self.detective_count} найдено")
        pc_level = sum(self.pc_parts.values())
        if pc_level > 0:
            print(f" 💻 Уровень ПК: {pc_level}")
        if self.work_progress > 0:
            print(f" ⌨️ Прогресс работы: {self.work_progress}/1000")
        print("=" * 50)

    def generate_person(self):
        gender = random.choice(["male", "female"])
        if gender == "male":
            name = random.choice(FIRST_NAMES_MALE)
            last = random.choice(LAST_NAMES_MALE)
        else:
            name = random.choice(FIRST_NAMES_FEMALE)
            last = random.choice(LAST_NAMES_FEMALE)
        age = random.randint(18, 80)
        bio = f"{name} {last}, {age} лет. "
        bio += random.choice([
            "Бизнесмен, замешанный в махинациях.",
            "Бывший полицейский, вышедший на пенсию.",
            "Преступник, скрывающийся от закона.",
            "Коррумпированный чиновник.",
            "Торговец оружием.",
            "Наркобарон.",
            "Беглый заключённый.",
            "Шпион."
        ])
        if random.random() < 0.05 and CELEBRITIES:
            celeb = random.choice(CELEBRITIES)
            name_parts = celeb.split()
            if len(name_parts) >= 2:
                name = name_parts[0]
                last = name_parts[1]
                bio = f"{celeb}. Знаменитость."
        return {"name": name, "last": last, "age": age, "gender": gender, "bio": bio}

    def generate_contract(self):
        person = self.generate_person()
        if random.random() < 0.1 and CELEBRITIES:
            celeb = random.choice(CELEBRITIES)
            name_parts = celeb.split()
            if len(name_parts) >= 2:
                person["name"] = name_parts[0]
                person["last"] = name_parts[1]
                person["bio"] = f"{celeb}. Знаменитость."
                person["price"] = random.randint(5000, 20000)
        else:
            person["price"] = random.randint(2000, 10000)
        return person

    def show_contract(self, contract):
        print("=" * 50)
        print("💼 КОНТРАКТ")
        print("=" * 50)
        print(f"Имя: {contract['name']} {contract['last']}")
        print(f"Возраст: {contract['age']} лет")
        print(f"Пол: {'Мужской' if contract['gender'] == 'male' else 'Женский'}")
        print(f"Биография: {contract['bio']}")
        print(f"💰 Цена: {contract['price']} ₽")
        print("=" * 50)

    def casino(self):
        print("🎰 КАЗИНО")
        print(f"У вас: {self.money} ₽")
        print("Выберите ставку:")
        print("1. 50% - выигрыш x1.5")
        print("2. 30% - выигрыш x2")
        print("3. 20% - выигрыш x3")
        print("4. Назад")
        try:
            choice = input("👉 ")
            if choice == "4":
                return
            if choice not in ["1", "2", "3"]:
                print("❌ Неверный выбор!")
                return
            bet = int(input("Сумма ставки (или 0 для выхода): "))
            if bet == 0:
                return
            if bet > self.money:
                print("❌ Недостаточно денег!")
                return
            if bet < 0:
                print("❌ Сумма должна быть положительной!")
                return

            if choice == "1":
                win_chance = 50
                multiplier = 1.5
            elif choice == "2":
                win_chance = 30
                multiplier = 2
            else:
                win_chance = 20
                multiplier = 3

            result = random.randint(1, 100)
            if result <= win_chance:
                win = int(bet * multiplier)
                self.money += win
                print(f"🎉 Вы выиграли {win} ₽! У вас {self.money} ₽")
            else:
                self.money -= bet
                print(f"😞 Вы проиграли {bet} ₽. У вас {self.money} ₽")
            self.advance_time(5, 2, 1)
        except ValueError:
            print("❌ Введите число!")

    def take_debt(self):
        print("💸 ВЗЯТЬ В ДОЛГ (максимум 5000 ₽)")
        try:
            amount = int(input("Сумма: "))
            if amount > 5000 or amount <= 0:
                print("❌ От 1 до 5000 ₽")
                return
            self.money += amount
            self.debt += amount
            self.debt_days = 0
            print(f"✅ Вы взяли {amount} ₽. Вернуть нужно с 20% через 5 дней.")
            self.advance_time(5, 1, 1)
        except ValueError:
            print("❌ Введите число!")

    def call_informant(self):
        if not self.informant_met:
            print("📞 У вас нет номера информатора.")
            return
        if self.informant_paid:
            print("📞 Вы уже заплатили информатору.")
            return
        if self.l_killed:
            print("📞 L уже мёртв. Информатор не нужен.")
            return
        print("📞 Вы звоните информатору...")
        print("🕵️ Информатор: 'Привет. Ты готов заплатить 100 000 ₽ за имя L?'")
        print(f"💰 У вас: {self.money} ₽")
        print("1. Заплатить 100 000 ₽")
        print("2. Позвонить позже")
        print("3. Убить информатора (через тетрадь)")
        choice = input("👉 ")
        if choice == "1":
            if self.money < 100000:
                print("❌ Недостаточно денег! Нужно 100 000 ₽")
                return
            self.money -= 100000
            self.informant_paid = True
            print("✅ Информатор: 'Имя L - L Lawliet. Но его лицо я покажу позже.'")
            print("📋 Имя L известно: L Lawliet")
            self.l_name_known = True
            self.advance_time(10, 2, 1)
        elif choice == "2":
            print("📞 'Позвони, когда будут деньги.'")
            self.advance_time(2, 1, 1)
        elif choice == "3":
            self.killed.append({"name": "Информатор", "method": "🫀 Остановка сердца"})
            self.suspicion += 20
            print("📓 Вы убили информатора.")
            print("💀 Он мёртв. Ты не узнаешь имя L.")
            self.informant_met = False
            self.advance_time(5, 3, 2)

    def girl_date(self):
        if not self.girl_phone or self.girl_met:
            print("❌ Свидание недоступно.")
            return
        print("=" * 50)
        print("💕 СВИДАНИЕ")
        print("=" * 50)
        print("Вы встречаетесь с девушкой в кафе. Она красивая, с карими глазами.")
        print("💬 Она: 'Ты Кира, да? Я следила за тобой.'")
        print("💬 'Я узнала твой номер через информатора. Ты мне интересен.'")
        print("💬 'Давай поедем к тебе? Я хочу узнать тебя ближе.'")

        print("\n📌 ВЫБОР:")
        print("1. 'Да, поехали ко мне.'")
        print("2. 'Нет, я не хочу.'")
        choice = input("👉 ")

        if choice == "1":
            print("=" * 50)
            print("🍷 ДОМА")
            print("=" * 50)
            print("Вы приехали к себе. Выпили вино, разговорились.")
            print("💬 Она: 'Ты не просто Кира. Ты — бог.'")
            print("💬 'И я хочу быть рядом с богом.'")
            print("🔥 Она целует тебя. Страстно.")
            print("🛏️ Вы переходите в спальню.")
            print("💋 Постельная сцена:")
            print("🔥 Она стягивает с тебя рубашку, проводит рукой по груди.")
            print("🔥 Её тело изгибается под тобой, она стонет.")
            print("🔥 Ты входишь в неё, она вскрикивает от удовольствия.")
            print("🔥 'Да... Ещё...' — шепчет она.")
            print("🔥 Вы двигаетесь в такт, ритм ускоряется.")
            print("💦 Она кончает с громким стоном, ты — следом.")
            print("💤 После — она прижимается к тебе и засыпает.")

            self.girl_met = True
            self.fame += 5
            print("\n💕 Утром она уходит, оставив записку:")
            print("'Я буду скучать по тебе, мой бог. Позвони мне когда-нибудь.'")
            print("=" * 50)
            self.advance_time(120, 30, 15)
        else:
            print("❌ Она уходит, разочарованная.")
            self.advance_time(15, 5, 3)

    def pay_business_debt(self):
        if self.business_debt <= 0:
            print("❌ У вас нет долга по бизнесам.")
            return
        if self.money < self.business_debt:
            print(f"❌ Недостаточно денег! Нужно: {self.business_debt} ₽")
            return
        self.money -= self.business_debt
        print(f"✅ Долг оплачен! -{self.business_debt} ₽")
        self.business_debt = 0
        self.business_days_left = 7
        self.advance_time(10, 2, 1)

    def buy_business(self):
        print("🏢 ПОКУПКА БИЗНЕСА")
        for i, biz in enumerate(BUSINESSES, 1):
            owned = " ✅ (есть)" if biz in self.businesses else ""
            print(f"{i}. {biz['name']} | Цена: {biz['price']} ₽ | Доход: {biz['income']} ₽/день | Налоги: {biz['tax']} ₽ | ЗП: {biz['salary']} ₽{owned}")
        print("0. Назад")
        try:
            choice = int(input("Выберите бизнес (0 - назад): ")) - 1
            if choice == -1:
                return
            if 0 <= choice < len(BUSINESSES):
                biz = BUSINESSES[choice]
                if biz in self.businesses:
                    print("❌ У вас уже есть этот бизнес!")
                    return
                if self.money < biz['price']:
                    print("❌ Недостаточно денег!")
                    return
                self.money -= biz['price']
                self.businesses.append(biz)
                print(f"✅ Вы купили {biz['name']}!")
                self.advance_time(30, 5, 3)
            else:
                print("❌ Неверный выбор")
        except ValueError:
            print("❌ Введите число!")

    def buy_island(self):
        if self.island:
            print("❌ У вас уже есть остров!")
            return
        if self.money < 5000000:
            print(f"❌ Недостаточно денег! Нужно 5 000 000 ₽. У вас: {self.money}")
            return
        self.money -= 5000000
        self.island = True
        print("🏝️ ПОЗДРАВЛЯЮ! Вы купили личный остров!")
        print("Теперь вы недосягаемы для врагов.")
        self.advance_time(60, 10, 5)

    def eat(self):
        if not self.fridge:
            print("🍔 Холодильник пуст. Купите продукты!")
            return
        print("🍔 ВЫБЕРИТЕ ПРОДУКТ ДЛЯ ЕДЫ:")
        for i, item in enumerate(self.fridge):
            print(f"{i+1}. {item['name']} | +{item['hunger']} голод, {item['energy']} энергия")
        try:
            choice = int(input("👉 ")) - 1
            if 0 <= choice < len(self.fridge):
                item = self.fridge.pop(choice)
                self.hunger += item['hunger']
                self.energy += item['energy']
                if self.hunger > 100:
                    self.hunger = 100
                if self.energy > 100:
                    self.energy = 100
                print(f"🍽️ Вы съели {item['name']}!")
                self.advance_time(item.get('time', 5), 2, 0)
            else:
                print("❌ Неверный выбор")
        except ValueError:
            print("❌ Введите число!")

    def sleep(self):
        try:
            hours = int(input("Сколько часов спать (1-12): "))
            if hours < 1 or hours > 12:
                print("❌ От 1 до 12 часов")
                return
            energy_gain = hours * 15
            if self.house > 0:
                energy_gain += HOUSES[self.house-1]["energy_bonus"]
            self.energy += energy_gain
            if self.energy > 100:
                self.energy = 100
            minutes = hours * 60
            self.advance_time(minutes, 0, 0)
            print(f"😴 Вы поспали {hours} часов (+{energy_gain} энергии)")
        except ValueError:
            print("❌ Введите число!")

    def work(self):
        bonus_money = 0
        for part, level in self.pc_parts.items():
            if part not in ["mouse", "keyboard"]:
                bonus_money += level

        speed_bonus = (self.pc_parts.get("mouse", 0) + self.pc_parts.get("keyboard", 0)) * 0.1
        char_value = 1.0 + speed_bonus

        print(f"💻 ЛЕГАЛЬНАЯ РАБОТА")
        print(f"📊 Прогресс: {self.work_progress}/1000 символов")
        print(f"💰 База: 500 ₽ за 1000 символов")
        print(f"💻 Бонус от ПК: +{bonus_money} ₽ к награде")
        print(f"🖱️ Бонус от мыши/клавиатуры: каждый символ засчитывается как x{char_value:.1f}")
        print(f"💰 Итого за 1000 символов: {int(500 + bonus_money)} ₽")
        print("Введите 'stop' чтобы выйти и сохранить прогресс")
        print("Введите любой символ чтобы продолжить печатать...")

        while True:
            cmd = input("👉 ")
            if cmd.lower() == "stop":
                print(f"💾 Прогресс сохранён: {self.work_progress}/1000")
                self.auto_save()
                return

            typed_count = len(cmd)
            if typed_count == 0:
                print("❌ Введите хоть что-то!")
                continue

            progress_gain = typed_count * char_value
            self.work_progress += progress_gain
            self.advance_time(typed_count, 0.25 * typed_count, 0.1 * typed_count)

            print(f"📊 Прогресс: {min(int(self.work_progress), 1000)}/1000 ({min(int(self.work_progress*100//1000), 100)}%)")
            print(f"   (введено {typed_count} символов → +{progress_gain:.1f} к прогрессу)")

            if self.work_progress >= 1000:
                reward = int(500 + bonus_money)
                self.money += reward
                self.work_progress = 0
                print(f"✅ Заказ выполнен! +{reward} ₽. У вас {self.money} ₽")
                self.auto_save()
                return

    def buy_product(self):
        print("🛒 ПРОДУКТОВЫЙ МАГАЗИН")
        categories = ["Хлебобулочные", "Мясные", "Рыбные", "Молочные", "Фрукты", "Овощи",
                      "Готовые блюда", "Сладости", "Напитки", "Энергетики", "Фастфуд",
                      "Суперфуды", "Орехи", "Соусы", "Завтраки", "Консервы", "Специи",
                      "Алкоголь", "Здоровое", "Разное", "Комплектующие ПК"]
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        print("0. Назад")
        try:
            cat = int(input("Категория: "))
            if cat == 0:
                return

            if cat == 21:
                self.buy_pc_parts()
                return

            idx = (cat-1) * 5
            if idx < 0 or idx >= len(PRODUCTS):
                print("❌ Неверная категория")
                return
            products = PRODUCTS[idx:idx+5]
            for i, p in enumerate(products):
                print(f"{i+1}. {p['name']} | +{p['hunger']} голод, {p['energy']} энергия | {p['price']} ₽")
            try:
                choice = int(input("Выберите продукт (0 - назад): ")) - 1
                if choice == -1:
                    return
                if 0 <= choice < len(products):
                    item = products[choice]
                    if self.money < item['price']:
                        print("❌ Недостаточно денег!")
                        return
                    self.money -= item['price']
                    self.fridge.append(item.copy())
                    print(f"✅ Вы купили {item['name']}!")
                    self.advance_time(10, 3, 2)
                else:
                    print("❌ Неверный выбор")
            except ValueError:
                print("❌ Введите число!")
        except ValueError:
            print("❌ Введите число!")

    def buy_pc_parts(self):
        print("🖥️ КОМПЛЕКТУЮЩИЕ ПК")
        for i, part in enumerate(PC_PARTS, 1):
            level = self.pc_parts.get(part["type"], 0)
            print(f"{i}. {part['name']} | Уровень: {level} | Цена: {part['price']} ₽")
        print("0. Назад")
        try:
            choice = int(input("Выберите комплектующую (0 - назад): ")) - 1
            if choice == -1:
                return
            if 0 <= choice < len(PC_PARTS):
                part = PC_PARTS[choice]
                if self.money < part['price']:
                    print("❌ Недостаточно денег!")
                    return
                self.money -= part['price']
                self.pc_parts[part["type"]] = self.pc_parts.get(part["type"], 0) + 1
                print(f"✅ Вы улучшили {part['name']} до уровня {self.pc_parts[part['type']]}!")
                self.advance_time(5, 2, 1)
            else:
                print("❌ Неверный выбор")
        except ValueError:
            print("❌ Введите число!")

    def apply_event(self, event):
        if 'money' in event:
            self.money += event['money']
        if 'hunger' in event:
            self.hunger += event['hunger']
        if 'energy' in event:
            self.energy += event['energy']
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger < 0:
            self.hunger = 0
        if self.energy > 100:
            self.energy = 100
        if self.energy < 0:
            self.energy = 0

    def walk(self):
        season = self.get_season()
        if random.random() < 0.3:
            event = random.choice(SEASONAL_EVENTS[season])
            print(f"🌤️ Сезонное событие: {event['text']}")
            self.apply_event(event)
        else:
            event = random.choice(EVENTS)
            print("🚶 Вы гуляете по городу...")
            time.sleep(1)
            print(f"📌 {event['text']}")
            self.apply_event(event)

        if random.random() < 0.2:
            person = self.generate_person()
            if person not in self.known_people:
                self.known_people.append(person)
                print(f"👤 Вы познакомились с {person['name']} {person['last']}!")

        if self.fame > 0 and random.random() < 0.3:
            print(f"🗣️ Люди вокруг говорят о Кире! Ваша слава растёт.")
            self.fame = min(self.fame + 1, 100)

        self.advance_time(60, 15, 10)

    def buy_car(self):
        print("🚗 АВТОСАЛОН")
        for i, car in enumerate(CARS, 1):
            current = " ✅ (ваша)" if self.car and self.car["name"] == car["name"] else ""
            print(f"{i}. {car['name']} | Цена: {car['price']} ₽ | Экономия времени: {car['time_reduce']}% | Экономия энергии: {car['energy_reduce']}%{current}")
        print("0. Назад")
        try:
            choice = int(input("Выберите машину (0 - назад): ")) - 1
            if choice == -1:
                return
            if 0 <= choice < len(CARS):
                car = CARS[choice]
                if self.money < car['price']:
                    print("❌ Недостаточно денег!")
                    return
                self.money -= car['price']
                self.car = car
                print(f"✅ Вы купили {car['name']}!")
                self.advance_time(30, 5, 3)
            else:
                print("❌ Неверный выбор")
        except ValueError:
            print("❌ Введите число!")

    def buy_house(self):
        print("🏠 НЕДВИЖИМОСТЬ")
        print("1️⃣ Купить жильё")
        print("2️⃣ Купить бизнес")
        print("3️⃣ Купить остров")
        print("4️⃣ Просмотр")
        print("5️⃣ Назад")
        choice = input("👉 ")
        if choice == "1":
            self._buy_house()
        elif choice == "2":
            self.buy_business()
        elif choice == "3":
            self.buy_island()
        elif choice == "4":
            self._view_property()
        elif choice == "5":
            return

    def _buy_house(self):
        print("🏠 ПОКУПКА ЖИЛЬЯ")
        for i, house in enumerate(HOUSES, 1):
            current = " ✅ (ваша)" if self.house == i else ""
            print(f"{i}. {house['name']} | Цена: {house['price']} ₽ | Бонус к энергии сна: +{house['energy_bonus']}%{current}")
        print("0. Назад")
        try:
            choice = int(input("Выберите жильё (0 - назад): ")) - 1
            if choice == -1:
                return
            if 0 <= choice < len(HOUSES):
                house = HOUSES[choice]
                if self.money < house['price']:
                    print("❌ Недостаточно денег!")
                    return
                self.money -= house['price']
                self.house = choice + 1
                print(f"✅ Вы купили {house['name']}!")
                self.advance_time(30, 5, 3)
            else:
                print("❌ Неверный выбор")
        except ValueError:
            print("❌ Введите число!")

    def _view_property(self):
        print("📋 ВАША СОБСТВЕННОСТЬ")
        if self.house > 0:
            print(f"🏠 Жильё: {HOUSES[self.house-1]['name']}")
        else:
            print("🏠 Жилья нет")
        if self.businesses:
            print("🏢 Бизнесы:")
            for biz in self.businesses:
                print(f"  {biz['name']} | Доход: {biz['income']} ₽/день")
        else:
            print("🏢 Бизнесов нет")
        if self.island:
            print("🏝️ Личный остров есть!")
        else:
            print("🏝️ Острова нет")
        if self.car:
            print(f"🚗 Машина: {self.car['name']}")
        input("Нажмите Enter...")

    def notebook(self):
        print("📓 ТЕТРАДЬ СМЕРТИ")
        print("1️⃣ Написать имя жертвы и выбрать способ смерти")
        print("2️⃣ Просмотреть список убитых")
        print("3️⃣ Назад")
        choice = input("👉 ")
        if choice == "1":
            if not self.known_people:
                print("❌ Вы никого не знаете! Идите гулять и знакомьтесь.")
                return
            print("👤 Кого вы знаете:")
            for i, person in enumerate(self.known_people, 1):
                print(f"{i}. {person['name']} {person['last']}")
            try:
                idx = int(input("Выберите номер (0 - отмена): ")) - 1
                if idx == -1:
                    return
                if 0 <= idx < len(self.known_people):
                    person = self.known_people[idx]
                    name = f"{person['name']} {person['last']}"

                    if name == "L Lawliet" or (person['name'] == "L" and person['last'] == ""):
                        if not self.l_name_known:
                            print("❌ Вы не знаете полное имя L! Нужно узнать его.")
                            return
                        if not self.l_face_known:
                            print("❌ Вы не знаете лицо L! Нужно увидеть его.")
                            return

                    print("\n💀 ВЫБЕРИТЕ СПОСОБ СМЕРТИ:")
                    for i, method in enumerate(DEATH_METHODS, 1):
                        print(f"{i}. {method}")
                    print("0. Случайный способ")
                    try:
                        method_choice = int(input("👉 "))
                        if method_choice == 0:
                            method = random.choice(DEATH_METHODS)
                        elif 1 <= method_choice <= len(DEATH_METHODS):
                            method = DEATH_METHODS[method_choice-1]
                        else:
                            print("❌ Неверный выбор!")
                            return
                    except ValueError:
                        print("❌ Введите число!")
                        return

                    if name == "Теру Миками" or (person['name'] == "Миками" and person['last'] == ""):
                        print("💀 Вы убили Миками!")
                        self.known_people.remove(person)
                        self.killed.append({"name": name, "method": method})
                        self.suspicion += 20
                        self.advance_time(5, 3, 2)
                        print("📌 Ниа начнёт расследование быстрее!")
                        return

                    if name == "Информатор":
                        print("💀 Вы убили информатора!")
                        self.known_people.remove(person)
                        self.killed.append({"name": name, "method": method})
                        self.suspicion += 20
                        self.informant_met = False
                        self.advance_time(5, 3, 2)
                        return

                    self.killed.append({"name": name, "method": method})
                    self.suspicion += 15

                    if name == "L Lawliet":
                        self.l_killed = True
                        self.fame = min(self.fame + 50, 100)
                        print(f"✍️ Имя {name} записано в тетрадь.")
                        print(f"💀 Способ: {method}")
                        print("🫀 L умирает...")
                        print("🌟 L мёртв! Вы победили!")
                        self.advance_time(5, 3, 2)
                        return

                    print(f"✍️ Имя {name} записано в тетрадь.")
                    print(f"💀 Способ: {method}")

                    if self.active_contract and self.active_contract['name'] == person['name'] and self.active_contract['last'] == person['last']:
                        if random.random() < 0.1:
                            print("❌ Вас обманули! Контракт фальшивка.")
                            self.suspicion += 15
                            self.active_contract = None
                        else:
                            self.money += self.active_contract['price']
                            print(f"💰 Вы получили {self.active_contract['price']} ₽ за контракт!")
                            self.active_contract = None
                            self.contracts_done += 1
                    else:
                        print("⚠️ Вы убили случайного человека без контракта.")
                        if random.random() < 0.2:
                            print("📰 Кто-то видел вас! Подозрение +20%")
                            self.suspicion += 20

                    self.known_people.remove(person)
                    self.advance_time(5, 3, 2)
                else:
                    print("❌ Неверный выбор")
            except ValueError:
                print("❌ Введите число!")
        elif choice == "2":
            if self.killed:
                print("📋 СПИСОК УБИТЫХ:")
                for i, kill in enumerate(self.killed, 1):
                    print(f"{i}. {kill['name']} — {kill['method']}")
            else:
                print("📭 Пока никого не убито.")
        elif choice == "3":
            return

    def contract_menu(self):
        print("💼 КОНТРАКТЫ")
        print("1️⃣ Взять новый контракт")
        print("2️⃣ Выполнить активный контракт (через тетрадь)")
        print("3️⃣ Отказаться от контракта (штраф 5000 ₽)")
        print("4️⃣ Назад")
        choice = input("👉 ")
        if choice == "1":
            if not self.contract_available:
                print("❌ Вы уже взяли контракт сегодня!")
                return
            if self.active_contract:
                print("❌ У вас уже есть активный контракт!")
                return
            contract = self.generate_contract()
            self.show_contract(contract)
            print("1️⃣ Принять контракт")
            print("2️⃣ Отказаться")
            choice2 = input("👉 ")
            if choice2 == "1":
                self.active_contract = contract
                if contract['name'] not in [p['name'] for p in self.known_people]:
                    self.known_people.append(contract)
                self.contract_available = False
                print(f"✅ Контракт принят! Убейте {contract['name']} {contract['last']} через тетрадь.")
                self.advance_time(10, 3, 2)
            else:
                print("❌ Отказ от контракта")
                self.advance_time(5, 1, 1)
        elif choice == "2":
            if not self.active_contract:
                print("❌ Нет активного контракта!")
                return
            print(f"📋 Активный контракт: {self.active_contract['name']} {self.active_contract['last']}")
            print("1️⃣ Убить через тетрадь")
            print("2️⃣ Назад")
            choice2 = input("👉 ")
            if choice2 == "1":
                name = f"{self.active_contract['name']} {self.active_contract['last']}"
                if name in [k['name'] for k in self.killed]:
                    print("❌ Этот человек уже мёртв!")
                    return

                print("\n💀 ВЫБЕРИТЕ СПОСОБ СМЕРТИ:")
                for i, method in enumerate(DEATH_METHODS, 1):
                    print(f"{i}. {method}")
                print("0. Случайный способ")
                try:
                    method_choice = int(input("👉 "))
                    if method_choice == 0:
                        method = random.choice(DEATH_METHODS)
                    elif 1 <= method_choice <= len(DEATH_METHODS):
                        method = DEATH_METHODS[method_choice-1]
                    else:
                        print("❌ Неверный выбор!")
                        return
                except ValueError:
                    print("❌ Введите число!")
                    return

                self.killed.append({"name": name, "method": method})
                self.suspicion += 15
                print(f"✍️ Имя {name} записано в тетрадь.")
                print(f"💀 Способ: {method}")

                if random.random() < 0.1:
                    print("❌ Вас обманули! Контракт фальшивка.")
                    self.suspicion += 15
                    self.active_contract = None
                else:
                    self.money += self.active_contract['price']
                    print(f"💰 Вы получили {self.active_contract['price']} ₽ за контракт!")
                    self.active_contract = None
                    self.contracts_done += 1
                self.advance_time(5, 3, 2)
            else:
                return
        elif choice == "3":
            if not self.active_contract:
                print("❌ Нет активного контракта!")
                return
            if self.money < 5000:
                print("❌ Недостаточно денег для штрафа! Нужно 5000 ₽")
                return
            self.money -= 5000
            print(f"💸 Вы отказались от контракта. Штраф 5000 ₽. У вас {self.money} ₽")
            self.active_contract = None
            self.advance_time(5, 1, 1)
        elif choice == "4":
            return

    def computer_menu(self):
        print("💻 КОМПЬЮТЕР")
        print("1️⃣  📰 Новости")
        print("2️⃣  💼 Контракты")
        print("3️⃣  💻 Легальная работа")
        print("4️⃣  🔙 Назад")
        choice = input("👉 ")
        if choice == "1":
            self.show_news()
        elif choice == "2":
            self.contract_menu()
        elif choice == "3":
            self.work()
        elif choice == "4":
            return

    def show_news(self):
        print("📰 НОВОСТИ")
        news_list = [
            "В городе спокойно. Ничего не происходит.",
            "Погода сегодня отличная!",
            "На рынке снизились цены на хлеб.",
            "В парке гуляют люди.",
            "Местный театр готовит новую постановку.",
            "В школе прошла линейка.",
            "Городской праздник состоится на выходных.",
            "В библиотеке открылась новая выставка.",
            "На стройке начался новый этап.",
            "В больнице поступило новое оборудование.",
            "Полиция проводит профилактические рейды.",
            "В реке поймали большую рыбу.",
            "На улице стало прохладно.",
            "В городе появилась новая кофейня.",
            "Местный художник выставил свои работы.",
            "В парке посадили новые деревья.",
            "На стадионе прошёл футбольный матч.",
            "В школе объявили каникулы.",
            "В городе открылась новая школа.",
            "На дорогах начались ремонтные работы.",
            "В ресторане новое меню.",
            "В театре будет балет.",
            "В музее выставка картин.",
            "На площади начался концерт.",
            "В парке проходит ярмарка.",
            "Полиция предупреждает о мошенниках.",
            "В городе отмечают праздник.",
            "В школе прошёл выпускной.",
            "Начался сезон дождей.",
            "В городе провели уборку.",
        ]
        if self.investigation and random.random() < 0.5:
            news_list.extend([
                "📰 Расследование убийств продолжается. Кира на свободе.",
                "📰 Полиция не может найти Киру. Он слишком умён.",
                "📰 L заявляет, что скоро поймает Киру.",
                "📰 В новостях обсуждают загадочного убийцу.",
                "📰 Кира стал легендой. Люди боятся выходить на улицу.",
                "📰 L нанёс удар по преступности.",
                "📰 Полиция признала, что не может поймать Киру.",
                "📰 Кира оставляет послания.",
                "📰 Новое убийство, совершённое Кирой.",
                "📰 Кира стал символом справедливости для многих.",
            ])
        if self.ending == "good":
            news_list.extend([
                "🌟 Мир признаёт Киру богом! Преступность падает!",
                "🌟 Кира создал новый мир без преступников!",
                "🌟 Войны прекратились. Мир живёт в порядке.",
            ])
        elif self.ending == "neutral":
            news_list.extend([
                "😐 Кира скрывается. Полиция ищет его.",
                "😐 Мир не знает, кто такой Кира. Но он всё ещё жив.",
                "😐 Кира стал легендой. Но его время прошло.",
            ])
        print(random.choice(news_list))
        input("Нажмите Enter...")
        self.advance_time(5, 1, 0)

    def main_menu(self):
        while self.running:
            self.show_stats()
            if self.investigation:
                print("📢 ВНИМАНИЕ! Идёт расследование по делу Киры!")
            if self.l_killed:
                print("🌟 L мёртв! Вы победили!")
            if self.ending == "good":
                print("🌟 ВЫ ПОБЕДИЛИ! Игра продолжается...")
            elif self.ending == "neutral":
                print("😐 ВЫ В БЕГАХ... Игра продолжается...")
            elif self.ending == "bad":
                print("⛓️ ВЫ В ТЮРЬМЕ. Начать заново? (введите 'restart')")
            print("ГЛАВНОЕ МЕНЮ:")
            print("1️⃣  📓 Тетрадь смерти")
            print("2️⃣  📱 Телефон")
            print("3️⃣  🏠 Дом")
            print("4️⃣  💻 Компьютер")
            print("5️⃣  🚶 Гулять по городу")
            print("6️⃣  💾 Сохранить игру")
            print("7️⃣  🏠 Недвижимость")
            print("0️⃣  🚪 Выйти")
            choice = input("👉 ")

            if self.ending == "bad" and choice.lower() == "restart":
                self.__init__()
                self.player_name = input("Введите ваше имя: ")
                print(f"👤 Добро пожаловать, {self.player_name}!")
                print("📖 23 апреля 2010 года. Вы нашли тетрадь смерти...")
                self.story_triggered = True
                self.story_index = 1
                input("Нажмите Enter чтобы начать...")
                for _ in range(3):
                    person = self.generate_person()
                    self.known_people.append(person)
                continue

            if choice == "1":
                self.notebook()
            elif choice == "2":
                self.phone_menu()
            elif choice == "3":
                self.home_menu()
            elif choice == "4":
                self.computer_menu()
            elif choice == "5":
                self.walk_menu()
            elif choice == "6":
                self.save()
                print("💾 Игра сохранена!")
            elif choice == "7":
                self.buy_house()
            elif choice == "0":
                self.running = False
                print("🚪 Выход из игры...")
            else:
                print("❌ Неверный выбор!")

    def phone_menu(self):
        print("📱 ТЕЛЕФОН")
        print("1️⃣  🎰 Казино")
        print("2️⃣  💸 Взять в долг")
        if self.informant_met and not self.informant_paid and not self.l_killed:
            print("3️⃣  🕵️ Позвонить информатору")
        if self.business_debt > 0:
            print("4️⃣  💰 Оплатить долг бизнеса")
        if self.girl_phone and not self.girl_met:
            print("5️⃣  💕 Свидание")
        print("3️⃣  🔙 Назад")
        choice = input("👉 ")

        if choice == "1":
            self.casino()
        elif choice == "2":
            self.take_debt()
        elif choice == "3":
            if self.informant_met and not self.informant_paid and not self.l_killed:
                self.call_informant()
            else:
                return
        elif choice == "4" and self.business_debt > 0:
            self.pay_business_debt()
        elif choice == "5" and self.girl_phone and not self.girl_met:
            self.girl_date()
        else:
            print("❌ Неверный выбор!")

    def home_menu(self):
        print("🏠 ДОМ")
        if self.fridge:
            print("🍔 Холодильник:")
            for i, item in enumerate(self.fridge):
                print(f"  {i+1}. {item['name']}")
        if self.house > 0:
            print(f"🏠 Жильё: {HOUSES[self.house-1]['name']} (бонус энергии +{HOUSES[self.house-1]['energy_bonus']})")
        print("1️⃣  🍽️ Поесть")
        print("2️⃣  😴 Поспать")
        print("3️⃣  🔙 Назад")
        choice = input("👉 ")
        if choice == "1":
            self.eat()
        elif choice == "2":
            self.sleep()
        elif choice == "3":
            return

    def walk_menu(self):
        print("🚶 ГУЛЯТЬ ПО ГОРОДУ")
        print("1️⃣  🛒 Продуктовый магазин")
        print("2️⃣  🚶 Просто гулять")
        print("3️⃣  🚗 Автосалон")
        print("4️⃣  🔙 Назад")
        choice = input("👉 ")
        if choice == "1":
            self.buy_product()
        elif choice == "2":
            time_reduce = 0
            energy_reduce = 0
            if self.car:
                time_reduce = self.car.get("time_reduce", 0)
                energy_reduce = self.car.get("energy_reduce", 0)
                if random.random() < 0.05:
                    repair_cost = self.car.get("repair_cost", 500)
                    print(f"🚗 У вашей машины поломка! Ремонт {repair_cost} ₽")
                    self.money -= repair_cost
                    self.advance_time(30, 5, 3)
            self.walk()
        elif choice == "3":
            self.buy_car()
        elif choice == "4":
            return

def main():
    game = Game()
    print("=" * 50)
    print("📓 ДОБРО ПОЖАЛОВАТЬ В ТЕТРАДЬ СМЕРТИ!")
    print("=" * 50)
    print("1️⃣ Новая игра")
    print("2️⃣ Загрузить игру")
    choice = input("👉 ")

    if choice == "2":
        if game.load():
            print("✅ Игра загружена!")
            game.main_menu()
            return
        else:
            print("❌ Нет сохранения! Начинаем новую игру.")
            choice = "1"

    if choice == "1":
        game.player_name = input("Введите ваше имя: ")
        print(f"👤 Добро пожаловать, {game.player_name}!")
        print("📖 23 апреля 2010 года. Вы нашли тетрадь смерти...")
        game.story_triggered = True
        print("=" * 50)
        print("📖 СЮЖЕТНОЕ СОБЫТИЕ:")
        print("=" * 50)
        print("📓 Вы нашли тетрадь смерти! Рюк появился перед вами.")
        print("🖊️ 'Это тетрадь смерти. Тот, чьё имя будет вписано, умрёт.'")
        print("💭 Вы понимаете, что это шанс создать новый мир...")
        print("=" * 50)
        game.story_index = 1
        input("Нажмите Enter чтобы начать...")
        for _ in range(3):
            person = game.generate_person()
            game.known_people.append(person)
        game.main_menu()
    else:
        print("❌ Неверный выбор! Начинаем новую игру.")
        game.player_name = input("Введите ваше имя: ")
        print(f"👤 Добро пожаловать, {game.player_name}!")
        print("📖 23 апреля 2010 года. Вы нашли тетрадь смерти...")
        game.story_triggered = True
        print("=" * 50)
        print("📖 СЮЖЕТНОЕ СОБЫТИЕ:")
        print("=" * 50)
        print("📓 Вы нашли тетрадь смерти! Рюк появился перед вами.")
        print("🖊️ 'Это тетрадь смерти. Тот, чьё имя будет вписано, умрёт.'")
        print("💭 Вы понимаете, что это шанс создать новый мир...")
        print("=" * 50)
        game.story_index = 1
        input("Нажмите Enter чтобы начать...")
        for _ in range(3):
            person = game.generate_person()
            game.known_people.append(person)
        game.main_menu()

if __name__ == "__main__":
    main()
