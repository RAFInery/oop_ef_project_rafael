import pickle
"""
RESET OR SET-UP THE PROGRAMME 
"""

class Reset:
	
	
    def reset(self):
        base_stock = {
            "clothes_keys": 0,
            "dayly_food_keys": 0,
            "hygiene_keys": 0,
            "leisure_keys": 0,
            "mobile_keys": 0}

        sum_totals = {
            "clothes_keys": 0,
            "dayly_food_keys": 0,
            "hygiene_keys": 0,
            "leisure_keys": 0,
            "mobile_keys": 0}
            
            
        cat_dict = {
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
            ]}

        saving_dict = {
            "stock": base_stock,
            "sum": sum_totals,
            "month": None,
            "cat":cat_dict}

        Reset.save(self, saving_dict)


    def save(self, saving_obj):
        pickle.dump(saving_obj, file=open("pickle_saving_FiPro.pkl", "wb"))


    def reload(self):
        with open("pickle_saving_FiPro.pkl", "rb") as f:
            reload_dic = pickle.load(f)
        return reload_dic


def set_up():
    reset = Reset()
    reset.reset()
    print (reset.reload())
# set_up()#-->uncomment and execute in order to reset and show the pickle-content

