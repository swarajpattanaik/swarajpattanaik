import webbrowser
import re
import sys
import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from pathlib import Path
from tkinter import messagebox

ASSETS_PATH = Path(__file__).resolve().parent / "assets"
print(ASSETS_PATH)

path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

output_path = ""


def btn_clicked():
    user_1 = user_entry.get()
    pass_1= pass_entry.get()
    #ogin_1 = login_entry.get()
    
#ERROR TEXT SETUP
    if not user_1:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter user name.")
        return
    if not pass_1:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Password.")
        return
  
def make_label(master, x, y, h, w, *args, **kwargs):
    f = tk.Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)

    label = tk.Label(f, *args, **kwargs)
    label.pack(fill=tk.BOTH, expand=1)
    return label

# create window geometry
window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "truck.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Tkinter Designer")
window.geometry("1920x1080")

#background image setup
canvas = tk.Canvas(
    window, bg="#ffffff", height=1080, width=1920,
    bd=0, highlightthickness=0, relief="flat")
canvas.place(x=0, y=0)
text_box_bg = tk.PhotoImage(file=ASSETS_PATH / "login-bg.png")
bg_entry_img = canvas.create_image(960,500, image=text_box_bg)

#truck png setup
truck_png = tk.PhotoImage(file=ASSETS_PATH / "truck.png")
bg_entry_img2 = canvas.create_image(219,134, image=truck_png)

#user test png
user_png = tk.PhotoImage(file=ASSETS_PATH / "USER.png")
bg_entry_img3 = canvas.create_image(120,350, image=user_png)
#test box for user
text_png1 = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
bg_entry_img4 = canvas.create_image(219,400, image=text_png1)

#password text
pass_png = tk.PhotoImage(file=ASSETS_PATH / "PASSWORD.png")
bg_entry_img5 = canvas.create_image(170,500, image=pass_png)
#test box for password
text_png2 = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg1.png")
bg_entry_img6 = canvas.create_image(219,550, image=text_png2)

#user entry setup
user_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
user_entry.place(x=60, y=380, width=250, height=45)
user_entry.focus()

#password entry setup
pass_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
pass_entry.place(x=60, y=520, width=250, height=45)
pass_entry.focus()

#login button setup

login_btn_img = tk.PhotoImage(file=ASSETS_PATH / "LOGIN.png")
login_btn = tk.Button(
    image=login_btn_img, borderwidth=0, highlightthickness=0,
    command=btn_clicked, relief="flat")
login_btn.place(x=120, y=650, width=180, height=55)


#window.resizable(False, False)
window.mainloop()


   