import json

x = {
    "name ":"andria",
    "age" : 11,
    "married" : False,
    "divorced" : False,
    "chldren" : False,
    "pets" : None,
    "cars" : [
         {"model" : "mercedes s class", "mpg" : 27.5},
     ]
   }

# convert into JSON:

y = json .dumps(x)

print(y)

# the result is a JSON string:



print(y)
