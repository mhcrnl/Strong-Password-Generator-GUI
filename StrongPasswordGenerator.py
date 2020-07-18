import secrets
import tkinter as tk


root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("500x300")

length_list = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,32,33,34,35,36,37,38,39,40]


check1_var = tk.IntVar()
check2_var = tk.IntVar()
check3_var = tk.IntVar()
check4_var = tk.IntVar()

dropvar = tk.IntVar()
dropvar.set(length_list[0]) #Default value

drop_text = tk.Text(root, height = 1, width = 20)
drop_text.insert(tk.INSERT, "Password Length")
drop_text["state"] = tk.DISABLED

password_text = tk.Text(root, height = 1, width = 20)
password_text.insert(tk.INSERT, "Your Password is:")
password_text["state"] = tk.DISABLED

check1_text = tk.Text(root, height = 1, width = 26)
check1_text.insert(tk.INSERT, "Include Uppercase Letters")
check1_text["state"] = tk.DISABLED
check1 = tk.Checkbutton(root, text="eg. = ABCD", variable = check1_var, onvalue = 1, offvalue = 0)

check2_text = tk.Text(root, height = 1, width = 26)
check2_text.insert(tk.INSERT, "Include Lowercase Letters")
check2_text["state"] = tk.DISABLED
check2 = tk.Checkbutton(root, text="eg. = adbc", variable = check2_var, onvalue = 1, offvalue = 0)

check3_text = tk.Text(root, height = 1, width = 26)
check3_text.insert(tk.INSERT, "Include Numbers")
check3_text["state"] = tk.DISABLED
check3 = tk.Checkbutton(root, text="eg. = 1234", variable = check3_var, onvalue = 1, offvalue = 0)

check4_text = tk.Text(root, height = 1, width = 26)
check4_text.insert(tk.INSERT, "Include Symbols")
check4_text["state"] = tk.DISABLED
check4 = tk.Checkbutton(root, text="eg. = !@#$ ", variable = check4_var, onvalue = 1, offvalue = 0)

drop = tk.OptionMenu(root, dropvar, *length_list)

e = tk.Entry(root, width = 40, borderwidth = 5)

#Grid
drop_text.grid(row = 3, column = 2)
password_text.grid(row = 9, column = 2)
check1_text.grid(row = 4, column = 2)
check1.grid(row = 4, column = 3)
check2_text.grid(row = 5, column = 2)
check2.grid(row = 5, column = 3)
check3_text.grid(row = 6, column = 2)
check3.grid(row = 6, column = 3)
check4_text.grid(row = 7, column = 2)
check4.grid(row = 7, column = 3)
drop.grid(row = 3, column = 3)

e.grid(row = 9, column = 3)

password_length = dropvar.get() 

