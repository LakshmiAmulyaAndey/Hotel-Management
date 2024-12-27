
import creator as cr
import hotel_admin as ha
import delivery_people as dp
import customer as cu

class swiggy:
    def swilog(self):
        while 1:
            print("Welcome To Swiggy's Page\n1. Creator Login\n2. Hotel Admin's Login\n3. Delivery People's Login\n4. Customer's Login\n5. Exit")
            zom = int(input("choose option : "))
            if(zom == 1):
                cr.creator().creator_page()
            elif(zom == 2):
                ha.hotel_admin().hotel_admin_page()
            elif(zom == 3):
                dp.delivery_people().delivery_page()
            elif(zom == 4):
                cu.customer().customer_page()
            elif(zom == 5):
                print("Exit From Swiggy's Page")
                print("-"*20)
                break
            else:
                print("Invalid Option")

z = swiggy()
z.swilog()