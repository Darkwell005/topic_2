cost = 1000#это число составляет 100%
discount = 20
quantity = 3
#Необходимо вычесть из 100%-20%,это будет составлять % единицы предмета со скидкой
discount1 = (100 - discount) * cost / 100
total_cost = discount1 * quantity
print('Стоимость вашего заказа:',total_cost,'рублей')
