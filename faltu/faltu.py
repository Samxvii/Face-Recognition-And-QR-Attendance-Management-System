import csv
import tkinter
root = tkinter.Tk()
root.title("Student Details")
root.configure(background='snow')

cs = "C:/Users/sansk/OneDrive/Desktop/New folder/Attendace_management_system-master/StudentDetails/StudentDetails.csv"
with open(cs, newline="") as file:
    reader = csv.reader(file)
    r = 0

    for col in reader:
        c = 0
        for row in col:
                            # i've added some styling
            label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                bg="snow", text=row, relief=tkinter.RIDGE)
            label.grid(row=r, column=c)
            c += 1
        r += 1
root.mainloop()