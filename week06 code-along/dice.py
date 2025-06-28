import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    root.option_add("*Font", "Helvetica 12")
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    frm_main.master.title("Dice")
    setup_main(frm_main)
    frm_main.mainloop()


def setup_main(frm):
    lbl_sides =Label(frm,text="Enter the number of sides on the die:")
    lbl_sides.grid(row=0, column=0, padx=5, pady=5)
    ent_sides = IntEntry(frm, width=2, lower_bound=2, upper_bound=20)
    ent_sides.grid(row=0, column=1, padx=5, pady=5)
    lbl_count = Label(frm, text="Enter the number of dice to roll:")
    lbl_count.grid(row=1, column=0, padx=5, pady=5)
    ent_count = IntEntry(frm, width=2, lower_bound=1, upper_bound=10)
    ent_count.grid(row=1, column=1, padx=5, pady=5)
    btn_roll = Button(frm,text="Roll")
    btn_roll.grid(row=2, column=0, columnspan=2, pady=5)
    lbl_roll = Label(frm, text="")
    lbl_roll.grid(row=3, column=0)

    def roll_dice(sides, count):
        sum = 0
        roll_text = ""
        for roll in range(count):
            die_roll = random.randint(1, sides)
            sum += die_roll
            roll_text += f"{die_roll} "
        roll_text += f"Total = {sum}"
        return roll_text


    def roll_action():
        try:
            side = ent_sides.get()
        except ValueError:
            lbl_roll.config(text="Please enter a valid number of sides.")
            return
        try:
            count = ent_count.get()
        except ValueError:
            lbl_roll.config(text="Please enter a valid number of dice.")
            return
        lbltext = roll_dice(side, count)
        lbl_roll.config(text=lbltext)
        lbl_roll.config(text="You rolled the dice")

    
    btn_roll.config(command=roll_action)




if __name__ == "__main__":
    
    main()