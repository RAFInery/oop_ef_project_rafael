import pickle

class Pickeling:

    def reload(self):
        with open("pickle_saving_FiPro.pkl", "rb") as f:
            reload_dic = pickle.load(f)
        return reload_dic


    def save(self, saving_obj):
        pickle.dump(saving_obj, file=open("pickle_saving_FiPro.pkl", "wb"))


    def save_data(self, status, stock, sume, month):
        if status == "inProgress":
            Pickeling.temporary_saving(stock, stock, sume, month)
        elif status == "final":
            Pickeling.monthly_reset(self, stock)


    def monthly_reset(self, base_stock):

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

        Pickeling.save(self, saving_dict)


    def temporary_saving(self, base_stock, sum_totals, month):
        saving_dict = {
            "stock": base_stock,
            "sum": sum_totals,
            "month": month}

        Pickeling.save(self, saving_dict)



