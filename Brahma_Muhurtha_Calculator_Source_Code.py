import datetime
import tkinter as tk

def calculate_brahma_muhurtha(sunrise_time):
    sunrise = datetime.datetime.strptime(sunrise_time, '%H:%M')
    brahma_muhurtha_start = sunrise - datetime.timedelta(hours=1, minutes=36)
    brahma_muhurtha_end = sunrise - datetime.timedelta(minutes=48)
    return brahma_muhurtha_start.strftime('%I:%M %p'), brahma_muhurtha_end.strftime('%I:%M %p')

def calculate_button_clicked():
    sunrise_time = sunrise_entry.get()
    brahma_muhurtha_start, brahma_muhurtha_end = calculate_brahma_muhurtha(sunrise_time)
    result_label.config(text=f"Brahma Muhurtha: {brahma_muhurtha_start} - {brahma_muhurtha_end}")

# create the GUI
root = tk.Tk()
root.title("Brahma Muhurtha Calculator")

# add labels and entry fields
sunrise_label = tk.Label(root, text="Enter Sunrise Time (HH:MM):")
sunrise_label.pack()

sunrise_entry = tk.Entry(root)
sunrise_entry.pack()

result_label = tk.Label(root)
result_label.pack()

# add the calculate button
calculate_button = tk.Button(root, text="Calculate Brahma Muhurtha", command=calculate_button_clicked)
calculate_button.pack()

root.mainloop()
