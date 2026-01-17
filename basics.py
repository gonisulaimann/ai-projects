x = "Excellent"
def myfunc2():
  global x
  x = "superb"
myfunc2()
print("Python is " + x)


a = "Harun"
def function():
  global a
  a = "Goni"
function()
print("My name is " + a)

d = 5
print(type(d))
e = "Hello"
print(type(e))
f = 3.14
print(type(f))
g = True
print(type(g))
h = {"apple"}
print(type(h))