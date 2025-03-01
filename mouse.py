import pyautogui
import time
import logging
import math

# Configurazione del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def move_in_circle(radius=50, num_steps=36, duration_total=2):
    """
    Muove il mouse lungo un percorso circolare a partire dalla posizione corrente.

    :param radius: Raggio del cerchio in pixel.
    :param num_steps: Numero di passi per completare il cerchio (più passi = movimento più fluido).
    :param duration_total: Durata totale del movimento circolare in secondi.
    """
    # Salva la posizione corrente del mouse come centro del cerchio
    center_x, center_y = pyautogui.position()
    logging.info(f"Avvio movimento circolare da ({center_x}, {center_y}) con raggio = {radius} pixel.")
    
    # Calcola il tempo da dedicare ad ogni passo
    step_duration = duration_total / num_steps
    
    # Esegue il movimento in un percorso circolare
    for i in range(num_steps + 1):  # +1 per completare il cerchio
        angle = 2 * math.pi * i / num_steps
        target_x = center_x + radius * math.cos(angle)
        target_y = center_y + radius * math.sin(angle)
        pyautogui.moveTo(target_x, target_y, duration=step_duration)
    
    # Ritorna alla posizione iniziale
    pyautogui.moveTo(center_x, center_y, duration=0.2)
    logging.info("Movimento circolare completato e posizione iniziale ripristinata.")

def keep_pc_awake(interval=15, radius=50, num_steps=36, circle_duration=2):
    """
    Esegue il movimento circolare ogni 'interval' secondi per evitare che il PC entri in sospensione.
    
    :param interval: Tempo in secondi tra un movimento e l'altro.
    :param radius: Raggio del cerchio in pixel.
    :param num_steps: Numero di passi per completare il cerchio.
    :param circle_duration: Durata totale del movimento circolare in secondi.
    """
    logging.info(f"Avvio script keep-awake: intervallo = {interval} sec, raggio = {radius} pixel.")
    
    try:
        while True:
            move_in_circle(radius=radius, num_steps=num_steps, duration_total=circle_duration)
            logging.info(f"In attesa di {interval} secondi prima del prossimo movimento...")
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Script interrotto dall'utente.")

if __name__ == "__main__":
    # Avvia lo script con un intervallo di 15 secondi, un raggio di 50 pixel,
    # 36 passi per il cerchio e una durata totale di 2 secondi per il movimento circolare.
    keep_pc_awake(interval=15, radius=50, num_steps=36, circle_duration=2)
