from pizza import Pizza, Salad

# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type hint on the pizza parameter, maybe not
# - if you use type hint ':Pizza' on the parameter, it should


def order_pizza(pizza):
    """Print a description of a pizza, along with its price."""

    # create printable description of the pizza such as
    # "small pizza with muschroom" or "small plain pizza"
    description = pizza.size
    if pizza.toppings:
        description += " pizza with "+ ", ".join(pizza.toppings)
    else:
        description += " plain cheese pizza"
    print(f"A {description}")
    print("Price:", pizza.getPrice(), "Baht")


def make_pizza(size, *toppings):
    """Build a pizza with optional toppings.

    :param size: size of the pizza
    :param toppings: optional names of toppings
    :returns: a pizza (of course)
    """
    pizza = Pizza(size)
    for topping in toppings:
        pizza.addTopping(topping)
    return pizza


if __name__ == "__main__":
    # small pizza with 3 toppings
    pizza = make_pizza('small', 'mushroom', 'pineapple', 'tomato')
    order_pizza(pizza)

    # a plain medium pizza
    pizza2 = make_pizza("medium")
    order_pizza(pizza2)

    # large pizza with only one topping
    pizza3 = make_pizza("large", "seafood")
    order_pizza(pizza3)
