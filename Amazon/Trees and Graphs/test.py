#numOfItems
#sortParam
#sortOrder
#itemsPerPage
#PageNumber
import collections
numOfItems = 2
sortOrder = 0
sortParam = 1
itemsPerPage = 2
PageNumber = 0

items = {
    'p3' : [5,2],
    'p2' : [4,3],
}

rev = True if sortOrder == 1 else False

if sortParam == 0:
    items = collections.OrderedDict(sorted(items.items(), reverse = rev))
else:
    items = collections.OrderedDict(sorted(items.items(), key=lambda item: item[1][sortParam-1],  reverse = rev))
print(items)
arr = [] * pageNumber
c = 0
while c < itemsperPage: 
    for k, v in x:
        arr[c].append(input[v])
# print arr[pageNumber]
    


