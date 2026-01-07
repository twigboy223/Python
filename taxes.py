print("this will do your tax or sale calculation but its very flawed becuase you. must plug in the sale or tax percent in this store")
import time
time.sleep(4)
tax_sale = input("do you want it as a tax or a sale? (tax or sale):    ")
if tax_sale == "tax":
    tax = input("what is the price of the item you are buying:     ")
    tax_cost = input("what is the store tax on this item (into hundreths):    ")
    tax_divider = float(tax_cost) / 100
    tax_amount = float(tax) * float(tax_divider)
    final_tax = float(tax_amount) + float(tax)
    print("the tax on the new item price is: ", final_tax)
if tax_sale == "sale":
    sale = input("what is the price of the item you are buying:     ")
    sale_cost = input("what is the store sale on this item (into hundreths):    ")
    sale_divider = float(sale_cost) / 100
    sale_amount = float(sale) * float(sale_divider)
    final_sale = float(sale) - float(sale_amount)
    print("the sale on the new item price is: ", final_sale)