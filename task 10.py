
facts = {
    "raining": True,
    "foggy": False,
    "cloudy": True,
    "sunny": False
}

fact = input("Enter a weather fact: ").lower()

if fact in facts:
    if facts[fact]:
        print(fact, "is True")
    else:
        print(fact, "is False")
else:
    print("Fact not found")
