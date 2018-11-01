"""imports"""
from functools import reduce
import pickle


"""Lists"""

sos_cat_dict = {
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
    cat_dict = None
    dict_numb_cat = None


    def load_cat_dict(self, cat):
        Entry.cat_dict = cat
        if Entry.cat_dict == None:
            Entry.cat_dict = sos_cat_dict
            print ("categories couldn't get loaded, ALTERNATIVE-SET in use! ")
        print ("Categories/Keys: ", Entry.cat_dict)


    def new_entry(self, cat):
        """
        :return: Entry. -summe, -reason, -date
        """
        Entry.load_cat_dict(self, cat)
        while True:
            Entry.summe = (input("Sum?: "))
            while True:

                try:
                    float(Entry.summe)
                    break

                except ValueError:
                    print("input has to be a number!")
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
                if quest in ["yes", "Yes", "ja", "Ja"]:
                    Entry.reason = input("Reason?: ")
                    continue
                else:
                    Entry.new_cat(self)
                    break
            else:
                break

        Entry.date = input("Date (day)?: ")
        return float(Entry.summe), Entry.reason, Entry.date, Entry.classifier


    def cat_checker(self):
        found = 0
        for i in Entry.cat_dict.keys():
            if Entry.reason in Entry.cat_dict[i]:
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
            a = input()
            try:
                Entry.dict_numb_cat = {"0": "clothes_keys", "1": "dayly_food_keys",
                "2": "hygiene_keys",
                "3": "leisure_keys", "4":"mobile_keys"}
                Entry.cat_dict[Entry.dict_numb_cat[a]].append(Entry.reason)
                break
            except KeyError:
                print ("Choose between given numbers!")


        Entry.classifier = Entry.dict_numb_cat[a]

            
class Cycle(Entry) :
    summe_list = []
    reason_list = []
    date_list = []
    classifier_list = []
    

    def cycle(self, cat):
        progress = None
        while not progress == "done":
            s, r, d, c = Cycle.new_entry(self, cat)
            Cycle.summe_list.append(s)
            Cycle.reason_list.append(r)
            Cycle.date_list.append(d)
            Cycle.classifier_list.append(c)
            progress = input("enter <done> to end, otherwhise tape any other key")


    def ret_entry_lists(self):
        entry_lists = (Cycle.summe_list, Cycle.reason_list, Cycle.date_list, Cycle.classifier_list)
        return entry_lists
     
     
    def ret_cat_dict(self):
        return Entry.cat_dict

