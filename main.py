class x:
  pin  = 1376
  def private(self):
    print("I am inside class! i am prodected  using 2underscores")
  def display(self):
    print("i am inside class without protection!",x.private)


#object creation
ob1 = x()
ob1.private()
ob1.display()
print(ob1.pin)