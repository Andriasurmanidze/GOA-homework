import json

x = {
  "name": "Andria",
  "age": 11,
  "married": False,
  "divorced": False,
  "children": ("None"),
  "pets": None,
  "cars": [
    {"model": "mercedes", "mpg": 27.5}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)