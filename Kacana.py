
from tkinter import Tk, Entry, Button, Label, StringVar
from tkinter import Toplevel

window = Tk()
window.geometry("800x600")
window.title("My work")

label = Label( text="Please select a language", font=('Times New Roman', 18))
label.pack(padx=20, pady=20)


def open_new_window():
    new_window = Toplevel(window)
    new_window.title("Japanese Window")
    new_window.geometry("300x200")

    entry_text = Entry(new_window)
    entry_text.pack()

    result = StringVar()
    result_label = Label(new_window, textvariable=result)
    result_label.pack()

    japanese_dictionary = {
    "hello": "konnichiwa",
    "thank you": "arigatou",
    "goodbye": "sayounara",
    "good morning": "ohayou",
    "good evening": "konbanwa",
    "excuse me": "sumimasen",
    "yes": "hai",
    "no": "iie",
    "love": "ai",
    "friend": "tomodachi",
    "family": "kazoku",
    "food": "tabemono",
    "drink": "nomimono",
    "school": "gakkou",
    "teacher": "sensei",
    "student": "gakusei",
    "time": "jikan",
    "japan": "nihon",
    "cat": "neko",
    "dog": "inu",
    "lion":'shishido',
    "tiger":'tora'
}

    def search(word):
        if word in japanese_dictionary.keys():
            result.set(japanese_dictionary[word])
            print(japanese_dictionary[word])
        else:
            result.set("Not Found")

    search_btn = Button(new_window, text="Search", font=("Times New Roman", 14), command=lambda: search(entry_text.get()))
    search_btn.pack()








button = Button(window, text="Japanese", width=50, height=2,font=('Times New Roman', 14), command=open_new_window)
button.pack(pady=20)
wuiehwiuevhwvijwhv

button2= Button(window, text="Igala", width=50, height=2,font=('Times New Roman', 14))
button2.pack(pady=20)
button3= Button(window, text="Japanese", width=50, height=2,font=('Times New Roman', 14))
button3.pack(pady=20)
button4= Button(window, text="Igbo", width=50, height=2,font=('Times New Roman', 14))
button4.pack(pady=20)
button5= Button(window, text="Hausa", width=50, height=2,font=('Times New Roman', 14))
button5.pack(pady=20)

window.mainloop()