import csv
with open("sales.csv","r") as original:
    read = csv.reader(original)
    next(read)

    with open("salesreport.csv","w") as new:
        write = csv.writer(new)
        write.writerow(["Customer ID","Total"])

        customer_id = " "
        grand_total = 0

        for row in read:
            if row [0] != customer_id:
                if customer_id != " ":
                    write.writerow([customer_id,round(grand_total,2)])
                print(row[0])
                print(grand_total)
                grand_total = 0
                customer_id = row[0]

            subtotal = float(row[3])
            tax = float(row[4])
            freight = float(row[5])
            total = subtotal+tax+freight
            grand_total += total

        write.writerow([customer_id, round(grand_total,2)])
            

