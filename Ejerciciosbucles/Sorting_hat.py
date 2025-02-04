Griffindor = 0
Revenclaw = 0
Hufflepuff = 0
Slytherin = 0


Q1 = int(input("Do you like Dawn or Dusk?\n 1 for Dawn, 2 for Dusk: "))

if Q1 == 1:
    Griffindor = 1
    Revenclaw = 1
elif Q1 == 2:
    Hufflepuff = 1
    Slytherin = 1
else:
    print("Invalid option")

Q2 = int(input("When I'm dead, I want to remember me as:\n 1 for Good, 2 for Great, 3 for Wise, 4 for Bold: "))

if Q2 == 1:
    Hufflepuff = 2
elif Q2 == 2:
    Slytherin = 2
elif Q2 == 3:
    Revenclaw = 2
elif Q2 == 4:
    Griffindor = 2
else:
    print("Invalid option")
    
Q3 = int(input("Which kind of instrument most pleases your ear?\n 1 for The violin, 2 for The trumpet, 3 for The piano, 4 for The drum: "))

if Q3 == 1:
    Slytherin = 4
elif Q3 == 2:
    Hufflepuff = 4
elif Q3 == 3:
    Revenclaw = 4
elif Q3 == 4:
    Griffindor = 4
else:
    print("Invalid option")
    
print("Griffindor: ", Griffindor)
print("Revenclaw: ", Revenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

houses = {
    "Griffindor": Griffindor,
    "Revenclaw": Revenclaw,
    "Hufflepuff": Hufflepuff,
    "Slytherin": Slytherin
}
    
print("The most score is: ", max(houses, key=houses.get))
