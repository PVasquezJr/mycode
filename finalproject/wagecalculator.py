from tkinter import *


class welcome_window:
    def __init__(self, master):
        self.master = master
        self.master.geometry('600x300+200+400')
        self.master.title('WELCOME')

        Label(self.master, text='Welcome to the wages calculator GUI')
        btn_wages = Button(self.master, bg="red", text="Wage Calculator", command=self.gotowages)
        btn2 = Button(self.master, text="Unit Converter", command=self.gotoconverter)
        btn_quit = Button(self.master, text="QUIT", command=self.finish)
        entry = Entry(self.master, width=50, bg="white", fg="red")

        btn_wages.grid(row=2, column=2)
        btn2.grid(row=2, column=6)
        btn_quit.grid(row=2, column=4)
        entry.grid(row=5, column=2)

    def gotowages(self):
        root2 = Toplevel(self.master)
        Wages(root2)

    def gotoconverter(self):
        root3 = Toplevel(self.master)
        Converter(root3)

    def finish(self):
        self.master.destroy()


class Wages:

    def __init__(self, master):
        self.nhours = DoubleVar()
        self.salaryh = DoubleVar()
        self.master = master
        self.master.geometry('500x200+100+200')
        self.master.title('Wages Calculator')

        Label(self.master, text='Welcome to the wages calculator GUI',
              fg='red').grid(row=0, column=2)
        Label(self.master, text='Enter your salary per hour').grid(
            row=3, column=0)
        Label(self.master, text='Enter the number of hours worked').grid(
            row=4, column=0)

        Entry(self.master, textvariable=self.salaryh).grid(row=3, column=2)
        Entry(self.master, textvariable=self.nhours).grid(row=4, column=2)
        Button(self.master, text="Calculate Salary",
               command=self.calculatesalary).grid(row=5, column=2)
        Button(self.master, text="Quit",
               command=self.quit).grid(row=6, column=2)

    def calculatesalary(self):
        hours = self.nhours.get()
        print(hours)
        hsal = self.salaryh.get()
        salary = hours * hsal
        print(salary)
        Label(self.master, text="your salary is:%.2f " %
              salary).grid(row=7, column=2)

    def quit(self):
        self.master.destroy()


class Converter:
    def __init__(self, master):
        self.nhours = DoubleVar()
        self.salaryh = DoubleVar()
        self.master = master
        self.master.geometry('500x200+100+200')
        self.master.title('Wages Calculator')

        Label(self.master, text='Welcome to the wages calculator GUI',
              fg='red').grid(row=0, column=2)
        Label(self.master, text='Enter your salary per hour').grid(
            row=3, column=0)
        Label(self.master, text='Enter the number of hours worked').grid(
            row=4, column=0)

        Entry(self.master, textvariable=self.salaryh).grid(row=3, column=2)
        Entry(self.master, textvariable=self.nhours).grid(row=4, column=2)
        Button(self.master, text="Calculate Salary",
               command=self.convert).grid(row=5, column=2)
        Button(self.master, text="Quit",
               command=self.quit).grid(row=6, column=2)

    def convert(self):
        hours = self.nhours.get()
        print(hours)
        hsal = self.salaryh.get()
        salary = hours * hsal
        print(salary)
        Label(self.master, text="your salary is:%.2f " %
              salary).grid(row=7, column=2)

    def quit(self):
        self.master.destroy()


def main():
    root = Tk()
    welcome_window(root)
    root.mainloop()


if __name__ == '__main__':
    main()

