def ft_plant_age():
    harvest_age = 60
    age = int(input("Enter plant age in days: "))
    if (age >= harvest_age):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")