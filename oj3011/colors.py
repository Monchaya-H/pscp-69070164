"""Colors"""
name_colors=input().capitalize()
name_2colors=input().capitalize()
if name_colors == "Red"  and name_2colors == "Yellow":
    print("Orange")
elif name_colors == "Yellow" and name_2colors == "Red":
    print("Orange")
elif name_colors == "Red" and name_2colors == "Blue":
    print("Violet")
elif name_colors == "Blue" and name_2colors =="Red":
    print("Violet")
elif name_colors == "Yellow" and name_2colors == "Blue":
    print("Green")
elif name_colors == "Blue" and name_2colors == "Yellow":
    print("Green")
elif name_colors== "Red" and name_2colors== "Red":
    print("Red")
elif name_colors == "Yellow" and name_2colors == "Yellow":
    print("Yellow")
elif name_colors == "Blue" and name_2colors == "Blue":
    print("Blue")
else:
    print("Error")
