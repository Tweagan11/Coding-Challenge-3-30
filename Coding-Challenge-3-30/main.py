import tkinter
import customtkinter
from RomanToNumber import roman_to_number
from NumberToRoman import number_to_roman


def helper_roman_to_number():
    var = roman_entry.get()
    result = roman_to_number(var)
    if result == -1:
        roman_final.configure(text="Invalid Roman Numeral", text_color="red")
        return
    if result == -2:
        roman_final.configure(text="Invalid Numeral Syntax", text_color="red")
        return
    roman_final.configure(text=f"Result: {result}", text_color="gray")
    return


def helper_number_to_roman():
    var = number_entry.get()
    result = number_to_roman(var)
    # Invalid input detection
    if result == -1:
        number_final.configure(text="Invalid Number", text_color="red")
        return
    # Too big of a number
    elif result == -2:
        number_final.configure(text="Number too large, limit is 3999.", text_color="gray")
        return
    # Negative Numbers
    elif result == -3:
        result = number_to_roman(abs(float(var)))
        number_final.configure(text=f"Invalid Number (Negative). Result for positive number: {result}", text_color="gray")
        return
    number_final.configure(text=f"Result: {result}", text_color="gray")
    return


# Add interface for user to access calculator
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()

app.geometry('600x400')
app.title('Roman Numeral Converter')

roman_title = customtkinter.CTkLabel(app, text="Roman Numeral to Number")
roman_title.pack(padx=10, pady=10)

# Add Roman -> Number convertor
numeral = tkinter.StringVar()
roman_entry = customtkinter.CTkEntry(app, width=200, height=20, placeholder_text="Enter a Roman Numeral",
                                     textvariable=numeral)
roman_entry.pack(pady=10)

roman_convertor_button = customtkinter.CTkButton(app, text="Convert", width=20, command=helper_roman_to_number)
roman_convertor_button.pack(pady=10)

roman_final = customtkinter.CTkLabel(app, text="")
roman_final.pack(padx=10, pady=10)

# Add Number -> Roman convertor
number_title = customtkinter.CTkLabel(app, text="Number to Roman Numeral")
number_title.pack(pady=10, padx=10)

number = tkinter.DoubleVar()
number_entry = customtkinter.CTkEntry(app, width=200, height=20, placeholder_text="Enter a Roman Numeral",
                                      textvariable=number)
number_entry.pack(pady=10)

number_convertor_button = customtkinter.CTkButton(app, text="Convert", width=20, command=helper_number_to_roman)
number_convertor_button.pack(pady=10)

number_final = customtkinter.CTkLabel(app, text="")
number_final.pack(padx=10, pady=10)

if __name__ == "__main__":
    app.mainloop()
