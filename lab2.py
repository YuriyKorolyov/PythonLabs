import json

class Weapon:
    

    def __init__(self,*args):
        self.__name = args[0]
        self.__damage = args[1]
        self.__range = args[2]

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self,damage):
    
         if damage <= 0:
            raise ValueError
         self.__damage = damage

        
    @property 
    def range(self):
        return self.__range
    @range.setter
    def range(self,_range):
            if _range <= 0:
                raise ValueError
            self.__range = _range
        

class Gun(Weapon):

    def __init__(self,*args):
        super().__init__(args[0],args[1],args[2])
        self.mode = args[3]    # single - False; automatic - True



    def hit(self, actor, target):

    
            if actor.posX + self.range < target.posX or actor.posY + self.range < target.posY:
                raise ValueError       

            if(self.mode):
                for i in range (3):
                    target.hp -= self.damage
            else:
                target.hp -= self.damage


class Person:
    def __init__(self,*args):
        if (len(args) == 1):
            self.posX = args[0]["posX"]
            self.posY = args[0]["posY"]
            self.hp = args[0]["hp"]
        else:
            self.posX = args[0]
            self.posY = args[1]
            self.hp = args[2]
 
    def move(self, x, y):
        self.posX= self.posX + x
        self.posY = self.posY + y
 
    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True
 
    def get_damage(self, amount):
        self.hp = self.hp - amount
 
    def get_coords(self):
        return (self.posX, self.posY)


class Enemy(Person):
    def __init__(self,*args):
        if (len(args) == 1):
            super().__init__(args[0]["posX"], args[0]["posY"], args[0]["hp"])
            self.weapon = args[0]["weapon"]
        else:    
            super().__init__(args[0], args[1], args[2])
            self.weapon = args[3]
 
    def hit(self, target):
        if(target.is_alive() & self.is_alive()):
            self.weapon.hit(self, target)   #enemy hits
        


class Hero(Person):

    def __init__(self, *args):
        if (len(args) == 1):
            super().__init__(args[0]["posX"], args[0]["posY"], args[0]["hp"])
            self.name = args[0]["name"]
            self.weapon = args[0]["weapon"]
        else:    
            super().__init__(args[0], args[1], args[2])
            self.name = args[3]
            self.weapon = args[4]

    def hit(self, target):
        if(target.is_alive()& self.is_alive()):
            self.weapon.hit(self,target)    # hero hits


class Group:
    def __init__(self):        
        self.members = []    

    def add_member(self, char):        
        self.members.append(char)

    def delete_member(self, char):
        if (self.memebers.find(char) >= 0):            
            self.members.pop(self.members.find(char))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def print(self):
        for item in self.members:
            item.print()

    def import_file(self):
        raw_party = json.load(open('data.json', 'r'))
        self.members = []
        for member in raw_party["members"]:
            if 'name' in member:
                self.add_member(Hero(member))
            else:
                self.add_member(Enemy(member))

    def export_file(self, file_name):
        with open(file_name, "w") as the_file:
            the_file.write(self.to_json())

kalash = Gun("Kalash",40,10,True)
#kalash.damage = -1
#kalash.range= -1
hero = Hero(1,2,300,"John",kalash)
enemy = Enemy(11,2,120,kalash)
print(enemy.hp)
hero.hit(enemy)
print(enemy.hp)
enemy.hit(hero)
print(hero.hp)
print(enemy.hp)
hero.hit(enemy)

###
group = Group()
group.add_member(hero)
group.add_member(enemy)
print("The Group was sended to JSON file")
group.export_file("data.json")
group.print()

group1 = Group()
group1.import_file("data.json")
print("\nThe Group received from JSON file")
group1.print()
