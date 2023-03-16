import tkinter as tk
import tkinter.messagebox as messagebox
import requests

class M3U8Checker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.results = []

    def create_widgets(self):
        self.url_label = tk.Label(self, text="Introduce una liga m3u8:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self)
        self.url_entry.pack()

        self.check_button = tk.Button(self, text="Comprobar", command=self.check_url)
        self.check_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def check_url(self):
        url = self.url_entry.get()
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                self.results.append((url, "Liga m3u8 funcionando correctamente", "green"))
                messagebox.showinfo("Resultado", "Liga m3u8 funcionando correctamente")
            else:
                self.results.append((url, "Liga m3u8 no disponible", "red"))
                messagebox.showerror("Resultado", "Liga m3u8 no disponible")
        except:
            self.results.append((url, "Liga m3u8 no disponible", "red"))
            messagebox.showerror("Resultado", "Liga m3u8 no disponible")
        self.url_entry.delete(0, tk.END)

root = tk.Tk()
app = M3U8Checker(master=root)
app.mainloop()

# Al cerrar la ventana, se imprime la lista de resultados
print(app.results)
