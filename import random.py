import random


x = input("Welcome to Mascarpone, your name? ")

tables = ("Table 1", "Table 2", "Table 3", "Table 4", "Table 5")
y = random.choice(list(tables))



menu = {
    "Oyster Aglio Olio": 850,
    "Ragú alla bolegnese": 740,
    "Smoked Beef Carbonara": 730,
    "Pasta Di Gamberi": 630,
    "Pizza(Napoletana, Siciliana, Vitello to natto, tivoli)": 800,
}

descriptions={
  "1": "Oyster Aglio Olio – pasta with garlic, oil, and oysters.",
    "Oyster Aglio Olio": "Oyster Aglio Olio – pasta with garlic, oil, and oysters.",
    "2": "Ragú alla bolegnese – a traditional Italian meat sauce with pasta.",
    "Ragú alla bolegnese": "Ragú alla bolegnese – a traditional Italian meat sauce with pasta.",
    "3": "Smoked Beef Carbonara – creamy pasta with smoked beef.",
    "Smoked Beef Carbonara": "Smoked Beef Carbonara – creamy pasta with smoked beef.",
    "4": "Pasta Di Gamberi – pasta with shrimp in a light sauce.",
    "Pasta Di Gamberi": "Pasta Di Gamberi – pasta with shrimp in a light sauce.",
    "5": "Pizza – choice of Napoletana, Siciliana, Vitello, Tivoli.",
    "Pizza": "Pizza – choice of Napoletana, Siciliana, Vitello, Tivoli.",
}




 "Oyster Aglio Olio": "spaghetti alle vongole, aglio, olio d'oliva, peperoncino",
    "Ragú alla bolegnese": "Beef ragú with pasta.",
    "Smoked beef Carbonara": "spaghetti, smokebeef, egg yolk" ,
    "Pasta Di Gamberi": "pasta, gamberi freschi, salsa cremosa, insalata",
    "Pizza": "Napoletana(salsa di pomodoro, pomodoro fesco e origano, condita con mozzarella.),  Siciliana(pomodoro, mozzarella, formaggi vari, salsicce italiane e piccanti, olive, funghi, peperoni, tonno, basilico fresco), Vittelo to natto(tomat, mozzarella, kogt kalvekod skiver m. tunsauce, kapers), Tivoli(tomat, mozzarella, skinke, pepperoni, marinerede artiskokker) "
Beverages = {
    "Water": 100,
    "Juice": 100,
    "Four loko": 350,
    "Beer": 400,
    "Whisky": 800,
    "Wine": 600,
}

Deserts = {
    "Cartocci": 400,
    "Sfogliatelle": 400,
    "Brownie": 400,
    "Tiramisu": 400,
}



total = 0


if y==tables[1] or y == tables[4] or y == tables[3]:
    print("Your table is", y)
    print("Our Menu:")
    for item, price in menu.items():
            print(f"{item}: ${price:.2f}")
 

    while True:
        try:
            order = (input("Enter the number of your order (0 to finish): "))
            if order == "0":
                break
            elif order.endswith("?"):  # Phase 3: description
                name = order[:-1].strip()
                if name in descriptions:
                    print(descriptions[name])
                else:
                    print("No description available.")
                continue
            order = int(order)
            
    
            match order:
                case 1: total = total + 850
                case 2:total = total + 740
                case 3:total = total + 730
                case 4:total = total + 630
                case 5:total = total + 800
                case 0:break
                case _:
                    print("We dont have that")
                    continue 
        except ValueError:
            print("Please enter a number.") 
    
    for item,price in Beverages.items():
        print(f"{item}: ${price:.2f}")
    while True:
        order = int(input("Enter the number of your Beverage (0 to finish): "))
        try:
            match order: 
                    case 1: total = total + 100
                    case 2:total = total + 100
                    case 3:total = total + 350
                    case 4:total = total + 400
                    case 5:total = total + 800
                    case 6: total= total + 600
                    case 0:break
                    case _:
                        print("We dont have that")
                        continue  
        except ValueError:
            print("Please enter a number.") 
    for item,price in Deserts.items():
        print(f"{item}: ${price:.2f}")
    while True:
        order = int(input("Enter the number of your desert (0 to finish): "))
        try:
            match order: 
                    case 1: total = total + 400
                    case 2:total = total + 400
                    case 3:total = total + 400
                    case 4:total = total + 400
                    case 0:break
                    case _:
                        print("We dont have that")
                        continue  

        except ValueError:
            print("Please enter a number.")
    itbis=(total*0.18)
    itbis_total= itbis+total
    print("Total:", total)

    print(f"Thank you,, {x}")
    print(f"Total:{total}")
    print(f"ITBIS:{itbis}")
    print(f"Final Total:{itbis_total}")
    
    bill=int(input("Card(1) or Cash(2)?:  "))
   
    money=[2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    balance=random.randint(1, 100000)


    if bill==2:
        given=float(input("How much cash?: ")) 
        if given<itbis_total:
            print("Not enough money")
        else:
         change=given-itbis_total
         print(change)
         for billete in money:
             if change//billete:
                print(f"{change//billete}*{billete}")
                change=change%billete
             



    elif bill==1:
        if balance<itbis_total:
            print("Sorry not enough money", x)
        else:
            result=balance-itbis_total
            print("Thanks for coming", result)#Revisar
    
    asktip=input("Want to add a tip?:  ")

    if asktip== "yes":
        tip=input("How much?: ") 
        print("Thanks,", x)
    else:
         print("Thanks,", x)



       
        


         

else:
    print("There are no tables,", x)