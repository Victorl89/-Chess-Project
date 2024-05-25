import os
import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
from screeninfo import get_monitors

# Καθορίζει τον τρέχοντα κατάλογο για φόρτωση των εικόνων πιο κάτω.
gdirectory = ''


class ChessboardGUI:
    def __init__(self, master, moves=None):
        self.master = master
        self.moves = moves
        self.master.title("Chessboard")
        # Λήψη διαστάσεων της οθόνης του χρήστη
        monitor = get_monitors()[0]
        screen_width = monitor.width
        screen_height = monitor.height

        # Ρύθμιση μεγέθους και κεντραρίσματος παραθύρου
        self.master.state('zoomed')
        self.board_canvas = tk.Canvas(self.master, width=screen_width // 2, height=screen_height)
        self.board_canvas.pack(side=tk.LEFT, fill="both", expand=True)
        self.moves_text = tk.Text(self.master, height=5, width=60)
        self.moves_text.pack(side=tk.TOP, padx=10, pady=10)
        self.scrollbar = tk.Scrollbar(self.master, command=self.moves_text.yview)
        self.moves_text.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
        self.moves_text.config(yscrollcommand=self.scrollbar.set)
        self.moves_text.config(yscrollcommand=self.scrollbar.set)
        self.next_button = tk.Button(
            self.master, text="Next Move", command=self.go_next, bg='#654321', fg='white')
        self.next_button.pack(side=tk.BOTTOM, padx=29, pady=10)

        self.previous_button = tk.Button(self.master, text="Previous Move", command=self.go_previous, bg='#654321',
                                         fg='white')
        self.previous_button.pack(side=tk.BOTTOM, padx=30, pady=10)
        if self.moves:
            formatted_moves = self.format_moves(self.moves)
            self.moves_text.insert(tk.END, formatted_moves)
        self.draw_chessboard()
        # Φόρτωση των εικόνων των πιονιών.
        self.load_images()

    def format_moves(self, moves):
        moves_list = moves.split()
        formatted_moves = []
        for i in range(0, len(moves_list), 2):
            move_pair = f"{moves_list[i]}"
            if i + 1 < len(moves_list):
                move_pair += f"\t\t{moves_list[i + 1]}\n"
            formatted_moves.append(move_pair)
        return " ".join(formatted_moves)

    # Σχεδίαση της σκακιέρας.
    def draw_chessboard(self):
        # Δημιουργία των τετραγώνων της σκακιέρας και καθορισμός του χρώματός τους.
        square_size = 120
        for row in range(8):
            for col in range(8):
                x0, y0 = col * square_size, row * square_size
                x1, y1 = x0 + square_size, y0 + square_size

                # Εναλλαγή του χρώματος μεταξύ των τετραγώνων.
                color = "#FFEBCD" if (row + col) % 2 == 0 else "#654321"
                self.board_canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def load_images(self):
        # Ορισμός των πιονιων του σκακιού και φόρτωση των εικόνων τους.
        board = [
            ["bR1", "bN1", "bB1", "bQ", "bK", "bB2", "bN2", "bR2"],
            ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--"],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--"],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--"],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--"],
            ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],
            ["wR1", "wN1", "wB1", "wQ", "wK", "wB2", "wN2", "wR2"],
        ]
        square_size = 120
        # Φόρτωση των εικόνων από τα αντίστοιχα αρχεία.
        piece_images = {
            "bp1": tk.PhotoImage(file=os.path.join(gdirectory, "bp1.png")),
            "bp2": tk.PhotoImage(file=os.path.join(gdirectory, "bp2.png")),
            "bp3": tk.PhotoImage(file=os.path.join(gdirectory, "bp3.png")),
            "bp4": tk.PhotoImage(file=os.path.join(gdirectory, "bp4.png")),
            "bp5": tk.PhotoImage(file=os.path.join(gdirectory, "bp5.png")),
            "bp6": tk.PhotoImage(file=os.path.join(gdirectory, "bp6.png")),
            "bp7": tk.PhotoImage(file=os.path.join(gdirectory, "bp7.png")),
            "bp8": tk.PhotoImage(file=os.path.join(gdirectory, "bp8.png")),
            "bR1": tk.PhotoImage(file=os.path.join(gdirectory, "bR1.png")),
            "bR2": tk.PhotoImage(file=os.path.join(gdirectory, "bR2.png")),
            "bN1": tk.PhotoImage(file=os.path.join(gdirectory, "bN1.png")),
            "bN2": tk.PhotoImage(file=os.path.join(gdirectory, "bN2.png")),
            "bB1": tk.PhotoImage(file=os.path.join(gdirectory, "bB1.png")),
            "bB2": tk.PhotoImage(file=os.path.join(gdirectory, "bB2.png")),
            "bQ": tk.PhotoImage(file=os.path.join(gdirectory, "bQ.png")),
            "bK": tk.PhotoImage(file=os.path.join(gdirectory, "bK.png")),
            "wp1": tk.PhotoImage(file=os.path.join(gdirectory, "wp1.png")),
            "wp2": tk.PhotoImage(file=os.path.join(gdirectory, "wp2.png")),
            "wp3": tk.PhotoImage(file=os.path.join(gdirectory, "wp3.png")),
            "wp4": tk.PhotoImage(file=os.path.join(gdirectory, "wp4.png")),
            "wp5": tk.PhotoImage(file=os.path.join(gdirectory, "wp5.png")),
            "wp6": tk.PhotoImage(file=os.path.join(gdirectory, "wp6.png")),
            "wp7": tk.PhotoImage(file=os.path.join(gdirectory, "wp7.png")),
            "wp8": tk.PhotoImage(file=os.path.join(gdirectory, "wp8.png")),
            "wR1": tk.PhotoImage(file=os.path.join(gdirectory, "wR1.png")),
            "wR2": tk.PhotoImage(file=os.path.join(gdirectory, "wR2.png")),
            "wN1": tk.PhotoImage(file=os.path.join(gdirectory, "wN1.png")),
            "wN2": tk.PhotoImage(file=os.path.join(gdirectory, "wN2.png")),
            "wB1": tk.PhotoImage(file=os.path.join(gdirectory, "wB1.png")),
            "wB2": tk.PhotoImage(file=os.path.join(gdirectory, "wB2.png")),
            "wQ": tk.PhotoImage(file=os.path.join(gdirectory, "wQ.png")),
            "wK": tk.PhotoImage(file=os.path.join(gdirectory, "wK.png")),
        }
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece != "--":
                    x0, y0 = col * square_size, row * square_size
                    self.board_canvas.create_image(x0 + square_size / 2, y0 + square_size / 2,
                                                   image=piece_images[piece])
        tk.mainloop()

    def go_next(self):
        # Λειτουργία για την εμφάνιση της επόμενης κίνησης.
        pass

    def go_previous(self):
        # Λειτουργία για την εμφάνιση της προηγούμενης κίνησης.
        pass


