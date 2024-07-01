# Задача:

# 1. Создайте два списка: 1 - название товаров в магазине, 2 - цены этих товаров. 
goods = ['яблоко', 'груша', 'слива', 'чеснок', 'банан']
prices = [310, 420, 400, 87, 280]
# print(type(goods))
# print(type(prices))
# print(goods)
# print(prices)

# 2. Объедините два списка, используя функцию zip. 
market = zip(goods, prices)
# print(market)
# print(type(market))

# 3. Конвертируйте результат сначала в список, а потом в словарь. 
# market_list = list(market)
market_dict = dict(market)

# 4. Результаты конвертации выведите в терминал.   
# print(market_list)
print(market_dict)