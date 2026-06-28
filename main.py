import random
import json
import os
import time
from datetime import datetime, timedelta

# ============== ДАННЫЕ ИГРЫ ==============

PRODUCTS = [
    {"name": "Хлеб", "hunger": 10, "energy": -5, "price": 50, "time": 1},
    {"name": "Багет", "hunger": 12, "energy": -5, "price": 70, "time": 1},
    {"name": "Булка", "hunger": 8, "energy": -3, "price": 40, "time": 1},
    {"name": "Круассан", "hunger": 10, "energy": 0, "price": 80, "time": 1},
    {"name": "Пирожок", "hunger": 12, "energy": -5, "price": 60, "time": 1},
    {"name": "Курица", "hunger": 20, "energy": 5, "price": 200, "time": 2},
    {"name": "Говядина", "hunger": 22, "energy": 5, "price": 300, "time": 2},
    {"name": "Свинина", "hunger": 20, "energy": 3, "price": 250, "time": 2},
    {"name": "Колбаса", "hunger": 15, "energy": 0, "price": 180, "time": 1},
    {"name": "Бекон", "hunger": 18, "energy": -5, "price": 220, "time": 1},
    {"name": "Лосось", "hunger": 15, "energy": 10, "price": 350, "time": 2},
    {"name": "Тунец", "hunger": 15, "energy": 8, "price": 300, "time": 2},
    {"name": "Скумбрия", "hunger": 14, "energy": 5, "price": 200, "time": 1},
    {"name": "Форель", "hunger": 16, "energy": 8, "price": 320, "time": 2},
    {"name": "Сардины", "hunger": 12, "energy": 5, "price": 150, "time": 1},
    {"name": "Молоко", "hunger": 10, "energy": 5, "price": 80, "time": 1},
    {"name": "Йогурт", "hunger": 10, "energy": 5, "price": 100, "time": 1},
    {"name": "Сыр", "hunger": 12, "energy": 5, "price": 150, "time": 1},
    {"name": "Масло", "hunger": 8, "energy": 5, "price": 120, "time": 1},
    {"name": "Кефир", "hunger": 10, "energy": 3, "price": 70, "time": 1},
    {"name": "Яблоко", "hunger": 8, "energy": 10, "price": 50, "time": 1},
    {"name": "Груша", "hunger": 8, "energy": 10, "price": 60, "time": 1},
    {"name": "Апельсин", "hunger": 8, "energy": 12, "price": 70, "time": 1},
    {"name": "Банан", "hunger": 10, "energy": 15, "price": 80, "time": 1},
    {"name": "Киви", "hunger": 6, "energy": 10, "price": 60, "time": 1},
    {"name": "Картошка", "hunger": 10, "energy": 5, "price": 40, "time": 1},
    {"name": "Помидор", "hunger": 8, "energy": 5, "price": 50, "time": 1},
    {"name": "Огурец", "hunger": 6, "energy": 3, "price": 30, "time": 1},
    {"name": "Морковь", "hunger": 8, "energy": 5, "price": 35, "time": 1},
    {"name": "Лук", "hunger": 6, "energy": 0, "price": 25, "time": 1},
    {"name": "Пицца", "hunger": 25, "energy": -10, "price": 400, "time": 5},
    {"name": "Бургер", "hunger": 22, "energy": -8, "price": 250, "time": 3},
    {"name": "Лапша", "hunger": 20, "energy": -5, "price": 200, "time": 3},
    {"name": "Суп", "hunger": 20, "energy": 5, "price": 180, "time": 3},
    {"name": "Пельмени", "hunger": 25, "energy": -5, "price": 280, "time": 4},
    {"name": "Шоколад", "hunger": 5, "energy": 15, "price": 120, "time": 1},
    {"name": "Печенье", "hunger": 5, "energy": 10, "price": 80, "time": 1},
    {"name": "Мармелад", "hunger": 3, "energy": 10, "price": 100, "time": 1},
    {"name": "Торт", "hunger": 10, "energy": 5, "price": 300, "time": 3},
    {"name": "Пряник", "hunger": 5, "energy": 8, "price": 60, "time": 1},
    {"name": "Кофе", "hunger": 0, "energy": 15, "price": 100, "time": 1},
    {"name": "Чай", "hunger": 0, "energy": 10, "price": 50, "time": 1},
    {"name": "Сок", "hunger": 5, "energy": 8, "price": 80, "time": 1},
    {"name": "Лимонад", "hunger": 3, "energy": 5, "price": 60, "time": 1},
    {"name": "Кола", "hunger": 3, "energy": 8, "price": 70, "time": 1},
    {"name": "Red Bull", "hunger": -5, "energy": 30, "price": 180, "time": 1},
    {"name": "Монстр", "hunger": -5, "energy": 28, "price": 200, "time": 1},
    {"name": "Flash", "hunger": -3, "energy": 25, "price": 150, "time": 1},
    {"name": "Adrenalin", "hunger": -5, "energy": 30, "price": 220, "time": 1},
    {"name": "Drive", "hunger": -3, "energy": 25, "price": 160, "time": 1},
    {"name": "Картошка фри", "hunger": 20, "energy": -15, "price": 150, "time": 2},
    {"name": "Наггетсы", "hunger": 18, "energy": -10, "price": 200, "time": 2},
    {"name": "Хот-дог", "hunger": 20, "energy": -10, "price": 120, "time": 2},
    {"name": "Сэндвич", "hunger": 18, "energy": -5, "price": 130, "time": 2},
    {"name": "Шаурма", "hunger": 25, "energy": -15, "price": 280, "time": 3},
    {"name": "Киноа", "hunger": 15, "energy": 20, "price": 350, "time": 2},
    {"name": "Чиа", "hunger": 10, "energy": 15, "price": 300, "time": 1},
    {"name": "Спирулина", "hunger": 5, "energy": 10, "price": 400, "time": 1},
    {"name": "Овес", "hunger": 15, "energy": 10, "price": 150, "time": 1},
    {"name": "Мюсли", "hunger": 15, "energy": 15, "price": 200, "time": 1},
    {"name": "Грецкий орех", "hunger": 10, "energy": 15, "price": 180, "time": 1},
    {"name": "Миндаль", "hunger": 10, "energy": 15, "price": 200, "time": 1},
    {"name": "Арахис", "hunger": 10, "energy": 10, "price": 120, "time": 1},
    {"name": "Кешью", "hunger": 10, "energy": 15, "price": 250, "time": 1},
    {"name": "Фисташки", "hunger": 10, "energy": 12, "price": 220, "time": 1},
    {"name": "Кетчуп", "hunger": 2, "energy": 0, "price": 30, "time": 0},
    {"name": "Майонез", "hunger": 2, "energy": 0, "price": 40, "time": 0},
    {"name": "Горчица", "hunger": 2, "energy": 0, "price": 30, "time": 0},
    {"name": "Соевый", "hunger": 2, "energy": 0, "price": 35, "time": 0},
    {"name": "Барбекю", "hunger": 2, "energy": 0, "price": 45, "time": 0},
    {"name": "Хлопья", "hunger": 15, "energy": 10, "price": 180, "time": 1},
    {"name": "Гранола", "hunger": 15, "energy": 15, "price": 220, "time": 1},
    {"name": "Каша", "hunger": 20, "energy": 10, "price": 120, "time": 2},
    {"name": "Панкейки", "hunger": 18, "energy": 5, "price": 200, "time": 3},
    {"name": "Омлет", "hunger": 20, "energy": 10, "price": 150, "time": 3},
    {"name": "Горошек", "hunger": 10, "energy": -5, "price": 80, "time": 1},
    {"name": "Кукуруза", "hunger": 10, "energy": -5, "price": 90, "time": 1},
    {"name": "Фасоль", "hunger": 12, "energy": -5, "price": 100, "time": 1},
    {"name": "Тушенка", "hunger": 18, "energy": -5, "price": 150, "time": 1},
    {"name": "Паштет", "hunger": 15, "energy": -3, "price": 120, "time": 1},
    {"name": "Соль", "hunger": 0, "energy": 0, "price": 20, "time": 0},
    {"name": "Перец", "hunger": 0, "energy": 0, "price": 25, "time": 0},
    {"name": "Корица", "hunger": 0, "energy": 0, "price": 30, "time": 0},
    {"name": "Ваниль", "hunger": 0, "energy": 0, "price": 40, "time": 0},
    {"name": "Паприка", "hunger": 0, "energy": 0, "price": 25, "time": 0},
    {"name": "Пиво", "hunger": 5, "energy": -30, "price": 150, "time": 2},
    {"name": "Вино", "hunger": 5, "energy": -30, "price": 400, "time": 3},
    {"name": "Водка", "hunger": 5, "energy": -40, "price": 300, "time": 2},
    {"name": "Ром", "hunger": 5, "energy": -35, "price": 500, "time": 2},
    {"name": "Виски", "hunger": 5, "energy": -35, "price": 600, "time": 2},
    {"name": "Протеин", "hunger": 5, "energy": 10, "price": 400, "time": 1},
    {"name": "Клетчатка", "hunger": 5, "energy": 5, "price": 300, "time": 1},
    {"name": "Омега-3", "hunger": 3, "energy": 8, "price": 350, "time": 1},
    {"name": "Коллаген", "hunger": 3, "energy": 5, "price": 500, "time": 1},
    {"name": "Витамины", "hunger": 3, "energy": 10, "price": 200, "time": 1},
    {"name": "Чипсы", "hunger": 3, "energy": 0, "price": 60, "time": 1},
    {"name": "Сухарики", "hunger": 3, "energy": 0, "price": 40, "time": 1},
    {"name": "Попкорн", "hunger": 3, "energy": 0, "price": 50, "time": 1},
    {"name": "Маршмеллоу", "hunger": 3, "energy": 5, "price": 80, "time": 1},
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

# 100 способов смерти
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
]

