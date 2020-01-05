import tkinter as tk

class FloatEntry(tk.Entry):
    def get(self):
        return float(super().get())

def fun():
    d = dystans_entry.get()
    s = float(spalanie_entry.get())
    c = float(cena_entry.get())
    wynik = d / 100 * s * c
    wynik_label.configure(text=f"Cena za przejazd: {wynik:.2f} PLN")

root = tk.Tk()
root.columnconfigure(1, weight=1)

dystans_label = tk.Label(master=root, text="Podaj dystans: ")
dystans_label.grid(row=0, column=0, sticky=tk.W)
dystans_entry = FloatEntry(master=root)
dystans_entry.grid(row=0, column=1, sticky=tk.EW)

spalanie_label = tk.Label(master=root, text="Podaj spalanie: ")
spalanie_label.grid(row=1, column=0, sticky=tk.W)
spalanie_entry = tk.Entry(master=root)
spalanie_entry.grid(row=1, column=1, sticky=tk.EW)

cena_label = tk.Label(master=root, text="Podaj cenę za litr paliwa: ")
cena_label.grid(row=2, column=0, sticky=tk.W)
cena_entry = tk.Entry(master=root)
cena_entry.grid(row=2, column=1, sticky=tk.EW)

wynik_label = tk.Label(master=root, text="")
wynik_label.grid(row=3, column=0, sticky=tk.W)
przycisk = tk.Button(master=root, text="Oblicz", command=fun)
przycisk.grid(row=3, column=1, sticky=tk.EW)


root.title("Moje pierwsze okienko")
root.mainloop()

