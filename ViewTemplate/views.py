from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
# Create your views here.

import random

class Person:
    def __init__(self, name, surname, age, number):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number

    def __str__(self):
        return f" {self.name} - {self.surname} ; Age {self.age}; Number: {self.number}"

def contacts(request):
    persons = [
        Person(name = "Alexey", surname = "Marahovskiy", age = 17, number = "33"),
        Person(name = "Dima", surname = "Dobrovolskiy", age = 18, number = "??"),
        Person(name = "Kolya", surname = "Belousov", age = 18 , number = "??"),
    ]
    return TemplateResponse(request, "contacts.html", {"persons": persons})
def style(request):
    return render(request, 'main_page.html')

def index(request):
    context = {}

    context["welcome_text"] = "You`re welcome!"
    context["html_tag"] = '<h3 style="color: red;"></h3>'
    context["value_int"] = 10
    context["value_float"] = 10.424242
    context["value_bool"] = False

    context["list"] = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    context["dict"] = {"key1":"value1", "key2":"value2"}
    context["person"] = Person("William", "Butcher", 30)
    context["random_value"] = random.randint(-100,100)
    context["empty_list"] = []

    return render(request, "index.html", context=context)
def text_format(request):
    return TemplateResponse(request, "text-format.html",{
        "list":[i for i in range(0,10)]
    })
class SportMain:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        # self.imgUrl = imgUrl

    def __str__(self):
        return f"Title: {self.title}, Text: {self.text}"

class Describer:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        # self.imgUrl = imgUrl
        def __str__(self):
            return f"Name: {self.name}, Text: {self.text}"



# def index(request):
#     context = {}
#
#     context["welcome_text"] = "Welcome to main site!"
#     context["html_tag"] = '<h3 style="color: red;"></h3>'
#     context["main"] = SportMain("Sport Web Site","It's main site of web sire for sport, here's few categories")
#     # context["football"] = Describer("Football", "Football is sport where two teams trying to punch to ball to gate")
#     # context["hockey"] = Describer("Hocker" , "Хоккей с шайбой — это динамичная командная игра на льду, в которой две команды на коньках пытаются забить шайбу в ворота соперника с помощью клюшек")
#     # context["basketball"] = Describer("Basket", "Баскетбол - спортивная командная игра с мячом, в которой мяч забрасывают руками в кольцо соперника.")
#     return render(request, "index.html", context=context)



def football(request):
    context = {}

    context["welcome_text"] = "Welcome to football site!"
    context["football"] = Describer("Football", "Football is sport where two teams trying to punch to ball to gate")

    return render(request, "football.html", context=context)

def hockey(request):
    context = {}

    context["welcome_text"] = "Welcome to hockey site!"
    context["hockey"] = Describer("Hockey" , "Хоккей с шайбой — это динамичная командная игра на льду, в которой две команды на коньках пытаются забить шайбу в ворота соперника с помощью клюшек")

    return render(request, "football.html", context=context)

def basketball(request):
    context = {}

    context["welcome_text"] = "Welcome to basketball site!"
    context["basketball"] = Describer("Basket", "Баскетбол - спортивная командная игра с мячом, в которой мяч забрасывают руками в кольцо соперника.")
    return render(request, "football.html", context=context)


class Recipe:
    recipe: str
    def __init__(self, recipe):
        self.recipe = recipe
    def __str__(self):
        return f"{self.recipe}"

def goulash(request , recipe:str = "goulash"):
    context = {}

    context["welcome_text"] = "Here recipt of goulash!"
    context["goulash"] = f"""<h1>Goulash</h1>\n
        <p>ИНГРЕДИЕНТЫ
            свинина или говядина: 500 г
            лук репчатый: 2 шт
            мука: 1 ст.л.
            томатный соус: 3 ст.л.
            лавровый лист	
            зелень петрушки, укропа	
            соль	
            свежемолотый перец
            Пошаговый рецепт - мясной гуляш

            Мясо вымыть, обсушить и нарезать кубиками.
            Лук мелко нарезать.
            В глубокой сковороде разогреть масло и обжарить мясо на сильном огне около 5 минут.
            Добавить к мясу лук и жарить, периодически помешивая, 5-7 минут на среднем огне.
            
            Гуляш посолить, поперчить, посыпать мукой, хорошо перемешать и жарить еще 2-3 минуты, периодически помешивая.
            Добавить томатный соус, хорошо перемешать.
            Влить в гуляш 2-3 стакана воды или мясного бульона, перемешать, добавить лавровый лист, накрыть крышкой и тушить на маленьком огне, при слабом кипении 1-1,5 часа.
    
            При подаче посыпать гуляш рубленой зеленью, приятного апетита.</p>
    """

    return render(request, "goulash.html", context=context)

def dumplings(request):
    context = {}
    context["welcome_text"] = "Recipe of dumplings !"

    context["dumplings"]= f"""<h1>Recipe of dumplings</h1>\n
    <p> Перший і найважливіший етап приготування пельменів — тісто.
     Перед ним стоїть кілька важливих задач. 
     По-перше, воно має міцно тримати начинку й сік, який утвориться при варінні. 
     По-друге, зовнішність теж має значення. 
     Правильне тісто для пельменів ніколи не розвариться, 
     буде тонким і ледь прозорим, не втратить своєї форми. 
     Щоб домашнє тісто вийшло піддатливим і тоненьким, потрібні лише вдалий рецепт та трохи практики. За класичною рецептурою вам знадобиться:

    борошно — 500 г;
    яйця — 2 шт;
    вода — 200 мл;
    сіль — 0,5 ч. л;
    рафінована рослинна олія — 1 ст. л.
    
    Борошно для тіста потрібно обов`язково просіяти. 
    Так воно насититься киснем і рівномірно поєднається з іншими компонентами. 
    Після цього викладіть борошно у вигляді гірки, зробіть у ньому невелике заглиблення й додайте в нього інші інгредієнти.
    Важливо, щоб яйця та вода були кімнатної температури.
    За бажанням замість води можна використати молоко або бульйон. 
    Не забувайте про краплю рафінованої олії, вона надасть готовому тісту еластичності й міцності.

    Тісто для пельменів зручно вимішувати в одному напрямку по колу, 
    обережно загортаючи борошно з боків до центру. 
    Вважається, що тісто потрібно вимішувати якомога довше, щоб воно стало м`якшим. 
    Щоб перевірити якість текстури просто натисніть на тісто пальцем. 
    В ідеалі має залишитися заглибинка, яка не зникає.

    Коли досягнете бажаної консистенції, дайте тісту трохи відпочити. 
    Покладіть його в глибоку посудину, накрийте рушником чи харчовою плівкою і залиште мінімум на 30 хвилин. 
    Протягом цього часу клейковина з борошна набухне й не буде рватися в процесі формування пельменів. 
    Так тісто буде міцним та пружним, а вироби з нього можна сміливо заморожувати. 
    """
    return render(request, "dumplings.html", context=context)

#
#     context["hockey"] = Describer("Hocker" , "Хоккей с шайбой — это динамичная командная игра на льду, в которой две команды на коньках пытаются забить шайбу в ворота соперника с помощью клюшек")
#     context["basketball"] = Describer("Basket", "Баскетбол - спортивная командная игра с мячом, в которой мяч забрасывают руками в кольцо соперника.")

# Task 2
