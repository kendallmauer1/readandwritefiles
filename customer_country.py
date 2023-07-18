
import csv
with open("customers.csv","r") as original:
    read = csv.reader(original)

    with open("customer_country.csv","w") as new:
        write = csv.writer(new)

        for column in read:
            write.writerow((column[1],column[2],column[4]))
