#python booleans

print(10>9)

print(10==9)

print(10<9)

print(bool("abc"))

print(bool(0))

#python operators

print(10*5)

print(10/2)

fruits=["apple","banana"]
if "apple" in fruits:
    print("Yes,apple is a fruit")


if(5!=10):
    print("5 and 10 is not equal")

if(5==10 or 4==4):
    print("at least one of statements is True")

fruits=["apple","banana","cherry"]
print(friuts[1])

fruits=["apple","banana","cherry"]
fruits[0]="kiwi"

fruits=["apple","banana","cherry"]
fruits.append("orange")

fruits=["apple","banana","cherry"]
fruits.insert(1,"lemon")

fruits=["apple","banana","cherry"]
fruits.remove("banana")

fruits=["apple","banana","cherry"]
print(fruits[-1])

fruits=["apple","banana","cherry","orange","kiwi","lemon","mango"]
print(fruits[2:5])

fruits=["apple","banana","cherry"]
print(len(fruits))

fruits=("apple","banana","cherry")
print(fruits[0])

fruits=("apple","banana","cherry")
print(len(fruits))

fruits=("apple","banana","cherry")
print(fruits[-1])

fruits=("apple","banana","cherry","orange","kiwi","lemon","mango")
print(fruits[2:5])

fruits={"apple","banana","cherry"}
if "apple" in fruits:
    print("Yes apple is a fruit")

fruits={"apple","banana","cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

a = 50
b = 10
if a>b:
    print("Hello World")

a=50
b=10
if a!=b:
    print("Hello World")

a=50
b=10
if a==b:
    print("Yes")
else:
    print("No")

a=50
b=10
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")

if a==b and c==d:
    print("Hello")

if a==b or c==d:
    print("Hello")

if 5>2:
    print("YES")


a=2
b=5
print("YES") if a == b else print("NO")

a=2
b=50
c=2
if a==c or b==c:
    print("YES")

i=1
while i<6:
    print(i)
    i+=1

i=1
while i<6:
    if i==3:
        break
    i+=1

i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
    print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
    print(x)

for x in range(6):
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)