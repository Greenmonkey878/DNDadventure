
name = input("your name is ?")
age = input("Enter your age")
weapon = input("Please select one. Spear, Sword, Dagger, Bow.(/n)")
gender = input("What is your gender?")
race = input("What is your race?")


print("Hello " + name + ".")
print("You are! " + age + ".")


# Filler for more customization.

if weapon == "Spear":
    print("You are given a Spear.")
elif weapon == "Sword":
    print("You are given a Sword.")
elif weapon == "Dagger":
    print("You are given a pair of Daggers.")
elif weapon == "Bow":
    print("You are given a Bow.")
else:
    print("Here is a pointy Stick.")


if race == "Dwarf":
    print("You are a Dwarf.")
elif race == "Elf":
    print("You are a Elf.")
elif race == "Orc":
    print("You are a Orc.")
elif race == "Human":
    print("You are a Human.")
else:
    print("Your a Gnome.")


if gender == "Male":
    print("You are a Male.")
elif gender == "Female":
    print("You are a Female.")
else:
    print("You are unisex.")


press_enter = input("Press enter to continue.")
print(press_enter)

print("You start your journey.")
print("Party enters house.")

#import random

Zombie = "You've encountered a Zombie!"
print(Zombie)

Zombie_attack = "Zombie attacks!"
health = "100"
zombie_health = "Zombie has 50hp."
dead = "0"
print(zombie_health)
while health != dead:
    health = input("Current mob Health.")
    if health == dead:
        print("Zombie has perished.")
    elif health == "paralyzed":
        print("Zombie paralyzed")
    else:
        print(Zombie_attack)


press_enter = input("Press enter to continue.")
print(press_enter)
print("Party continues walking through door.")
