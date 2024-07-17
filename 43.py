dic = {
    "pial":17,
    "mim":118,
    "adip":115,
    "piyas":119,
    "piyas":119,    
}

print(dic)
print(type(dic))
print(len(dic))
print(dic["pial"]) 

print(dic.values()) 
print(dic.keys())

dic ["pial"] =12345
print(dic)

more_dic = {"nadia" : 123}

dic.update(more_dic)
print(dic)
dic.pop("pial")
print(dic)

dic.popitem()
print(dic)
#dic.clear()
print(dic)

for x in dic:
    print(x)

for x in dic:
    print(dic[x])
    
for x in dic.items():
    print(x)
    
for x,y in dic.items():
    print(x,y)
    
    #nesed dictionary


phone = {
    "area1": {
        "x":111,
        "y":2,
        "z":3,   
    },
    "area2": {
        "p":1,
        "q":2,
        "r":3, 
    },
    "area3": {
        "a":1,
        "b":2,
        "c":3,
        
    }
}

print(phone)
print(phone["area1"]["x"])