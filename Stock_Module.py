class Stock:
    """
    base_stock = {
        "clothes_keys":0,
        "dayly_food_keys":0,
        "hygiene_keys":0,
        "leisure_keys":0,
        "mobile_keys":0}
    """

    base_stock = None

    def monthly_stock(self,mc=48.00, mf=300.00,mh=24.00,ml=94.00,mm=35.00):
        fill_up_dict = {"clothes_keys":mc,
                        "dayly_food_keys":mf,
                        "hygiene_keys":mh,
                        "leisure_keys":ml,
                        "mobile_keys":mm}

        for i in Stock.base_stock.keys():
            Stock.base_stock[i] += fill_up_dict[i]


    def check_month(self, saving_dict):
        Stock.base_stock = saving_dict["stock"]
        if saving_dict["month"] is None:
            inp = input("Month of your entries?: ")
            saving_dict["month"] = inp
            Stock.monthly_stock(self)


    def return_stock(self):
        return Stock.base_stock





