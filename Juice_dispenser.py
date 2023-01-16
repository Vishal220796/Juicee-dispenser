from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.title("Encapsulation")
root.geometry("800x600")
root.config(bg="lightblue")
#Heading
label_heading = Label(root, text="Juice Center",bg="lightblue", font=("Sylfaen",18,"bold","italic"))
label_heading.place(relx=0.05,rely=0.1, anchor= W)
#Logo image
juice = ImageTk.PhotoImage(Image.open ("Juice logo.jpg"))
juice_image=Label(root, image=juice, bg="lightblue")
juice_image.place(relx=0.2, rely=0.4,anchor=CENTER)
#Load Images
apple = ImageTk.PhotoImage(Image.open ("apple.jpg"))
mango = ImageTk.PhotoImage(Image.open ("Banana.jpeg"))
orange = ImageTk.PhotoImage(Image.open ("orange.jpg"))
oreomilkshake= ImageTk.PhotoImage(Image.open ("Oreo milkshake.jpg"))
chocolatemilkshake = ImageTk.PhotoImage(Image.open ("chocolate milkshake.jpg"))
strawberrymilkshake = ImageTk.PhotoImage(Image.open ("strawberry milkshake.jpg"))
watermelon = ImageTk.PhotoImage(Image.open ("watermelon.jpg"))
#Fruit Images
fruit_image=Label(root, bg="lightblue")
fruit_image.place(relx=0.8, rely=0.8,anchor=CENTER)
#Label Select Fruit
label_name = Label(root, text="Select fruit ",bg="lightblue", font=("Bahnschrift Light",15))
label_name.place(relx=0.96,rely=0.2, anchor= E)
#Dropdown
fruit_list = ["Apple","Banana","Orange","Watermelon","chocolate milkshake","Oreo milkshake","strawberry milkshake"]
fruit_dropdown = ttk.Combobox(root,state = "readonly", values=fruit_list, justify="right") 
fruit_dropdown.place(relx=0.95, rely=0.25, anchor= E)
#Label Enter Quantity
label_quantity = Label(root, text="Enter Quantity ",bg="lightbluee", font=("Bahnschrift Light",15))
label_quantity.place(relx=0.96,rely=0.35, anchor= E)
#Entry Element
input_quantity = Entry(root)
input_quantity.place(relx=0.95,rely=0.4, anchor= E)
#Total Cost Label
label_show_amount = Label(root ,bg="lightblue", font=("Bahnschrift Light",12))
label_show_amount.place(relx=0.95,rely=0.7, anchor= E)
#Quantity Label
label_show_quantity = Label(root ,bg="lightblue", font=("Bahnschrift Light",12))
label_show_quantity.place(relx=0.95,rely=0.8, anchor= E)
class Juice:
    def __init__(self, fruit_name, quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 250
    def __caculateCost(self):
        total_cost = self.quantity * self.__cost
        label_show_amount['text'] = "You have to pay : "+str(total_cost)+" USD"
        if(self.fruit  == "Apple"):
            calorie = (self.quantity * 52)/100
            fruit_image['image'] = apple
        elif(self.fruit  == "Banana"):
            calorie = (self.quantity * 60)/100
            fruit_image['image'] = Banana
        elif(self.fruit  == "Orange"):
            calorie = (self.quantity * 47)/100
            fruit_image['image'] = orange
        elif(self.fruit  == "chocolate milkshake"):
            calorie = (self.quantity * 80)/100
            fruit_image['image'] = chocolatemilkshake
        elif(self.fruit  == "Oreo milkshake"):
            calorie = (self.quantity * 72)/100
            fruit_image['image'] = oreomilkshake
        elif(self.fruit  == "strawberry milkshake"):
            calorie = (self.quantity * 80)/100
            fruit_image['image'] = strawberrymilkshake

        label_show_quantity['text'] = "x"+str(self.quantity)+" = "+str(calorie)

    def getCost(self):
        self.__caculateCost()
def orderJuice():
    fruit = fruit_dropdown.get()
    quantity = input_quantity.get()
    obj1 = Juice(fruit,quantity)
    obj1.getCost()
btn = Button(root, text="TOTAL", bg="red3", fg="white", padx=10, pady=1,  font=("Arial",11, "bold"), relief=FLAT, command=orderJuice)
btn.place(relx=0.95,rely=0.5, anchor= E)
root.mainloop()