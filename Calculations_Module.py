class Calculate:
    new_sum = {
        "clothes_keys":0,
        "dayly_food_keys":0,
        "hygiene_keys":0,
        "leisure_keys":0,
        "mobile_keys":0}

    total_sum = {
        "clothes_keys":0,
        "dayly_food_keys":0,
        "hygiene_keys":0,
        "leisure_keys":0,
        "mobile_keys":0}

    old_sum = None

    new_entry = None


    def new_sum_calc(self, sum_list, classification_list):
        for i in range(len(sum_list)):
            k = classification_list[i]
            Calculate.new_sum[k] += sum_list[i]


    def load_current_sum(self, reload_dict):
        Calculate.old_sum = reload_dict["sum"]


    def calc_total_sum(self, reload_dict, entry_lists):
        Calculate.load_current_sum(self, reload_dict)
        if entry_lists == None:
            Calculate.total_sum = Calculate.old_sum
            Calculate.new_entry = False

        else:
            sum_list, classification_list = entry_lists[0], entry_lists[3]
            Calculate.new_sum_calc(self, sum_list, classification_list)
            for i in Calculate.new_sum.keys():
                print ("new_sum: ", Calculate.new_sum)
                print ("old_sum: ", Calculate.old_sum)
                Calculate.total_sum[i] += Calculate.new_sum[i]
                Calculate.total_sum[i] += Calculate.old_sum[i]
            Calculate.new_entry = True
        return Calculate.total_sum


    def stock_balance(self, base_stock):
        if Calculate.new_entry == True:
            for i in base_stock.keys():
                base_stock[i] = base_stock[i] - Calculate.new_sum[i]
        return base_stock


    def ret_new_sum(self):
        return Calculate.new_sum



