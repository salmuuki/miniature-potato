import pygame
import sys
import random


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

        # Aktualisierung den Bildschirm
        pygame.display.flip()

        # Event-Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                maus_position = pygame.mouse.get_pos()

                # Überprüfen, ob auf "Leicht", "Mittel" oder "Schwer" geklickt wurde
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

    wortliste = ["PYTHON", "JAVASCRIPT", "GITHUB", "PYGAME", "PHP"]
    zufallswort = list(random.choice(wortliste).upper())
    geratenes_wort = ['_' for _ in zufallswort]

    versuche = 6  # Anzahl der erlaubten Versuche
    korrekte_guesses = 0

    schriftartBuchstaben = pygame.font.Font(None, 36)
    schriftartVersuche = pygame.font.Font(None, 30)
    schriftartWort = pygame.font.Font(None, 70)



    
    while True:
        screen.fill((80, 255, 90))

        button_width, button_height = 30, 30
        abstand = 5
        x, y = 170, 400

        button_list = []  


        for i in range(26):
            buchstabe = chr(i + 65)
            button_rect = pygame.Rect(x, y, button_width, button_height)
            pygame.draw.rect(screen, (255, 255, 255), button_rect)
            buchstabe_text = schriftartBuchstaben.render(buchstabe, True, (0, 0, 0))
            screen.blit(buchstabe_text, (x + 5, y + 5))

            button_speichern = {'rect': button_rect, 'letter': buchstabe}
            button_list.append(button_speichern)
            x += button_width + abstand
            if (i + 1) % 13 == 0:
                x = 170
                y += 35


        anzeige_wort = schriftartWort.render(" ".join(geratenes_wort), True, (0, 0, 0))
        wort_rechteck = anzeige_wort.get_rect(center=(breite // 2, höhe // 2))
        screen.blit(anzeige_wort, wort_rechteck)

        for event in pygame.event.get():  # Ereignisse abrufen
            if event.type == pygame.QUIT:  # Überprüfen, ob das Fenster geschlossen wurde
                beende_spiel()  # Spiel beenden, wenn das Fenster geschlossen wird
            elif ist_button_gedrueckt(event, button_list):  # Überprüfen, ob ein Button gedrückt wurde
                gedrueckter_button = next(button for button in button_list if button['rect'].collidepoint(pygame.mouse.get_pos()))  # Den gedrückten Button finden
                geratener_buchstabe = gedrueckter_button['letter']  # Den Buchstaben des gedrückten Buttons bekommen
                
                if geratener_buchstabe in zufallswort:  # Überprüfen, ob der geratene Buchstabe im Zufallswort enthalten ist
                    if geratener_buchstabe not in geratenes_wort:   # Überprüfen, ob Buchstabe schon erraten wurde
                        for i in range(len(zufallswort)):  # Für jeden Index im Zufallswort überprüfen
                            if zufallswort[i] == geratener_buchstabe:  # Überprüfen, ob der geratene Buchstabe an dieser Position steht
                                geratenes_wort[i] = geratener_buchstabe  # Den geratenen Buchstaben in das geratene Wort einfügen
                                korrekte_guesses += 1  # Die Anzahl der korrekten Vermutungen erhöhen
                else:
                    versuche -= 1  # Wenn der geratene Buchstabe nicht im Zufallswort ist, die Anzahl der Versuche reduzieren

            

        
        
        if korrekte_guesses == len(zufallswort) or versuche == 0:

            button_list.clear # button liste wird geleert, damit kein buchstabe betätigt werden kann
        
        anzeige_versuche = schriftartVersuche.render(f"Versuche übrig: {versuche}", True, (0, 0, 0))
        screen.blit(anzeige_versuche, (50, 550))

        
        # Button für Hauptmenü
        
        schriftart_hauptmenü = pygame.font.Font(None, 20)
        hauptmenü_button = pygame.Rect(breite // 2 - 350, höhe // 2 - 250, 150, 50)
        pygame.draw.rect(screen, (220, 220, 220), hauptmenü_button)
        hauptmenü_text = schriftart_hauptmenü.render("Hauptmenü", True, (0, 0, 0))
        hauptmenü_rechteck = hauptmenü_text.get_rect(center=hauptmenü_button.center)
        screen.blit(hauptmenü_text, hauptmenü_rechteck)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                maus_position = pygame.mouse.get_pos()
                if hauptmenü_rechteck.collidepoint(maus_position):
                    hauptmenü()


        bild = ["hangman0.png",
                "hangman1.png",
                "hangman2.png",
                "hangman3.png",
                "hangman4.png",
                "hangman5.png",
                "hangman6.png"]
        
        if versuche == 6:
            hangman_bild = pygame.image.load(bild[0])
        elif versuche == 5:
            hangman_bild = pygame.image.load(bild[1])
        elif versuche == 4:
            hangman_bild = pygame.image.load(bild[2])
        elif versuche == 3:
            hangman_bild = pygame.image.load(bild[3])
        elif versuche == 2:
            hangman_bild = pygame.image.load(bild[4])
        elif versuche == 1:
            hangman_bild = pygame.image.load(bild[5])
        elif versuche <= 0:
            hangman_bild = pygame.image.load(bild[6])

        
        screen.blit(hangman_bild, (550, 70))


        
        
        # Code für Wort erraten oder nicht erraten
        if korrekte_guesses == len(zufallswort):

            schriftart = pygame.font.Font(None, 50)
            erraten_text = schriftart.render("Du hast das Wort erraten!!!", True, (0, 0, 0))
            screen.blit(erraten_text, (50, 120))


            # Button für Neustarten
            Neustart_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), Neustart_button)
            Neustart_text = schriftart.render("Neu Starten", True, (0, 0, 0))
            Neustart_rechteck = Neustart_text.get_rect(center=Neustart_button.center)
            screen.blit(Neustart_text, Neustart_rechteck)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    maus_position = pygame.mouse.get_pos()
                    if Neustart_rechteck.collidepoint(maus_position):
                        spiel_leicht()

            

    
        elif versuche == 0:

            schriftart = pygame.font.Font(None, 50)
            erraten_text = schriftart.render("Du hast das Wort NICHT erraten", True, (0, 0, 0))
            screen.blit(erraten_text, (50, 120))


            # Button für Neustarten
            Neustart_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), Neustart_button)
            Neustart_text = schriftart.render("Neu Starten", True, (0, 0, 0))
            Neustart_rechteck = Neustart_text.get_rect(center=Neustart_button.center)
            screen.blit(Neustart_text, Neustart_rechteck)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    maus_position = pygame.mouse.get_pos()
                    if Neustart_rechteck.collidepoint(maus_position):
                        spiel_leicht()
            
            

        pygame.display.flip()



