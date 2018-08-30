"""imports"""
from functools import reduce
import pickle


"""Lists"""

summe = []
reason = []
date = []
keys_dict = {
    "categories":[
        'clothes', 'daylyfood', 'hygiene',
        'leisure', 'mobile'
        ],
    "clothes_keys":[
        'T-Shirt', 'Hose', 'Pulli',
        'Unterhosen', 'Socken', 'Schuhe'
        ],
    "dayly_food_keys":[
        'Mittagessen', 'Mensa', 'Verpflegung'
        ],
    "hygiene_keys":[
        'Friseur', 'Gel', 'Deo',
        'Rasierer', 'Shampo'
        ],
    "leisure_keys":[
        'Sport', 'Ausgang', 'Kino'
        ],
    "mobile_keys":[
        'Abbo', 'Zusatzkosten'
        ]
}#Todo: adjust the key in the "cat_checker()"

summe_totals = [
    [], #0-clothes
    [], #1-food
    [], #2-hygiene
    [], #3-leisure
    [] #4-mobile
    ]

class Entry:
    var = pass


    def cat_checker(self):
        k = 0
        found = 0
        for i in keys_dict.keys():
            if reason[-1] in keys_dict[i]:
                summe_totals[k].append(summe[-1])
                k += 1
                found = 1
                break

    def new_cat(self):
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

    # def cat_check_cycle(self): #Todo: Insert this cycle into the "main cycle"
    #     if not found == 1:
    #         quest = (input("Oops...want to write it again?"))
    #         if quest == "yes":
    #             reason.pop(-1)
    #             reason.append(input("Reason?"))
    #             cat_checker()

class Stock:
    base_stock = [
        0.00,  # clothes
        0.00,  # daylyfood
        0.00,  # hygiene
        0.00,  # leisure
        0.00  # mobile
    ]

    fresh_stock = []

    def load(self):
        with open("pickle_stock.pkl", "rb") as f:
            Stock.base_stock = pickle.load(f)


    def new_month(self,mc=48.00, mf=300.00,mh=24.00,ml=94.00,mm=35.00):# monthly clothes, -food, -hygiene, -leisure, -mobile
            k = 0
            for i in [mc, mf, mh, ml, mm]:
                Stock.base_stock[k] = Stock.base_stock[k]+ i
                k += 1


    def adjust_fresh_stock(self, value):
        Stock.fresh_stock = value


    def save_fresh_stock(self):
        saved_stock = Stock.fresh_stock
        pickle.dump(saved_stock, file=open("pickle_stock.pkl", "wb"))




