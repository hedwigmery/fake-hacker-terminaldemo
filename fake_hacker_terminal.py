import tkinter as tk
import random
import time

def terminale_yaz():
    komutlar = [
        "[+] Sistem baslatiliyor...",
        "[+] Guvenlik modulleri yukleniyor...",
        "[+] Sanal IP taramasi basladi...",
        "[+] Portlar analiz ediliyor...",
        "[!] Supheli baglanti simule edildi.",
        "[+] Fake exploit kontrolu yapiliyor...",
        "[+] Veriler sifrelenmis gibi gosteriliyor...",
        "[+] Erisim testi tamamlandi.",
        "[✓] Sistem guvenli. Simulasyon basarili."
    ]

    yazi = random.choice(komutlar)
    terminal.insert(tk.END, yazi + "\n")
    terminal.see(tk.END)

    pencere.after(700, terminale_yaz)

def matrix_efekti():
    karakterler = "01ABCDEF#$%&"
    satir = "".join(random.choice(karakterler) for _ in range(60))
    terminal.insert(tk.END, satir + "\n")
    terminal.see(tk.END)

def ana_ekran():
    splash.destroy()

    global pencere, terminal

    pencere = tk.Tk()
    pencere.title("Hedwigmery Hacker Terminal")
    pencere.geometry("800x500")
    pencere.configure(bg="black")

    baslik = tk.Label(
        pencere,
        text="HEDWIGMERY CYBER TERMINAL",
        font=("Consolas", 20, "bold"),
        bg="black",
        fg="#00ff41"
    )
    baslik.pack(pady=15)

    terminal = tk.Text(
        pencere,
        bg="black",
        fg="#00ff41",
        insertbackground="#00ff41",
        font=("Consolas", 11),
        width=90,
        height=22
    )
    terminal.pack(pady=10)

    buton_frame = tk.Frame(pencere, bg="black")
    buton_frame.pack(pady=10)

    tk.Button(
        buton_frame,
        text="Matrix Efekti",
        command=matrix_efekti,
        bg="#003b00",
        fg="#00ff41",
        font=("Consolas", 10, "bold"),
        width=18
    ).grid(row=0, column=0, padx=8)

    tk.Button(
        buton_frame,
        text="Temizle",
        command=lambda: terminal.delete("1.0", tk.END),
        bg="#003b00",
        fg="#00ff41",
        font=("Consolas", 10, "bold"),
        width=18
    ).grid(row=0, column=1, padx=8)

    tk.Button(
        buton_frame,
        text="Cikis",
        command=pencere.destroy,
        bg="#3b0000",
        fg="#ff4d4d",
        font=("Consolas", 10, "bold"),
        width=18
    ).grid(row=0, column=2, padx=8)

    terminal.insert(tk.END, ">>> Hosgeldin Hedwigmery\n")
    terminal.insert(tk.END, ">>> Simulasyon terminali aktif edildi.\n\n")

    terminale_yaz()

    pencere.mainloop()

splash = tk.Tk()
splash.title("Acilis")
splash.geometry("520x300")
splash.configure(bg="black")
splash.resizable(False, False)

tk.Label(
    splash,
    text="HOSGELDIN",
    font=("Consolas", 22, "bold"),
    bg="black",
    fg="#00ff41"
).pack(pady=45)

tk.Label(
    splash,
    text="Hedwigmery",
    font=("Consolas", 34, "bold"),
    bg="black",
    fg="#00ff41"
).pack(pady=10)

tk.Label(
    splash,
    text="Cyber Terminal yukleniyor...",
    font=("Consolas", 12),
    bg="black",
    fg="#00aa2a"
).pack(pady=20)

splash.after(3000, ana_ekran)
splash.mainloop()