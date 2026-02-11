
""" store_items = {
    "item1" = {
        "name": "evil tv",
        "price": 500,
        "department": "televisions",
        "desc": "tv that eats your carpet"
    },
    "item2" = {
        "name": "sinister camera",
        "price": 2,
        "department": "cameras",
        "desc": "this camera is broken but v pretty :33"
    },
    "item3" = {
        "name": "funky latop",
        "price": 100000,
        "department": "laptops",
        "desc": "it explosions"
    }
} """
#for some reson the above code does not work??
#even though it is the exact same as below, which does work

store_items = {
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
}

""" print(store_items["item1"]["name"]) """
""" print(store_items) """

for index, item in enumerate(store_items):
    print(index, ":", item["name"])
