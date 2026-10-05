"""
GESTION PLANNING - Interface claire, plein écran, CustomTkinter
Design : Light mode, tons verts/blancs/gris naturels, style professionnel équestre
"""

import customtkinter as ctk
from tkinter import messagebox, StringVar
import tkinter as tk
from datetime import datetime, timedelta

# ─── Thème global ─────────────────────────────────────────────────────────────
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

C = {
    "bg":           "#F0F4F0",
    "panel":        "#FFFFFF",
    "card":         "#F7FAF7",
    "border":       "#D0DDD0",
    "header_bg":    "#2D6A4F",
    "header_fg":    "#FFFFFF",
    "accent":       "#40916C",
    "accent_h":     "#1B4332",
    "accent2":      "#74C69D",
    "save_bg":      "#1B4332",
    "add_bg":       "#52B788",
    "del_bg":       "#C0392B",
    "abs_bg":       "#E74C3C",
    "corr_bg":      "#E67E22",
    "text":         "#1A2B1A",
    "text_dim":     "#5A7A5A",
    "nav_bg":       "#D8EDD8",
    "sel_cav":      "#2D6A4F",
    "sel_cav_fg":   "#FFFFFF",
    "sel_chv":      "#40916C",
    "sel_chv_fg":   "#FFFFFF",
    "badge_0":      "#E74C3C",
    "badge_1":      "#F39C12",
    "badge_2":      "#27AE60",
    "badge_3":      "#2980B9",
    "sp_red":       "#FADBD8",
    "sp_orange":    "#FDEBD0",
    "sp_gold":      "#FEF9E7",
    "sp_violet":    "#F5EEF8",
    "sp_cyan":      "#EAF4FB",
}

FT  = ("Trebuchet MS", 20, "bold")
FH  = ("Trebuchet MS", 12, "bold")
FL  = ("Segoe UI", 11)
FS  = ("Segoe UI", 10)
FM  = ("Consolas", 10)
FB  = ("Segoe UI Semibold", 11)

CHEVAUX_DATA = [
    ("VIOLETTE",0),("NEVA",0),("BRIOSSO",0),("SURPRISE",1),
    ("PEPITE",0,"red"),("PANDA",0,"orange"),("PONPON",0),("NUAGE",2,"gold"),
    ("HOUSTON",1),("REGLISSE",0),("NAVARA",1),("TONNERRE",0),
    ("GRISETTE",1),("DANETTE",3),("TIC",2),("TAC",0),
    ("SEGOVIA",1,"violet"),("LITTLE",0),("PAOLA",1),("MANGO",0),
    ("SORBET",0),("RASTA",0),("PEGASE",0),("BALKIS",0),
    ("BALI",0),("CARA",0),("SAMOURAI",0),("FLICKA",0),
    ("BANZAI",0),("KID",0),("DIESEL",0),("SHAMIRA",0),
    ("SINAI",0),("ETOILE",0),("VASCO",0),("DOMINO",0),
    ("ESPOIR",0),("JAZZY",0),("ICHIBAI",0),("CHOGUN",0),
    ("ALTAI",0),("WAR",0),("TALIA",0),("TANGO",0),
    ("ICARE",0),("ENZO",0),("FGHFG",0,"cyan"),
]

CAVALIERS = ["MIA","NATHANAELLE","ROSE","ESTELLE","LOU","GRISETTE","ILIADE","LOUISE"]

HISTORIQUE_CAVALIER = [
    ("s-1","mercredi 11-10-2023","PANDA","thème1"),
    ("s-2","mercredi 04-10-2023","PEPITE","thème2"),
    ("s-3","mercredi 27-09-2023","NUAGE","thème3"),
]

PLANNING_PREVIEW = (
    "10H   LENA    RAPHAELLE avec SURPRISE\n"
    "13H30 LENA    NATHANAELLE avec SEGOVIA\n"
    "14H   LENA    LEONIE avec DANETTE | VICTOIRE avec HOUSTON\n"
    "              LEONIE avec NAVARA | LEONIE avec TIC\n"
    "15H   KARINE  HANAE avec NUAGE | CHLOE avec PAOLA\n"
    "15H   LENA    JOY avec TIC\n"
    "17H   LENA    OCEANE avec DANETTE\n"
    "18H   KARINE  GABY avec NUAGE\n"
    "18H   LENA    KYLLIAN avec GRISETTE"
)

SP_COLOR = {"red":"sp_red","orange":"sp_orange","gold":"sp_gold",
            "violet":"sp_violet","cyan":"sp_cyan"}