# Κλάση για την επιλογή παιχνιδιού από τα αρχεία PGN.
class GameSelectionWindow:
    def __init__(self, games, callback):
        self.callback = callback
        self.games = games

        self.root = tk.Tk()
        self.root.title("Game Selection")
        window_size = 400
        self.root.geometry(f"{window_size * 2}x{window_size * 2}")

        # Δημιουργία λίστας με τα διαθέσιμα παιχνίδια.
        self.label = tk.Label(self.root, text="Select a game:")
        self.label.pack()

        self.listbox = tk.Listbox(self.root, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(padx=10, pady=10, fill='both', expand=True)
        self.scrollbar = tk.Scrollbar(self.listbox, command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Εισαγωγή των παιχνιδιών στη λίστα.
        for i, game_info in enumerate(games, 1):
            self.listbox.insert(tk.END, f"Game {i}: {game_info}")
        self.listbox.pack()
        # Κουμπί επιλογής παιχνιδιού.
        self.button = tk.Button(self.root, text="Select", command=self.select_game)
        self.button.pack()

    def select_game(self):
        # Επιλογή παιχνιδιού από τη λίστα και κλήση της αντίστοιχης συνάρτησης επιλογής, display_selected_game
        # (selected_game_info)
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_game_index = selected_index[0]
            selected_game_info = self.games[selected_game_index]  # Retrieve selected game info
            self.callback(selected_game_info)
            self.root.destroy()
        else:
            messagebox.showwarning("No Selection", "Please select a game.")


# Κλάση που εμφανίζει το αρχικό παράθυρο με τις επιλογές όπως και την δήλωση directory.
class InitialWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='#654321')
        self.root.title("Chess Project")
        window_size = 900
        self.root.geometry(f"{window_size}x{window_size}")
        # Προσθήκη εικόνας φόντου.
        background_image = PhotoImage(file="background_image.png")
        background_label = tk.Label(self.root, image=background_image)
        background_label.place(relwidth=1, relheight=1)
        # Προσθήκη εικονιδίου παραθύρου
        image_icon = PhotoImage(file="Icon.png")
        self.root.iconphoto(False, image_icon)

        # Δημιουργία μενού.
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open Directory", command=self.open_directory)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_from_toolbar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Ετικέτα τίτλου.
        self.label = tk.Label(self.root, text="Welcome to Graphical Representation of Chess", font=('Arial', 18),
                              fg='white')
        self.label.pack(padx=10, pady=10)
        self.label.configure(bg='#654321')

        # Πλαίσιο κειμένου για την εμφάνιση των πληροφοριών του παιχνιδιού.
        self.textbox = tk.Text(self.root, height=20, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10, fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.textbox, command=self.textbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.textbox.config(yscrollcommand=self.scrollbar.set)

        # Μενού δεξιού κλικ στο πλαίσιο κειμένου.
        self.textbox_menu = tk.Menu(self.root, tearoff=0)
        self.textbox_menu.add_command(label="Copy", command=self.copy_text)
        self.textbox.bind("<Button-3>", self.show_textbox_menu)

        # Κουμπί για την προβολή της σκακιέρας (γίνεται η εντολή open chessboard
        # που με την σειρά της ανατρέχει στην κλάση chessboard gui)

        self.button = tk.Button(self.root, text="Chessboard", font=('Arial', 18), command=self.open_chessboard)
        self.button.pack(padx=10, pady=39)
        self.button.configure(bg='#f5f5dc')

        # Κλείσιμο παραθύρου με επιβεβαίωση απο τον χρήστη
        self.root.protocol('WM_DELETE_WINDOW', self.closing_window)
        self.root.mainloop()

    def open_directory(self):
        # Άνοιγμα παραθύρου για την επιλογή φακέλου με αρχεία PGN.
        directory = filedialog.askdirectory()
        if directory:
            pgn_files = self.display_pgn_files(directory)
            if pgn_files:
                self.select_pgn_file(directory, pgn_files)
            else:
                messagebox.showinfo("No PGN files", "No PGN files found in the selected directory.")

    def copy_text(self):
        # Αντιγραφή επιλεγμένου κειμένου.
        selected = self.textbox.selection_get()
        self.root.clipboard_clear()
        self.root.clipboard_append(selected)

    @staticmethod
    def display_pgn_files(folder_path):
        # Εμφάνιση αρχείων PGN στον επιλεγμένο φάκελο.
        pgn_files = [file for file in os.listdir(folder_path) if file.endswith('.pgn')]
        if pgn_files:
            return pgn_files
        else:
            return ["No PGN files found in the folder."]

    def select_pgn_file(self, directory, pgn_files):
        # Επιλογή αρχείου PGN και προβολή των διαθέσιμων παιχνιδιών.
        NameSelectionWindow(pgn_files, directory, self.show_pgn_games)

    def show_pgn_games(self, directory, selected_file):
        # Εμφάνιση παιχνιδιών από το επιλεγμένο αρχείο PGN.
        try:
            with open(os.path.join(directory, selected_file), 'r') as file:
                file_content = file.read()
                games = file_content.split('\n\n')
                self.display_games(games)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {selected_file} not found.")

    def display_games(self, games):
        # Εμφάνιση παιχνιδιών για επιλογή απο τον χρήστη.
        games_to_display = []
        current_game = ""

        for line in games:
            line = line.strip()
            if line.startswith("[Event"):
                if current_game:
                    games_to_display.append(current_game.strip())
                current_game = line + "\n"
            else:
                current_game += line + "\n"

        if current_game:
            games_to_display.append(current_game.strip())

        GameSelectionWindow(games_to_display, self.display_selected_game)

    def display_selected_game(self, selected_game_info):
        # Εμφάνιση των πληροφοριών του επιλεγμένου παιχνιδιού στο πλαίσιο κειμένου.
        self.textbox.delete('1.0', tk.END)
        self.textbox.insert(tk.END, selected_game_info)

    def show_textbox_menu(self, event):  # Εμφάνιση μενού δεξιού κλικ στο πλαίσιο κειμένου.

        self.textbox_menu.post(event.x_root, event.y_root)

    def open_chessboard(self):  # Άνοιγμα παραθύρου της σκακιέρας με περασμένες τις κινήσεις της επιλεγμένης παρτίδας.
        selected_game_info = self.textbox.get("11.0", tk.END)
        chessboard_window = tk.Toplevel(self.root)
        ChessboardGUI(chessboard_window, moves=selected_game_info)

    def closing_window(self):  # Ερώτημα για επιβεβαίωση κλεισίματος του παραθύρου.
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def exit_from_toolbar(self):  # Έξοδος από το πρόγραμμα από το μενού.
        self.closing_window()


class NameSelectionWindow:  # Κλάση για την επιλογή αρχείου PGN.
    def __init__(self, names, directory, callback):
        self.callback = callback
        self.directory = directory
        self.root = tk.Tk()
        self.root.title("Name Selection")
        window_size = 400
        self.root.geometry(f"{window_size}x{window_size}")

        self.label = tk.Label(self.root, text="Select a PGN file:")  # Ετικέτα επιλογής αρχείου PGN.
        self.label.pack()

        # Λίστα με τα ονόματα των αρχείων PGN στον φάκελο.
        self.listbox = tk.Listbox(self.root, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(padx=10, pady=10, fill='both', expand=True)
        self.scrollbar = tk.Scrollbar(self.listbox, command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        for name in names:
            self.listbox.insert(tk.END, name)
        self.listbox.pack()

        self.button = tk.Button(self.root, text="Select", command=self.select_pgn_file)  # Κουμπί επιλογής αρχείου PGN.
        self.button.pack()

    def select_pgn_file(self):  # Επιλογή αρχείου PGN και κλήση της συνάρτησης προβολής παιχνιδιών.
        selected_index = self.listbox.curselection()                        # display_games(games)
        if selected_index:
            selected_name = self.listbox.get(selected_index)
            self.callback(self.directory, selected_name)
            self.root.destroy()
        else:
            messagebox.showwarning("No Selection", "Please select a PGN file.")


# Εκκίνηση της εφαρμογής.
InitialWindow()
