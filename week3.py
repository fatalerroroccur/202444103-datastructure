l = [99,8,-7,8,16]
for i in range(len(l)):
    print(f"{l[i]:3} {id(l[i])}")

groups = ['hot','seventeen','blackpink','njz']
ratings = [1,2,3,4]
group_rating = dict(list(zip(groups,ratings)))
print(group_rating)


#def duplicate_city(cities):
#    result_city = []
#    s=set()
#    for city in cities:
#        l1 = len(s)
#        s.add(city)
#        l2 = len(s)
#        if l1 == l2:
#            result_city.append(city)
#        return result_city
#cities = ['incheon','seoul','incheon','incheon','gwangju']
#cities = set(cities)
#cities.add('incheon')
#print(cities)
#print(set(duplicate_city(cities)))

def inters(l3,l4):
    l5 = []
        for v in l3:
            if v in l4:
                l5.append(v)
        return l5
    l3 = [45,5,22,31,7,19]
    l4 = [22,1,5,2,27,27,19,23,13,41]
    print(inters(l3,l4))