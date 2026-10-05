import customtkinter as ctk

# ================= PALETTE =================
COLORS = {
    "bg": "#F2E9E4",
    "card": "#FFFFFF",
    "primary": "#2E4F3E",
    "secondary": "#8abd45",
    "info": "#95CDD3",
    "warning": "#E8A87C",
    "danger": "#D9534F",
    "success": "#8FD694",
    "text": "#1E1E1E"
}


class MockController:
    pass


class MainView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=COLORS["bg"])

        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        # GRID
        self.grid_columnconfigure(0, weight=1)  # élèves
        self.grid_columnconfigure(1, weight=1)  # chevaux
        self.grid_columnconfigure(2, weight=2)  # planning

        self.grid_rowconfigure(0, weight=0)  # header (fixe)
        self.grid_rowconfigure(1, weight=2)  
        self.grid_rowconfigure(2, weight=1)  
        self.grid_rowconfigure(3, weight=5)  


        self.create_header()
        self.create_main()
        self.create_footer()

    # ================= HEADER =================
    def create_header(self):
        header = ctk.CTkFrame(self, fg_color=COLORS["primary"], corner_radius=20)
        header.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 5))


        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header,
            text="🐎 Planning Écurie",
            font=("Arial", 18, "bold"),
            text_color="white"
        ).grid(row=0, column=0, padx=20, pady=10, sticky="w")

    # ================= MAIN =================
    def create_main(self):
        self.create_students()
        self.create_horses()
        self.create_planning()

    # ================= ÉLÈVES =================
    def create_students(self):
        frame = self.create_card("Élèves", 1, 0,rowspan=2)

        time_frame = ctk.CTkFrame(frame, fg_color="transparent")
        time_frame.pack(fill="x", padx=10, pady=(0, 10))

        ctk.CTkButton(
            time_frame,
            text="⬅️",
            width=40,
            fg_color=COLORS["secondary"]
        ).pack(side="left", padx=5)

        self.current_time_label = ctk.CTkLabel(
            time_frame,
            text="14h",
            font=("Arial", 14, "bold")
        )
        self.current_time_label.pack(side="left", expand=True)

        ctk.CTkButton(
            time_frame,
            text="➡️",
            width=40,
            fg_color=COLORS["secondary"]
        ).pack(side="right", padx=5)

        # LISTE
        scroll = ctk.CTkScrollableFrame(frame, fg_color="transparent")
        scroll.pack(fill="both", expand=True)

        for i in range(10):
            item = ctk.CTkFrame(
                scroll,
                fg_color=COLORS["info"],
                corner_radius=12
            )
            item.pack(fill="x", pady=2)

            ctk.CTkLabel(
                item,
                text=f"Élève {i+1}",
                font=("Arial", 13, "bold"),
                text_color="black"
            ).pack(side="left", padx=(10, 5), pady = 2)

            ctk.CTkLabel(
                item,
                text="trestrestreslongnom de cheval.com c'est ici on verra bien • Bella • Jazz",
                font=("Arial", 10),
                text_color="black"
            ).pack(side="right", padx=10)
        
        # AJOUT ÉLÈVE EN BAS
        bottom_frame = ctk.CTkFrame(frame, fg_color="transparent")
        bottom_frame.pack(fill="x", padx=10, pady=1)

        self.entry_student = ctk.CTkEntry(
            bottom_frame,
            placeholder_text="Ajouter élève ponctuel..."
        )
        self.entry_student.pack(side="left", fill="x", expand=True, padx=(0, 5))

        ctk.CTkButton(
            bottom_frame,
            text="Ajouter",
            fg_color=COLORS["secondary"]
        ).pack(side="right")
        
        theme_frame = ctk.CTkFrame(frame, fg_color="transparent")
        theme_frame.pack(fill="x", padx=10, pady=1)

        self.theme_entry = ctk.CTkEntry(
            theme_frame,
            placeholder_text="Modifier le thème..."
        )
        self.theme_entry.pack(side="left", fill="x", expand=True, padx=(0, 5),pady=(0,10))

        ctk.CTkButton(
            theme_frame,
            text="Définir",
            fg_color=COLORS["secondary"],
            # command=self.update_theme
        ).pack(side="right", pady=(0,10))



        # ================= NOUVELLE CARTE ACTIONS =================
        actions_card = ctk.CTkFrame(
            self,
            fg_color=COLORS["card"],
            corner_radius=15
        )

        actions_card.grid(
            row=1, column=2,
            sticky="nsew",
            padx=10, pady=5
        )

        ctk.CTkLabel(
            actions_card,
            text="Sélection",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 2))

        info_frame = ctk.CTkFrame(actions_card, fg_color="transparent")
        info_frame.pack(fill="x", padx=10, pady=(5, 2))

        self.selected_time = ctk.CTkLabel(
            info_frame,
            text="14h",
            font=("Arial", 14, "bold")
        )
        self.selected_time.pack(side="left", padx=5)

        self.selected_student = ctk.CTkLabel(
            info_frame,
            text="Emma",
            font=("Arial", 14, "bold")
        )
        self.selected_student.pack(side="left", padx=20)

        self.selected_horse = ctk.CTkLabel(
            info_frame,
            text="Bella",
            font=("Arial", 14, "bold")
        )
        self.selected_horse.pack(side="left", padx=20)

        # Boutons
        btn_frame = ctk.CTkFrame(actions_card, fg_color="transparent")
        btn_frame.pack(fill="x", pady=2)

        for text in ["➕ Ajouter", "❌ Supprimer", "💾 Enregistrer"]:
            ctk.CTkButton(
                btn_frame,
                text=text,
                fg_color=COLORS["primary"]
            ).pack(side="left", padx=5)

        # Utilisation cheval
        ctk.CTkLabel(
            actions_card,
            text="Utilisation du cheval",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 5))

        for i in range(4):
            ctk.CTkLabel(
                actions_card,
                text=f"{14+i}h → Élève {i+1}"
            ).pack(anchor="w", padx=10)

        # Actions
        action_btn_frame = ctk.CTkFrame(actions_card, fg_color="transparent")
        action_btn_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(
            action_btn_frame,
            text="⚠️ Absent (last)",
            fg_color=COLORS["warning"],
            width=120
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            action_btn_frame,
            text="✏️ Correction",
            fg_color=COLORS["secondary"],
            width=120
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            action_btn_frame,
            text="🚫 Absent (this)",
            fg_color=COLORS["danger"],
            width=120
        ).pack(side="left", padx=5)




    # ================= CHEVAUX =================
    def create_horses(self):
        frame = self.create_card("Chevaux", 1, 1, rowspan=3)

        scroll = ctk.CTkScrollableFrame(frame, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=10, pady=(0,5) )

        for i in range(30):
            count = i % 5

            if count == 4:
                color = COLORS["danger"]
            elif count == 3:
                color = COLORS["warning"]
            else:
                color = COLORS["success"]

            item = ctk.CTkFrame(scroll, fg_color=color, corner_radius=20)
            item.pack(fill="x", pady=0)

            ctk.CTkLabel(item, text=f"Cheval {i+1}", text_color="black")\
                .pack(side="left", padx=10, pady=1)

            ctk.CTkLabel(item, text=f"{count}/4", text_color="black")\
                .pack(side="right", padx=10)

    # ================= PLANNING =================
    def create_planning(self):
        frame = self.create_card("Planning", 2, 2, rowspan=2)

        scroll = ctk.CTkScrollableFrame(frame, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=5, pady=5)

        hours = ["14h", "15h", "16h", "17h", "18h"]

        for h in hours:
            row = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=12)
            row.pack(fill="x", pady=3)

            ctk.CTkLabel(row, text=h, width=60).pack(side="left", padx=10)
            ctk.CTkLabel(row, text="Emma", width=120).pack(side="left")
            ctk.CTkLabel(row, text="Bella", width=120).pack(side="left")
            ctk.CTkLabel(row, text="Thème", width=120).pack(side="left")

            ctk.CTkButton(
                row,
                text="Modifier",
                fg_color=COLORS["primary"],
                width=80
            ).pack(side="right", padx=10)



    # ================= HISTORIQUE =================
    def create_footer(self):
        frame = ctk.CTkFrame(self, fg_color=COLORS["card"], corner_radius=20)
        frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)


        ctk.CTkLabel(
            frame,
            text="Historique",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=15, pady=(10, 0))

        box = ctk.CTkTextbox(frame, height=80)
        box.pack(fill="both", expand=True, padx=15, pady=10)

        box.insert("end", "Emma → Bella (14h)\nLeo → Jazz (15h)\n")

    # ================= CARD =================
    def create_card(self, title, row, col, rowspan=1):
        frame = ctk.CTkFrame(
            self,
            fg_color=COLORS["card"],
            corner_radius=20
        )
        frame.grid(row=row, column=col, rowspan=rowspan, sticky="nsew", padx=5, pady=5)

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Arial", 16, "bold")
        ).pack(anchor="w", padx=15, pady=10)

        return frame


# ================= MAIN ================= 
if __name__ == "__main__":
    ctk.set_appearance_mode("light") 
    root = ctk.CTk() 
    root.title("Planning Écurie") 
    root.geometry("1300x750") 
    root.configure(fg_color=COLORS["bg"]) 
    app = MainView(root, MockController()) 
    root.mainloop()



