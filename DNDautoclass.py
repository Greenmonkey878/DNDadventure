import DNDoneshot

Class Character:
    def __init__(name,age,weapon,gender,race):
        self.name = name
        self.age = age
        self.weapon = weapon
        self.gender = gender
        self.race = race
    
    def swing_weapon(self):
        print("You swing your weapon")
    
    def getinfo(self):
        return {name: self.name,
                age: self.age,
                weapon: self.weapon,
                gender: self.gender,
                race: self.race}

