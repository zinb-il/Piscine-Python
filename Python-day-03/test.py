# class Test:
#     def __init__(self):
#         self.att1 = 'ttt'
#         self.__price = 1000
#         print("New object was created")
    
#     def sell(self):
#         print("The selling price is:{}".format(self.__price))
    
#     def setPrice(self, price):
#         self.__price = price


# def main():
#     e = Test()
#     print(e.sell())

# if __name__ == "__main__":
#     main()


class Laptop:
	def __init__(self):
		self.__price = 45000
		
	def sell(self):
		print("The selling price is:- {}".format(self.__price))
		
	def setPrice(self, price):
		self.__price = price

def main():
    #creating the object or instance
    l1 = Laptop()
    

    # #access selling price
    # l1.sell()

    # #change the values
    l1.__price = 50000
    l1.sell()

    #change the value using setPrice
    print(l1.__price)
    # l1.sell()

if __name__ == "__main__":
    main()