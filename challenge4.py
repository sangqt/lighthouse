item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']
amount_list = [600, 150, 15, 165]
wholesale_price_list = [7000, 1000, 1000, 800]
retail_price = [12.99, 8.99, 9.99, 3.99]
for i in range(len(item_list)):
    retail = retail_price[i] * amount_list[i]
    if(retail > wholesale_price_list[i]):
        print(f"{item_list[i]}. No")
    else:
        print(f"{item_list[i]}. Yes")
