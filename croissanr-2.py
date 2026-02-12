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
]

print("welcome !! to evil store.")
for index, item in enumerate(store_items):
    print(index, ":", item["name"])
selection = int(input("select an item number to purchase!  "))
cart = []
def cart_addition(x):
    for i in store_items:
        if ('x = index'):
            print(f"({item["name"]} has been added to cart)")
            cart.append(x)
            print(f"(Items in your cart: {cart}")

cart_addition(selection)