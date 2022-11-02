import os
import tkinter as tk
import rsa
import hashlib

# ***** GLOBAL VARIABLES ***** #
objects = []
root = tk.Tk()
# Gruv Scheme
bg0 = '#665c54'
bg2 = '#504945'
red = '#fb4934'
green = '#98971a'
yellow = '#fabd2f'
fg4 = '#a89984'
fg3 = '#bdae98'
# Visual Elements
LEnt = tk.Entry(root, width=20, bg=bg2, fg=fg3, highlightbackground=bg2, highlightcolor=fg3)
UEnt = tk.Entry(root, width=20, bg=bg2, fg=fg3, highlightbackground=bg2, highlightcolor=fg3)
PEnt = tk.Entry(root, show='*', width=20, bg=bg2, fg=fg3, highlightbackground=bg2, highlightcolor=fg3)
labelLabel = tk.Label(root, text="Label:", bg=bg0, fg=fg3)
userLabel = tk.Label(root, text="Username:", bg=bg0, fg=fg3)
topLabel = tk.Label(root, text="LedgerLock V0.0.1", bg=bg0, fg=green)
passLabel = tk.Label(root, text="Password:", bg=bg0, fg=fg3)
quit = tk.Button(root, text="QUIT", background=bg0, fg=red, highlightbackground='black', highlightcolor='black', activebackground=bg2, activeforeground=red)
subButton = tk.Button(root, text="Submit", bg=bg0, fg=green, highlightbackground='black', highlightcolor='black', activebackground=bg2, activeforeground=green)
# encryption/storage back end bits
storage = open("vaultFile.txt", "a+")
publicKey, privateKey = rsa.newkeys(256)

# ***** LOOK PREFERENCES ***** #
root.title("LedgerLock V0.0.1")
root.geometry('550x700')
root.config(highlightcolor='green')
root.configure(bg=bg0)


# ***** SET UP ***** #
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main()

    def main(self):
        # Title bar at top
        topLabel.grid(row=1, column=1)
        # Instructions

        # Label Label...
        labelLabel.grid(row=2, column=1, sticky='W')
        # Label Entry
        LEnt.grid(row=2, column=2, sticky='E')
        # Username Label
        userLabel.grid(row=3, column=1, sticky='W')
        # Password Label
        passLabel.grid(row=4, column=1, sticky='W')
        # Username Entry
        UEnt.grid(row=3, column=2, sticky='E')
        # Password Entry
        PEnt.grid(row=4, column=2, sticky='E')
        # Submit Button
        subButton.configure(command=submit)
        subButton.grid(row=6, column=2, sticky='E')
        # Quit Button
        quit.configure(command=self.master.destroy)
        quit.grid(row=6, column=1, sticky="W")

        self.grid()


# ***** FUNCTIONS ***** #
def submit():
    # Pull Info from entry fields
    logUandL(UEnt.get(), LEnt.get())
    logP(PEnt.get())


# Todo: Overload this to encrypt the same way with an extra input
def logUandL(UserIn, LabelIn):
    # log Label
    print(LabelIn)
    # storage.write('\n' + 'Label:' + LabelIn)
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
    salt = os.urandom(32)
    digest = hashlib.pbkdf2_hmac('sha256', pswSave, salt, 10000)
    print(digest)
    # Inserts Password into storage file
    # storage.write('Password:' + digest)
    # Clears the input field
    PEnt.delete(0, 'end')


app = App(master=root)
app.mainloop()
