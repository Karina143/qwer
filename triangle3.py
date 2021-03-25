from graph import*
def triangle(x,y):
    polygon([(x,y),(x+40,y),(x+20,y+30)])
brushColor("purple")
triangle(30,30)
brushColor("red")
triangle(50,60)
brushColor("green")
triangle(70,30)
run()
