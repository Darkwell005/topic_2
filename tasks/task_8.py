oklad: int = 50000
tax_rate: float = 0.13  #13% в десятичной 0.13

tax: float = oklad * tax_rate
salary: float=oklad - tax

print('Размер зарплаты:',oklad)
print('Размер подоходного налога:',tax)
print('Сумма на руки:',salary)