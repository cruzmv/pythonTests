#list
li = ['feijao','arroz','ovo']
print(li)

#tople
tl = (1,2,3)
print(tl)

#set
st = {1,2,3}
print(st)

#Dictionary
dy = {
	"key1": "Valor1",
	"key2": "Valor2"
}
print(dy)
print(dy["key1"])

x = 10
q = input("número: \n")
qi = int(q)

if (x > qi):
    print("x e maior q qi")
elif(x == qi):
    print("x igual qi")
else:
    print("x:",x,"qi: ",qi)
    


while(x>0):
    x -=1
    print (x)


for i in range(0,12):
    print(i)
    #break
    #continue
    
    
    
def printList(l1):
    for it in l1:
        print("value: ",it)

print('-----------------------')

print('function printList')
printList(li)

print('-----------------------')

for n in li:
    print(n)
    
    
