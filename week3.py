l = [99,8,-7,8,16]
for i in range(len(l)):
    print(f"{l[i]:3} {id(l[i])}")

groups = ['hot','seventeen','blackpink','njz']
ratings = [1,2,3,4]
group_rating = dict(list(zip(groups,ratings)))
print(group_rating)