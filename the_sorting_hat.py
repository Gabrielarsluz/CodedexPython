print("What do you prefer? Insert 1 to dawn or 2 to dusk")

question1 = int(input("Chose a number: "))

gryffindor, ravenclaw, hufflepuff, slyterin = 0,0,0,0


if question1 == 1:
  gryffindor += 1
  ravenclaw += 1

elif question1 == 2:
  hufflepuff += 1
  slyterin += 1

else:
  print("Wrong input." )

print("When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

question2 = int(input("Enter the number of your choice: "))


if question2 == 1:
  hufflepuff += 2

elif question2 == 2:
  slyterin += 2

elif question2 == 3:
 ravenclaw += 2


elif question2 == 4:
  gryffindor += 2

else:
  print("Wrong input." )

print("Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

question3= int(input("Enter the number of your choice: "))


if question3 == 1:
  slyterin += 4

elif question3 == 2:
  hufflepuff += 4

elif question3 == 3:
 ravenclaw += 4

elif question3 == 4:
  gryffindor += 4

else:
  print("Wrong input." )

print("Your results:")
print("-" * 15)
print("Slyterin!", slyterin)
print("Hufflepuff!", hufflepuff)
print("Ravenclaw!", ravenclaw)
print("Gryffindor!", gryffindor)
print("-" * 15)

if hufflepuff >= slyterin and hufflepuff >= ravenclaw and hufflepuff >= gryffindor:
    print("Your house is Hufflepuf! You made",hufflepuff,"points!")
elif slyterin >= hufflepuff and slyterin >= ravenclaw and slyterin >= gryffindor:
    print("Your house is Slyterin! You made",slyterin,"points!")
elif ravenclaw >= hufflepuff and ravenclaw >= slyterin and ravenclaw >= gryffindor:
    print("Your house is Ravenclaw! You made",ravenclaw, "points!")
elif gryffindor >= hufflepuff and gryffindor >= ravenclaw and gryffindor >= slyterin:
    print("Your house is Gryffindor! You made",gryffindor, "points!")
