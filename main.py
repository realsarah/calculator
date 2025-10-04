import tkinter as tk
import re
window = tk.Tk()

lbl_number = tk.Label(
    master=window,
    text="",
    width=30,
    height=3,
)
lbl_number.grid(row=0, column=0, columnspan=4)


def btn_one():
    lbl_number["text"] += "1"


btn1 =tk.Button(
    master=window,
    text=1,
    command=btn_one,
    height=3,
)
btn1.grid(row=1, column=0, sticky="ewsn")


def btn_tow():
    lbl_number["text"] += "2"


btn2 = tk.Button(
    master=window,
    text=2,
    command=btn_tow,
    height=3,
)
btn2.grid(row=1, column=1, sticky="ewsn")


def btn_tree():
    lbl_number["text"] += "3"


btn3 = tk.Button(
    master=window,
    text=3,
    command=btn_tree,
    height=3,
)
btn3.grid(row=1, column=2, sticky="ewsn")


def btn_pluss():
    if lbl_number["text"]=="":
        return
    else: 
        lbl_number["text"] += "+"


btn_pluss = tk.Button(
    master=window,
    text="+",
    command=btn_pluss,
    height=3,
)

btn_pluss.grid(row=1, column=3, sticky="ewsn")


def btn_four():
    lbl_number["text"] += "4"


btn4 = tk.Button(
    master=window,
    text=4,
    command=btn_four,
    height=3,
)
btn4.grid(row=2, column=0, sticky="ewsn")


def btn_five():
    lbl_number["text"] += "5"


btn5 = tk.Button(
    master=window,
    text=5,
    command=btn_five,
    height=3,
)
btn5.grid(row=2, column=1, sticky="ewsn")


def btn_six():
    lbl_number["text"] += "6"


btn6 = tk.Button(
    master=window,
    text=6,
    command=btn_six,
    height=3,
)
btn6.grid(row=2, column=2, sticky="ewsn")


def btn_menha():
    if lbl_number["text"]=="":
        return
    else: 
        lbl_number["text"] += "-"


btn_menha = tk.Button(
    master=window,
    text="-",
    command=btn_menha,
    height=3,
)
btn_menha.grid(row=2, column=3, sticky="ewsn")


def btn_seven():
    lbl_number["text"] += "7"


btn7 = tk.Button(
    master=window,
    text=7,
    command=btn_seven,
    height=3,
)
btn7.grid(row=3, column=0, sticky="ewsn")


def btn_eight():
    lbl_number["text"] += "8"


btn8 = tk.Button(
    master=window,
    text=8,
    command=btn_eight,
    height=3,
)
btn8.grid(row=3, column=1, sticky="ewsn")


def btn_nine():
    lbl_number["text"] += "9"


btn9 = tk.Button(
    master=window,
    text=9,
    command=btn_nine,
    height=3,
)
btn9.grid(row=3, column=2, sticky="ewsn")


def btn_zarb():
    if lbl_number["text"]=="":
        return
    else: 
        lbl_number["text"] += "*"


btn_zarb = tk.Button(
    master=window,
    text="*",
    command=btn_zarb,
    height=3,
)
btn_zarb.grid(row=3, column=3, sticky="ewsn")


def btn_ashar(): 
    text= lbl_number["text"]  
    if text =="":
        return
    
    parts = re.split(r"[\+\-\*]", text)
    last_part = parts[-1]

    if "." in last_part :
        return
    else:
        lbl_number["text"] += "."
    


btn_ashar = tk.Button(
    master=window,
    text=".",
    command=btn_ashar,
    height=3,
)
btn_ashar.grid(row=4, column=0, sticky="ewsn")


def btn_zerro():
    lbl_number["text"] += "0"


btn_zerro = tk.Button(
    master=window,
    text=0,
    command=btn_zerro,
    height=3,
)
btn_zerro.grid(row=4, column=1, sticky="ewsn")


def btn_cleaner():
    lbl_number["text"] = ""


btn_cleaner = tk.Button(
    master=window,
    text="c",
    command=btn_cleaner,
    height=3,
)
btn_cleaner.grid(row=4, column=2, sticky="ewsn")


def btn_result():
    lbl_number["text"] = str(eval(lbl_number["text"]))


btn_result = tk.Button(
    master=window,
    text="=",
    command=btn_result,
    height=3,
)
btn_result.grid(row=4, column=3, sticky="ewsn")
window.title("Calculator")
window.mainloop()
