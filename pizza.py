class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size):
        self.size = size
        self.toppings = []

    def getPrice(self):
        """Price of pizza depends on size and number of toppings."""
        if self.size == 'small':
            price = 120 + 20*len(self.toppings)
        elif self.size == 'medium':
            price = 200 + 20*len(self.toppings)
        elif self.size == 'large':
            price = 280 + 20*len(self.toppings)
        else:
            raise ValueError("Unknown pizza size "+self.size)
        return price
    
    def addTopping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)


class Salad:
    """Mixed vegetable salad, in various sizes."""

    def __init__(self, size):
        """Salad can be small or large."""
        if size not in ('small','large'):
            raise ValueError("Size must be small or large")
        self.size = size

    def getPrice(self):
        """Price of a salad depends only on size."""
        if self.size == 'small':
            price = 25
        elif self.size == 'large':
            price = 40
        else:
            raise ValueError("Unknown salad size "+self.size)
        return price
