"""imports"""
from functools import reduce
import pickle


"""Lists"""

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
    summe = None
    reason = "back"
    date = None


    def new_entry(self):
        """
        :return: Entry. -summe, -reason, -date
        """
        while True:
            Entry.summe = (input("Sum?"))
            while True:
                try:
                    int(Entry.summe)
                    break
                except ValueError:
                    print("value has to be a number!")
                    Entry.summe = input()

            Entry.reason = input("Reason?")
            if Entry.reason== "back":
                print("rewrite the sum")
                continue

        while True:
            if Entry.cat_checker() == 0:
                quest = (input("Oops...want to write it again?"))
                if quest == "yes":
                    Entry.reason = input("Reason: ")
                    continue
                else:
                    Entry.new_cat()
                    break
            else:
                break

        date = input("Date?")
        return Entry.summe, Entry.reason, Entry.date


    def cat_checker(self):
        k = 0
        found = 0
        for i in keys_dict.keys():
            if Entry.reason in keys_dict[i]:
                k += 1
                found = 1
                break
        return found


    def new_cat(self):
        print("to wich category belongs", Entry.reason, "?",
              "\n0 = clothes",
              "\n1 = food",
              "\n2 = hygiene",
              "\n3 = leisure",
              "\n4 = mobile")

        a = input()

        dict_numb_cat = {0: "clothes", 1: "food", 2: "hygiene", 3: "leisure", 4:"mobile"}
        keys_dict[dict_numb_cat[a]].append(Entry.reason)




class Cycle(Entry) :
    summe_list = []
    reason_list = []
    date_list = []


    def cycle(self):
        progress = None
        while not progress == "done":
            s, r, d = Cycle.new_entry(self)
            Cycle.summe_list.append(s)
            Cycle.reason_list.append(r)
            Cycle.date_list.append(d)
            progress = input()


    def printOverview(self):
        b = 0
        space = (" ")
        for obs in Cycle.summe_list:
            print(Cycle.summe_list[b], 10 * space, Cycle.reason_list[b], 10 * space, Cycle.date_list[b])
            if len(Cycle.summe_list) > 1:
                b += 1
            else:
                break







