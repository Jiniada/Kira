import random
import json
import os
import time
from datetime import datetime, timedelta

# ============== ДАННЫЕ ИГРЫ ==============

PRODUCTS = [
    # Хлебобулочные
    {"name": "Хлеб", "hunger": 10, "energy": -5, "price": 50},
    {"name": "Багет", "hunger": 12, "energy": -5, "price": 70},
    {"name": "Булка", "hunger": 8, "energy": -3, "price": 40},
    {"name": "Круассан", "hunger": 10, "energy": 0, "price": 80},
    {"name": "Пирожок", "hunger": 12, "energy": -5, "price": 60},
    # Мясные
    {"name": "Курица", "hunger": 20, "energy": 5, "price": 200},
    {"name": "Говядина", "hunger": 22, "energy": 5, "price": 300},
    {"name": "Свинина", "hunger": 20, "energy": 3, "price": 250},
    {"name": "Колбаса", "hunger": 15, "energy": 0, "price": 180},
    {"name": "Бекон", "hunger": 18, "energy": -5, "price": 220},
    # Рыбные
    {"name": "Лосось", "hunger": 15, "energy": 10, "price": 350},
    {"name": "Тунец", "hunger": 15, "energy": 8, "price": 300},
    {"name": "Скумбрия", "hunger": 14, "energy": 5, "price": 200},
    {"name": "Форель", "hunger": 16, "energy": 8, "price": 320},
    {"name": "Сардины", "hunger": 12, "energy": 5, "price": 150},
    # Молочные
    {"name": "Молоко", "hunger": 10, "energy": 5, "price": 80},
    {"name": "Йогурт", "hunger": 10, "energy": 5, "price": 100},
    {"name": "Сыр", "hunger": 12, "energy": 5, "price": 150},
    {"name": "Масло", "hunger": 8, "energy": 5, "price": 120},
    {"name": "Кефир", "hunger": 10, "energy": 3, "price": 70},
    # Фрукты
    {"name": "Яблоко", "hunger": 8, "energy": 10, "price": 50},
    {"name": "Груша", "hunger": 8, "energy": 10, "price": 60},
    {"name": "Апельсин", "hunger": 8, "energy": 12, "price": 70},
    {"name": "Банан", "hunger": 10, "energy": 15, "price": 80},
    {"name": "Киви", "hunger": 6, "energy": 10, "price": 60},
    # Овощи
    {"name": "Картошка", "hunger": 10, "energy": 5, "price": 40},
    {"name": "Помидор", "hunger": 8, "energy": 5, "price": 50},
    {"name": "Огурец", "hunger": 6, "energy": 3, "price": 30},
    {"name": "Морковь", "hunger": 8, "energy": 5, "price": 35},
    {"name": "Лук", "hunger": 6, "energy": 0, "price": 25},
    # Готовые блюда
    {"name": "Пицца", "hunger": 25, "energy": -10, "price": 400},
    {"name": "Бургер", "hunger": 22, "energy": -8, "price": 250},
    {"name": "Лапша", "hunger": 20, "energy": -5, "price": 200},
    {"name": "Суп", "hunger": 20, "energy": 5, "price": 180},
    {"name": "Пельмени", "hunger": 25, "energy": -5, "price": 280},
    # Сладости
    {"name": "Шоколад", "hunger": 5, "energy": 15, "price": 120},
    {"name": "Печенье", "hunger": 5, "energy": 10, "price": 80},
    {"name": "Мармелад", "hunger": 3, "energy": 10, "price": 100},
    {"name": "Торт", "hunger": 10, "energy": 5, "price": 300},
    {"name": "Пряник", "hunger": 5, "energy": 8, "price": 60},
    # Напитки
    {"name": "Кофе", "hunger": 0, "energy": 15, "price": 100},
    {"name": "Чай", "hunger": 0, "energy": 10, "price": 50},
    {"name": "Сок", "hunger": 5, "energy": 8, "price": 80},
    {"name": "Лимонад", "hunger": 3, "energy": 5, "price": 60},
    {"name": "Кола", "hunger": 3, "energy": 8, "price": 70},
    # Энергетики
    {"name": "Red Bull", "hunger": -5, "energy": 30, "price": 180},
    {"name": "Монстр", "hunger": -5, "energy": 28, "price": 200},
    {"name": "Flash", "hunger": -3, "energy": 25, "price": 150},
    {"name": "Adrenalin", "hunger": -5, "energy": 30, "price": 220},
    {"name": "Drive", "hunger": -3, "energy": 25, "price": 160},
    # Фастфуд
    {"name": "Картошка фри", "hunger": 20, "energy": -15, "price": 150},
    {"name": "Наггетсы", "hunger": 18, "energy": -10, "price": 200},
    {"name": "Хот-дог", "hunger": 20, "energy": -10, "price": 120},
    {"name": "Сэндвич", "hunger": 18, "energy": -5, "price": 130},
    {"name": "Шаурма", "hunger": 25, "energy": -15, "price": 280},
    # Суперфуды
    {"name": "Киноа", "hunger": 15, "energy": 20, "price": 350},
    {"name": "Чиа", "hunger": 10, "energy": 15, "price": 300},
    {"name": "Спирулина", "hunger": 5, "energy": 10, "price": 400},
    {"name": "Овес", "hunger": 15, "energy": 10, "price": 150},
    {"name": "Мюсли", "hunger": 15, "energy": 15, "price": 200},
    # Орехи
    {"name": "Грецкий орех", "hunger": 10, "energy": 15, "price": 180},
    {"name": "Миндаль", "hunger": 10, "energy": 15, "price": 200},
    {"name": "Арахис", "hunger": 10, "energy": 10, "price": 120},
    {"name": "Кешью", "hunger": 10, "energy": 15, "price": 250},
    {"name": "Фисташки", "hunger": 10, "energy": 12, "price": 220},
    # Соусы
    {"name": "Кетчуп", "hunger": 2, "energy": 0, "price": 30},
    {"name": "Майонез", "hunger": 2, "energy": 0, "price": 40},
    {"name": "Горчица", "hunger": 2, "energy": 0, "price": 30},
    {"name": "Соевый", "hunger": 2, "energy": 0, "price": 35},
    {"name": "Барбекю", "hunger": 2, "energy": 0, "price": 45},
    # Завтраки
    {"name": "Хлопья", "hunger": 15, "energy": 10, "price": 180},
    {"name": "Гранола", "hunger": 15, "energy": 15, "price": 220},
    {"name": "Каша", "hunger": 20, "energy": 10, "price": 120},
    {"name": "Панкейки", "hunger": 18, "energy": 5, "price": 200},
    {"name": "Омлет", "hunger": 20, "energy": 10, "price": 150},
    # Консервы
    {"name": "Горошек", "hunger": 10, "energy": -5, "price": 80},
    {"name": "Кукуруза", "hunger": 10, "energy": -5, "price": 90},
    {"name": "Фасоль", "hunger": 12, "energy": -5, "price": 100},
    {"name": "Тушенка", "hunger": 18, "energy": -5, "price": 150},
    {"name": "Паштет", "hunger": 15, "energy": -3, "price": 120},
    # Специи
    {"name": "Соль", "hunger": 0, "energy": 0, "price": 20},
    {"name": "Перец", "hunger": 0, "energy": 0, "price": 25},
    {"name": "Корица", "hunger": 0, "energy": 0, "price": 30},
    {"name": "Ваниль", "hunger": 0, "energy": 0, "price": 40},
    {"name": "Паприка", "hunger": 0, "energy": 0, "price": 25},
    # Алкоголь
    {"name": "Пиво", "hunger": 5, "energy": -30, "price": 150},
    {"name": "Вино", "hunger": 5, "energy": -30, "price": 400},
    {"name": "Водка", "hunger": 5, "energy": -40, "price": 300},
    {"name": "Ром", "hunger": 5, "energy": -35, "price": 500},
    {"name": "Виски", "hunger": 5, "energy": -35, "price": 600},
    # Здоровое
    {"name": "Протеин", "hunger": 5, "energy": 10, "price": 400},
    {"name": "Клетчатка", "hunger": 5, "energy": 5, "price": 300},
    {"name": "Омега-3", "hunger": 3, "energy": 8, "price": 350},
    {"name": "Коллаген", "hunger": 3, "energy": 5, "price": 500},
    {"name": "Витамины", "hunger": 3, "energy": 10, "price": 200},
    # Разное
    {"name": "Чипсы", "hunger": 3, "energy": 0, "price": 60},
    {"name": "Сухарики", "hunger": 3, "energy": 0, "price": 40},
    {"name": "Попкорн", "hunger": 3, "energy": 0, "price": 50},
    {"name": "Маршмеллоу", "hunger": 3, "energy": 5, "price": 80},
    {"name": "Жевачка", "hunger": 1, "energy": 0, "price": 20},
]

