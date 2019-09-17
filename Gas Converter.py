#Spencer Paquette 9/17/19
def gasConverter():
    gasGallons = float(input("How many gallons of gas are you using?"))
    gasLiters = gasGallons * 3.78541178
    oilBarrels = gasGallons / 19.5
    carbonProduced = gasGallons * 20
    price = gasGallons * 3.35
    print("Liters:", gasLiters)
    print("Number of oil barrels:", oilBarrels)
    print("Pounds of CO2 produced:", carbonProduced)
    print("Price in USD:", price)
gasConverter()
