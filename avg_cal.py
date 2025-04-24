import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
label = tk.Label(window, text="Average Marks Calculator")
label.pack()

label = tk.Label(window, text="Mid 1 Marks")
label.pack()
entry_box1 = tk.Entry(window, width=30)  
entry_box1.pack(pady=10) 

label = tk.Label(window, text="Mid 2 Marks")
label.pack()
entry_box2 = tk.Entry(window, width=30)  
entry_box2.pack(pady=10) 

label = tk.Label(window, text="assignment Marks")
label.pack()
entry_box3 = tk.Entry(window, width=30)  
entry_box3.pack(pady=10) 

def get_texts():
    text1 = entry_box1.get()
    text2 = entry_box2.get()
    text3 = entry_box3.get()
    # print("Entered text a:", text1)
    # print("Entered text b:", text2)
    avg(text1, text2 , text3)

get_button = tk.Button(window, text="Get Text", command=get_texts)
get_button.pack()

def avg(text1, text2, text3):
    try:
        a = int(text1)
        b = int(text2)
        c = int(text3)
        average = ((a + b) / 2) + c
        print("Average Marks:", average )
        display_result(average)
    except ValueError:
        print("Please enter valid numbers.")


output_text = tk.Text(window)
output_text.pack()

def display_result(average):
   output_text.insert(tk.END," average manrks is : " + str(average) + "\n")


window.mainloop()