class GestionPlanning(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Gestion Planning  •  v1.85")
        self.configure(fg_color=C["bg"])
        self.after(0, lambda: self.state("zoomed"))

        self._date      = datetime(2023, 10, 18)
        self._moniteur  = "LENA"
        self._heure     = "13H30"
        self._sel_cav   = StringVar(value="NATHANAELLE")
        self._sel_chv   = StringVar(value="FGHFG")
        self._theme_var = StringVar()
        self._new_name  = StringVar()
        self._new_theme = StringVar()
        self._cav_btns  = {}
        self._chv_btns  = {}

        self._build_ui()


    def _build_ui(self):
        self._build_topbar()
        body = ctk.CTkFrame(self, fg_color=C["bg"])
        body.pack(fill="both", expand=True, padx=8, pady=(0,8))
        body.grid_columnconfigure(0, weight=2, minsize=220)
        body.grid_columnconfigure(1, weight=3, minsize=270)
        body.grid_columnconfigure(2, weight=4)
        body.grid_columnconfigure(3, weight=6)
        body.grid_rowconfigure(0, weight=1)
        self._build_col_cavaliers(body)
        self._build_col_chevaux(body)
        self._build_col_actions(body)
        self._build_col_planning(body)

    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=C["header_bg"], corner_radius=0, height=54)
        bar.pack(fill="x")
        bar.pack_propagate(False)

        ctk.CTkLabel(bar, text="🐴  GESTION PLANNING",
                      font=FT, text_color=C["header_fg"]).pack(side="left", padx=20, pady=10)

        nav = ctk.CTkFrame(bar, fg_color="transparent")
        nav.pack(side="left", padx=24)

        ctk.CTkButton(nav, text="◀", width=30, height=28,
                       fg_color=C["accent2"], text_color=C["header_bg"],
                       hover_color=C["accent"], font=("Segoe UI Semibold",12),
                       corner_radius=7, command=self._prev_day).pack(side="left", padx=2)

        self._date_lbl = ctk.CTkLabel(nav, text=self._fmt_date(),
                                       font=("Trebuchet MS",13,"bold"),
                                       text_color=C["header_fg"], width=230)
        self._date_lbl.pack(side="left", padx=8)

        ctk.CTkButton(nav, text="▶", width=30, height=28,
                       fg_color=C["accent2"], text_color=C["header_bg"],
                       hover_color=C["accent"], font=("Segoe UI Semibold",12),
                       corner_radius=7, command=self._next_day).pack(side="left", padx=2)

        self._slot_lbl = ctk.CTkLabel(nav,
                                       text=f"  •  {self._heure}  {self._moniteur}",
                                       font=("Segoe UI Semibold",12),
                                       text_color=C["accent2"])
        self._slot_lbl.pack(side="left", padx=8)

        ctk.CTkLabel(bar, text="v1.85", font=("Segoe UI",10),
                      text_color=C["accent2"]).pack(side="right", padx=16)
        
        ctk.CTkButton(bar, text="📊", width=30, height=28,
                       fg_color=C["accent2"], text_color=C["header_bg"],
                       hover_color=C["accent"], font=("Segoe UI Semibold",12),
                       corner_radius=7).pack(side="right", padx=2)
        
        ctk.CTkButton(bar, text="⚙️", width=30, height=28,
                       fg_color=C["accent2"], text_color=C["header_bg"],
                       hover_color=C["accent"], font=("Segoe UI Semibold",12),
                       corner_radius=7).pack(side="right", padx=2)

        
        
        ctk.CTkButton(bar, text="Jour", width=60, height=28,
                          fg_color=C["accent2"], text_color=C["header_bg"],
                            hover_color=C["accent"], font=FB, corner_radius=7,
                            command=lambda: messagebox.showinfo("Jour", "Affichage du jour sélectionné !")
                            ).pack(side="right", padx=2)
        
        ctk.CTkButton(bar, text="Nouveau Jour", width=100, height=28,
                          fg_color=C["accent"], text_color="white",
                          hover_color=C["accent_h"], font=FB, corner_radius=7,
                          command=lambda: messagebox.showinfo("Nouveau Jour", "Création d'un nouveau jour !")
                          ).pack(side="right", padx=12)


    # ── Col 0 : Cavaliers ─────────────────────────────────────────────────────
    def _build_col_cavaliers(self, parent):
        col = self._panel(parent, 0)
        self._section_title(col, "👤  Cavaliers")

        scr = ctk.CTkScrollableFrame(col, fg_color=C["card"], corner_radius=8)
        scr.pack(fill="both", expand=True, padx=8, pady=(0,6))

        for name in CAVALIERS:
            is_sel = name == self._sel_cav.get()
            btn = ctk.CTkButton(
                scr, text=name, anchor="w", height=34,
                fg_color=C["sel_cav"] if is_sel else "transparent",
                text_color=C["sel_cav_fg"] if is_sel else C["text"],
                hover_color=C["accent2"], font=FL, corner_radius=7,
                command=lambda n=name: self._select_cav(n)
            )
            btn.pack(fill="x", pady=2, padx=4)
            self._cav_btns[name] = btn

        self._sep(col)
        self._section_title(col, "➕  Ajouter cavalier", small=True)
        ctk.CTkEntry(col, textvariable=self._new_name,
                      placeholder_text="Nouveau nom...",
                      fg_color=C["card"], border_color=C["border"],
                      text_color=C["text"], height=32).pack(fill="x", padx=8, pady=2)
        ctk.CTkButton(col, text="Rattrapage", height=30,
                       fg_color=C["accent"], text_color="white",
                       hover_color=C["accent_h"], font=FB, corner_radius=8,
                       command=self._rattrapage).pack(fill="x", padx=8, pady=(2,6))

        self._sep(col)
        self._section_title(col, "🏷  Ajouter thème", small=True)
        ctk.CTkEntry(col, textvariable=self._new_theme,
                      placeholder_text="Nouveau thème...",
                      fg_color=C["card"], border_color=C["border"],
                      text_color=C["text"], height=32).pack(fill="x", padx=8, pady=2)
        ctk.CTkButton(col, text="Ajouter le thème", height=30,
                       fg_color=C["card"], text_color=C["accent"],
                       border_width=2, border_color=C["accent"],
                       hover_color=C["accent2"], font=FB, corner_radius=8,
                       command=self._add_theme).pack(fill="x", padx=8, pady=(2,10))

    # ── Col 1 : Chevaux ───────────────────────────────────────────────────────
    def _build_col_chevaux(self, parent):
        col = self._panel(parent, 1)
        self._section_title(col, "🐎  Chevaux")

        leg = ctk.CTkFrame(col, fg_color="transparent")
        leg.pack(fill="x", padx=8, pady=(0,4))
        for txt, clr in [("0","badge_0"),("1","badge_1"),("2","badge_2"),("3+","badge_3")]:
            ctk.CTkLabel(leg, text=f" {txt} ", height=18, fg_color=C[clr],
                          corner_radius=5, font=("Segoe UI",8,"bold"),
                          text_color="white").pack(side="left", padx=2)

        scr = ctk.CTkScrollableFrame(col, fg_color=C["card"], corner_radius=8)
        scr.pack(fill="both", expand=True, padx=8, pady=(0,8))
        scr.grid_columnconfigure(0, weight=0, minsize=26)
        scr.grid_columnconfigure(1, weight=1)

        for i, row in enumerate(CHEVAUX_DATA):
            name = row[0]; count = row[1]
            sp   = row[2] if len(row) > 2 else None
            is_sel = name == self._sel_chv.get()
            row_bg = C.get(SP_COLOR.get(sp,""), C["card"]) if not is_sel else C["sel_chv"]
            fg     = C["sel_chv_fg"] if is_sel else C["text"]
            badge_c = C["badge_3"] if count>=3 else C[f"badge_{min(count,2)}"]

            badge = ctk.CTkLabel(scr, text=str(count), width=22, height=20,
                                  fg_color=badge_c, corner_radius=5,
                                  font=("Segoe UI",8,"bold"), text_color="white")
            badge.grid(row=i, column=0, padx=(3,2), pady=1, sticky="w")

            btn = ctk.CTkButton(
                scr, text=name, anchor="w", height=24,
                fg_color=row_bg, text_color=fg,
                hover_color=C["accent2"], font=FS, corner_radius=6,
                command=lambda n=name: self._select_chv(n)
            )
            btn.grid(row=i, column=1, padx=(0,3), pady=1, sticky="ew")
            self._chv_btns[name] = (btn, badge)

    # ── Col 2 : Actions ───────────────────────────────────────────────────────
    def _build_col_actions(self, parent):
        col = self._panel(parent, 2)
        col.grid_rowconfigure(3, weight=1)

        self._section_title(col, "ℹ️  Infos cavalier")

        info_hdr = ctk.CTkFrame(col, fg_color=C["nav_bg"], corner_radius=8)
        info_hdr.pack(fill="x", padx=8, pady=(0,4))
        ctk.CTkButton(info_hdr, text="ABS", width=55, height=28,
                       fg_color=C["abs_bg"], text_color="white",
                       hover_color="#A93226", font=FB, corner_radius=6,
                       command=lambda: messagebox.showinfo("ABS","Marqué absent")
                       ).pack(side="right", padx=6, pady=5)
        ctk.CTkButton(info_hdr, text="Correction", width=80, height=28,
                       fg_color=C["corr_bg"], text_color="white",
                       hover_color="#CA6F1E", font=FB, corner_radius=6
                       ).pack(side="right", padx=2, pady=5)
        ctk.CTkLabel(info_hdr, text="Historique des séances",
                      font=FL, text_color=C["text_dim"]).pack(side="left", padx=10, pady=5)

        for sem, date_str, cheval, theme in HISTORIQUE_CAVALIER:
            rf = ctk.CTkFrame(col, fg_color=C["nav_bg"], corner_radius=7)
            rf.pack(fill="x", padx=8, pady=2)
            ctk.CTkLabel(rf, text=sem, width=34, font=("Segoe UI Semibold",10),
                          text_color=C["accent"]).pack(side="left", padx=6, pady=4)
            ctk.CTkLabel(rf, text=date_str, font=FS,
                          text_color=C["text_dim"]).pack(side="left", padx=4)
            ctk.CTkLabel(rf, text=cheval, font=("Segoe UI Semibold",10),
                          text_color=C["header_bg"]).pack(side="left", padx=4)
            ctk.CTkLabel(rf, text=theme, font=FS,
                          text_color=C["text_dim"]).pack(side="left", padx=4)

        self._sep(col)
        self._section_title(col, "⏱  Heure de travail", small=True)
        self._hw_text = ctk.CTkTextbox(col, fg_color=C["card"], text_color=C["text"],
                                        font=FM, height=65, border_width=1,
                                        border_color=C["border"])
        self._hw_text.pack(fill="x", padx=8, pady=(0,4))

        seq = ctk.CTkFrame(col, fg_color=C["header_bg"], corner_radius=9)
        seq.pack(fill="x", padx=8, pady=4)
        self._seq_lbl = ctk.CTkLabel(
            seq,
            text=f"  {{{self._heure} {self._moniteur}}}   "
                 f"{self._sel_chv.get()}   {self._sel_cav.get()}",
            font=("Trebuchet MS", 12, "bold"), text_color="white"
        )
        self._seq_lbl.pack(pady=7, anchor="w", padx=10)

        self._sep(col)
        self._section_title(col, "🏷  Thème de la séance", small=True)
        ctk.CTkEntry(col, textvariable=self._theme_var,
                      placeholder_text="ex: thème1",
                      fg_color=C["card"], border_color=C["border"],
                      text_color=C["text"], height=32).pack(fill="x", padx=8, pady=(0,6))

        self._sep(col)
        act = ctk.CTkFrame(col, fg_color="transparent")
        act.pack(fill="x", padx=8, pady=4)
        act.grid_columnconfigure(0, weight=1)
        act.grid_columnconfigure(1, weight=1)
        ctk.CTkButton(act, text="＋  Ajouter", height=40,
                       fg_color=C["add_bg"], text_color="white",
                       hover_color=C["accent_h"], font=FB, corner_radius=10,
                       command=self._ajouter).grid(row=0, column=0, sticky="ew", padx=(0,4))
        ctk.CTkButton(act, text="✕  Supprimer", height=40,
                       fg_color=C["del_bg"], text_color="white",
                       hover_color="#922B21", font=FB, corner_radius=10,
                       command=self._supprimer).grid(row=0, column=1, sticky="ew", padx=(4,0))

        ctk.CTkButton(col, text="💾   ENREGISTRER", height=48,
                       fg_color=C["save_bg"], text_color="white",
                       hover_color="#0D2B1C",
                       font=("Trebuchet MS", 14, "bold"), corner_radius=10,
                       command=self._enregistrer).pack(fill="x", padx=8, pady=(6,10))

    # ── Col 3 : Historique + Planning ─────────────────────────────────────────
    def _build_col_planning(self, parent):
        col = self._panel(parent, 3)
        col.grid_rowconfigure(0, weight=1)
        col.grid_rowconfigure(1, weight=2)
        
        
        
        self.tabview = ctk.CTkTabview(col, fg_color="white")
        self.tabview.pack(padx=15, pady=15, fill="both", expand=True)
        self.tabview.add("Prévisualisation")
        self.tabview.add("Historique")

        # Zone de texte
        self.preview_text = ctk.CTkTextbox(self.tabview.tab("Prévisualisation"), font=("Consolas", 12), border_width=1)
        self.preview_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.preview_text.insert("0.0", "Planning du Mercredi :\n\n13H30 LENA : NATHANAELLE avec SEGOVIA\n14H00 LENA : LEONIE avec NAVARA")
        
        self.preview_hist = ctk.CTkScrollableFrame(self.tabview.tab("Historique"), fg_color=C["card"], corner_radius=8)
        self.preview_hist.pack(fill="both", expand=True, padx=5, pady=5)
        # self.preview_hist.insert("0.0", "Planning du Mercredi :\n\n13H30 LENA : NATHANAELLE avec SEGOVIA\n14H00 LENA : LEONIE avec NAVARA")
        for i in range(5):
            btn = ctk.CTkButton(
                self.preview_hist, text="ajout 13h30 LENA : NATHANAELLE avec SEGOVIA", anchor="w", height=24,
                fg_color=C["card"], text_color=C["text"])
            btn.pack(fill="x", pady=2, padx=4)
        
        
    # ─── UI helpers ───────────────────────────────────────────────────────────
    def _panel(self, parent, col):
        f = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        f.grid(row=0, column=col, sticky="nsew",
               padx=(0 if col==0 else 4, 4 if col<3 else 0), pady=0)
        f.grid_columnconfigure(0, weight=1)
        return f

    def _section_title(self, parent, text, small=False):
        font  = ("Segoe UI Semibold",10) if small else FH
        color = C["text_dim"] if small else C["header_bg"]
        ctk.CTkLabel(parent, text=text, font=font,
                      text_color=color).pack(anchor="w", padx=10, pady=(8,3))

    def _sep(self, parent):
        ctk.CTkFrame(parent, fg_color=C["border"], height=1,
                      corner_radius=0).pack(fill="x", padx=8, pady=4)

    # ─── Logique ──────────────────────────────────────────────────────────────
    def _fmt_date(self):
        j = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
        return f"{j[self._date.weekday()]}  {self._date.strftime('%d-%m-%Y')}"

    def _prev_day(self):
        self._date -= timedelta(days=1)
        self._date_lbl.configure(text=self._fmt_date())

    def _next_day(self):
        self._date += timedelta(days=1)
        self._date_lbl.configure(text=self._fmt_date())

    def _select_cav(self, name):
        old = self._sel_cav.get()
        self._sel_cav.set(name)
        if old in self._cav_btns:
            self._cav_btns[old].configure(fg_color="transparent", text_color=C["text"])
        self._cav_btns[name].configure(fg_color=C["sel_cav"], text_color=C["sel_cav_fg"])
        self._refresh_seq()

    def _select_chv(self, name):
        old = self._sel_chv.get()
        self._sel_chv.set(name)
        if old in self._chv_btns:
            btn, _ = self._chv_btns[old]
            btn.configure(fg_color=C["card"], text_color=C["text"])
        btn, _ = self._chv_btns[name]
        btn.configure(fg_color=C["sel_chv"], text_color=C["sel_chv_fg"])
        self._refresh_seq()

    def _refresh_seq(self):
        self._seq_lbl.configure(
            text=f"  {{{self._heure} {self._moniteur}}}   "
                 f"{self._sel_chv.get()}   {self._sel_cav.get()}"
        )

    def _rattrapage(self):
        name = self._new_name.get().strip()
        if name:
            messagebox.showinfo("Rattrapage", f"Rattrapage ajouté pour : {name}")
        else:
            messagebox.showwarning("Attention", "Saisir un nom de cavalier.")

    def _add_theme(self):
        t = self._new_theme.get().strip()
        if t:
            messagebox.showinfo("Thème", f"Thème ajouté : {t}")
        else:
            messagebox.showwarning("Attention", "Saisir un thème.")

    def _ajouter(self):
        cav = self._sel_cav.get(); chv = self._sel_chv.get()
        theme = self._theme_var.get()
        if cav and chv:
            line = f"{self._heure} {self._moniteur} : {cav} avec {chv}"
            if theme:
                line += f"  ({theme})"
            self._preview_box.configure(state="normal")
            self._preview_box.insert("end", "\n" + line)
            self._preview_box.configure(state="disabled")

    def _supprimer(self):
        messagebox.showinfo("Supprimer", "Dernière entrée supprimée.")

    def _enregistrer(self):
        messagebox.showinfo("Enregistré ✓", "Planning enregistré avec succès.")


if __name__ == "__main__":
    try:
        import customtkinter
    except ImportError:
        raise ImportError("Installez customtkinter : pip install customtkinter")
    app = GestionPlanning()
    app.mainloop()