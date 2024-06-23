data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

dict={}

for i in data:
    if i['item'] not in dict:
        dict[i['item']] = i['amount']
    else:
        dict[i['item']] += i['amount']
    
print(dict)
    