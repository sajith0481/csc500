import numpy as np

# Define the types of equipment
equipment_types = ["Rifles", "Tanks", "Helicopters", "Field Rations", "Night Vision Goggles"]
equipment_dict = {equipment: index for index, equipment in enumerate(equipment_types)}

# Initialize the inventory array with zeros
inventory = np.zeros(len(equipment_types), dtype=int)

# Function to update the inventory
def update_inventory(item, quantity):
    if item in equipment_dict:
        inventory[equipment_dict[item]] += quantity
    else:
        print("Item not recognized.")

# Example updates
update_inventory("Rifles", 150)
update_inventory("Tanks", 30)
update_inventory("Helicopters", 15)

# Print the updated inventory
for equipment, index in equipment_dict.items():
    print(f"{equipment}: {inventory[index]} units")