def spiel_mittel():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    pygame.display.set_caption("Hangman Spiel")

    wortliste = ["Java", "HTML", "CSS", "SHELL","OBJECTIVE","SCALA"]
    zufallswort = list(random.choice(wortliste).upper())
    geratenes_wort = ['_' for _ in zufallswort]

    versuche = 6  # Anzahl der erlaubten Versuche
    korrekte_guesses = 0

    schriftartBuchstaben = pygame.font.Font(None, 36)
    schriftartVersuche = pygame.font.Font(None, 30)
    schriftartWort = pygame.font.Font(None, 70)



    
    while True:
        screen.fill((255, 180, 55))

        button_width, button_height = 30, 30
        abstand = 5
        x, y = 170, 400

        button_list = []  


        for i in range(26):
            buchstabe = chr(i + 65)
            button_rect = pygame.Rect(x, y, button_width, button_height)
            pygame.draw.rect(screen, (255, 255, 255), button_rect)
            buchstabe_text = schriftartBuchstaben.render(buchstabe, True, (0, 0, 0))
            screen.blit(buchstabe_text, (x + 5, y + 5))

            button_speichern = {'rect': button_rect, 'letter': buchstabe}
            button_list.append(button_speichern)
            x += button_width + abstand
            if (i + 1) % 13 == 0:
                x = 170
                y += 35


        anzeige_wort = schriftartWort.render(" ".join(geratenes_wort), True, (0, 0, 0))
        wort_rechteck = anzeige_wort.get_rect(center=(breite // 2, höhe // 2))
        screen.blit(anzeige_wort, wort_rechteck)

        for event in pygame.event.get():  # Ereignisse abrufen
            if event.type == pygame.QUIT:  # Überprüfen, ob das Fenster geschlossen wurde
                beende_spiel()  # Spiel beenden, wenn das Fenster geschlossen wird
            elif ist_button_gedrueckt(event, button_list):  # Überprüfen, ob ein Button (Buchstabe) gedrückt wurde
                gedrueckter_button = next(button for button in button_list if button['rect'].collidepoint(pygame.mouse.get_pos()))  # Den gedrückten Button finden
                geratener_buchstabe = gedrueckter_button['letter']  # Den Buchstaben des gedrückten Buttons erhalten
                
                if geratener_buchstabe in zufallswort:  # Überprüfen, ob der geratene Buchstabe im Zufallswort enthalten ist
                    if geratener_buchstabe not in geratenes_wort:   # Überprüfen, ob Buchstabe schon erraten wurde
                        for i in range(len(zufallswort)):  # Für jeden Index im Zufallswort überprüfen
                            if zufallswort[i] == geratener_buchstabe:  # Überprüfen, ob der geratene Buchstabe an dieser Position steht
                                geratenes_wort[i] = geratener_buchstabe  # Den geratenen Buchstaben in das geratene Wort einfügen
                                korrekte_guesses += 1  # Die Anzahl der korrekten Vermutungen erhöhen
                else:
                    versuche -= 1  # Wenn der geratene Buchstabe nicht im Zufallswort ist, die Anzahl der Versuche reduzieren

            

        
        
        if korrekte_guesses == len(zufallswort) or versuche == 0:

            button_list.clear # button liste wird geleert, damit kein buchstabe betätigt werden kann
        
        anzeige_versuche = schriftartVersuche.render(f"Versuche übrig: {versuche}", True, (0, 0, 0))
        screen.blit(anzeige_versuche, (50, 550))

        
        # Button für Hauptmenü
        
        schriftart_hauptmenü = pygame.font.Font(None, 20)
        hauptmenü_button = pygame.Rect(breite // 2 - 350, höhe // 2 - 250, 150, 50)
        pygame.draw.rect(screen, (220, 220, 220), hauptmenü_button)
        hauptmenü_text = schriftart_hauptmenü.render("Hauptmenü", True, (0, 0, 0))
        hauptmenü_rechteck = hauptmenü_text.get_rect(center=hauptmenü_button.center)
        screen.blit(hauptmenü_text, hauptmenü_rechteck)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                maus_position = pygame.mouse.get_pos()
                if hauptmenü_rechteck.collidepoint(maus_position):
                    hauptmenü()


        bild = ["hangman0.png",
                "hangman1.png",
                "hangman2.png",
                "hangman3.png",
                "hangman4.png",
                "hangman5.png",
                "hangman6.png"]
        
        if versuche == 6:
            hangman_bild = pygame.image.load(bild[0])
        elif versuche == 5:
            hangman_bild = pygame.image.load(bild[1])
        elif versuche == 4:
            hangman_bild = pygame.image.load(bild[2])
        elif versuche == 3:
            hangman_bild = pygame.image.load(bild[3])
        elif versuche == 2:
            hangman_bild = pygame.image.load(bild[4])
        elif versuche == 1:
            hangman_bild = pygame.image.load(bild[5])
        elif versuche <= 0:
            hangman_bild = pygame.image.load(bild[6])

        
        screen.blit(hangman_bild, (550, 70))


        
        
        # Code für Wort erraten oder nicht erraten
        if korrekte_guesses == len(zufallswort):

            schriftart = pygame.font.Font(None, 50)
            erraten_text = schriftart.render("Du hast das Wort erraten!!!", True, (0, 0, 0))
            screen.blit(erraten_text, (50, 120))


            # Button für Neustarten
            Neustart_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), Neustart_button)
            Neustart_text = schriftart.render("Neu Starten", True, (0, 0, 0))
            Neustart_rechteck = Neustart_text.get_rect(center=Neustart_button.center)
            screen.blit(Neustart_text, Neustart_rechteck)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    maus_position = pygame.mouse.get_pos()
                    if Neustart_rechteck.collidepoint(maus_position):
                        spiel_mittel()

            

    
        elif versuche == 0:

            schriftart = pygame.font.Font(None, 50)
            erraten_text = schriftart.render("Du hast das Wort NICHT erraten", True, (0, 0, 0))
            screen.blit(erraten_text, (50, 120))


            # Button für Neustarten
            Neustart_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), Neustart_button)
            Neustart_text = schriftart.render("Neu Starten", True, (0, 0, 0))
            Neustart_rechteck = Neustart_text.get_rect(center=Neustart_button.center)
            screen.blit(Neustart_text, Neustart_rechteck)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    maus_position = pygame.mouse.get_pos()
                    if Neustart_rechteck.collidepoint(maus_position):
                        spiel_mittel()
            
            

        pygame.display.flip()


