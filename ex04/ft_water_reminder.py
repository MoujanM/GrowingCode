def ft_water_reminder():
    last_water = int(input("Days since last watering: "))
    max_dry = 2;
    if last_water <= max_dry:
        print("Plants are fine.")
    else:
        print("Water the plants!")