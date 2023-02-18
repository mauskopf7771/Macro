import tkinter as tk
from tkinter import IntVar

# Things to add: 
# Saves client previous data so it loads everything up from the point it was closed
# clear button which clears all fields
# convert between different metric systems

# PAL adjusts for levels of activity
# Sedetary = 1.1-1.39 - Spend all day sitting
# Low physical activity = 1.40 - 1.59 - Office worker, does some walking
# Active = 1.60 - 1.89 - Traiing 1 hour a day or active person who walks 6-8 miles a day
# Very Active = 1.90 - 2.50 - Several hours of vigarous activity per day

########################################################################################################

##### Create the window
win = tk.Tk()
win.title('Macro')
win.resizable(height = None, width = None)
win.geometry('1000x800')

# Exit Button
exit = tk.Button(win, text = 'Exit', width = 25, command = win.destroy)
exit.place(relwidth = 0.2, relheight = 0.1, relx = 0, rely = 0.9)

#Get Gender values
def get_gender():
    print(gender.get())

# Male/Female boxes
gender = tk.StringVar()
mfb1 = tk.Radiobutton(win, text = 'Male', variable = gender, value = 5, command = get_gender)
mfb2 = tk.Radiobutton(win, text = 'Female', variable = gender, value = -161, command = get_gender)
genderLabel = tk.Label(win, text = 'Are you male or female?')
genderLabel.place(relx = 0.0, rely = 0.46)
mfb1.place(relwidth = 0.1, relheight = 0.05, relx = 0.3, rely = 0.45)
mfb2.place(relwidth = 0.1, relheight = 0.05, relx = 0.3, rely = 0.5)

# Weight Height Age Inputs
askweight = tk.Label(win, text = 'Please input your weight (kg)')
askweight.place(relx = 0, rely = 0.4)
weight = tk.Entry(win)
weight.place(relx = 0.3, rely = 0.4)

askheight = tk.Label(win, text = 'Please input your height (cm)')
askheight.place(relx = 0.0, rely = 0.35)
height = tk.Entry(win)
height.place(relx = 0.3, rely = 0.35)

askage = tk.Label(win, text = 'How old are you?')
askage.place(relx = 0.0, rely = 0.3)
age = tk.Entry(win)
age.place(relx = 0.3, rely = 0.3)


# Calculate button
def calculate_mifflin():
    miffmiff = int(round(((((10*float(weight.get())) + (6.25 * float(height.get())) - (5-float(age.get())) + 5)) + float(gender.get())) * float(PAL.get()), 0))
    # Calculate Macros
    protein = int(round(((float(weight.get())*2.2)*0.8), 0))
    fat = int(round(((float(weight.get()) *2.2)*0.35), 0))
    proteincals = protein * 4
    fatcals = fat * 9
    calPF = proteincals + fatcals
    carbs = int(round(((miffmiff - calPF)/4), 0))

    mifflin.configure(text = 'Your BMR is: ' + str(miffmiff) + ' Calories \n Protein: ' + str(protein) + 'g \n Fat: ' + str(fat) + 'g \n Carbs: ' + str(carbs) + 'g')


# Button to do calculation
calcButton = tk.Button(win, text = 'Calculate', command = calculate_mifflin)
calcButton.place(relx = 0.05, rely = 0.6)

# Display calculation output
mifflin = tk.Label(win)
mifflin.place(relx = 0.5, rely = 0.8)

# Get PAL Information
def get_PAL():
    print(PAL.get())

#PAL RadioButtons
PAL = tk.StringVar()
pal_sed_btn = tk.Radiobutton(win, text = 'Seditary', variable = PAL, value = 1.1, command = get_PAL)
pal_sed_btn.place(relx = 0.5, rely = 0.5,)
pal_low = tk.Radiobutton(win, text = 'Low', variable = PAL, value = 1.40, command = get_PAL)
pal_low.place(relx = 0.5, rely = 0.55)
pal_active = tk.Radiobutton(win, text = 'Active', variable = PAL, value = 1.60, command = get_PAL)
pal_active.place(relx = 0.5, rely = 0.6)
pal_very = tk.Radiobutton(win, text = 'Very Active', variable = PAL, value = 1.90, command = get_PAL)
pal_very.place(relx = 0.5, rely = 0.65) 


win.mainloop()
