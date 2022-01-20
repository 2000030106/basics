# class Client:
#     name = "satya sai"
#     phone = "1236547890"
#     email = "saisrujan123@gmail.com"
#     purchases = 12.0
#
#
# def main():
#     firstClient = Client()
#     firstClient.name = "satya sai"
#     firstClient.email = "saisrujan123@gmail.com"
#     print(firstClient.name)
#     print(firstClient.phone)
#     print(firstClient.email)
#     print(firstClient.purchases)

#
# class Person:
#     name="I have no name :("
#     def sayName(self):

class Person:
    name="Satyasai"
    def sayName(self):
        print("My name is ",self.name)

def main():
    x1 = Person()
    x1.sayName()
    x2 = Person()
    x2.sayName()
    x1.name="abc"
    x2.name="xyz"
    print(x1.name)
    print(x2.name)
main()
