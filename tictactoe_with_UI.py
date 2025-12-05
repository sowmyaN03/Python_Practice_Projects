import tkinter as tk
from tkinter import messagebox


class TicTacToeApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#d7ecff")

        self.current_player = "X"
        self.board = [" "] * 9
        self.game_active = True
        self.cells: list[dict] = []

        self.primary_bg = "#d7ecff"  # light blue
        self.accent_bg = "#c8b5ff"  # soft violet
        self.accent_fg = "#2d1e5f"
        self.border_color = "#9f8add"
        self.x_color = "#4da3ff"  # blue for X
        self.o_color = "#b07bff"  # purple for O
        self.cell_size = 90
        self.corner_radius = 20

        self.status_label = tk.Label(
            self.root,
            text="Player X's turn",
            font=("Arial", 14, "bold"),
            bg=self.primary_bg,
            fg=self.accent_fg,
        )
        self.status_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))

        self.create_board()

        reset_button = tk.Button(
            self.root,
            text="Reset",
            font=("Arial", 12, "bold"),
            width=12,
            bg=self.accent_bg,
            fg=self.accent_fg,
            activebackground=self.border_color,
            activeforeground="white",
            relief="raised",
            command=self.reset_game,
        )
        reset_button.grid(row=5, column=0, columnspan=3, pady=(5, 10))

    def create_board(self) -> None:
        """Create the 3x3 grid of rounded cells."""
        for i in range(9):
            canvas = tk.Canvas(
                self.root,
                width=self.cell_size,
                height=self.cell_size,
                bg=self.primary_bg,
                highlightthickness=0,
            )
            rect_id = self.draw_rounded_rect(
                canvas,
                5,
                5,
                self.cell_size - 5,
                self.cell_size - 5,
                self.corner_radius,
                fill=self.accent_bg,
                outline=self.border_color,
                width=2,
            )
            text_id = canvas.create_text(
                self.cell_size // 2,
                self.cell_size // 2,
                text="",
                font=("Arial", 28, "bold"),
                fill=self.accent_fg,
            )

            row = 1 + i // 3
            col = i % 3
            canvas.grid(row=row, column=col, padx=5, pady=5)
            canvas.bind("<Button-1>", lambda event, idx=i: self.handle_click(idx))

            self.cells.append({"canvas": canvas, "rect": rect_id, "text": text_id})

    def draw_rounded_rect(
        self,
        canvas: tk.Canvas,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        radius: int,
        **kwargs,
    ) -> int:
        """Draw a rounded rectangle on the given canvas and return its id."""
        points = [
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)

    def handle_click(self, index: int) -> None:
        """Handle a player's move when a button is clicked."""
        if not self.game_active:
            return

        if self.board[index] != " ":
            return  # ignore clicks on filled cells

        self.board[index] = self.current_player
        cell = self.cells[index]
        canvas = cell["canvas"]
        rect_id = cell["rect"]
        text_id = cell["text"]

        fill_color = self.x_color if self.current_player == "X" else self.o_color
        canvas.itemconfig(rect_id, fill=fill_color)
        canvas.itemconfig(text_id, text=self.current_player, fill="white")

        if self.check_winner(self.current_player):
            self.status_label.config(text=f"Player {self.current_player} wins!")
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.disable_board()
            return

        if self.is_board_full():
            self.status_label.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_board()
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player: str) -> bool:
        """Return True if the given player has won."""
        winning_combos = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        return any(
            self.board[a] == self.board[b] == self.board[c] == player
            for a, b, c in winning_combos
        )

    def is_board_full(self) -> bool:
        """Return True if there are no empty spaces left on the board."""
        return all(cell != " " for cell in self.board)

    def disable_board(self) -> None:
        """Disable all buttons so no more moves can be made."""
        self.game_active = False

    def reset_game(self) -> None:
        """Reset the game to the initial state."""
        self.current_player = "X"
        self.board = [" "] * 9
        self.game_active = True
        for cell in self.cells:
            canvas = cell["canvas"]
            rect_id = cell["rect"]
            text_id = cell["text"]
            canvas.itemconfig(rect_id, fill=self.accent_bg)
            canvas.itemconfig(text_id, text="", fill=self.accent_fg)
        self.status_label.config(text="Player X's turn")


def main() -> None:
    root = tk.Tk()
    TicTacToeApp(root)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()


