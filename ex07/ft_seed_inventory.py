def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        unit = f'{unit} available'
    if unit == "grams":
        unit = f'{unit} total'
    if unit == "area":
        unit = f'covers {unit} meters'
    seed = seed_type.title()
    print(f'{seed} seeds : {quantity} {unit}')
    

""" 
ft_seed_inventory("tomato", 15, "packets")

ft_seed_inventory("carrot", 8, "grams")

ft_seed_inventory("lettuce", 12, "area") 

"""

