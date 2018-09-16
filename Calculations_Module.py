class Calculate:
    sum_totals = {
        "clothes_keys":0,
        "dayly_food_keys":0,
        "hygiene_keys":0,
        "leisure_keys":0,
        "mobile_keys":0
    }

    def sum_calc(self, sum_list, classification_list):
        for i in range(len(sum_list)):
            k = classification_list[i]
            Calculate.sum_totals[k] = Calculate.sum_totals[k] + sum_list[i]


    def stock_balance(self, sum_totals, base_stock):
        for i in base_stock.keys():
            base_stock[i] = base_stock[i] - sum_totals[i]


    def ret_sum_totals(self):
        return Calculate.sum_totals



