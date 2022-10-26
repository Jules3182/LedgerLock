import tkinter as tk
import rsa
import random
import string

# ***** GLOBAL VARIABLES ***** #
objects = []
root = tk.Tk()
UEnt = tk.Entry(root, width=20, bg='black', fg='green', highlightbackground='green', highlightcolor='lightgreen')
PEnt = tk.Entry(root, show='*', width=20, bg='black', fg='green', highlightbackground='green', highlightcolor='lightgreen')
userLabel = tk.Label(root, text="Username:", bg='black', fg='green')
topLabel = tk.Label(root, text="LedgerLock V0.0.1", bg='black', fg='lightgreen')
passLabel = tk.Label(root, text="Password:", bg='black', fg='green')
quit = tk.Button(root, text="QUIT", background="black", fg='red', highlightbackground='black',highlightcolor='black')
subButton = tk.Button(root, text="Submit", bg='black', fg='lightgreen', highlightbackground='black',highlightcolor='black')

storage = open("vaultFile.txt", "a+")
publicKey, privateKey = rsa.newkeys(512)

# ***** LOOK PREFERENCES ***** #
root.title("LedgerLock V0.0.1")
root.geometry('550x700')
root.config(highlightcolor='green')
root.configure(bg='black')


# ***** SET UP ***** #
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main()

    def main(self):
        # Title bar at top
        topLabel.grid(row=1, column=1)
        # Instructions

        # Username Label
        userLabel.grid(row=2, column=1, sticky='W')
        # Password Label
        passLabel.grid(row=3, column=1, sticky='W')
        # Username Entry
        UEnt.grid(row=2, column=2, sticky='E')
        # Password Entry
        PEnt.grid(row=3, column=2, sticky='E')
        # Submit Button
        subButton.command = submit
        subButton.grid(row=6, column=2, sticky='E')
        # Quit Button
        quit.command = self.master.destroy
        quit.grid(row=6, column=1, sticky="W")

        self.grid()


# ***** FUNCTIONS ***** #
def submit():
    # Pull Info from entry fields
    logU(UEnt.get())
    logP(PEnt.get())


# Todo: Overload this to encrypt the same way with an extra input
def logU(UserIn):
    # Logs Username
    print(UserIn)
    # Encrypts username
    usrSave = rsa.encrypt(UserIn.encode(), publicKey)
    print(usrSave)
    # Inserts Password into storage file
    # storage.write('\n' + 'Username:' + usrSave)
    # Clears the input field
    UEnt.delete(0, 'end')


def logP(PassIn):
    # Encrypts password then logs it
    print(PassIn)
    # Encrypts Password
    pswSave = rsa.encrypt(PassIn.encode(), publicKey)
    # Gotta Salt It
    # letters = string.ascii_letters
    pswSave.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(10))
    print(pswSave)
    # Inserts Password into storage file
    # storage.write('Password:' + pswSave)
    # Clears the input field
    PEnt.delete(0, 'end')


app = App(master=root)
app.mainloop()
