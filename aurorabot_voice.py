import pyttsx3

# Inizializza motore vocale
voce = pyttsx3.init()
voce.setProperty('rate', 150)      # Velocità del parlato
voce.setProperty('volume', 1)      # Volume massimo

# Lista di messaggi che AuroraBot può dire
messaggi = [
    "AuroraBot attivato. Pronta all'analisi visiva!",
    "Rilevamento completato: area sicura rilevata.",
    "Attenzione: ostacolo presente nella zona!",
    "Analisi ambientale marziana in corso...",
    "Tutto sotto controllo. Pronta a ricevere nuovi comandi!"
]

# AuroraBot parla ogni frase
for frase in messaggi:
    voce.say(frase)
    voce.runAndWait()
