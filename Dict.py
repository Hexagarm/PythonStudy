#Key与value的组合
d = {'micle':85, 'bob':10}
print (d)

#输出key的value值
print(d["bob"])
#输出key的value值,如果key不存在则输出none
print(d.get("bob"))
print(d.get('b'))

#删除key
d.pop('bob')
print(d)