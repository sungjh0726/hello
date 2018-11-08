class Bank:
	def __init__(self):
		self.money = 0 #내자신이 갖고있는 머니가 빵원이다
		print("Bank가 생성되었습니다!!")
    def deposit(self, money):
		self.money += money; 

wooribank = Bank()
shinhan = Bank()
m = Singer()
l = Singer()


class Dog:
	def __init__(self):
		self.name = "bori"
		print( self.name "was Born")

	def speak(self):
		print("YELP!", self.name)

    def wag(self):
    		print("Dog's wag tail")

    def __del__(self):
            print("destroy!!")


puddle = Dog()
