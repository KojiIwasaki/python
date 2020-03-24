class myclass():
    def myname(self, who):
        self.name = who

class myclass2(myclass):
    def myaddress(self, jyusho):
        self.address = jyusho

class myclass3(myclass2):
    def myage(self, age):
        self.age = age

person1 = myclass3()

person1.myname("Yamada")
person1.myaddress("Tokyo")
person1.myage(20)

print(person1.name, person1.address, person1.age)