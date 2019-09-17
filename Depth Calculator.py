#Spencer Paquette 9/17/19
def depthCalc():
    lakeVol = float(input("What is the volume of the great lakes"))
    usArea = float(input("What is the area of the contiguous United States"))
    depth = lakeVol / usArea
    print("The new depth is:", depth)
depthCalc()
