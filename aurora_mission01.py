import pygame
import pyttsx3

# Inizializza PyGame e Aurora
pygame.init()
voce = pyttsx3.init()

# Imposta finestra
WIDTH, HEIGHT = 800, 600
finestra = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 AuroraMission_01 – Centro Controllo")

# Colori
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
VERDE = (0, 200, 0)
ROSSO = (200, 0, 0)
GRIGIO = (50, 50, 50)

# Font
font = pygame.font.SysFont("Arial", 24)

# Stato missione
batteria = 100
connessione = True
messaggio = "Missione attiva. Pronta a ricevere comandi."

def parla(testo):
    voce.say(testo)
    voce.runAndWait()

def disegna_gui():
    finestra.fill(NERO)

    # Titolo
    titolo = font.render("AuroraMission_01 - Centro di Controllo", True, BIANCO)
    finestra.blit(titolo, (20, 20))

    # Batteria
    pygame.draw.rect(finestra, GRIGIO, (50, 100, 300, 30))
    colore_batt = VERDE if batteria > 30 else ROSSO
    pygame.draw.rect(finestra, colore_batt, (50, 100, 3 * batteria, 30))
    batt_txt = font.render(f"Batteria: {batteria}%", True, BIANCO)
    finestra.blit(batt_txt, (370, 100))

    # Connessione
    conn_txt = "Online" if connessione else "Persa"
    conn_color = VERDE if connessione else ROSSO
    conn_stato = font.render(f"Connessione: {conn_txt}", True, conn_color)
    finestra.blit(conn_stato, (50, 150))

    # Messaggio vocale
    box = pygame.Rect(50, 500, 700, 60)
    pygame.draw.rect(finestra, GRIGIO, box)
    testo = font.render(messaggio, True, BIANCO)
    finestra.blit(testo, (60, 520))

    pygame.display.flip()

# Loop principale
running = True
parla(messaggio)

while running:
    disegna_gui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simula consumo batteria
    pygame.time.delay(1000)
    batteria -= 1

    if batteria == 30:
        messaggio = "⚠️ Batteria al 30%. Consumo critico!"
        parla(messaggio)

    if batteria == 0:
        messaggio = "🔴 Missione terminata. AuroraBot si spegne."
        parla(messaggio)
        running = False

pygame.quit()
