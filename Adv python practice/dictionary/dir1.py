d1={"student":"prasad","student id":101,"student sal":89000.00}
d2={"name":"ravi","id":102,"sal":99000.00}
d1.update(d2)
d2["degn"]="developer"
d1.update(d2)
d3=d1.values()
print(d3)

#d3=d1.keys()
#d5=d2.keys()
#d4=d2.values()
#d5=d1.values()
print(d1["student sal"])
print(d2["sal"])