def populationCalculator():
    CURRENT_POPULATION = float(307357870)
    years = float(input("How many years"))
    seconds = years * 31536000
    births = 7 * seconds
    deaths = 13 * seconds
    immigrants = 35 * seconds
    newTotal = int(births + immigrants - deaths + CURRENT_POPULATION)
    print("The projected population", years, "years from now is", newTotal)
populationCalculator()
