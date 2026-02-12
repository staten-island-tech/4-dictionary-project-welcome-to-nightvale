""" 
store_items = [
    {
        "name": "evil tv",
        "price": 500,
        "department": "televisions",
        "desc": "tv that eats your carpet"
    },
 {
        "name": "sinister camera",
        "price": 2,
        "department": "cameras",
        "desc": "this camera is broken but v pretty :33"
    },
  {
        "name": "funky latop",
        "price": 100000,
        "department": "laptops",
        "desc": "it explosions"
    }
] """
""" store_items = {
    "item1" : {
        "name": "evil tv",
        "price": 500,
        "department": "televisions",
        "desc": "tv that eats your carpet"
    },
    "item2" : {
        "name": "sinister camera",
        "price": 2,
        "department": "cameras",
        "desc": "this camera is broken but v pretty :33"
    },
    "item3" : {
        "name": "funky latop",
        "price": 100000,
        "department": "laptops",
        "desc": "it explosions"
    },
} """


store_items = [
    {
        "name": "grass",
        "price": 500,
        "desc": "lovely foilage"
    },
 {
        "name": "evil gargoyle",
        "price": 2,
        "desc": "he watches"
    },
  {
        "name": "orb",
        "price": 100000,
        "desc": "it explosions"
    }
]

""" print(store_items[0]["name"]) """
""" print(store_items) """

""" print("welcome !! to store.")
for index, item in enumerate(store_items):
    print(index, ":", item["name"])
selection = int(input("select an item number to purchase!  "))
def purchase(x):
    if x == index:
        print(item[x])

purchase(selection) """

print("welcome !! to store.")
for index, item in enumerate(store_items):
    print(index, ":", item["name"])
    selection = int(input("select an item number to purchase!  "))
    x = selection
def cart_addition(y)
    if x > store_items:
        
print(store_items[x]["name"])