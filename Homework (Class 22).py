def tup_prod(tuple):

  product = 1 
  for i in tuple:
    product *= i 
  return product

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

product1 = tup_prod(tup1)
product2 = tup_prod(tup2)

print('The product of tup1 is:', product1)
print('The product of tup2 is:', product2)