HOUSES = [
    {"name": "🏚️ Комната в общежитии", "price": 10000, "energy_bonus": 5},
    {"name": "🏚️ Маленькая квартира", "price": 30000, "energy_bonus": 10},
    {"name": "🏚️ Средняя квартира", "price": 60000, "energy_bonus": 15},
    {"name": "🏚️ Большая квартира", "price": 100000, "energy_bonus": 20},
    {"name": "🏚️ Квартира в центре", "price": 150000, "energy_bonus": 25},
    {"name": "🏚️ Пентхаус", "price": 300000, "energy_bonus": 35},
    {"name": "🏚️ Особняк", "price": 500000, "energy_bonus": 50},
]

EVENTS = [
    {"text": "Вы нашли 100 рублей на земле!", "money": 100, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вы выиграли в лотерею 500 рублей!", "money": 500, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вам вернули старый долг 300 рублей!", "money": 300, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вы нашли золотую цепочку!", "money": 1000, "hunger": 0, "energy": 0, "health": 0},
    {"text": "На вас напали грабители! -300 рублей", "money": -300, "hunger": 0, "energy": -10, "health": -20},
    {"text": "Вас чуть не сбила машина", "money": 0, "hunger": 0, "energy": -10, "health": -10},
    {"text": "Вы попали в драку и получили травму", "money": 0, "hunger": 0, "energy": -20, "health": -30},
    {"text": "Вас остановила полиция для проверки", "money": -500, "hunger": 0, "energy": -10, "health": 0},
    {"text": "Вы простудились. Лекарства 100 рублей", "money": -100, "hunger": 0, "energy": -10, "health": -10},
    {"text": "Вы отравились едой", "money": 0, "hunger": -20, "energy": -20, "health": -20},
    {"text": "У вас аллергия. Таблетки 80 рублей", "money": -80, "hunger": 0, "energy": -5, "health": -10},
    {"text": "Вы заболели гриппом", "money": -200, "hunger": 0, "energy": -30, "health": -30},
    {"text": "Порвалась одежда. Новая 500 рублей", "money": -500, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Сломался телефон. Ремонт 1000 рублей", "money": -1000, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Потеряли ключи. Новые 300 рублей", "money": -300, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Подарок на 400 рублей", "money": 400, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Сильный дождь, промокли", "money": 0, "hunger": 0, "energy": -10, "health": -5},
    {"text": "Сильная жара. Вода 50 рублей", "money": -50, "hunger": 0, "energy": -5, "health": 0},
    {"text": "Тёплая погода подняла настроение", "money": 0, "hunger": 0, "energy": 15, "health": 5},
    {"text": "Пожар в соседнем доме", "money": -1000, "hunger": 0, "energy": -30, "health": -10},
    {"text": "Авария. Помогли пострадавшим -300", "money": -300, "hunger": 0, "energy": -10, "health": 0},
    {"text": "Спасли кошку. Вознаграждение 200", "money": 200, "hunger": 0, "energy": -10, "health": 0},
]

SEASONAL_EVENTS = {
    "winter": [
        {"text": "Сильный снегопад! Вы замёрзли", "money": -100, "hunger": 0, "energy": -10, "health": -5},
        {"text": "Слепили снеговика! + настроение", "money": 0, "hunger": 0, "energy": 5, "health": 0},
    ],
    "spring": [
        {"text": "Весеннее тепло! + энергия", "money": 0, "hunger": 0, "energy": 10, "health": 5},
        {"text": "Пошёл дождь, промокли", "money": 0, "hunger": 0, "energy": -5, "health": -5},
    ],
    "summer": [
        {"text": "Сильная жара! Мороженое 50р", "money": -50, "hunger": 5, "energy": 5, "health": 0},
        {"text": "Загорали и обгорели", "money": 0, "hunger": 0, "energy": -5, "health": -10},
    ],
    "autumn": [
        {"text": "Листопад! + настроение", "money": 0, "hunger": 0, "energy": 5, "health": 0},
        {"text": "Ветер сорвал шапку -200р", "money": -200, "hunger": 0, "energy": 0, "health": 0},
    ]
}

# ============== СЮЖЕТ ==============
STORY_EVENTS = [
    {"day": 1, "text": "Вы нашли тетрадь смерти! Рюк появился перед вами."},
    {"day": 2, "text": "В новостях сообщают о загадочной смерти криминального авторитета."},
    {"day": 3, "text": "Интерпол подключился к расследованию. Впервые показывают L."},
    {"day": 4, "text": "L заявляет: 'Я найду Киру и остановлю его'."},
    {"day": 5, "text": "L заявил, что Кира находится в России! Это ложный след."},
    {"day": 6, "text": "Вас останавливает полицейский для проверки документов."},
    {"day": 7, "text": "L заявил: 'Кира - студент, ему 17-20 лет'. Вы в шоке!"},
    {"day": 8, "text": "Вы встречаете информатора. Он знает, кто такой L. Но просит 100 000 ₽."},
    {"day": 9, "text": "Новости: L приближается к разгадке."},
    {"day": 10, "text": "L даёт пресс-конференцию."},
    {"day": 11, "text": "Вы следите за полицейскими участками."},
    {"day": 12, "text": "Информатор: 'Я могу сказать имя L за 100 000 ₽'."},
    {"day": 13, "text": "Вы узнаёте, что L связан с Ватари и Интерполом."},
    {"day": 14, "text": "L нанёс удар по преступности."},
    {"day": 15, "text": "Вы нашли информацию: L также известен как 'L Lawliet'."},
    {"day": 16, "text": "Информатор: 'У меня есть фото L! Приходи!'"},
    {"day": 17, "text": "L: 'Кира, я знаю, что ты смотришь меня'."},
    {"day": 18, "text": "Вы узнали лицо L! Это он — L Lawliet."},
    {"day": 19, "text": "L намекает, что знает, кто вы."},
    {"day": 20, "text": "Встреча с L. Вы должны убить его."},
    {"day": 21, "text": "Вы узнаёте полное имя L: L Lawliet."},
    {"day": 22, "text": "ФИНАЛ: Вы записываете имя L Lawliet в тетрадь смерти."},
]

# ============== КЛАСС ИГРЫ ==============

class Game:
    def __init__(self):
        self.player_name = ""
        self.money = 5000
        self.hunger = 80
        self.energy = 70
        self.health = 100
        self.suspicion = 0
        self.fame = 0
        self.title = "Студент"
        self.day = 1
        self.date = datetime(2010, 4, 23)
        self.time = datetime(2010, 4, 23, 8, 0, 0)  # Текущее время с секундами
        self.fridge = []
        self.killed = []
        self.debt = 0
        self.debt_days = 0
        self.investigation = False
        self.kira_news = False
        self.location = "home"
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
        self.news_hour = 0

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
            "health": self.health,
            "suspicion": self.suspicion,
            "fame": self.fame,
            "title": self.title,
            "day": self.day,
            "date": self.date.isoformat(),
            "time": self.time.isoformat(),
            "fridge": self.fridge,
            "killed": self.killed,
            "debt": self.debt,
            "debt_days": self.debt_days,
            "investigation": self.investigation,
            "kira_news": self.kira_news,
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
            "contract_available": self.contract_available
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
        self.health = data["health"]
        self.suspicion = data["suspicion"]
        self.fame = data.get("fame", 0)
        self.title = data["title"]
        self.day = data["day"]
        self.date = datetime.fromisoformat(data["date"])
        self.time = datetime.fromisoformat(data.get("time", data["date"] + "T08:00:00"))
        self.fridge = data["fridge"]
        self.killed = data["killed"]
        self.debt = data["debt"]
        self.debt_days = data["debt_days"]
        self.investigation = data["investigation"]
        self.kira_news = data["kira_news"]
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
        self.loaded = True
        return True

    def auto_save(self):
        self.save()

    def advance_time(self, minutes, energy_cost=0):
        """Продвинуть время на N минут, потратить энергию"""
        self.time += timedelta(minutes=minutes)
        self.energy -= energy_cost
        if self.energy < 0:
            self.energy = 0
        # Проверка на новый день
        if self.time.hour == 0 and self.time.minute == 0 and self.time.second == 0:
            self.new_day()
        # Генерация новостей каждый час
        if self.time.minute == 0 and self.time.second == 0:
            self.news_hour += 1
            self.generate_hourly_news()

    def new_day(self):
        """Наступление нового дня"""
        self.day += 1
        self.date += timedelta(days=1)
        self.hunger -= random.randint(5, 10)
        self.energy -= random.randint(5, 10)
        if self.hunger < 0:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0
        self.contract_available = True
        self.news_hour = 0
        self.check_story()
        self.auto_save()

        if self.hunger <= 10:
            print("❌ Вы упали в голодный обморок! Вас увезли в больницу.")
            self.hunger = 50
            self.energy = 30
            self.money -= 3000
            self.health -= 20
            self.time += timedelta(days=7)
            self.day += 7
            print(f"🏥 Вы провели неделю в больнице. -3000 ₽")

        if self.energy <= random.randint(0, 15):
            missing = 100 - self.energy
            minutes = missing * 15
            print(f"💤 Вы вырубились от усталости на {minutes} минут!")
            self.energy = 30
            if random.random() < 0.3:
                stolen = random.randint(100, 1000)
                self.money -= stolen
                print(f"👤 Вас обокрали на {stolen} ₽")

        if self.debt > 0:
            self.debt_days += 1
            if self.debt_days >= 5:
                self.suspicion += 10
                self.debt = 0
                self.debt_days = 0
                print("⚠️ Вы не вернули долг! Подозрение +10%")

        if self.suspicion >= 100 and self.fame < 100:
            self.fame = min(self.fame + 1, 100)
            self.suspicion = min(self.suspicion, 100)
            if self.fame >= 100:
                self.title = "Кира - Бог нового мира"
                print("🌟 ВЫ СТАЛИ КИРОЙ! Мир признаёт вас богом!")

        if self.suspicion >= 100:
            self.investigation = True
            self.title = "Кира"
            if not self.kira_news:
                self.kira_news = True
                print("📰 ВНИМАНИЕ! Новости говорят о загадочном убийце по прозвищу Кира!")

        self.active_contract = None

    def check_story(self):
        """Проверка сюжетных событий"""
        if self.story_done:
            return
        if self.story_index >= len(STORY_EVENTS):
            self.story_done = True
            return
        event = STORY_EVENTS[self.story_index]
        if self.day >= event["day"]:
            if self.story_index == 0 and not self.story_triggered:
                self.story_triggered = True
                print("=" * 50)
                print("📖 СЮЖЕТНОЕ СОБЫТИЕ:")
                print("=" * 50)
                print("📓 Вы нашли тетрадь смерти! Рюк появился перед вами.")
                print("🖊️ 'Это тетрадь смерти. Тот, чьё имя будет вписано, умрёт.'")
                print("💭 Вы понимаете, что это шанс создать новый мир...")
                print("💭 Мир без преступников, где правят справедливость и порядок.")
                print("💭 Вы будете богом этого нового мира. Никто не остановит вас.")
                print("=" * 50)
                input("Нажмите Enter чтобы продолжить...")
                self.story_index += 1
            else:
                print("=" * 50)
                print(f"📖 СЮЖЕТНОЕ СОБЫТИЕ: День {event['day']}")
                print("=" * 50)
                print(event["text"])
                print("=" * 50)
                input("Нажмите Enter чтобы продолжить...")
                self.story_index += 1

    def generate_hourly_news(self):
        """Новости каждый час"""
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
        if self.investigation and random.random() < 0.3:
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
        print(f"📰 {random.choice(news_list)}")
        if self.fame > 0 and random.random() < 0.2:
            print(f"🗣️ Люди вокруг говорят о Кире! Ваша слава растёт.")
            self.fame = min(self.fame + 1, 100)

    def show_stats(self):
        status = "❤️" if self.health > 60 else "💔"
        time_str = self.time.strftime("%H:%M:%S")
        months = ["января", "февраля", "марта", "апреля", "мая", "июня",
                  "июля", "августа", "сентября", "октября", "ноября", "декабря"]
        date_str = f"{self.day} {months[self.date.month-1]} {self.date.year}"
        print("=" * 50)
        print(f"        📓 ТЕТРАДЬ СМЕРТИ - СИМУЛЯТОР")
        print(f"        👤 {self.player_name}")
        print(f"        📅 {date_str}  ⏰ {time_str}")
        print("=" * 50)
        print(f" {status} Здоровье: {self.health}%  |  🍔 Голод: {self.hunger}/100")
        print(f" ⚡ Энергия: {self.energy}/100  |  💰 Деньги: {self.money} ₽")
        if self.fame > 0:
            print(f" ⭐ Слава: {self.fame}%  |  🏆 Звание: {self.title}")
        else:
            print(f" 🕵️ Подозрение: {self.suspicion}%  |  🏆 Звание: {self.title}")
        if self.debt > 0:
            print(f" 💸 Долг: {self.debt} ₽ (осталось {5 - self.debt_days} дней)")
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
        pc_level = sum(self.pc_parts.values())
        if pc_level > 0:
            print(f" 💻 Уровень ПК: {pc_level}")
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
        return {"name": name, "last": last, "age": age, "gender": gender, "bio": bio}

    def generate_contract(self):
        person = self.generate_person()
        price = random.randint(2000, 10000)
        person["price"] = price
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
            self.advance_time(5, 2)
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
            self.advance_time(5, 1)
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
            self.advance_time(10, 2)
        else:
            print("📞 'Позвони, когда будут деньги.'")
            self.advance_time(2, 1)

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
                self.advance_time(item.get('time', 5), 2)
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
            self.advance_time(minutes, 0)
            print(f"😴 Вы поспали {hours} часов (+{energy_gain} энергии)")
        except ValueError:
            print("❌ Введите число!")

    def work(self):
        pc_level = sum(self.pc_parts.values())
        bonus_money = 0
        for part, level in self.pc_parts.items():
            if part not in ["mouse", "keyboard"]:
                bonus_money += level

        char_bonus = (self.pc_parts.get("mouse", 0) + self.pc_parts.get("keyboard", 0)) * 0.1
        total_char_value = 1.0 + char_bonus

        print(f"💻 Легальная работа: печатайте 1000 символов")
        print(f"💰 База: 500 ₽ за 1000 символов")
        print(f"💻 Бонус от ПК: +{bonus_money} ₽")
        print(f"🖱️ Бонус от мыши/клавиатуры: символ x{total_char_value:.1f}")
        print(f"💰 Итого за 1000 символов: {int(500 + bonus_money)} ₽")
        print("Введите 'start' чтобы начать печатать. 'stop' - отмена")
        cmd = input("👉 ")
        if cmd.lower() == "start":
            print("🖱️ Начинайте печатать случайные символы...")
            typed = 0
            target = 1000
            while typed < target:
                char = input("Введите символ: ")
                if char == "":
                    continue
                typed += total_char_value
                self.advance_time(1, 0.25)
                print(f"Прогресс: {min(int(typed), target)}/{target} ({min(int(typed*100//target), 100)}%)")
                if typed >= target:
                    reward = int(500 + bonus_money)
                    self.money += reward
                    print(f"✅ Заказ выполнен! +{reward} ₽. У вас {self.money} ₽")
                    break

    def buy_product(self):
        print("🛒 ПРОДУКТОВЫЙ МАГАЗИН")
        print("Категории:")
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
                    self.advance_time(10, 3)
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
                self.advance_time(5, 2)
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
        if 'health' in event:
            self.health += event['health']
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger < 0:
            self.hunger = 0
        if self.energy > 100:
            self.energy = 100
        if self.energy < 0:
            self.energy = 0
        if self.health > 100:
            self.health = 100
        if self.health < 0:
            self.health = 0

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

        self.advance_time(60, 15)

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
                self.advance_time(30, 5)
            else:
                print("❌ Неверный выбор")
        except ValueError:
            print("❌ Введите число!")

    def buy_house(self):
        print("🏠 НЕДВИЖИМОСТЬ")
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
                self.advance_time(30, 5)
            else:
                print("❌ Неверный выбор")
        except ValueError:
            print("❌ Введите число!")

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

                    # Проверка на L
                    if name == "L Lawliet" or (person['name'] == "L" and person['last'] == ""):
                        if not self.l_name_known:
                            print("❌ Вы не знаете полное имя L! Нужно узнать его.")
                            return
                        if not self.l_face_known:
                            print("❌ Вы не знаете лицо L! Нужно увидеть его.")
                            return

                    # Выбор способа смерти
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

                    if name == "L Lawliet":
                        self.l_killed = True
                        self.fame = 100
                        self.title = "Кира - Бог нового мира"
                        print(f"✍️ Имя {name} записано в тетрадь.")
                        print(f"💀 Способ: {method}")
                        print("🫀 L умирает...")
                        print("🌟 МИР ПРИЗНАЁТ ВАС ПОБЕДИТЕЛЕМ!")
                        self.advance_time(5, 3)
                        return

                    print(f"✍️ Имя {name} записано в тетрадь.")
                    print(f"💀 Способ: {method}")

                    if self.active_contract and self.active_contract['name'] == person['name'] and self.active_contract['last'] == person['last']:
                        if random.random() < 0.1:
                            print("❌ Вас обманули! Контракт оказался фальшивкой.")
                            self.suspicion += 15
                            self.active_contract = None
                        else:
                            self.money += self.active_contract['price']
                            print(f"💰 Вы получили {self.active_contract['price']} ₽ за выполнение контракта!")
                            self.active_contract = None
                            self.contracts_done += 1
                    else:
                        print("⚠️ Вы убили случайного человека без контракта.")
                        if random.random() < 0.2:
                            print("📰 Кто-то видел вас! Подозрение сильно выросло!")
                            self.suspicion += 20

                    self.known_people.remove(person)
                    self.advance_time(5, 3)
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
                print("❌ Вы уже взяли контракт сегодня! Ждите следующего дня.")
                return
            if self.active_contract:
                print("❌ У вас уже есть активный контракт! Выполните или откажитесь от него.")
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
                self.advance_time(10, 3)
            else:
                print("❌ Отказ от контракта")
                self.advance_time(5, 1)
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
                    print("❌ Вас обманули! Контракт оказался фальшивкой.")
                    self.suspicion += 15
                    self.active_contract = None
                else:
                    self.money += self.active_contract['price']
                    print(f"💰 Вы получили {self.active_contract['price']} ₽ за выполнение контракта!")
                    self.active_contract = None
                    self.contracts_done += 1
                self.advance_time(5, 3)
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
            self.advance_time(5, 1)
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
            self.generate_hourly_news()
            self.advance_time(5, 1)
            input("Нажмите Enter...")
        elif choice == "2":
            self.contract_menu()
        elif choice == "3":
            self.work()
        elif choice == "4":
            return

    def main_menu(self):
        while self.running:
            self.show_stats()
            if self.investigation:
                print("📢 ВНИМАНИЕ! Идёт расследование по делу Киры!")
            if self.l_killed:
                print("🌟 ВЫ ПОБЕДИЛИ! L мёртв! Мир ваш!")
            print("ГЛАВНОЕ МЕНЮ:")
            print("1️⃣  📓 Тетрадь смерти")
            print("2️⃣  📱 Телефон")
            print("3️⃣  🏠 Дом")
            print("4️⃣  💻 Компьютер")
            print("5️⃣  🚶 Гулять по городу")
            print("6️⃣  💾 Сохранить игру")
            print("0️⃣  🚪 Выйти")
            choice = input("👉 ")

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
        print("4️⃣  🔙 Назад")
        choice = input("👉 ")
        if choice == "1":
            self.casino()
        elif choice == "2":
            self.take_debt()
        elif choice == "3" and self.informant_met and not self.informant_paid and not self.l_killed:
            self.call_informant()
        elif choice == "4" or choice == "":
            return
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
        print("4️⃣  🏠 Недвижимость")
        print("5️⃣  🔙 Назад")
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
                    self.advance_time(30, 5)
            self.walk()
        elif choice == "3":
            self.buy_car()
        elif choice == "4":
            self.buy_house()
        elif choice == "5":
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
        else:
            print("❌ Нет сохранения! Начинаем новую игру.")
            choice = "1"

    if choice == "1":
        game.player_name = input("Введите ваше имя: ")
        print(f"👤 Добро пожаловать, {game.player_name}!")
        print("📖 23 апреля 2010 года. Вы нашли тетрадь смерти...")
        # Первое сюжетное событие
        game.story_triggered = True
        print("=" * 50)
        print("📖 СЮЖЕТНОЕ СОБЫТИЕ:")
        print("=" * 50)
        print("📓 Вы нашли тетрадь смерти! Рюк появился перед вами.")
        print("🖊️ 'Это тетрадь смерти. Тот, чьё имя будет вписано, умрёт.'")
        print("💭 Вы понимаете, что это шанс создать новый мир...")
        print("💭 Мир без преступников, где правят справедливость и порядок.")
        print("💭 Вы будете богом этого нового мира. Никто не остановит вас.")
        print("=" * 50)
        game.story_index = 1
        input("Нажмите Enter чтобы начать...")
        for _ in range(3):
            person = game.generate_person()
            game.known_people.append(person)
    else:
        print("❌ Неверный выбор!")
        return

    game.main_menu()

if __name__ == "__main__":
    main()
