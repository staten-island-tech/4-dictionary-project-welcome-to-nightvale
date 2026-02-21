""" store_items = [
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

""" print("welcome !! to evil store.")
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

cart_addition(selection) """

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
    },
  {
        "name": "canned scream",
        "price": 43.21,
        "desc": "please do not open while inside store"
    },
  {
        "name": "whimsical frog",
        "price": 200,
        "desc": "eats cannoli :33"
    },
  {
        "name": "spooky mirror",
        "price": 1.50,
        "desc": "BROKEN"
    },
  {
        "name": "hedge maze",
        "price": 2500,
        "desc": "may include friends"
    }
]

cart = []
t = []
def cart_addition(x):
    for index, item in enumerate(store_items):
        if x == index:
            cart.append(item["name"])
            print(f"{item["name"]} has been added to cart")
def total(y):
    for index, item in enumerate(store_items):
        if y == index:
            t.append(item["price"])

print("welcome !! to store.")
for index, item in enumerate(store_items):
    print(index, ":", item["name"])
selection = int(input("select an item number to purchase!  "))

cart_addition(selection)
total(selection)

ask_cont = input("would you like to keep shopping? (indeed/nuh uh)  ")
while ask_cont == "indeed":
    selectionn = int(input("select another item!  "))
    cart_addition(selectionn)
    total(selectionn)
    ask_cont = input("would you like to keep shopping? (indeed/nuh uh)  ")

print("thank you for shopping !!")
print(f"Your cart: {cart}")
print(f"Your total: ${sum(t)}")