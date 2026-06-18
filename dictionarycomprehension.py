#Dictionary Comprehension

products={
    "name":'apple',
    "quantity":40,
    "price":2000
}


y= {keys:items / 2 for keys,items in products.items() if keys == 'price' }
print(y)

# tomorrow lambda and modules