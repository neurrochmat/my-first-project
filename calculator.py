from functools import partial
import tkinter as tk

class aplikasiKalkulator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Kalkulator tkinter")
        self.membuatTombol()
        self.penentu = False
        
    def membuatTombol(self):
        self.layar = tk.Entry(self, width=25)
        self.layar.grid(row=0, column=0, columnspan=4)
        btn_list = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-',
            'C', '/', '*',
            '='
        ]
        baris = 1
        kolom = 0
        for penampung in btn_list:
            perintah = partial(self.hitung, penampung)
            if penampung == '=':
                tk.Button(self, text='=', width=25, command=perintah).grid(row=baris, column=kolom, columnspan=4)
            elif penampung == 'C':
                tk.Button(self, text='C', width=5, command=perintah).grid(row=baris, column=kolom)
            else:
                tk.Button(self, text=penampung, width=5, command=perintah).grid(row=baris, column=kolom)
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris += 1

    def hitung(self, key):
        if self.penentu and key != '=':
            self.layar.delete(0, tk.END)
            self.penentu = False
        if key == '=':
            try:
                result = eval(self.layar.get())
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, str(result))
            except:
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, "Error")
        elif key == 'C':
            self.layar.delete(0, tk.END)
        else:
            self.layar.insert(tk.END, key)

panggil = aplikasiKalkulator()
panggil.mainloop()
