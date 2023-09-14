#!/usr/bin/env python3

class CashRegister:
  
  total = 0
  last_transaction_price = 0
  

  def __init__(self, discount=0):
    self.discount = discount
    self.items = []

  @property
  def discount(self):
    return self._discount
  @discount.setter
  def discount(self, discount):
      self._discount = discount

  @property
  def items(self):
    return self._items
  @items.setter
  def items(self, items):
    self._items = items

  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.last_transaction_price = price * quantity
    for i in range(quantity):
      self.items += [title]

  def apply_discount(self):
    if self.discount != 0:
      self.total *= (100 - self.discount) / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction_price
    self.items.pop(-1)