def print_password(checkvar1, checkvar2, checkvar3, checkvar4, dropvar):
    uppercase_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","S","R","T","U","V","X","Y","Z"]
    numbers_list =   ["0","1","2","3","4","5","6","7","8","9"]
    lowercase_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","s","r","t","u","v","x","y","z"]
    symbols_list =   ["!","@","#","$","%","&","/","(",")","=","?","¡","¿","-","_","*","+"]
    
    complete_list = uppercase_list + numbers_list + lowercase_list + symbols_list

    rand_upper = secrets.choice(uppercase_list)
    rand_number = secrets.choice(numbers_list)
    rand_lower = secrets.choice(lowercase_list)
    rand_symbols = secrets.choice(symbols_list)

    pass_length = dropvar.get()
    random_password = ""
    character = ""


    # Nothing selected
    if checkvar1 == 0 and checkvar2 == 0 and checkvar3 == 0 and checkvar4 == 0:
        e.delete(0, tk.END)
        e.insert(0, "You must select at least one character set!")
    # All selected
    elif checkvar1 == 1 and checkvar2 == 1 and checkvar3 == 1 and checkvar4 == 1:
        temp_pass = rand_upper + rand_number + rand_lower + rand_symbols
        for i in range(pass_length - 4):
            character = secrets.choice(complete_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    # 2 Options selected
    elif checkvar1 == 1 and checkvar2 == 1 and checkvar3 == 0 and checkvar4 == 0:
        temp_pass = rand_upper + rand_lower
        temp_list = uppercase_list + lowercase_list
        for i in range(pass_length - 2):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 1 and checkvar2 == 0 and checkvar3 == 1 and checkvar4 == 0:
        temp_pass = rand_upper + rand_number
        temp_list = uppercase_list + numbers_list
        for i in range(pass_length - 2):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 1 and checkvar2 == 0 and checkvar3 == 0 and checkvar4 == 1:
        temp_pass = rand_upper + rand_symbols
        temp_list = uppercase_list + symbols_list
        for i in range(pass_length - 2):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 0 and checkvar2 == 1 and checkvar3 == 0 and checkvar4 == 1:
        temp_pass = rand_lower + rand_symbols
        temp_list = lowercase_list + symbols_list
        for i in range(pass_length - 2):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 0 and checkvar2 == 1 and checkvar3 == 1 and checkvar4 == 0:
        temp_pass = rand_lower + rand_number
        temp_list = lowercase_list + numbers_list
        for i in range(pass_length - 2):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 0 and checkvar2 == 0 and checkvar3 == 1 and checkvar4 == 1:
        temp_pass = rand_number + rand_symbols
        temp_list = numbers_list + symbols_list
        for i in range(pass_length - 2):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    # 3 options
    elif checkvar1 == 1 and checkvar2 == 1 and checkvar3 == 1 and checkvar4 == 0:
        temp_pass = rand_upper + rand_lower + rand_number
        temp_list = uppercase_list + lowercase_list + numbers_list 
        for i in range(pass_length - 3):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 0 and checkvar2 == 1 and checkvar3 == 1 and checkvar4 == 1:
        temp_pass = rand_lower + rand_number + rand_symbols
        temp_list = lowercase_list + numbers_list + symbols_list
        for i in range(pass_length - 3):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 1 and checkvar2 == 0 and checkvar3 == 1 and checkvar4 == 1:
        temp_pass = rand_upper + rand_number + rand_symbols
        temp_list = uppercase_list + numbers_list + symbols_list
        for i in range(pass_length - 3):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    elif checkvar1 == 0 and checkvar2 == 1 and checkvar3 == 1 and checkvar4 == 1:
        temp_pass = rand_lower + rand_number + rand_symbols
        temp_list = lowercase_list + numbers_list + symbols_list
        for i in range(pass_length - 3):
            character = secrets.choice(temp_list)
            temp_pass += character
        e.delete(0, tk.END)
        e.insert(0, temp_pass)
    # One choice only
    else:
        if  checkvar1 == 1 and checkvar2 == 0 and checkvar3 == 0 and checkvar4 == 0:
            for i in range(pass_length):
                character = secrets.choice(uppercase_list)
                random_password += character
        elif checkvar1 == 0 and checkvar2 == 1 and checkvar3 == 0 and checkvar4 == 0:
            for i in range(pass_length):
                character = secrets.choice(lowercase_list)
                random_password += character
        elif checkvar1 == 0 and checkvar2 == 0 and checkvar3 == 1 and checkvar4 == 0:
            for i in range(pass_length):
                character = secrets.choice(numbers_list)
                random_password += character
        elif checkvar1 == 0 and checkvar2 == 0 and checkvar3 == 0 and checkvar4 == 1:
            for i in range(pass_length):
                character = secrets.choice(symbols_list)
                random_password += character
        e.delete(0, tk.END)
        e.insert(0, random_password)



button_generate = tk.Button(root, text="Generate Password",padx=40, pady=15, command= lambda: print_password(check1_var.get(), check2_var.get(), check3_var.get(), check4_var.get(), dropvar)).grid(row=8, column=3)


root.mainloop()