def spiel_schwer():
    
    screen = pygame.display.set_mode((800, 600))

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    pygame.display.set_caption("Hangman Spiel")

    wortliste = ["C","SQL","SWIFT","ARDUINO","ASSEMBLY"]
    zufallswort = list(random.choice(wortliste).upper())
    geratenes_wort = ['_' for _ in zufallswort]

    versuche = 6  # Anzahl der erlaubten Versuche
    korrekte_guesses = 0

    schriftartBuchstaben = pygame.font.Font(None, 36)
    schriftartVersuche = pygame.font.Font(None, 30)
    schriftartWort = pygame.font.Font(None, 70)



    while True:
        screen.fill((255, 70, 110))

        button_width, button_height = 30, 30
        abstand = 5
        x, y = 170, 400

        button_list = []  


        for i in range(26):
            buchstabe = chr(i + 65)
            button_rect = pygame.Rect(x, y, button_width, button_height)
            pygame.draw.rect(screen, (255, 255, 255), button_rect)
            buchstabe_text = schriftartBuchstaben.render(buchstabe, True, (0, 0, 0))
            screen.blit(buchstabe_text, (x + 5, y + 5))

            button_speichern = {'rect': button_rect, 'letter': buchstabe}
            button_list.append(button_speichern)
            x += button_width + abstand
            if (i + 1) % 13 == 0:
                x = 170
                y += 35


        anzeige_wort = schriftartWort.render(" ".join(geratenes_wort), True, (0, 0, 0))
        wort_rechteck = anzeige_wort.get_rect(center=(breite // 2, höhe // 2))
        screen.blit(anzeige_wort, wort_rechteck)

        if versuche == 6:
            hangman_bild = pygame.image.load("hangman0.png")
        elif versuche == 5:
            hangman_bild = pygame.image.load("hangman1.png")
        elif versuche == 4:
            hangman_bild = pygame.image.load("hangman2.png")
        elif versuche == 3:
            hangman_bild = pygame.image.load("hangman3.png")
        elif versuche == 2:
            hangman_bild = pygame.image.load("hangman4.png")
        elif versuche == 1:
            hangman_bild = pygame.image.load("hangman5.png")
        elif versuche <= 0:
            hangman_bild = pygame.image.load("hangman6.png")
        
        screen.blit(hangman_bild, (550, 70))



        for event in pygame.event.get():  # Ereignisse abrufen
            if event.type == pygame.QUIT:  # Überprüfen, ob das Fenster geschlossen wurde
                beende_spiel()  # Spiel beenden, wenn das Fenster geschlossen wird
            elif ist_button_gedrueckt(event, button_list):  # Überprüfen, ob ein Button (Buchstabe) gedrückt wurde
                gedrueckter_button = next(button for button in button_list if button['rect'].collidepoint(pygame.mouse.get_pos()))  # Den gedrückten Button finden
                geratener_buchstabe = gedrueckter_button['letter']  # Den Buchstaben des gedrückten Buttons bekommen
                
                if geratener_buchstabe in zufallswort:  # Überprüfen, ob der geratene Buchstabe im Zufallswort enthalten ist
                    if geratener_buchstabe not in geratenes_wort:   # Überprüfen, ob Buchstabe schon erraten wurde
                        for i in range(len(zufallswort)):  # Für jeden Index im Zufallswort überprüfen
                            if zufallswort[i] == geratener_buchstabe:  # Überprüfen, ob der geratene Buchstabe an dieser Position steht
                                geratenes_wort[i] = geratener_buchstabe  # Den geratenen Buchstaben in das geratene Wort einfügen
                                korrekte_guesses += 1  # Die Anzahl der korrekten Vermutungen erhöhen
                else:
                    versuche -= 1  # Wenn der geratene Buchstabe nicht im Zufallswort ist, die Anzahl der Versuche reduzieren

        if korrekte_guesses == len(zufallswort) or versuche == 0:

            button_list.clear # button liste wird geleert, damit kein buchstabe betätigt werden kann
        
        anzeige_versuche = schriftartVersuche.render(f"Versuche übrig: {versuche}", True, (0, 0, 0))
        screen.blit(anzeige_versuche, (50, 550))


        # Button für Hauptmenü
        
        schriftart_hauptmenü = pygame.font.Font(None, 20)
        hauptmenü_button = pygame.Rect(breite // 2 - 350, höhe // 2 - 250, 150, 50)
        pygame.draw.rect(screen, (220, 220, 220), hauptmenü_button)
        hauptmenü_text = schriftart_hauptmenü.render("Hauptmenü", True, (0, 0, 0))
        hauptmenü_rechteck = hauptmenü_text.get_rect(center=hauptmenü_button.center)
        screen.blit(hauptmenü_text, hauptmenü_rechteck)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                maus_position = pygame.mouse.get_pos()
                if hauptmenü_rechteck.collidepoint(maus_position):
                    hauptmenü()


        # Code für Wort erraten oder nicht erraten
        if korrekte_guesses == len(zufallswort):

            schriftart = pygame.font.Font(None, 50)
            erraten_text = schriftart.render("Du hast das Wort erraten!!!", True, (0, 0, 0))
            screen.blit(erraten_text, (50, 120))

            # Button für Starten
            Neustart_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), Neustart_button)
            Neustart_text = schriftart.render("Neu Starten", True, (0, 0, 0))
            Neustart_rechteck = Neustart_text.get_rect(center=Neustart_button.center)
            screen.blit(Neustart_text, Neustart_rechteck)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    maus_position = pygame.mouse.get_pos()
                    if Neustart_rechteck.collidepoint(maus_position):
                        spiel_schwer()

            

    
        elif versuche == 0:

            schriftart = pygame.font.Font(None, 50)
            erraten_text = schriftart.render("Du hast das Wort NICHT erraten", True, (0, 0, 0))
            screen.blit(erraten_text, (50, 120))

            

            # Button für Neustarten
            Neustart_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), Neustart_button)
            Neustart_text = schriftart.render("Neu Starten", True, (0, 0, 0))
            Neustart_rechteck = Neustart_text.get_rect(center=Neustart_button.center)
            screen.blit(Neustart_text, Neustart_rechteck)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    maus_position = pygame.mouse.get_pos()
                    if Neustart_rechteck.collidepoint(maus_position):
                        spiel_leicht()
            
            

        pygame.display.flip()


# GUI jetzt starten
hauptmenü()
