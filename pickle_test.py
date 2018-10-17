import pickle
"""
RESET THE PROGRAMME
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

        saving_dict = {
            "stock": base_stock,
            "sum": sum_totals,
            "month": None}

        Reset.save(self, saving_dict)


    def save(self, saving_obj):
        pickle.dump(saving_obj, file=open("pickle_saving_FiPro.pkl", "wb"))


    def reload(self):
        with open("pickle_saving_FiPro.pkl", "rb") as f:
            reload_dic = pickle.load(f)
        return reload_dic

reset = Reset()
#reset.reset()
print (reset.reload())

# print (pic.reload()) -->Check if it worked!

