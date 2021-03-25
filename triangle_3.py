from graph import*
def triangle(x,y,a,b):
    polygon([(x,y),(x+a,y+b),(x-a,y+b)])
brushColor("green")
triangle(70,50,10,15)
triangle(6,80,20,10)
triangle(80,90,30,10)
triangle(80,100,40,10)
run()

