import pickle

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

    def ret_base_stock(self):
        return Stock.base_stock