import csv


if __name__ == '__main__':
    filename = r"c:/Users/sai/Desktop/Accounting_比格沃斯_purchases.csv"
    with open(filename,'r',encoding='utf-8',errors='ignore') as f:
        reader = csv.reader(f)
        print(reader)

        for row in reader:
            print(row)




