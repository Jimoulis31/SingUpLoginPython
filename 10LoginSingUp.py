from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Sing Up by Mitsos")
window.geometry("600x300")
window.configure(bg="#1e1e1e")
window.resizable(False, False)

loginwindow = Toplevel(window)
loginwindow.title("Login by Mitsos")
loginwindow.geometry("600x300")
loginwindow.configure(bg="#1e1e1e")
loginwindow.withdraw()

Label(window, text='Sign Up', font=('Arial', 24, 'bold'), bg="#1e1e1e", fg="#ffffff").grid(row=0, column=1, columnspan=2, pady=10)

Label(window, text='Username:', font=('Arial', 16), bg="#1e1e1e", fg="#ffffff").grid(row=1, column=0, sticky=E, padx=10, pady=5)
userlogtxt = Entry(window, font=('Arial', 16), width=30)
userlogtxt.grid(row=1, column=1, padx=10, pady=5)

Label(window, text='Password:', font=('Arial', 16), bg="#1e1e1e", fg="#ffffff").grid(row=2, column=0, sticky=E, padx=10, pady=5)
passlogtxt = Entry(window, font=('Arial', 16), show="*", width=30)
passlogtxt.grid(row=2, column=1, padx=10, pady=5)

Label(window, text='Email:', font=('Arial', 16), bg="#1e1e1e", fg="#ffffff").grid(row=3, column=0, sticky=E, padx=10, pady=5)
emaillogtxt = Entry(window, font=('Arial', 16), width=30)
emaillogtxt.grid(row=3, column=1, padx=10, pady=5)

saved_email = None
saved_pass = None
saved_user = None

def passwordcheck(password):
    min_len = 8
    special_chars = set('!@#$%^&*()-_=+[]{};:,.<>?/\\|`~"\'')
    if not password:
        return False, "Password is empty."
    if len(password) < min_len:
        return False, f"Password must be at least {min_len} characters."
    upper = lower = number = special = False
    for w in password:
        if w.isupper(): upper = True
        elif w.islower(): lower = True
        elif w.isdigit(): number = True
        elif w in special_chars: special = True
    missing = []
    if not upper: missing.append("an uppercase letter")
    if not lower: missing.append("a lowercase letter")
    if not number: missing.append("a number")
    if not special: missing.append("a special character (e.g. !,@,#,$,%)")
    if missing: return False, "Password must contain " + ", ".join(missing) + "."
    return True, ""

def signup():
    global saved_email, saved_pass, saved_user
    username = userlogtxt.get().strip()
    password = passlogtxt.get()
    email = emaillogtxt.get().strip()
    if not (username and password and email):
        messagebox.showerror("Error", "Please fill all fields")
        return
    ok, reason = passwordcheck(password)
    if not ok:
        messagebox.showerror("Weak Password", reason)
        return
    saved_user, saved_email, saved_pass = username, email, password
    messagebox.showinfo("Success", "Account created successfully!")
    window.withdraw()
    loginwindow.deiconify()

Button(window, text="Sign Up", font=("Arial", 16, "bold"), bg="#ff6666", fg="#000", width=20, command=signup).grid(row=4, column=1, columnspan=2, pady=20)

Label(loginwindow, text='Login', font=('Arial', 24, 'bold'), bg="#1e1e1e", fg="#ffffff").grid(row=0, column=1, columnspan=2, pady=10)

Label(loginwindow, text='Email:', font=('Arial', 16), bg="#1e1e1e", fg="#ffffff").grid(row=1, column=0, sticky=E, padx=10, pady=5)
emaillogtxt2 = Entry(loginwindow, font=('Arial', 16), width=30)
emaillogtxt2.grid(row=1, column=1, padx=10, pady=5)

Label(loginwindow, text='Password:', font=('Arial', 16), bg="#1e1e1e", fg="#ffffff").grid(row=2, column=0, sticky=E, padx=10, pady=5)
passlogtxt2 = Entry(loginwindow, font=('Arial', 16), show="*", width=30)
passlogtxt2.grid(row=2, column=1, padx=10, pady=5)

signup_tag = Label(
    window,
    text="Made by Mitsos",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="#ff9999"
)

signup_tag.place(relx=0.0, rely=1.0, anchor="sw", x=15, y=-15)


login_tag = Label(
    loginwindow,
    text="Made by Mitsos",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="#ff9999"
)

login_tag.place(relx=1.0, rely=1.0, anchor="se", x=-15, y=-15)



def loginin():
    email = emaillogtxt2.get().strip()
    password = passlogtxt2.get()
    if saved_email is None:
        messagebox.showerror("Login Error", "No account created yet.")
        loginwindow.withdraw()
        window.deiconify()
        return
    if email == saved_email and password == saved_pass:
        messagebox.showinfo("Welcome", f"Welcome {saved_user}!")
        loginwindow.destroy()
        window.destroy()
    else:
        messagebox.showerror("Login Error", "Wrong email or password!")

Button(loginwindow, text="Login", font=("Arial", 16, "bold"), bg="#66ff66", fg="#000", width=20, command=loginin).grid(row=3, column=1, columnspan=2, pady=15)
Button(loginwindow, text="Back", font=("Arial", 12), bg="#cccccc", width=10, command=lambda: [loginwindow.withdraw(), window.deiconify()]).grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
