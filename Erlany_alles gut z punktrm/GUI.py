import tkinter as tk
from Erlang import Algorytm
from main import Model
from wykres import generate_graph

zmienne = []
graph = ""
x = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190]
y = []
inputs = []
x2=None
y2=None

# Funkcja do otwierania nowych okien
def open_instructions_window():
    instructions_window = tk.Toplevel(root)
    instructions_window.title("Instrukcje")
    instructions_window.geometry("700x750")

    # Wczytaj treść z pliku tekstowego
    try:
        with open("instrukcje.txt", "r", encoding="utf-8") as file:
            instrukcje_text = file.read()
    except FileNotFoundError:
        instrukcje_text = "Plik z instrukcjami nie został znaleziony."

    instructions_label = tk.Label(instructions_window, text=instrukcje_text, font=("Helvetica", 12), wraplength=680,
                                  justify="left")
    instructions_label.pack(padx=10, pady=10)

def open_erlang_window():
    erlang_window = tk.Toplevel(root)
    erlang_window.title("Erlang")
    erlang_window.geometry("500x700")

    # Wczytaj treść z pliku tekstowego
    try:
        with open("erlang.txt", "r", encoding="utf-8") as file:
            erlang_text = file.read()
    except FileNotFoundError:
        erlang_text = "Plik z opisem Erlanga nie został znaleziony."
    erlang_label = tk.Label(erlang_window, text=erlang_text, font=("Helvetica", 12), wraplength=480,justify="left")
    erlang_label.pack(padx=10, pady=10)

def open_engset_window():
    engset_window = tk.Toplevel(root)
    engset_window.title("Engset")
    engset_window.geometry("500x700")

    # Wczytaj treść z pliku tekstowego
    try:
        with open("engset.txt", "r", encoding="utf-8") as file:
            engset_text = file.read()
    except FileNotFoundError:
        engset_text = "Plik z opisem Engseta nie został znaleziony."
    engset_label = tk.Label(engset_window, text=engset_text, font=("Helvetica", 12), wraplength=480,justify="left")
    engset_label.pack(padx=10, pady=10)

def open_graph_window():
    print('x', x)
    print('y', y)
    print('in', inputs)
    print('gr', graph)
    print('x2',x2)
    print('y2', y2)
    generate_graph(x, y, inputs, graph,x2,y2)
    '''
    instructions_window = tk.Toplevel(root)
    instructions_window.title("Graph")
    instructions_window.geometry("500x400")
    instructions_label = tk.Label(instructions_window, text="Tutaj będzie wykres.", font=("Helvetica", 12))
    instructions_label.pack(padx=10, pady=10)
    '''

# Funkcja do sprawdzania zawartości pól by jedno zdezaktywować
def check_variable_entries(*args):
    val1 = value_entry1.get()
    val2 = value_entry2.get()
    val3 = value_entry3.get()

    # Sprawdzenie, czy jakiekolwiek pole jest puste, jeśli tak, pokaż wykres i wynik
    if val1 and val2 and not val3:
        value_entry3.config(state="disabled")
        chart_button.config(state="disabled")
    elif val1 and val3 and not val2:
        value_entry2.config(state="disabled")
        chart_button.config(state="normal")
    elif val2 and val3 and not val1:
        value_entry1.config(state="disabled")
        chart_button.config(state="normal")
    else:
        value_entry1.config(state="normal")
        value_entry2.config(state="normal")
        value_entry3.config(state="normal")

def get_variable_entries(*args):
    val1 = value_entry1.get()
    val2 = value_entry2.get()
    val3 = value_entry3.get()
    zmienne = [val1, val2, val3]
    global graph,x2,y2,inputs, y

    if val1 and val2 and not val3:
        try:
            val1 = float(val1)
            val2 = int(val2)
            graph = ""
            chart_button.config(state="disabled")
            model = Model(traffic=val1, lines=val2, blocking_rate=False)
            wynik_label.config(text=Algorytm(model).sprawdzanie())
        except ValueError:
            wynik_label.config(text="Błąd, Podana wartość nie jest liczbą")

    elif val1 and val3 and not val2:
        try:
            val1 = float(val1)
            val3 = float(val3)
            inputs = [val3]
            y.clear()
            graph = "Traffic"
            chart_button.config(state="normal")
            model = Model(traffic=val1, lines=False, blocking_rate=val3)
            wynik_label.config(text=Algorytm(model).sprawdzanie())
            x2 = val1
            y2=Algorytm(model).sprawdzanie()
            for i in range(len(x)):
                model = Model(traffic=x[i], lines=False, blocking_rate=inputs[0])
                y.append(Algorytm(model).sprawdzanie())
        except ValueError:
            wynik_label.config(text="Błąd, Podana wartość nie jest liczbą")

    elif val2 and val3 and not val1:
        try:
            val2 = int(val2)
            val3 = float(val3)
            inputs = [val3]
            y.clear()
            graph = "Lines"
            chart_button.config(state="normal")
            model = Model(traffic=False, lines=val2, blocking_rate=val3)
            wynik_label.config(text=Algorytm(model).sprawdzanie())
            x2 = val2
            y2 = Algorytm(model).sprawdzanie()
            for i in range(len(x)):
                model = Model(traffic=False, lines=x[i], blocking_rate=inputs[0])
                y.append(Algorytm(model).sprawdzanie())
        except ValueError:
            wynik_label.config(text="Błąd, Podana wartość nie jest liczbą")

    return zmienne

