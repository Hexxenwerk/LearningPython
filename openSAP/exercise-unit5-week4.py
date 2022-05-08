with open('invoice_data.txt') as file:
    for line in file:
        item, count_str, price_str = line.strip().split()
        count, price = int(count_str), float(price_str)
        print(f'{item:15}{count:3}{price:7.2f}{count*price:8.2f}')
