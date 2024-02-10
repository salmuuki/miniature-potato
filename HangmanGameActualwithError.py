# this is the version with actual excel 
import pandas as pd


import pygame
import sys
import random
import openpyxl



# Initialisierung von Pygame
pygame.init()

# Fenstergröße und Farben
breite, höhe = 800, 600
hintergrundfarbe = (255, 255, 255)
button_farbe = (50, 150, 255)

# Einrichtung des Fensters
screen = pygame.display.set_mode((breite, höhe))
pygame.display.set_caption("Hangman Spiel")


# Funktion zum Starten des Spiels
def starte_spiel(schwierigkeit):
    # Hier kannst du den Code für das Hangman-Spiel hinzufügen
    print(f"Spiel gestartet mit Schwierigkeitsgrad: {schwierigkeit}")
    if schwierigkeit == "Leicht":
        spiel_leicht()
    elif schwierigkeit == "Mittel":
        spiel_mittel()
    elif schwierigkeit == "Schwer":
        spiel_schwer()


# Funktion zum Beenden des Programms
def beende_spiel():
    pygame.quit()
    sys.exit()


# Hauptfunktion für die GUI
def hauptmenü():
    schwierigkeitsstufen = ["Leicht", "Mittel", "Schwer"]
    aktuelle_schwierigkeit_index = 0

    while True:
        screen.fill(hintergrundfarbe)

        # Hangman-Logo
        schriftart = pygame.font.Font(None, 100)
        logo_text = schriftart.render("Hangman", True, (0, 0, 0))
        logo_rechteck = logo_text.get_rect(center=(breite // 2, höhe // 4))
        screen.blit(logo_text, logo_rechteck)

        # Schwierigkeitsgrad-Text
        schwierigkeits_text = schriftart.render(schwierigkeitsstufen[aktuelle_schwierigkeit_index], True, (0, 0, 0))
        schwierigkeits_rechteck = schwierigkeits_text.get_rect(center=(breite // 2, höhe // 2))
        screen.blit(schwierigkeits_text, schwierigkeits_rechteck)

        # Leicht Text
        schriftart_leicht = pygame.font.Font(None, 70)
        leicht_text = schriftart_leicht.render("Leicht", True, (0, 0, 0))
        leicht_rechteck = leicht_text.get_rect(center=(200, 400))
        screen.blit(leicht_text, leicht_rechteck)

        # Mittel Text
        schriftart_mittel = pygame.font.Font(None, 70)
        mittel_text = schriftart_mittel.render("Mittel", True, (0, 0, 0))
        mittel_rechteck = mittel_text.get_rect(center=(400, 400))
        screen.blit(mittel_text, mittel_rechteck)

        # Schwer Text
        schriftart_schwer = pygame.font.Font(None, 70)
        schwer_text = schriftart_schwer.render("Schwer", True, (0, 0, 0))
        schwer_rechteck = schwer_text.get_rect(center=(600, 400))
        screen.blit(schwer_text, schwer_rechteck)

        # Button für Starten
        start_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
        pygame.draw.rect(screen, button_farbe, start_button)
        start_text = schriftart.render("Starten", True, (0, 0, 0))
        start_rechteck = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_rechteck)

        # Aktualisiere den Bildschirm
        pygame.display.flip()

        # Event-Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                maus_position = pygame.mouse.get_pos()

                # Überprüfe, ob auf "Leicht", "Mittel" oder "Schwer" geklickt wurde
                if leicht_rechteck.collidepoint(maus_position):
                    aktuelle_schwierigkeit_index = 0
                elif mittel_rechteck.collidepoint(maus_position):
                    aktuelle_schwierigkeit_index = 1
                elif schwer_rechteck.collidepoint(maus_position):
                    aktuelle_schwierigkeit_index = 2
                elif start_button.collidepoint(maus_position):
                    starte_spiel(schwierigkeitsstufen[aktuelle_schwierigkeit_index])

def ist_button_gedrueckt(event, button_list):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        for button in button_list:
            if button['rect'].collidepoint(mouse_pos):
                return True


def spiel_leicht():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hangman Spiel")

    excel_file_path = "C:\\Users\\Nouairah\\OneDrive - Perga GmbH\\Documents\\Mosbach\\EXCEL HANGMAN.xlsx"  # Replace with your actual Excel file path
    vocab_df = pd.read_excel(excel_file_path, engine='openpyxl')
    
    if vocab_df.empty or "Leicht" not in vocab_df.columns:
        print("Error: DataFrame is empty. Please check your Excel file.")
        beende_spiel
    
    zufallswort = list(random.choice(vocab_df["Leicht"]).upper())
    geratenes_wort = ['_' for _ in zufallswort]

    versuche = 6  # Anzahl der erlaubten Versuche
    korrekte_guesses = 0

    schriftart = pygame.font.Font(None, 36)

    
    while True:
        screen.fill((80, 255, 90))

        button_width, button_height = 30, 30
        abstand = 5
        x, y = 50, 50

        button_list = []

        for i in range(26):
            buchstabe = chr(i + 65)
            button_rect = pygame.Rect(x, y, button_width, button_height)
            pygame.draw.rect(screen, (255, 255, 255), button_rect)
            buchstabe_text = schriftart.render(buchstabe, True, (0, 0, 0))
            screen.blit(buchstabe_text, (x + 5, y + 5))

            button_speichern = {'rect': button_rect, 'letter': buchstabe}
            button_list.append(button_speichern)
            x += button_width + abstand
            if (i + 1) % 13 == 0:
                x = 50
                y += button_height + abstand


        anzeige_wort = schriftart.render(" ".join(geratenes_wort), True, (0, 0, 0))
        screen.blit(anzeige_wort, (200, 400))

        for event in pygame.event.get():  # Ereignisse abrufen (z. B. Tastatureingaben oder Mausklicks)
            if event.type == pygame.QUIT:  # Überprüfen, ob das Fenster geschlossen wurde
                beende_spiel()  # Beende das Spiel, wenn das Fenster geschlossen wird
            elif ist_button_gedrueckt(event, button_list):  # Überprüfen, ob ein Button (Buchstabe) gedrückt wurde
                gedrueckter_button = next(button for button in button_list if button['rect'].collidepoint(pygame.mouse.get_pos()))  # Den gedrückten Button finden
                geratener_buchstabe = gedrueckter_button['letter']  # Den Buchstaben des gedrückten Buttons erhalten
                
                if geratener_buchstabe in zufallswort:  # Überprüfen, ob der geratene Buchstabe im Zufallswort enthalten ist
                    for i in range(len(zufallswort)):  # Für jeden Index im Zufallswort überprüfen
                        if zufallswort[i] == geratener_buchstabe:  # Überprüfen, ob der geratene Buchstabe an dieser Position steht
                            geratenes_wort[i] = geratener_buchstabe  # Den geratenen Buchstaben in das geratene Wort einfügen
                            korrekte_guesses += 1  # Die Anzahl der korrekten Vermutungen erhöhen
                else:
                    versuche -= 1  # Wenn der geratene Buchstabe nicht im Zufallswort ist, die Anzahl der Versuche reduzieren

        anzeige_versuche = schriftart.render(f"Versuche übrig: {versuche}", True, (0, 0, 0))
        screen.blit(anzeige_versuche, (200, 500))

        if korrekte_guesses == len(zufallswort):
            print("Herzlichen Glückwunsch! Du hast das Wort erraten.")
            beende_spiel()
        elif versuche == 0:
            print(f"Leider verloren! Das richtige Wort war: {''.join(zufallswort)}")
            beende_spiel()

        pygame.display.flip()



def spiel_mittel():
    screen = pygame.display.set_mode((800, 600))

    while True:
        screen.fill((255, 200, 70))

        schriftart = pygame.font.Font(None, 80)
        logo_text = schriftart.render("Mittel", True, (0, 0, 0))
        logo_rechteck = logo_text.get_rect(center=(breite // 2, höhe // 4))
        screen.blit(logo_text, logo_rechteck)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()


def spiel_schwer():
    screen = pygame.display.set_mode((800, 600))

    while True:
        screen.fill((255, 70, 110))

        schriftart = pygame.font.Font(None, 80)
        logo_text = schriftart.render("Schwer", True, (0, 0, 0))
        logo_rechteck = logo_text.get_rect(center=(breite // 2, höhe // 4))
        screen.blit(logo_text, logo_rechteck)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()




# Starte die GUI
hauptmenü()

# line 121 and 122 (obtains the excel path that everyone should change to use it with their own pc)
# 120 to 130 are the error i would say
