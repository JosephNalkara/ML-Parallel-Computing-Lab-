from itertools import combinations

transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Eggs'],
    ['Milk', 'Bread', 'Eggs'],
    ['Milk', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Butter', 'Eggs']
]

def item_set_1(transactions):
  item_sets=set()
  for i in transactions:
    for item in i:
      item_set.add(item)
  return item_set

item_set = item_set_1(transactions)
print(item_set)

n=len(transactions)
print(n)
def support(item_set,transactions):
  count=0
  for i in transactions:
    if set(item_set).issubset(set(i)):
      count+=1
  return count/n

sup=support(item_set,transactions)
print(sup)
