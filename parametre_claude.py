"""
ECURIE MANAGER - Gestion des paramètres de l'école équestre
Design : Light mode, tons verts/blancs/gris — cohérent avec GestionPlanning
Listes remplacées par CTkScrollableFrame + boutons (sélection visuelle)
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os
from datetime import datetime

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
    "text":         "#1A2B1A",
    "text_dim":     "#5A7A5A",
    "nav_bg":       "#D8EDD8",
    "sel_bg":       "#2D6A4F",   # bouton sélectionné
    "sel_fg":       "#FFFFFF",
}

FT  = ("Trebuchet MS", 20, "bold")
FH  = ("Trebuchet MS", 12, "bold")
FL  = ("Segoe UI", 11)
FS  = ("Segoe UI", 10)
FM  = ("Consolas", 10)
FB  = ("Segoe UI Semibold", 11)
FSM = ("Segoe UI", 9)


# ─── Helpers UI ───────────────────────────────────────────────────────────────

def _btn(parent, text, command=None, fg=None, hover=None,
         width=160, height=34, font=None):
    return ctk.CTkButton(
        parent, text=text, command=command,
        fg_color=fg or C["add_bg"], hover_color=hover or C["accent_h"],
        text_color="white", font=font or FB,
        corner_radius=8, width=width, height=height,
    )

def _btn_del(parent, text, command=None, width=160, height=34):
    return _btn(parent, text, command, fg=C["del_bg"], hover="#922B21",
                width=width, height=height)

def _section_title(parent, text, small=False):
    font  = ("Segoe UI Semibold", 10) if small else FH
    color = C["text_dim"] if small else C["header_bg"]
    ctk.CTkLabel(parent, text=text, font=font,
                 text_color=color).pack(anchor="w", padx=10, pady=(8, 3))

def _sep(parent):
    ctk.CTkFrame(parent, fg_color=C["border"], height=1,
                 corner_radius=0).pack(fill="x", padx=8, pady=4)

def _panel(parent, col):
    padx_l = 0 if col == 0 else 4
    padx_r = 0 if col == 2 else 4
    f = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=12,
                     border_width=1, border_color=C["border"])
    f.grid(row=0, column=col, sticky="nsew",
           padx=(padx_l, padx_r), pady=0)
    f.grid_columnconfigure(0, weight=1)
    return f

def _entry(parent, placeholder="", width=200, textvariable=None):
    kw = dict(textvariable=textvariable) if textvariable else {}
    return ctk.CTkEntry(
        parent, placeholder_text=placeholder,
        fg_color=C["card"], border_color=C["border"],
        text_color=C["text"], placeholder_text_color=C["text_dim"],
        font=FL, corner_radius=6, width=width, **kw,
    )


# ─── Widget liste à boutons ────────────────────────────────────────────────────

class ButtonList:
    """
    CTkScrollableFrame rempli de CTkButton.
    Gère la sélection unique avec highlight vert foncé.
    API publique :
        .frame        → le CTkScrollableFrame à placer dans le layout
        .set(items)   → recharge la liste
        .selected()   → renvoie le texte de l'item sélectionné ou None
        .selected_index() → renvoie l'index ou None
    """

    def __init__(self, parent, on_select=None, item_height=30):
        self._on_select  = on_select
        self._item_height = item_height
        self._buttons: list[ctk.CTkButton] = []
        self._sel_idx: int | None = None

        self.frame = ctk.CTkScrollableFrame(
            parent,
            fg_color=C["card"],
            corner_radius=8,
            border_width=1,
            border_color=C["border"],
            scrollbar_button_color=C["accent"],
            scrollbar_button_hover_color=C["accent_h"],
        )

    def set(self, items: list[str]):
        """Vide et recharge tous les boutons."""
        for btn in self._buttons:
            btn.destroy()
        self._buttons.clear()
        self._sel_idx = None

        for i, label in enumerate(items):
            btn = ctk.CTkButton(
                self.frame,
                text=label,
                anchor="w",
                height=self._item_height,
                fg_color="transparent",
                text_color=C["text"],
                hover_color=C["accent2"],
                font=FL,
                corner_radius=6,
                command=lambda idx=i: self._select(idx),
            )
            btn.pack(fill="x",  padx=4)
            self._buttons.append(btn)

    def _select(self, idx: int):
        # Désélectionner l'ancien
        if self._sel_idx is not None and self._sel_idx < len(self._buttons):
            self._buttons[self._sel_idx].configure(
                fg_color="transparent", text_color=C["text"]
            )
        # Sélectionner le nouveau
        self._sel_idx = idx
        self._buttons[idx].configure(
            fg_color=C["sel_bg"], text_color=C["sel_fg"]
        )
        if self._on_select:
            self._on_select(self._buttons[idx].cget("text"))

    def selected(self) -> str | None:
        if self._sel_idx is not None and self._sel_idx < len(self._buttons):
            return self._buttons[self._sel_idx].cget("text")
        return None

    def selected_index(self) -> int | None:
        return self._sel_idx


# ─── Application principale ───────────────────────────────────────────────────

class EcurieManager(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Écurie Manager  •  Paramètres  •  v2.0")
        self.configure(fg_color=C["bg"])
        self.after(0, lambda: self.state("zoomed"))

        # ── Données ──
        self.jours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
        self.jour_var = tk.StringVar(value="Mercredi")

        self.moniteurs_data: list[tuple[str, str]] = [
            ("admin", "aloykyllian31@gmail.com"),
            ("Lena",  "delmaslena@gmail.com"),
            ("Manon", "delmasmanon@gmail.com"),
        ]
        self.user_var = tk.StringVar(value="admin")

        self.chevaux: list[str] = [
            "VIOLETTE","NEVA","BRIOSSO","SURPRISE","PEPITE","PANDA",
            "PONPON","NUAGE","HOUSTON","REGLISSE","NAVARA","P. TONNERRE",
            "GRISETTE","DANETTE","TIC","TAC","SEGOVIA","LITTLE","PAOLA",
            "MANGO","SORBET","RASTA","PEGASE","BALKIS","BALI","CARA",
            "SAMOURAI","FLICKA","BANZAI","KID","DIESEL","SHAMIRA","SINAI",
            "ETOILE","VASCO","DOMINO","ESPOIR","JAZZY","ICHIBAI","CHOGUN",
            "ALTAI","WAR","TALIA","TANGO","ICARE",
        ]
        self.heures: list[str] = [
            "9H LENA","10H LENA","13H30 LENA","14H LENA","15H LENA",
            "15H MANON","16H LENA","17H LENA","17H MANON","18H LENA",
            "18H MANON","19H LENA",
        ]
        self.eleves: list[str] = [
            "LOLA","VICTOIRE","LILA","LEONIE","JULIA","NOA","LAURA","ELENA",
        ]
        self.log_lines: list[str] = [
            "KYLLIAN/-1","TARA/6",r"\heure/9H LENA","RAPHAELLE/-1",
            "MAELLE/-1","MAEVA/-1","JULLIA/-1","HUGO/-1","JOHAN/-1",
            "XCBNXC/3",r"\heure/10H LENA","MIA/-1","NATHANAELLE/-1",
            "ROSE/-1","ESTELLE/-1","LOU/-1","ILIADE/-1","LOUISE/-1",
            r"\heure/13H30 LENA","LOLA/-1","VICTOIRE/-1","LILA/-1",
            "LEONIE/-1","JULIA/-1",
        ]

        self._build_ui()
        self._refresh_all()

    # ─────────────────────────── BUILD ────────────────────────────────────────

    def _build_ui(self):
        self._build_topbar()

        body = ctk.CTkFrame(self, fg_color=C["bg"])
        body.pack(fill="both", expand=True, padx=8, pady=(6, 8))
        body.grid_columnconfigure(0, weight=2, minsize=210)
        body.grid_columnconfigure(1, weight=2, minsize=210)
        body.grid_columnconfigure(2, weight=5, minsize=440)
        body.grid_rowconfigure(0, weight=1)

        self._build_col_chevaux(body)
        self._build_col_heures(body)
        self._build_col_right(body)

        self._build_footer()

    # ── Topbar ────────────────────────────────────────────────────────────────

    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=C["header_bg"], corner_radius=0, height=54)
        bar.pack(fill="x")
        bar.pack_propagate(False)

        ctk.CTkLabel(bar, text="🐴  ÉCURIE MANAGER — Paramètres",
                     font=FT, text_color=C["header_fg"]).pack(side="left", padx=20, pady=10)

        ctk.CTkFrame(bar, width=2, fg_color=C["accent2"],
                     corner_radius=0).pack(side="left", fill="y", pady=8)

        ctk.CTkLabel(bar, text="  Jour :", font=FL,
                     text_color=C["accent2"]).pack(side="left", padx=(10, 4))
        ctk.CTkComboBox(
            bar, values=self.jours, variable=self.jour_var, width=130,
            font=FL, fg_color=C["accent_h"], border_color=C["accent2"],
            button_color=C["accent"], dropdown_fg_color=C["accent_h"],
            text_color="white",
        ).pack(side="left", padx=(0, 12))

        ctk.CTkLabel(bar, text="Utilisateur :", font=FL,
                     text_color=C["accent2"]).pack(side="left", padx=(0, 4))
        self._user_cb = ctk.CTkComboBox(
            bar,
            values=[m[0] for m in self.moniteurs_data],
            variable=self.user_var, width=130,
            font=FL, fg_color=C["accent_h"], border_color=C["accent2"],
            button_color=C["accent"], dropdown_fg_color=C["accent_h"],
            text_color="white",
        )
        self._user_cb.pack(side="left", padx=(0, 16))

        # Boutons droite
        ctk.CTkLabel(bar, text="v2.0", font=FSM,
                     text_color=C["accent2"]).pack(side="right", padx=16)

        for lbl, cmd in [
            ("📊 Excel réf.", self._ouvrir_excel),
            ("📤 Exporter",   self._exporter),
            ("📥 Importer",   self._importer),
        ]:
            ctk.CTkButton(
                bar, text=lbl, command=cmd,
                width=110, height=28,
                fg_color=C["accent2"], text_color=C["header_bg"],
                hover_color=C["accent"], font=FB, corner_radius=7,
            ).pack(side="right", padx=4)

        ctk.CTkButton(
            bar, text="💾  ENREGISTRER", command=self._enregistrer,
            width=160, height=36,
            fg_color=C["save_bg"], hover_color="#0D2B1C",
            text_color="white", font=("Trebuchet MS", 13, "bold"), corner_radius=8,
        ).pack(side="right", padx=(12, 6))

    # ── Colonne Chevaux ───────────────────────────────────────────────────────

    def _build_col_chevaux(self, parent):
        col = _panel(parent, 0)

        _section_title(col, "🐎  Chevaux")

        self.bl_chevaux = ButtonList(col)
        self.bl_chevaux.frame.pack(fill="both", expand=True, padx=8, pady=(0, 4))

        _sep(col)
        _section_title(col, "Ajouter / Supprimer", small=True)

        self.entry_cheval = _entry(col, "Nom du cheval…")
        self.entry_cheval.pack(fill="x", padx=8, pady=(0, 4))
        _btn(col, "➕  Ajouter cheval", self._ajouter_cheval).pack(fill="x", padx=8, pady=2)
        _btn_del(col, "🗑  Supprimer cheval", self._supprimer_cheval).pack(fill="x", padx=8, pady=(2, 12))

    # ── Colonne Heures ────────────────────────────────────────────────────────

    def _build_col_heures(self, parent):
        col = _panel(parent, 1)

        _section_title(col, "🕐  Cours / Heures")

        self.bl_heures = ButtonList(col)
        self.bl_heures.frame.pack(fill="both", expand=True, padx=8, pady=(0, 4))

        _sep(col)
        _section_title(col, "Créer / Supprimer", small=True)

        self.entry_heure = _entry(col, "Ex: 14H LENA…")
        self.entry_heure.pack(fill="x", padx=8, pady=(0, 4))
        _btn(col, "➕  Créer heure", self._creer_heure).pack(fill="x", padx=8, pady=2)
        _btn_del(col, "🗑  Supprimer heure", self._supprimer_heure).pack(fill="x", padx=8, pady=(2, 12))

    # ── Colonne droite ────────────────────────────────────────────────────────

    def _build_col_right(self, parent):
        col = _panel(parent, 2)

        # ─ Rangée Élèves + Moniteurs côte à côte ─
        row_top = ctk.CTkFrame(col, fg_color="transparent")
        row_top.pack(fill="x", padx=8, pady=(4, 0))
        row_top.grid_columnconfigure(0, weight=1)
        row_top.grid_columnconfigure(1, weight=1)

        # ── Sous-panel Élèves ──
        pnl_e = ctk.CTkFrame(row_top, fg_color=C["card"], corner_radius=10,
                              border_width=1, border_color=C["border"])
        pnl_e.grid(row=0, column=0, sticky="nsew", padx=(0, 4))

        _section_title(pnl_e, "👩‍🎓  Élèves")

        self.bl_eleves = ButtonList(pnl_e)
        self.bl_eleves.frame.pack(fill="both", expand=True, padx=6, pady=(0, 4))
        self.bl_eleves.frame.configure(height=200)

        # Champ + boutons élèves
        self.entry_eleve = _entry(pnl_e, "Nom de l'élève…")
        self.entry_eleve.pack(fill="x", padx=6, pady=(0, 4))
        row_be = ctk.CTkFrame(pnl_e, fg_color="transparent")
        row_be.pack(fill="x", padx=6, pady=(0, 4))
        _btn(row_be, "➕ Créer", self._creer_eleve, width=100, height=30).pack(side="left", padx=(0, 4))
        _btn_del(row_be, "🗑 Suppr.", self._supprimer_eleve, width=90, height=30).pack(side="left")

        # Option carte
        opts_e = ctk.CTkFrame(pnl_e, fg_color=C["nav_bg"], corner_radius=8)
        opts_e.pack(fill="x", padx=6, pady=(0, 8))
        self.cb_carte = ctk.CTkCheckBox(
            opts_e, text="À la carte",
            font=FS, text_color=C["text"],
            fg_color=C["accent"], hover_color=C["accent_h"],
            checkmark_color="white",
        )
        self.cb_carte.pack(side="left", padx=8, pady=5)
        self.entry_seances = _entry(opts_e, "Nb séances", width=90)
        self.entry_seances.pack(side="right", padx=8, pady=5)

        # ── Sous-panel Moniteurs ──
        pnl_m = ctk.CTkFrame(row_top, fg_color=C["card"], corner_radius=10,
                              border_width=1, border_color=C["border"])
        pnl_m.grid(row=0, column=1, sticky="nsew", padx=(4, 0))

        _section_title(pnl_m, "👨‍🏫  Moniteurs")

        self.bl_moniteurs = ButtonList(pnl_m, item_height=32)
        self.bl_moniteurs.frame.pack(fill="both", expand=True, padx=6, pady=(0, 4))
        self.bl_moniteurs.frame.configure(height=200)

        # Champs + boutons moniteurs
        row_nom = ctk.CTkFrame(pnl_m, fg_color="transparent")
        row_nom.pack(fill="x", padx=6, pady=(0, 3))
        ctk.CTkLabel(row_nom, text="Nom :", font=FS,
                     text_color=C["text_dim"], width=46).pack(side="left")
        self.entry_moniteur = _entry(row_nom, "Moniteur…")
        self.entry_moniteur.pack(side="left", fill="x", expand=True, padx=(4, 0))

        row_mail = ctk.CTkFrame(pnl_m, fg_color="transparent")
        row_mail.pack(fill="x", padx=6, pady=(0, 4))
        ctk.CTkLabel(row_mail, text="Mail :", font=FS,
                     text_color=C["text_dim"], width=46).pack(side="left")
        self.entry_mail = _entry(row_mail, "email@…")
        self.entry_mail.pack(side="left", fill="x", expand=True, padx=(4, 0))

        row_bm = ctk.CTkFrame(pnl_m, fg_color="transparent")
        row_bm.pack(fill="x", padx=6, pady=(0, 8))
        _btn(row_bm, "➕ Ajouter", self._ajouter_moniteur, width=110, height=30).pack(side="left", padx=(0, 4))
        _btn_del(row_bm, "🗑 Suppr.", self._supprimer_moniteur, width=90, height=30).pack(side="left")

        _sep(col)

        # ─ Journal ─
        _section_title(col, "📋  Journal d'activité (fichier référence)")

        log_outer = ctk.CTkFrame(col, fg_color=C["card"],
                                  corner_radius=8, border_width=1,
                                  border_color=C["border"])
        log_outer.pack(fill="both", expand=True, padx=8, pady=(0, 10))

        self.log_text = tk.Text(
            log_outer,
            bg=C["card"], fg=C["text"], font=FM,
            relief="flat", bd=0, highlightthickness=0,
            state="disabled", wrap="none",
        )
        sb_log = tk.Scrollbar(log_outer, orient="vertical",
                              command=self.log_text.yview,
                              bg=C["nav_bg"], troughcolor=C["bg"],
                              activebackground=C["accent"])
        self.log_text.configure(yscrollcommand=sb_log.set)
        sb_log.pack(side="right", fill="y", padx=(0, 2), pady=4)
        self.log_text.pack(fill="both", expand=True, padx=(6, 0), pady=6)

        self.log_text.tag_config("heure",  foreground=C["header_bg"],
                                 font=("Consolas", 10, "bold"))
        self.log_text.tag_config("normal", foreground=C["text"])

    # ── Footer ────────────────────────────────────────────────────────────────

    def _build_footer(self):
        ft = ctk.CTkFrame(self, fg_color=C["panel"], corner_radius=0, height=26)
        ft.pack(fill="x", side="bottom")
        ft.pack_propagate(False)
        self.status_var = tk.StringVar(value="Prêt.")
        ctk.CTkLabel(ft, textvariable=self.status_var,
                     font=FSM, text_color=C["text_dim"]).pack(side="left", padx=12)
        ctk.CTkLabel(ft, text="Écurie Manager v2.0",
                     font=FSM, text_color=C["border"]).pack(side="right", padx=12)

    # ─────────────────────────── REFRESH ──────────────────────────────────────

    def _refresh_all(self):
        self.bl_chevaux.set(self.chevaux)
        self.bl_heures.set(self.heures)
        self.bl_eleves.set([f"{e}  –  -1 séance" for e in self.eleves])
        self.bl_moniteurs.set([f"👤 {m[0]}   •   {m[1]}" for m in self.moniteurs_data])
        self._refresh_log()

    def _refresh_log(self):
        self.log_text.config(state="normal")
        self.log_text.delete("1.0", tk.END)
        for line in self.log_lines:
            tag = "heure" if line.startswith(r"\heure") else "normal"
            self.log_text.insert(tk.END, line + "\n", tag)
        self.log_text.config(state="disabled")

    def _set_status(self, msg):
        ts = datetime.now().strftime("%H:%M:%S")
        self.status_var.set(f"[{ts}]  {msg}")

    # ─────────────────────────── ACTIONS ──────────────────────────────────────

    # ── Chevaux ──
    def _ajouter_cheval(self):
        nom = self.entry_cheval.get().strip().upper()
        if nom:
            self.chevaux.append(nom)
            self.bl_chevaux.set(self.chevaux)
            self.entry_cheval.delete(0, tk.END)
            self._set_status(f"Cheval « {nom} » ajouté.")
        else:
            messagebox.showwarning("Attention", "Saisissez un nom de cheval.")

    def _supprimer_cheval(self):
        idx = self.bl_chevaux.selected_index()
        if idx is not None:
            nom = self.chevaux.pop(idx)
            self.bl_chevaux.set(self.chevaux)
            self._set_status(f"Cheval « {nom} » supprimé.")
        else:
            messagebox.showwarning("Attention", "Cliquez d'abord sur un cheval pour le sélectionner.")

    # ── Heures ──
    def _creer_heure(self):
        val = self.entry_heure.get().strip().upper()
        if val:
            self.heures.append(val)
            self.bl_heures.set(self.heures)
            self.entry_heure.delete(0, tk.END)
            self.log_lines.append(rf"\heure/{val}")
            self._refresh_log()
            self._set_status(f"Heure « {val} » créée.")
        else:
            messagebox.showwarning("Attention", "Saisissez une heure.")

    def _supprimer_heure(self):
        idx = self.bl_heures.selected_index()
        if idx is not None:
            val = self.heures.pop(idx)
            self.bl_heures.set(self.heures)
            self._set_status(f"Heure « {val} » supprimée.")
        else:
            messagebox.showwarning("Attention", "Cliquez d'abord sur une heure pour la sélectionner.")

    # ── Élèves ──
    def _creer_eleve(self):
        nom = self.entry_eleve.get().strip().upper()
        if nom:
            self.eleves.append(nom)
            self.bl_eleves.set([f"{e}  –  -1 séance" for e in self.eleves])
            self.entry_eleve.delete(0, tk.END)
            self.log_lines.append(f"{nom}/-1")
            self._refresh_log()
            self._set_status(f"Élève « {nom} » créé.")
        else:
            messagebox.showwarning("Attention", "Saisissez un nom d'élève.")

    def _supprimer_eleve(self):
        idx = self.bl_eleves.selected_index()
        if idx is not None:
            nom = self.eleves.pop(idx)
            self.bl_eleves.set([f"{e}  –  -1 séance" for e in self.eleves])
            self._set_status(f"Élève « {nom} » supprimé.")
        else:
            messagebox.showwarning("Attention", "Cliquez d'abord sur un élève pour le sélectionner.")

    # ── Moniteurs ──
    def _ajouter_moniteur(self):
        nom  = self.entry_moniteur.get().strip()
        mail = self.entry_mail.get().strip()
        if nom and mail:
            self.moniteurs_data.append((nom, mail))
            self.bl_moniteurs.set([f"👤 {m[0]}   •   {m[1]}" for m in self.moniteurs_data])
            # Mettre à jour le combobox utilisateur
            self._user_cb.configure(values=[m[0] for m in self.moniteurs_data])
            self.entry_moniteur.delete(0, tk.END)
            self.entry_mail.delete(0, tk.END)
            self._set_status(f"Moniteur « {nom} » ajouté.")
        else:
            messagebox.showwarning("Attention", "Remplissez le nom et le mail.")

    def _supprimer_moniteur(self):
        idx = self.bl_moniteurs.selected_index()
        if idx is not None:
            nom = self.moniteurs_data.pop(idx)[0]
            self.bl_moniteurs.set([f"👤 {m[0]}   •   {m[1]}" for m in self.moniteurs_data])
            self._user_cb.configure(values=[m[0] for m in self.moniteurs_data])
            self._set_status(f"Moniteur « {nom} » supprimé.")
        else:
            messagebox.showwarning("Attention", "Cliquez d'abord sur un moniteur pour le sélectionner.")

    # ── Persistance ──
    def _enregistrer(self):
        data = {
            "jour":      self.jour_var.get(),
            "user":      self.user_var.get(),
            "chevaux":   self.chevaux,
            "heures":    self.heures,
            "eleves":    self.eleves,
            "moniteurs": self.moniteurs_data,
            "log":       self.log_lines,
        }
        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON", "*.json"), ("Tous les fichiers", "*.*")],
            title="Enregistrer sous…",
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self._set_status(f"Sauvegardé : {os.path.basename(path)}")
            messagebox.showinfo("Enregistré ✓", f"Données sauvegardées :\n{path}")

    def _importer(self):
        path = filedialog.askopenfilename(
            filetypes=[("JSON", "*.json"), ("Tous les fichiers", "*.*")],
            title="Importer paramètres…",
        )
        if path:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.jour_var.set(data.get("jour", "Mercredi"))
            self.user_var.set(data.get("user", "admin"))
            self.chevaux        = data.get("chevaux", [])
            self.heures         = data.get("heures", [])
            self.eleves         = data.get("eleves", [])
            self.moniteurs_data = [tuple(m) for m in data.get("moniteurs", [])]
            self.log_lines      = data.get("log", [])
            self._refresh_all()
            self._user_cb.configure(values=[m[0] for m in self.moniteurs_data])
            self._set_status(f"Importé : {os.path.basename(path)}")

    def _exporter(self):
        self._enregistrer()

    def _ouvrir_excel(self):
        path = filedialog.askopenfilename(
            filetypes=[("Excel", "*.xlsx *.xls"), ("Tous les fichiers", "*.*")],
            title="Ouvrir fichier Excel de référence…",
        )
        if path:
            if os.name == "nt":
                os.startfile(path)
            else:
                os.system(f'open "{path}"')
            self._set_status(f"Excel ouvert : {os.path.basename(path)}")


# ─── Lancement ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        import customtkinter
    except ImportError:
        print("Installez customtkinter :  pip install customtkinter")
        raise SystemExit(1)

    app = EcurieManager()
    app.mainloop()