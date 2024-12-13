class x:
  pin  = 1376
  def __private(self):
    print("I am inside class! i am prodected  using 2underscores")
  def display(self):
    print("i am inside class without protection!",x.__private)


#object creation
ob1 = x()
ob1.__private()
ob1.display()
print(ob1.pin)