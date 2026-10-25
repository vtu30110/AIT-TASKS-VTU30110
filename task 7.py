
monkey = "Door"
box = "Window"
banana = "Center"
on_box = False
has_banana = False

actions = [
    "Move monkey to the box",
    "Push box to the center",
    "Climb onto the box",
    "Grasp the banana"
]

print("Monkey Banana Problem")
print("Goal: Get the banana")

for action in actions:
    print(action)

    if action == "Move monkey to the box":
        monkey = box

    elif action == "Push box to the center":
        monkey = banana
        box = banana

    elif action == "Climb onto the box":
        on_box = True

    elif action == "Grasp the banana" and on_box:
        has_banana = True

if has_banana:
    print("Success! Monkey got the banana.")
