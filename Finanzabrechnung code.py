"""imports"""
from functools import reduce
import pickle


"""Lists"""

summe = []
reason = []
date = []

categories = [
    'clothes', 'daylyfood', 'hygiene',
    'leisure', 'mobile'
    ]
clothes_keys = [
    'T-Shirt', 'Hose', 'Pulli',
    'Unterhosen', 'Socken', 'Schuhe'
    ]
dayly_food_keys = [
    'Mittagessen', 'Mensa', 'Verpflegung'
    ]
hygiene_keys = [
    'Friseur', 'Gel', 'Deo',
    'Rasierer', 'Shampo'
    ]
leisure_keys = [
    'Sport', 'Ausgang', 'Kino'
    ]
mobile_keys = [
    'Abbo', 'Zusatzkosten'
    ]

summe_totals = [
    [], #0-clothes
    [], #1-food
    [], #2-hygiene
    [], #3-leisure
    [] #4-mobile
    ]
base_stock = [
              0.00, # clothes
              0.00, # daylyfood
              0.00, # hygiene
              0.00, # leisure
              0.00 # mobile
              ]
fresh_stock = []

"""variables"""
space20 = 20*(" ")
space = (" ")


"""functions for the overview"""
def new_month():
    global new
    new = input ("new month?")
    if new == "yes":
        saved_stock = [0,0,0,0,0]
        pickle.dump(saved_stock, file=open("pickle_stock.pkl", "wb"))


    def base_stock_load():
        global base_stock
        with open("pickle_stock.pkl", "rb") as f:
            base_stock = pickle.load(f)
    base_stock_load()


def cat_checker():
    if reason[-1] in clothes_keys:
        summe_totals[0].append(summe[-1])

    elif reason[-1] in dayly_food_keys:
        summe_totals[1].append(summe[-1])

    elif reason[-1] in hygiene_keys:
        summe_totals[2].append(summe[-1])

    elif reason[-1] in leisure_keys:
        summe_totals[3].append(summe[-1])

    elif reason[-1] in mobile_keys:
        summe_totals[4].append(summe[-1])

    else:
        quest = (input("Oops...want to write it again?"))
        if quest == "yes":
            reason.pop(-1)
            reason.append(input("Reason?"))
            cat_checker()
        else:
           def new_cat():
               print("to wich category belongs", reason[-1], "?",
                     "\n0 = clothes",
                     "\n1 = food",
                     "\n2 = hygiene",
                     "\n3 = leisure",
                     "\n4 = mobile")

               quest = input()

               if quest == "0":
                   summe_totals[0].append(summe[-1])

               elif quest == "1":
                   summe_totals[1].append(summe[-1])


               elif quest == "2":
                   summe_totals[2].append(summe[-1])


               elif quest == "3":
                   summe_totals[3].append(summe[-1])


               else:
                   summe_totals[4].append(summe[-1])

           return new_cat()


def append_objects():
    reason.append("back")
    while reason[-1] == "back":
        reason.pop(-1)
        summe.append(input("Sum?"))
        while True:
            try:
                int(summe[-1])
                break
            except ValueError:
                print ("value has to be a number!")
                summe.pop(-1)
                summe.append(input())

        reason.append(input("Reason?"))
        if reason[-1] == "back":
            summe.pop(-1)
            print("rewrite the sum")
        else:
            break
    cat_checker()
    date.append (input("Date?"))


def overview():
    append_objects()
    progress = input()
    while not progress == "done":
        append_objects()
        progress = input()


def printOverview():
    b = 0
    for obs in summe:
        print(summe[b], 10*space, reason[b], 10*space, date[b])
        if len(summe) > 1:
            b += 1
        else:
            break


def calc_cat() :
    b = 0
    for obs in range(5):
        if len(summe_totals[b])>1:
            summe_totals[b] = reduce(lambda x, y: round(float(x),2) + round(float(y),2), summe_totals[b])
        elif len(summe_totals[b]) == 1:
            summe_totals[b] = float(summe_totals[b][0])
        else:
            summe_totals[b] = 0.00
        b += 1


def monthly_stock(mc, mf, mh, ml, mm):#monthly clothes, -food, -hygiene, -leisure, -mobile
    base_stock[0] = base_stock[0] + mc
    base_stock[1] = base_stock[1] + mf
    base_stock[2] = base_stock[2] + mh
    base_stock[3] = base_stock[3] + ml
    base_stock[4] = base_stock[4] + mm


def statistical_stock():
    b = 0
    for obs in range(5):
        fresh_stock.append(base_stock[b] - float(summe_totals[b]))
        b += 1


def writing_to_file(filename,month):
    b = 0
    for obs in summe:
        x = 20
        x = x - (len(reason[b]) - 6) #Durchschnittslänge der Keys = 6
        with open(filename, "a") as f:
            f.write(str(summe[b]))
            f.write(".-")
            f.write(space20)
            f.write(reason[b])
            f.write(x * space)
            f.write(date[b])
            f.write(month)
            f.write("\n")
            b += 1
    final = input("Is this your final entry?")
    if final == "yes":
        with open(filename, "a") as f:
            f.write ("Kleider Total: ")
            f.write(str(summe_totals[0]))
            f.write(".-")
            f.write(" (")
            f.write(str(fresh_stock[0]))
            f.write(") ")

            f.write("Essen Total: ")
            f.write(str(summe_totals[1]))
            f.write(".-")
            f.write(" (")
            f.write(str(fresh_stock[1]))
            f.write(") ")

            f.write("Hygiene Total: ")
            f.write(str(summe_totals[2]))
            f.write(".-")
            f.write(" (")
            f.write(str(fresh_stock[2]))
            f.write(") ")

            f.write("Freizeit Total: ")
            f.write(str(summe_totals[3]))
            f.write(".-")
            f.write(" (")
            f.write(str(fresh_stock[3]))
            f.write(") ")

            f.write("Handy Total: ")
            f.write(str(summe_totals[4]))
            f.write(".-")
            f.write(" (")
            f.write(str(fresh_stock[4]))
            f.write(")")


def pickle_data():
    saved_stock = fresh_stock
    pickle.dump(saved_stock, file=open("pickle_stock.pkl", "wb"))


"""Code"""
new_month()
if new == "yes":
    monthly_stock(48.00, 300.00, 24.00, 94.00, 35.00)
overview()
calc_cat()
statistical_stock()
pickle_data()
printOverview()
writing_to_file("Testliches_file.txt",".03")
print ("end of real finance-program")

"""
Pickeling works like cheses!
However, the sum is not properly calculated.
The sum has to be pickeled too.
"""