import os

# org
load_org = True
start_org = 0
count_org = 500
index_org = "org"

# people
load_people = True
start_people = 0
count_people = 5000
index_people = "people"

# all
headers = {
    'Authorization': os.environ['authorization'] if 'authorization' in os.environ else "",
    'Content-Type': 'application/json'
}

profession = ["столяр", "плотник", "уборщик", "манеджер", "директор", "архитектор", "учитель", "продавец", "водитель", "Клининг Менеджер", "Лесник", "Стажер 1-й категории", "Полировщик рогов Лося", "Архитектор систем промышленной эксплуатации"]
education = ["высшее", "среднее", "неоконченное высшее", "средне специальное"]
citizenship = ["РФ", "иное"]
floor = ["мужской", "женский"]
org = ["Корпорация", "Романычь", "Бабочка", "Лютик", "Калинка", "Малинка", "Радуга", "Поросенок", "Лось", "Апробация", "Эксплуатация", "Порядок", "Разминка", "Лом", "Слон", "Комунга", "Ротограмма"]