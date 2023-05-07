class Vehicles:
	carName1 = "Tesla Model X"
	carName2 = "Mustang"
	def main(self):
		print("I have", self.carName1)
		print("I have", self.carName2)


Vehicle_class_object=Vehicles()
print("Your car is:", Vehicle_class_object.carName1)
Vehicle_class_object.main()