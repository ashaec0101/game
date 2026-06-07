thisset = {"apple", "banana", "cherry"}
print(f"Current inventory: {thisset}")
print("~trips and falls~\n I THINK I LOST SOMETHING?!\n") 
for x in thisset:
 print(f"The {x} was dropped into the abyss")
 thisset.discard(x)
 break
print(f"Current inventory: {thisset}")
fruit= input("What new fruit did you find to add to your bag?: ")
thisset.add(fruit)
print(f"Current inventory: {thisset}")

