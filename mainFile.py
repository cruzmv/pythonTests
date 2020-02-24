cf = "main.txt"
f = open(cf,"r")

print(f.name)
print(f.closed)
print(f.mode)

st = f.read()
print(":",st)

fw = open(cf,"a")
fw.write("New Line\n")
fw.close()
f.close()
print('-------------------------')

from oops import Emp

p = Emp("Maurício",41)
p.pName()
p.pAge()
print('-------------------------')
print('{} {}'.format(p.name,p.age))

	
