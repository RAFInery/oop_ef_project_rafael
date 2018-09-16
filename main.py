from Stock_Module import Stock
from Entry_Module import Cycle, Entry
from Calculations_Module import Calculate
from Writing_Module import Writing

def stock_func():
    global stock
    stock = Stock()
    stock.continue_or_new()
stock_func()


def cycle_func():
    global cycle
    cycle = Cycle()
    # entry = Entry()
    print (cycle.cycle())
cycle_func()


def calculate_func():
    sum_list, class_list = cycle.ret_sum_and_class()
    # sum_list, class_list = [10,30], ["dayly_food_keys", "dayly_food_keys"]
    base_stock = stock.return_stock()
    calculate = Calculate()
    calculate.sum_calc(sum_list, class_list)
    calculate.stock_balance(calculate.sum_totals, base_stock)
calculate_func()


def write_func():
    pass


def saving_func():
    stock.save_stock()
# saving_func()





