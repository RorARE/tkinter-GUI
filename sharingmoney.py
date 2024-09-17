import tkinter
from tkinter import *
from tkinter import ttk
#Global variables
n=0
b=0
class Feedback:
    def __init__(self, master):
        master.configure(background='#e1d8b9')
        #Frame 1 ...............................................................
        self.thisdict={}
        self.mylist=[]
        self.newlist=[]
        self.my_list=[]
        self.frame_1 = ttk.Frame(master)
        self.frame_1.grid(row=0, column=0)
        ttk.Label(self.frame_1, text='Friends list').grid(row=0, column=0)
        self.entry_name=ttk.Entry(self.frame_1)
        self.entry_name.grid(row=1,column=0)
        ttk.Button(self.frame_1, text='add friend', command=self.add).grid(row=2,column=0)
        self.listbox=Listbox(self.frame_1,height=10,width=5)
        self.listbox.grid(row=3,column=0)
        ttk.Button(self.frame_1, text='remove friend', command=self.remove).grid(row=2,column=1)
        #Frame 2 ...............................................................
        self.frame_2 = ttk.Frame(master)
        self.frame_2.grid(row=1, column=0)
        self.entry_cost=ttk.Entry(self.frame_2)
        self.entry_cost.grid(row=1,column=0)
        self.costs=StringVar()
        self.combobox=ttk.Combobox(self.frame_2,textvariable=self.costs)
        self.combobox.grid(row=2,column=0)
        self.combobox.bind("<<ComboboxSelected>>", self.option_selected)
        ttk.Button(self.frame_2, text='add costs', command=self.add_costs).grid(row=1,column=1)
        ttk.Button(self.frame_2, text='remove costs', command=self.remove_costs).grid(row=1,column=2)
        self.price=StringVar()
        self.spinbox=ttk.Spinbox(self.frame_2, from_=0, to=100,textvariable=self.price)
        self.spinbox.grid(row=2,column=1)
        ttk.Button(self.frame_2, text='set costs', command=self.set_costs).grid(row=3,column=2)
        #Frame 3................................................................
        self.frame_3 = ttk.Frame(master)
        self.frame_3.grid(row=2, column=0)
        self.name_price=StringVar()
        self.combobox1=ttk.Combobox(self.frame_3,textvariable=self.name_price)
        self.combobox1.grid(row=0,column=0)
        self.combobox1.bind("<<ComboboxSelected>>", self.options_selected)
        ttk.Button(self.frame_3, text='paid', command=self.paid).grid(row=2,column=1)
        ttk.Button(self.frame_3, text='show', command=self.show).grid(row=1,column=1)
    #Functions of frame 3.......................................................
    def show(self):
        self.newlist=[]
        total_costs = sum(self.thisdict.values())
        div = len(self.mylist) if self.mylist else 1
        portion = total_costs / div
        self.newlist = [f"{item} {portion} 'unpaid'" for item in self.mylist]
        print(self.newlist)
        self.combobox1.config(values=self.newlist)

    def options_selected(self,event):
        self.item_3=self.combobox1.get()
        return self.item_3
    def paid(self):
        k=0
        for item in self.newlist:
            if item==self.item_3:
                break
            k=k+1
        paid_one=self.newlist[k]
        new_item=paid_one[0:-7]
        self.newlist.remove(paid_one)
        self.newlist.append(new_item)
        self.combobox1.set('')
        self.combobox1.config(values=self.newlist)


    #Functions of Frame 2 ......................................................
    def add_costs(self):
        global b
        new_item = self.entry_cost.get()
        if new_item!='':
            self.my_list.append(new_item)
            self.combobox.config(values=self.my_list)
        self.entry_cost.delete(0,'end')
        return self.my_list
    def option_selected(self,event):
        self.item_2=self.combobox.get()
        return self.item_2
    def remove_costs(self):
        self.my_list.remove(self.item_2)
        self.combobox.config(values=self.my_list)
        self.combobox.set('')
        return self.my_list
    def set_costs(self):
        price_1=self.spinbox.get()
        price_1=int(price_1)
        self.thisdict.update({self.item_2:price_1})
        print(self.thisdict)
        self.combobox.set('')
        self.spinbox.set(0)
        return self.thisdict
    #Functions of Frame 1 ......................................................
    def remove(self):
        for i in self.listbox.curselection():
            item_4=self.listbox.get(i)
            self.mylist.remove(item_4)
            print(i)
            self.listbox.delete(i)
        return self.mylist
    def clear(self):
        self.entry_name.delete(0,'end')
    def add(self):
        global n
        name = self.entry_name.get()
        if name!='':
            n=n+1
            self.mylist.append(name)
            self.clear()
            self.listbox.insert(n,name)
        #print(self.mylist)
        return self.mylist
def main():

    root = tkinter.Tk()
    root.geometry('800x800')
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__":
    main()
