class Item:
    def __init__(self, item_id, item_name):
        self.id = item_id
        self.name = item_name
        self.review = 0
        self.star = 0

    def review(self, item):
        item.review +=1
        self.star +=1



item1 = Item("001","Sakshi")
item2 = Item("002", "Diksha")

item1.review(item2)
print(item1.review)
print(item1.star)
print(item2.review)
print(item2.star)


