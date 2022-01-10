# Coffee-Machine
**MenuItemClass**

Attributes:

**- name**
    (str) The name of the drink.
    e.g. “latte”
**- cost**
    (float) The price of the drink.
    e.g1.
**- ingredients**
    (dictionary) The ingredients and amounts required to make the drink.
    e.g.{“water”: 100, “coffee”: 16}

**MenuClass**

Methods:

- **get_items()**
    Returns all the names of the available menu items as a concatenated string.
    e.g.“latte/espresso/cappuccino”
**- find_drink(order_name)**
    Parameterorder_name: (str) The name of the drinksorder.
    Searches the menu for a particular drink by name. Returns aMenuItemobject if it exists,
    otherwise returnsNone.

**CoffeeMakerClass**

Methods:

**- report()**
    Prints a report of all resources.
    e.g.
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
**- is_resource_sufficient(drink)**
    Parameterdrink: (MenuItem) TheMenuItemobject tomake.
    Returns True when the drink order can be made, False if ingredients are insufficient.
    e.g.
    True
**- make_coffee(order)**
Parameterorder: (MenuItem) The MenuItem object to make.
Deducts the required ingredients from the resources.

**MoneyMachineClass**

Methods:

**- report()**
    Prints the current profit
    e.g.
    Money: $
**- make_payment(cost)**
    Parametercost: (float) The cost of the drink.
    Returns True when payment is accepted, or False if insufficient.
    e.g.False


