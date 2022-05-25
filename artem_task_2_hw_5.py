lst_products = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg']
i = 0
new_products = []
while i <= len(lst_products) - 1:
    if lst_products[i] != "eg":
        new_products.append(lst_products[i])
    i += 1

print(new_products)