FIRST_NAMES = ["Александр", "Дмитрий", "Максим", "Иван", "Андрей", "Артем", "Михаил", "Сергей", "Николай", "Владимир",
               "Алексей", "Егор", "Павел", "Роман", "Кирилл", "Виктор", "Олег", "Юрий", "Анатолий", "Григорий",
               "Анна", "Екатерина", "Мария", "Ольга", "Татьяна", "Наталья", "Ирина", "Елена", "Светлана", "Юлия",
               "Алиса", "Дарья", "Полина", "Виктория", "Ксения", "Евгения", "Валерия", "Анастасия", "Варвара", "Ульяна"]

LAST_NAMES = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Волков", "Козлов", "Морозов", "Новиков",
              "Соколов", "Лебедев", "Ковалев", "Медведев", "Виноградов", "Белов", "Тарасов", "Крылов", "Орлов", "Мамонтов",
              "Морозова", "Соколова", "Лебедева", "Ковалева", "Медведева", "Виноградова", "Белова", "Тарасова", "Крылова", "Орлова"]

EVENTS = [
    # Удача
    {"text": "Вы нашли 100 рублей на земле!", "money": 100, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вы выиграли в лотерею 500 рублей!", "money": 500, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вам вернули старый долг 300 рублей!", "money": 300, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вы нашли золотую цепочку!", "money": 1000, "hunger": 0, "energy": 0, "health": 0},
    # Опасность
    {"text": "На вас напали грабители! -300 рублей", "money": -300, "hunger": 0, "energy": -10, "health": -20},
    {"text": "Вас чуть не сбила машина", "money": 0, "hunger": 0, "energy": -10, "health": -10},
    {"text": "Вы попали в драку и получили травму", "money": 0, "hunger": 0, "energy": -20, "health": -30},
    {"text": "Вас остановила полиция для проверки", "money": -500, "hunger": 0, "energy": -10, "health": 0, "suspicion": 10},
    # Болезни
    {"text": "Вы простудились. Пришлось купить лекарства за 100 рублей", "money": -100, "hunger": 0, "energy": -10, "health": -10},
    {"text": "Вы отравились некачественной едой", "money": 0, "hunger": -20, "energy": -20, "health": -20},
    {"text": "У вас аллергия. Купили таблетки за 80 рублей", "money": -80, "hunger": 0, "energy": -5, "health": -10},
    {"text": "Вы заболели гриппом", "money": -200, "hunger": 0, "energy": -30, "health": -30},
    # Быт
    {"text": "У вас порвалась одежда. Пришлось купить новую за 500 рублей", "money": -500, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Сломался телефон. Ремонт 1000 рублей", "money": -1000, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вы потеряли ключи и потратили 300 на новые", "money": -300, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Вам подарили подарок на 400 рублей", "money": 400, "hunger": 0, "energy": 0, "health": 0},
    # Погода
    {"text": "Начался сильный дождь, вы промокли", "money": 0, "hunger": 0, "energy": -10, "health": -5},
    {"text": "Сильная жара. Вы выпили воды за 50 рублей", "money": -50, "hunger": 0, "energy": -5, "health": 0},
    {"text": "Град повредил вашу одежду, потратили 200 на штопку", "money": -200, "hunger": 0, "energy": 0, "health": 0},
    {"text": "Тёплая погода подняла настроение", "money": 0, "hunger": 0, "energy": 15, "health": 5},
    # Чрезвычайные
    {"text": "В соседнем доме пожар. Вы помогали и потеряли телефон", "money": -1000, "hunger": 0, "energy": -30, "health": -10},
    {"text": "Произошла авария. Вы отдали 300 на помощь пострадавшим", "money": -300, "hunger": 0, "energy": -10, "health": 0},
    {"text": "Вы спасли кошку и получили вознаграждение 200 рублей", "money": 200, "hunger": 0, "energy": -10, "health": 0},
    # Связанные с Кирой
    {"text": "В новостях говорят о загадочных убийствах. Ваше сердце ёкнуло", "money": 0, "hunger": 0, "energy": -5, "health": 0, "suspicion": 5},
    {"text": "Полиция ищет Киру. Вы чувствуете слежку", "money": 0, "hunger": 0, "energy": -10, "health": 0, "suspicion": 10},
    {"text": "Кто-то оставил записку с именем Киры", "money": 0, "hunger": 0, "energy": 0, "health": 0, "suspicion": 15},
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
        self.title = "Студент"
        self.day = 1
        self.date = datetime(2010, 4, 23)
        self.fridge = []
        self.killed = []
        self.debt = 0
        self.debt_days = 0
        self.investigation = False
        self.kira_news = False
        self.location = "home"
        self.running = True
        self.loaded = False

    def save(self):
        data = {
            "player_name": self.player_name,
            "money": self.money,
            "hunger": self.hunger,
            "energy": self.energy,
            "health": self.health,
            "suspicion": self.suspicion,
            "title": self.title,
            "day": self.day,
            "date": self.date.isoformat(),
            "fridge": self.fridge,
            "killed": self.killed,
            "debt": self.debt,
            "debt_days": self.debt_days,
            "investigation": self.investigation,
            "kira_news": self.kira_news
        }
        with open("save.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("💾 Игра сохранена!")

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
        self.title = data["title"]
        self.day = data["day"]
        self.date = datetime.fromisoformat(data["date"])
        self.fridge = data["fridge"]
        self.killed = data["killed"]
        self.debt = data["debt"]
        self.debt_days = data["debt_days"]
        self.investigation = data["investigation"]
        self.kira_news = data["kira_news"]
        self.loaded = True
        return True

    def next_day(self):
        self.day += 1
        self.date += timedelta(days=1)
        self.hunger -= random.randint(5, 10)
        self.energy -= random.randint(5, 10)
        if self.hunger < 0:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0

        # Проверка голода
        if self.hunger <= 10:
            print("❌ Вы упали в голодный обморок! Вас увезли в больницу.")
            time.sleep(1)
            self.hunger = 50
            self.energy = 30
            self.money -= 3000
            self.health -= 20
            self.date += timedelta(days=7)
            self.day += 7
            print(f"🏥 Вы провели неделю в больнице. -3000 ₽")
            time.sleep(1)

        # Проверка энергии (автоотруб)
        if self.energy <= random.randint(0, 15):
            missing = 100 - self.energy
            minutes = missing * 15
            print(f"💤 Вы вырубились от усталости на {minutes} минут!")
            time.sleep(1)
            self.energy = 30
            # Шанс ограбления
            if random.random() < 0.3:
                stolen = random.randint(100, 1000)
                self.money -= stolen
                print(f"👤 Вас обокрали на {stolen} ₽")

        # Долг
        if self.debt > 0:
            self.debt_days += 1
            if self.debt_days >= 5:
                self.suspicion += 10
                self.debt = 0
                self.debt_days = 0
                print("⚠️ Вы не вернули долг! Подозрение +10%")

        # Проверка подозрения
        if self.suspicion >= 100:
            self.suspicion = 100
            self.investigation = True
            self.title = "Кира"
            if not self.kira_news:
                self.kira_news = True
                print("📰 ВНИМАНИЕ! Новости говорят о загадочном убийце по прозвищу Кира!")

    def show_stats(self):
        status = "❤️" if self.health > 60 else "💔"
        print("=" * 50)
        print(f"        📓 ТЕТРАДЬ СМЕРТИ - СИМУЛЯТОР")
        print(f"        👤 {self.player_name}")
        print(f"        📅 {self.date.strftime('%d %B %Y')}")
        print("=" * 50)
        print(f" {status} Здоровье: {self.health}%  |  🍔 Голод: {self.hunger}/100")
        print(f" ⚡ Энергия: {self.energy}/100  |  💰 Деньги: {self.money} ₽")
        print(f" 🕵️ Подозрение: {self.suspicion}%  |  🏆 Звание: {self.title}")
        if self.debt > 0:
            print(f" 💸 Долг: {self.debt} ₽ (осталось {5 - self.debt_days} дней)")
        if self.fridge:
            print(f" 🧊 В холодильнике: {len(self.fridge)} продуктов")
        print("=" * 50)

    def generate_contract(self):
        name = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        age = random.randint(18, 80)
        price = random.randint(2000, 10000)
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
        return {"name": name, "last": last, "age": age, "price": price, "bio": bio}

    def show_contract(self, contract):
        print("=" * 50)
        print("💼 КОНТРАКТ")
        print("=" * 50)
        print(f"Имя: {contract['name']} {contract['last']}")
        print(f"Возраст: {contract['age']} лет")
        print("Фото: [ASCII генерация]")
        print(f"Биография: {contract['bio']}")
        print(f"💰 Цена: {contract['price']} ₽")
        print("=" * 50)
        print("1️⃣ Принять контракт")
        print("2️⃣ Отказаться")
        choice = input("👉 ")
        return choice == "1"

    def generate_news(self):
        news = []
        if self.investigation:
            news.append(f"📰 Расследование убийств продолжается. Полиция ищет Киру.")
            news.append(f"📰 Следователи заявляют о новом убийстве, совершённом Кирой.")
            news.append(f"📰 Кира становится легендой. Обсуждают в интернете.")
            news.append(f"📰 В городе паника. Все боятся загадочных смертей.")
        else:
            news.append(f"📰 В городе произошло ограбление. Преступник скрылся.")
            news.append(f"📰 В этом году цены выросли на 5%.")
            news.append(f"📰 Завтра ожидается дождливая погода.")
            news.append(f"📰 В парке найден мёртвый голубь.")
            news.append(f"📰 Учёные объявили о новом прорыве.")
        return random.choice(news)

    def casino(self):
        print("🎰 КАЗИНО")
        print("У вас: " + str(self.money) + " ₽")
        try:
            bet = int(input("Ваша ставка (или 0 для выхода): "))
            if bet == 0:
                return
            if bet > self.money:
                print("❌ Недостаточно денег!")
                return
            result = random.randint(1, 100)
            if result >= 50:
                win = bet * 2
                self.money += win
                print(f"🎉 Вы выиграли {win} ₽! У вас {self.money} ₽")
            else:
                self.money -= bet
                print(f"😞 Вы проиграли {bet} ₽. У вас {self.money} ₽")
        except:
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
        except:
            print("❌ Введите число!")

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
            else:
                print("❌ Неверный выбор")
        except:
            print("❌ Введите число!")

    def sleep(self):
        try:
            hours = int(input("Сколько часов спать (1-12): "))
            if hours < 1 or hours > 12:
                print("❌ От 1 до 12 часов")
                return
            energy_gain = hours * 15
            self.energy += energy_gain
            if self.energy > 100:
                self.energy = 100
            self.date += timedelta(hours=hours)
            print(f"😴 Вы поспали {hours} часов (+{energy_gain} энергии)")
            self.next_day()
        except:
            print("❌ Введите число!")

    def work(self):
        print("💻 Легальная работа: печатайте 1000 символов за 500 ₽")
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
                typed += 1
                print(f"Прогресс: {typed}/{target} ({typed*100//target}%)")
                if typed == target:
                    self.money += 500
                    print(f"✅ Заказ выполнен! +500 ₽. У вас {self.money} ₽")
                    self.next_day()
                    break

    def buy_product(self):
        print("🛒 ПРОДУКТОВЫЙ МАГАЗИН")
        print("Категории:")
        print("1. Хлебобулочные")
        print("2. Мясные")
        print("3. Рыбные")
        print("4. Молочные")
        print("5. Фрукты")
        print("6. Овощи")
        print("7. Готовые блюда")
        print("8. Сладости")
        print("9. Напитки")
        print("10. Энергетики")
        print("11. Фастфуд")
        print("12. Суперфуды")
        print("13. Орехи")
        print("14. Соусы")
        print("15. Завтраки")
        print("16. Консервы")
        print("17. Специи")
        print("18. Алкоголь")
        print("19. Здоровое")
        print("20. Разное")
        print("0. Назад")
        try:
            cat = int(input("Категория: "))
            if cat == 0:
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
                else:
                    print("❌ Неверный выбор")
            except:
                print("❌ Введите число!")
        except:
            print("❌ Введите число!")

    def walk(self):
        event = random.choice(EVENTS)
        print("🚶 Вы гуляете по городу...")
        time.sleep(1)
        print(f"📌 {event['text']}")
        if 'money' in event:
            self.money += event['money']
        if 'hunger' in event:
            self.hunger += event['hunger']
        if 'energy' in event:
            self.energy += event['energy']
        if 'health' in event:
            self.health += event['health']
        if 'suspicion' in event:
            self.suspicion += event['suspicion']
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
        if self.suspicion > 100:
            self.suspicion = 100
        if self.suspicion < 0:
            self.suspicion = 0
        self.next_day()

    def notebook(self):
        print("📓 ТЕТРАДЬ СМЕРТИ")
        print("1️⃣ Написать имя жертвы")
        print("2️⃣ Просмотреть список убитых")
        print("3️⃣ Назад")
        choice = input("👉 ")
        if choice == "1":
            name = input("Введите полное имя жертвы: ")
            if name.strip():
                self.killed.append(name)
                self.suspicion += 15
                print(f"✍️ Имя {name} записано в тетрадь.")
                print("💀 Смерть наступит через 40 секунд...")
                self.money += random.randint(1000, 5000)
                print(f"💰 Вы получили {self.money} ₽ за контракт (автоматически)")
                self.next_day()
            else:
                print("❌ Имя не может быть пустым!")
        elif choice == "2":
            if self.killed:
                print("📋 СПИСОК УБИТЫХ:")
                for i, name in enumerate(self.killed, 1):
                    print(f"{i}. {name}")
            else:
                print("📭 Пока никого не убито.")
        elif choice == "3":
            return

    def main_menu(self):
        while self.running:
            self.show_stats()
            if self.investigation:
                print("📢 ВНИМАНИЕ! Идёт расследование по делу Киры!")
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
            elif choice == "0":
                self.running = False
                print("🚪 Выход из игры...")
            else:
                print("❌ Неверный выбор!")

    def phone_menu(self):
        print("📱 ТЕЛЕФОН")
        print("1️⃣  🎰 Казино")
        print("2️⃣  💸 Взять в долг")
        print("3️⃣  🔙 Назад")
        choice = input("👉 ")
        if choice == "1":
            self.casino()
        elif choice == "2":
            self.take_debt()
        elif choice == "3":
            return

    def home_menu(self):
        print("🏠 ДОМ")
        if self.fridge:
            print("🍔 Холодильник:")
            for i, item in enumerate(self.fridge):
                print(f"  {i+1}. {item['name']}")
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

    def computer_menu(self):
        print("💻 КОМПЬЮТЕР")
        print("1️⃣  📰 Новости")
        print("2️⃣  💼 Контракты")
        print("3️⃣  💻 Легальная работа")
        print("4️⃣  🔙 Назад")
        choice = input("👉 ")
        if choice == "1":
            print(self.generate_news())
            input("Нажмите Enter...")
        elif choice == "2":
            contract = self.generate_contract()
            if self.show_contract(contract):
                self.killed.append(f"{contract['name']} {contract['last']}")
                self.money += contract['price']
                self.suspicion += 20
                print(f"✅ Контракт выполнен! +{contract['price']} ₽")
                self.next_day()
            else:
                print("❌ Отказ от контракта")
        elif choice == "3":
            self.work()
        elif choice == "4":
            return

    def walk_menu(self):
        print("🚶 ГУЛЯТЬ ПО ГОРОДУ")
        print("1️⃣  🛒 Продуктовый магазин")
        print("2️⃣  🚶 Просто гулять")
        print("3️⃣  🔙 Назад")
        choice = input("👉 ")
        if choice == "1":
            self.buy_product()
        elif choice == "2":
            self.walk()
        elif choice == "3":
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
        input("Нажмите Enter чтобы начать...")
    else:
        print("❌ Неверный выбор!")
        return

    game.main_menu()

if __name__ == "__main__":
    main()
