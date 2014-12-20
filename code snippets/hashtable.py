
def make_hashtable(nbuckets):
    l = []
    for i in range(nbuckets):
        l.append([])
    return l

def hashtable_get_bucket(htable,keyword):
    buckets = len(htable)
    h = hash_string(keyword,buckets)
    return htable[h]



def hash_string(keyword,buckets):
    sum_of_alpha = 0
    for c in keyword:
        sum_of_alpha += ord(c)
    return sum_of_alpha % buckets    

def hashtable_add(htable,key,value):
    loc = hashtable_get_bucket(htable,key)
    loc.append([key,value])
    return htable        


def hashtable_lookup(htable,key):
    for buckets in htable:
        for lists in buckets:
            if lists[0]== key:
                return lists[1]
    return None        

def hashtable_update(htable,key,value):
    h = hashtable_lookup(htable,key)
    if h != None:
        bucket = hashtable_get_bucket(htable,key)
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value       
    else:
        hashtable_add(htable,key,value)
    return htable

"""
-----------------------------------------------------------------



table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

print hashtable_get_bucket(table, "Brick")
#>>> []

print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

-----------------------------------------------------------------



table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]


---------------------------------------------------------------------


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Francis')
#>>> 13

print hashtable_lookup(table, 'Louis')
#>>> 29

print hashtable_lookup(table, 'Zoe')
#>>> 14

--------------------------------------------------------



table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], 
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], 
#>>> ['Rochelle', 94]]]

"""