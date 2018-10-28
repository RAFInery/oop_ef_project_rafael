from Stock_Module import Stock
from Entry_Module import Cycle, Entry
from Calculations_Module import Calculate
from Writing_Module import Writing
from Pickle_Module import Pickeling


class Main:
    # general objects
    reload_dict = None
    entry_lists = None
    summe = None
    end_stock = None
    entry_status = "inProgress"
    cat_dict = None
    # instances
    stock = Stock()
    cycle = Cycle()
    pic = Pickeling()
    writing = None
    calculate = Calculate()


    def pickeling_func(self):
        Main.reload_dict = Main.pic.reload()


    def stock_func(self):
        Main.stock.check_month(Main.reload_dict)


    def cycle_func(self):
        Main.cycle.cycle(Main.reload_dict["cat"])
        Main.entry_lists = Main.cycle.ret_entry_lists()
        Main.cat_dict = Main.cycle.ret_cat_dict


    def calculate_func(self):
        Main.total_sum = Main.calculate.calc_total_sum(Main.reload_dict, Main.entry_lists)
        # sum_list, class_list = [10,30], ["dayly_food_keys", "dayly_food_keys"]
        base_stock = Main.stock.base_stock
        Main.end_stock = Main.calculate.stock_balance(base_stock)
        print (Main.end_stock, "(end_stock)", Main.total_sum, "(total_sum)")


    def write_func(self):
        Main.writing.list_entries(summe_list=Main.entry_lists[0], reason_list=Main.entry_lists[1],
                             date_list=Main.entry_lists[2])


    def main_board(self):
        Main.pickeling_func(self)
        Main.stock_func(self)
        Main.writing = Writing(Main.reload_dict["month"])
        while True:
            inp = input("<new entry> or <final calculations>?: ")
            if inp == "new entry" or inp == "final calculations":
                inp2 = None
                if inp == "new entry":
                    Main.new_entry = True
                    Main.cycle_func(self)
                    Main.write_func(self)
                    inp2 = input("Was this your last entry?: ")
                Main.calculate_func(self)
                if inp2 in ["yes", "Yes", "YES", "ja", "Ja"] or inp == "final calculations":
                    Main.writing.write_bilance(Main.total_sum, Main.end_stock)
                    Main.entry_status = "final"
                Main.pic.save_data(Main.entry_status, Main.end_stock, 
                Main.total_sum, Main.reload_dict["month"], Entry.cat_dict)
                break


start = Main()
start.main_board()