import tkinter as tk
import random
import pyttsx3

# Inizializza la voce
voce = pyttsx3.init()
voce.setProperty('rate', 150)

# Variabili globali
livello_batteria = 100
stato_allarme = False

# Funzione per aggiornare la batteria
def aggiorna_batteria():
    global livello_batteria
    if livello_batteria > 0 and not stato_allarme:
        livello_batteria -= 1
        batteria_var.set(f"Batteria: {livello_batteria}%")
        canvas.itemconfig(batteria_barra, width=2*livello_batteria)
        if livello_batteria <= 20:
            canvas.itemconfig(batteria_barra, fill="red")
            voce.say("⚠️ Batteria quasi scarica!")
            voce.runAndWait()
    root.after(1000, aggiorna_batteria)

# Funzione di ricarica
def ricarica_batteria():
    global livello_batteria
    livello_batteria = 100
    canvas.itemconfig(batteria_barra, fill="green")
    batteria_var.set("🔋 Batteria: 100%")
    voce.say("🔌 Batteria ricaricata al massimo.")
    voce.runAndWait()

# Simula un guasto casuale
def genera_guasto():
    global stato_allarme
    if random.random() < 0.1:
        stato_allarme = True
        canvas.itemconfig(batteria_barra, fill="gray")
        stato_var.set("🚨 Guasto comunicazione!")
        voce.say("🚨 Attenzione, guasto alla comunicazione rilevato!")
        voce.runAndWait()
    else:
        stato_var.set("✅ Comunicazione stabile.")
    root.after(5000, genera_guasto)

# Interazione vocale base
def stato_batteria():
    voce.say(f"La batteria è al {livello_batteria} percento.")
    voce.runAndWait()

# GUI
root = tk.Tk()
root.title("AuroraBot GUI - Missione 01")
root.geometry("400x300")

canvas = tk.Canvas(root, width=200, height=50)
canvas.pack(pady=20)

# Barra batteria
batteria_barra = canvas.create_rectangle(0, 0, 200, 50, fill="green")

batteria_var = tk.StringVar()
batteria_var.set("🔋 Batteria: 100%")
batteria_label = tk.Label(root, textvariable=batteria_var, font=("Helvetica", 14))
batteria_label.pack()

stato_var = tk.StringVar()
stato_var.set("✅ Comunicazione stabile.")
stato_label = tk.Label(root, textvariable=stato_var, font=("Helvetica", 12))
stato_label.pack()

btn_ricarica = tk.Button(root, text="🔌 Ricarica Batteria", command=ricarica_batteria)
btn_ricarica.pack(pady=10)

btn_voce = tk.Button(root, text="🎙️ Aurora, stato batteria?", command=stato_batteria)
btn_voce.pack()

# Avvia
aggiorna_batteria()
genera_guasto()
root.mainloop()
