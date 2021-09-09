class UI:
    @staticmethod
    def home():
        print(r"""
         ______________________________________
________|                Taxis                 |_______
\       |               Kochbuch               |      /
 \      |                (2021)                |     /
 /      |______________________________________|     \
/__________)                                (_________\ """)
        print(f"\n--- H A U P T M E N Ü ---\n"
              f"\n"
              f"(0) Neues Rezept (von Chefkoch)\n"
              f"(9) Neues Rezept (freihand)\n"
              f"\n"
              f"(1) Zufälliges Rezept\n"
              f"(2) Rezept Suchen\n"
              f"(3) Alle Rezepte anzeigen"
              f"\n"
              f"-------------------------")

        while True:
            choice = input("0 / 9 // 1 / 2 / 3 ? ")

            if choice in ["0", "1", "2", "3", "9"]:
                return choice

            elif choice in ["exit", "quit", "q", "ende"]:
                print("Kochbuch wird beendet...")
                quit()

            print("Ungültige Auswahl")

    @staticmethod
    def recipe_menu():
        print(f"(1) Zutatenliste verschicken (Telegram)\n"
              f"(0) Hauptmenü\n")

        while True:
            choice = input("1 // 0 ? ")

            if choice in ["1", "0"]:
                return choice

            elif choice in ["exit", "quit", "q", "ende"]:
                print("Kochbuch wird beendet...")
                quit()

            print("Ungültige Auswahl")
