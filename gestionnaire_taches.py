import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

FICHIER_TACHES = "taches.json"

# Charger les tâches depuis le fichier JSON
def charger_taches():
    try:
        with open(FICHIER_TACHES, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Sauvegarder les tâches
def sauvegarder_taches(taches):
    with open(FICHIER_TACHES, "w") as f:
        json.dump(taches, f, indent=4)

# Ajouter une tâche
def ajouter_tache():
    desc = entry_desc.get()
    deadline = entry_deadline.get()
    priorite = priorite_var.get()

    if not desc.strip():
        messagebox.showwarning("Erreur", "La description ne peut pas être vide.")
        return

    # Vérif deadline
    if deadline.strip():
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Erreur", "Format de date invalide (YYYY-MM-DD).")
            return
    else:
        deadline = None

    tache = {
        "description": desc,
        "deadline": deadline,
        "statut": "à faire",
        "priorite": priorite
    }
    taches.append(tache)
    sauvegarder_taches(taches)
    rafraichir_liste()
    entry_desc.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)

# Supprimer une tâche
def supprimer_tache():
    try:
        index = liste_taches.curselection()[0]
        t = taches.pop(index)
        sauvegarder_taches(taches)
        rafraichir_liste()
        messagebox.showinfo("Supprimée", f"Tâche supprimée : {t['description']}")
    except IndexError:
        messagebox.showwarning("Erreur", "Sélectionne une tâche à supprimer.")

# Marquer comme terminée
def terminer_tache():
    try:
        index = liste_taches.curselection()[0]
        taches[index]["statut"] = "terminée"
        sauvegarder_taches(taches)
        rafraichir_liste()
    except IndexError:
        messagebox.showwarning("Erreur", "Sélectionne une tâche à terminer.")

# Rafraîchir l’affichage
def rafraichir_liste():
    liste_taches.delete(0, tk.END)
    for t in taches:
        deadline = f" (deadline: {t['deadline']})" if t['deadline'] else ""
        texte = f"{t['description']} {deadline} | {t['statut']} | Priorité: {t['priorite']}"
        liste_taches.insert(tk.END, texte)

# Interface Tkinter
root = tk.Tk()
root.title("Gestionnaire de tâches")

taches = charger_taches()

# Zone saisie description
tk.Label(root, text="Description:").pack()
entry_desc = tk.Entry(root, width=40)
entry_desc.pack()

# Zone saisie deadline
tk.Label(root, text="Deadline (YYYY-MM-DD):").pack()
entry_deadline = tk.Entry(root, width=20)
entry_deadline.pack()

# Choix priorité
tk.Label(root, text="Priorité:").pack()
priorite_var = tk.StringVar(value="Moyenne")
tk.Radiobutton(root, text="Haute 🔴", variable=priorite_var, value="Haute").pack()
tk.Radiobutton(root, text="Moyenne 🟡", variable=priorite_var, value="Moyenne").pack()
tk.Radiobutton(root, text="Basse 🟢", variable=priorite_var, value="Basse").pack()

# Boutons
tk.Button(root, text="Ajouter", command=ajouter_tache).pack(pady=5)
tk.Button(root, text="Supprimer", command=supprimer_tache).pack(pady=5)
tk.Button(root, text="Marquer comme terminée", command=terminer_tache).pack(pady=5)

# Liste des tâches
liste_taches = tk.Listbox(root, width=70, height=10)
liste_taches.pack(pady=10)

rafraichir_liste()

root.mainloop()

