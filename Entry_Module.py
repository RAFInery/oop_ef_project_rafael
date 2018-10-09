"""imports"""
from functools import reduce
import pickle


"""Lists"""

cat_dict = {
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
}


class Entry:
    summe = None
    reason = None
    date = None
    classifier = None


    def new_entry(self):
        """
        :return: Entry. -summe, -reason, -date
        """
        while True:
            Entry.summe = (input("Sum?: "))
            while True:

                try:
                    float(Entry.summe)
                    break

                except ValueError:
                    print("value has to be a number!")
                    Entry.summe = input("Sum?: ")

            Entry.reason = input("Reason?: ")
            if Entry.reason == "back":
                print("rewrite the sum")
                continue
            else:
                break

        while True:
            if Entry.cat_checker(self) == 0:
                quest = (input("Oops...want to write it again?"))
                if quest == "yes":
                    Entry.reason = input("Reason?: ")
                    continue
                else:
                    Entry.new_cat(self)
                    break
            else:
                break

        Entry.date = input("Date?: ")
        return int(Entry.summe), Entry.reason, Entry.date, Entry.classifier


    def cat_checker(self):
        found = 0
        for i in cat_dict.keys():
            if Entry.reason in cat_dict[i]:
                found = 1
                Entry.classifier = i
                break
        return found


    def new_cat(self):
        print("to wich category belongs", Entry.reason, "?",
              "\n0 = clothes",
              "\n1 = food",
              "\n2 = hygiene",
              "\n3 = leisure",
              "\n4 = mobile")
        while True:
            a = int(input())
            try:
                dict_numb_cat = {0: "clothes_keys", 1: "dayly_food_keys", 2: "hygiene_keys",
                                 3: "leisure_keys", 4:"mobile_keys"}
                cat_dict[dict_numb_cat[a]].append(Entry.reason)
                break
            except KeyError:
                print ("Choose between given numbers!")

        Entry.classifier = dict_numb_cat[a]






class Cycle(Entry) :
    summe_list = []
    reason_list = []
    date_list = []
    classifier_list = []


    def cycle(self):
        progress = None
        while not progress == "done":
            s, r, d, c = Cycle.new_entry(self)
            Cycle.summe_list.append(s)
            Cycle.reason_list.append(r)
            Cycle.date_list.append(d)
            Cycle.classifier_list.append(c)
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

    def ret_entry_lists(self):
        entry_lists = (Cycle.summe_list, Cycle.reason_list, Cycle.date_list, Cycle.classifier_list)
        return entry_lists








