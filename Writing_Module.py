class Writing:
    def __init__(self, filename, month, end_stock, sum_totals):
        self.filename = filename
        self.month = month
        self.end_stock = end_stock
        self.sum_totals = sum_totals


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
                f.write(self.month)
                f.write("\n")
                b += 1


    def write_statistics(self):
            with open(self.filename, "a") as f:
                f.write ("Kleider Total: ")
                f.write(str(self.sum_totals[0]))
                f.write(".-")
                f.write(" (")
                f.write(str(self.end_stock[0]))
                f.write(") ")

                f.write("Essen Total: ")
                f.write(str(self.sum_totals[1]))
                f.write(".-")
                f.write(" (")
                f.write(str(self.end_stock[1]))
                f.write(") ")

                f.write("Hygiene Total: ")
                f.write(str(self.sum_totals[2]))
                f.write(".-")
                f.write(" (")
                f.write(str(self.end_stock[2]))
                f.write(") ")

                f.write("Freizeit Total: ")
                f.write(str(self.sum_totals[3]))
                f.write(".-")
                f.write(" (")
                f.write(str(self.end_stock[3]))
                f.write(") ")

                f.write("Handy Total: ")
                f.write(str(self.sum_totals[4]))
                f.write(".-")
                f.write(" (")
                f.write(str(self.end_stock[4]))
                f.write(")")


    def writing_process(self):
        Writing.list_entries(self)
        final = input("Is this your final entry?")
        if final == "yes":
            Writing.write_statistics(self)
