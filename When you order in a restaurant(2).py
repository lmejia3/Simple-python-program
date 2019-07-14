# Restaurant Tab Calculation Program
# This program will calculate a restaurant tab with tax

# initialization
tax= 0.08
yes=1
no=0

#program greeting
print("Welcome to my humble abode, the best restaurant in the world!!!!")
print("Type 1/0 if you want or not one of the following dishes:")

# cost of ordered items

appetizer_per=print("Pulpo Gallega,$25")
Pulpo_Gallega=int(25)
Pulpo=float(input("Buy?:"))
entree1_per=print("Red Snapper Fillet,$35")
Red_Snapper_Fillet=int(35)
Red=float(input("Buy?:"))
entree2_per=print("Paella Peska,$30")
Paella_Peska=int(30)
Paella=float(input("Buy?:"))
entree3_per=print("Main Lobster Tail,$35")
Main_Lobster_Tail=int(35)
Main=float(input("Buy?:"))
dessert_per=print("Tiramisu,$8")
Tiramisu=int(8)
Tira=float(input("Buy?:"))

#total items
amt_per=Pulpo_Gallega + Red_Snapper_Fillet + Paella_Peska + Main_Lobster_Tail + Tiramisu

#compute tab with tax
items_cost = amt_per
tab = items_cost + items_cost * tax

#display amount owed
print('\nordered items: $', format(items_cost, '.2f'))
print('ordered items: $', format(items_cost * tax, '.2f'))
print('Check: $', format(tab, '.2f'))
