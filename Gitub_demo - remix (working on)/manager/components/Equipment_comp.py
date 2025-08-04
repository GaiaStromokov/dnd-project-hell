import json
import shared
from Sheet.get_set import *
from collections import defaultdict

class Item:
    def __init__(self, name, attributes):
        self.Name = name
        for key, value in attributes.items():
            setattr(self, key, value)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __repr__(self):
        attributes = {k: v for k, v in self.__dict__.items()}
        attr_str = ', '.join(f"{k}={repr(v)}" for k, v in attributes.items())
        return f"Item({attr_str})"

class Bazaar:
    def __init__(self):
        self.items = self.load_items("dist/item_comp.json")
        self.Category_LU = defaultdict(list)
        self.Slot_LU = defaultdict(list)
        self.Property_LU = defaultdict(list)
        self.Tier_LU = defaultdict(list)
        self.Prof_LU = defaultdict(list)

        for name, item in self.items.items():
            for cat in item.Cat:
                self.Category_LU[cat].append(name)

            self.Slot_LU[item.Slot].append(name)

            if hasattr(item, 'Prop'):
                for prop in item.Prop:
                    self.Property_LU[prop].append(name)
            
            self.Tier_LU[item.Tier].append(name)

            if item.Tier == 0:
                if item.Slot == "Weapon":
                    self.Prof_LU["Weapon"].append(name)
                elif item.Slot == "Armor":
                    self.Prof_LU["Armor"].append(name)

    def load_items(self, filepath):
        items_dict = {}
        with open(filepath, mode='r', encoding='utf-8') as json_file:
            for name, attributes in json.load(json_file).items():
                items_dict[name] = Item(name, attributes)
        return items_dict

    def Category(self, category):
        return self.Category_LU.get(category, [])

    def Mult_Category(self, tier, *categories):
        category_items = set.intersection(*(set(self.Category(c)) for c in categories))
        tier_items = set(self.Tier_LU.get(tier, []))
        return list(category_items & tier_items)

    def Slot(self, slot):
        return self.Slot_LU.get(slot, [])

    def Property(self, prop):
        return self.Property_LU.get(prop, [])

    def Item(self, name):
        return self.items.get(name)

    def Tier(self, tier):
        return self.Tier_LU.get(tier, [])
        
    def Prof(self, prof):
        return self.Prof_LU.get(prof, [])
    
    @property
    def OffHand(self):
        return list(set(self.Slot("Hand")) - set(self.Property("Two-handed")))

    def __repr__(self):
        return '\n'.join(self.items.keys())