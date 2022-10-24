import tkinter as tk
import rsa

# ***** GLOBAL VARIABLES ***** #
objects = []
root = tk.Tk()
UEnt = tk.Entry(root, bd=5)
PEnt = tk.Entry(root, bd=5)
storage = open("vaultFile.txt", "a+")
publicKey, privateKey = rsa.newkeys(512)

# ***** LOOK PREFERENCES ***** #
root.title("LedgerLock V0.0.1")
root.geometry('550x700')
root.config(highlightcolor='green')


# ***** SET UP ***** #
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main()

    def main(self):
        # Title bar at top
        topLabel = tk.Label(self, text="LedgerLock V0.0.1")
        topLabel.grid(row=0, column=0)
        # Instructions

        # Username Label
        userLabel = tk.Label(self, text="Username:")
        userLabel.grid(row=2, column=0, sticky='w')
        # Password Label
        passLabel = tk.Label(self, text="Password:")
        passLabel.grid(row=3, column=0, sticky='w')
        # Username Entry
        UEnt.grid(row=2, column=1)
        # Password Entry
        PEnt.grid(row=3, column=1)
        # Submit Button
        subButton = tk.Button(self, text="Submit", command=submit)
        subButton.grid(row=6, column=1)

        # Quit Button
        quit = tk.Button(self, text="QUIT", background="red", command=self.master.destroy)
        quit.grid(row=7, column=2)
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
    print(pswSave)
    # Inserts Password into storage file
    # storage.write('Password:' + pswSave)
    # Clears the input field
    PEnt.delete(0, 'end')


app = App(master=root)
app.mainloop()
