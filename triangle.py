from graph import*
def triangle(x,y):
    polygon([(x,y),(x+40,y),(x,y+30)])
brushColor("purple")
triangle(50,40)
brushColor("red")
triangle(10,40)
brushColor("green")
triangle(50,10)
run()
