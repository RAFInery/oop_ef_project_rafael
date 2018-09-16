import pickle

class Stock:

    base_stock = {
        "clothes_keys":0.00,
        "dayly_food_keys":0.00,
        "hygiene_keys":0.00,
        "leisure_keys":0.00,
        "mobile_keys":0.00}


    def load(self):
        with open("pickle_stock.pkl", "rb") as f:
            Stock.base_stock = pickle.load(f)


    def new_month(self,mc=48.00, mf=300.00,mh=24.00,ml=94.00,mm=35.00):
        stock_list = [mc, mf, mh, ml, mm]
        k = 0
        for i in Stock.base_stock.keys():
            Stock.base_stock[i] = Stock.base_stock[i]+ stock_list[k]
            k += 1


    def save_stock(self):
        saved_stock = Stock.base_stock
        pickle.dump(saved_stock, file=open("pickle_stock.pkl", "wb"))


    def continue_or_new(self):
        while True:
            quest = input("<new month> or <continue>?")
            if quest == "new month":
                Stock.new_month(self)
                break
            elif quest == "continue":
                Stock.load(self)
                break
            else:
                print ("unvalid entry!")


    def return_stock(self):
        return Stock.base_stock


