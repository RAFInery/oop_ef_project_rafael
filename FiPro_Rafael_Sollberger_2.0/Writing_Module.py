class Writing:

    filename = None
    end_stock = None
    sum_totals = None

    def __init__(self, month):
        self.month = month

        def set_filename(self):
            Writing.filename = "Abrechnung_%s" % (self.month)
        set_filename(self)


    def list_entries(self, summe_list, reason_list, date_list):
        space = " "
        b = 0
        for obs in summe_list:
            x = 20
            x = x - (len(reason_list[b]) - 6) #Durchschnittslänge der Keys = 6

            with open(self.filename, "a") as f:
                f.write(str(summe_list[b]))
                f.write(".-")
                f.write(space*20)
                f.write(reason_list[b])
                f.write(space * x)
                f.write(date_list[b])
                f.write(space)
                f.write(self.month)
                f.write("\n")
                b += 1


    def get_st_and_es(self, sum_totals, end_stock):
        Writing.sum_totals = sum_totals
        Writing.end_stock = end_stock


    def write_statistics(self):
        with open(self.filename, "a") as f:
            f.write ("Kleider Total: ")
            f.write(str(Writing.sum_totals["clothes_keys"]))
            f.write(".-")
            f.write(" (")
            f.write(str(Writing.end_stock["clothes_keys"]))
            f.write(") ")

            f.write("Essen Total: ")
            f.write(str(self.sum_totals["dayly_food_keys"]))
            f.write(".-")
            f.write(" (")
            f.write(str(self.end_stock["dayly_food_keys"]))
            f.write(") ")

            f.write("Hygiene Total: ")
            f.write(str(self.sum_totals["hygiene_keys"]))
            f.write(".-")
            f.write(" (")
            f.write(str(self.end_stock["hygiene_keys"]))
            f.write(") ")

            f.write("Freizeit Total: ")
            f.write(str(self.sum_totals["leisure_keys"]))
            f.write(".-")
            f.write(" (")
            f.write(str(self.end_stock["leisure_keys"]))
            f.write(") ")

            f.write("Handy Total: ")
            f.write(str(self.sum_totals["mobile_keys"]))
            f.write(".-")
            f.write(" (")
            f.write(str(self.end_stock["mobile_keys"]))
            f.write(")")


    def write_bilance(self, sum_totals, end_stock):
        Writing.get_st_and_es(self, sum_totals, end_stock)
        Writing.write_statistics(self)

