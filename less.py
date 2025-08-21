class Pizza:
    ingredients=[]
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

bbq = Pizza.barbecue()
# peperoni = Pizza.peperoni()
# margherita = Pizza.margherita()
print(sorted(bbq.ingredients))
# print(sorted(peperoni.ingredients))
# print(sorted(margherita.ingredients))