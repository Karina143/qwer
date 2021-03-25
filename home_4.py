from graph import*
def frame(x,y):
    penSize(3)
    penColor("black")
    brushColor("green")
    rectangle(x,y,x+50,y+50)
def roof(x,y):
    brushColor("brown")
    polygon( [(x-5,y),(x+25,y-25),(x+55,y),(x-5,y)])
def window(x,y):
    penColor("white")
    penSize(3)
    brushColor("black")
    rectangle(x+10,y+10,x+25,y+35)
    line(x+10,y+20,x+25,y+20)
    line(x+17,y+20,x+17,y+35)
def home(x,y):
    frame(x,y)
    roof(x,y)
    window(x,y)
    
print("Введите координаты домика")
x = int(input("x= "))
y = int(input("y= "))

home(10,100)
home(80,100)
home(150,100)
home(220,100)
run()