# Tworzymy główne okno
root = tk.Tk()
root.title("Erlang Calculator")
root.geometry("600x550")

# Dodajemy tytuł
title_label = tk.Label(root, text="Erlang Calculator", font=("Helvetica", 24))
title_label.pack(pady=20)

# Kontener na przyciski
button_frame = tk.Frame(root)
button_frame.pack()

# Dodajemy przyciski
instructions_button = tk.Button(button_frame, text="Instrukcje", command=open_instructions_window, width=15)
instructions_button.pack(side="left", padx=20, pady=10)

erlang_button = tk.Button(button_frame, text="Erlang", command=open_erlang_window, width=15)
erlang_button.pack(side="left", padx=20, pady=10)

engset_button = tk.Button(button_frame, text="Engset", command=open_engset_window, width=15)
engset_button.pack(side="left", padx=20, pady=10)

# Dodajemy etykietę pod przyciskami
select_label = tk.Label(root, text="Wprowadź wartości", font=("Helvetica", 15))
select_label.pack(pady=10)

# Dodajemy zmienne, zakresy i pola do wprowadzania wartości
variable_frame = tk.Frame(root)
variable_frame.pack()

# Pierwsza zmienna
variable1_label = tk.Label(variable_frame, text="A :", font=("Helvetica", 13), width=10)
variable1_label.grid(row=0, column=0, padx=20, pady=10)

variable11_label = tk.Label(variable_frame, text="0<A<200", font=("Helvetica", 10), width=10)
variable11_label.grid(row=1, column=0, padx=20, pady=10)

value_entry1 = tk.Entry(variable_frame)
value_entry1.grid(row=2, column=0, padx=20, pady=10)
value_entry1.bind("<KeyRelease>", check_variable_entries)

# Druga zmienna
variable2_label = tk.Label(variable_frame, text="N :", font=("Helvetica", 13), width=10)
variable2_label.grid(row=0, column=1, padx=20, pady=10)

variable22_label = tk.Label(variable_frame, text="0<N<200", font=("Helvetica", 10), width=10)
variable22_label.grid(row=1, column=1, padx=20, pady=10)

value_entry2 = tk.Entry(variable_frame)
value_entry2.grid(row=2, column=1, padx=20, pady=10)
value_entry2.bind("<KeyRelease>", check_variable_entries)

# Trzecia zmienna
variable3_label = tk.Label(variable_frame, text="B(A,N) :", font=("Helvetica", 13), width=10)
variable3_label.grid(row=0, column=2, padx=20, pady=10)

variable33_label = tk.Label(variable_frame, text="0<B<1", font=("Helvetica", 10), width=10)
variable33_label.grid(row=1, column=2, padx=20, pady=10)

value_entry3 = tk.Entry(variable_frame)
value_entry3.grid(row=2, column=2, padx=20, pady=10)
value_entry3.bind("<KeyRelease>", check_variable_entries)

# dodajemy miejsce na wynik i wykres, aktywne pod pewnymi warunkami
wynik_labell = tk.Label(root, text="Wynik:", width=15, font=("Helvetica", 15))
wynik_labell.pack(pady=10)

wynik_label = tk.Label(root, text="", width=50, font=("Helvetica", 15))
wynik_label.pack(pady=10)

chart_button = tk.Button(root, text="Pokaż wykres", command=open_graph_window, width=15, state="disabled")
chart_button.pack(pady=10)

wynik_button = tk.Button(root, text="Pokaż wynik", width=15, command = get_variable_entries)
wynik_button.pack(pady=10)
# Uruchamiamy pętlę zdarzeń
root.mainloop()
