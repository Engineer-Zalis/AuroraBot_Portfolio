import cv2
import numpy as np

print("🛰️ AuroraBot - Analisi visione su mappa simulata")

# Carica la mappa simulata
img = cv2.imread("mappa_marziana_simulata.png")
if img is None:
    print("❌ Errore: immagine non trovata.")
    exit()

# Converti da BGR a HSV (per analisi colori)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Colore ROSSO (ostacoli)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)

# Colore VERDE (percorribile)
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Crea una copia per mostrare evidenziamenti
output = img.copy()
output[mask_red > 0] = [0, 0, 255]       # evidenzia ostacoli in rosso vivo
output[mask_green > 0] = [0, 255, 0]     # evidenzia zone libere in verde acceso

# Mostra tutto
cv2.imshow("🌍 Mappa originale", img)
cv2.imshow("🔴 Ostacoli rilevati", mask_red)
cv2.imshow("🟢 Zone libere", mask_green)
cv2.imshow("🧠 Visione AuroraBot", output)

print("✅ Analisi completata! Premi Q per uscire.")
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()



