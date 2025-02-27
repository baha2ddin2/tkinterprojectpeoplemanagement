import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
class Employee:
    def __init__(self, nom, prenom, age, matricule, nbr_heures, tarif_horaire):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.matricule = matricule
        self.nbr_heures = nbr_heures
        self.tarif_horaire = tarif_horaire
    def calculate_salary(self):
        try:
            return float(self.nbr_heures) * float(self.tarif_horaire)
        except ValueError:
            return 0.0
    def to_list(self):
        return [
            self.nom,
            self.prenom,
            self.age,
            self.matricule,
            self.nbr_heures,
            self.tarif_horaire,
            f"{self.calculate_salary():.2f}"
        ]
def save_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    with open(file_path, "w") as file:
        for item in tree.get_children():
            values = tree.item(item, "values")
            file.write(",".join(values) + "\n")
    messagebox.showinfo("Succès", "Données sauvegardées avec succès!")
def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    tree.delete(*tree.get_children())
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            tree.insert("", "end", values=values)
    messagebox.showinfo("Succès", "Données importées avec succès!")
def validate_entries(*entries):
    for entry in entries:
        if not entry.get().strip():
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis!")
            return False
    return True
def ajouter():
    def save_ajout():
        if not validate_entries(entry_nom, entry_prenom, entry_matricule):
            return
        employee = Employee(
            entry_nom.get(),
            entry_prenom.get(),
            spinbox_age.get(),
            entry_matricule.get(),
            spinbox_nbr_heures.get(),
            spinbox_tarif_horaire.get()
        )
        tree.insert("", "end", values=employee.to_list())
        add_window.destroy()
    def cancel():
        add_window.destroy()
    add_window = tk.Toplevel(root)
    add_window.title("Ajouter")
    tk.Label(add_window, text="Nom :").grid(row=0, column=0)
    entry_nom = tk.Entry(add_window, font=("Arial", 10))
    entry_nom.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(add_window, text="Prenom :").grid(row=1, column=0)
    entry_prenom = tk.Entry(add_window, font=("Arial", 10))
    entry_prenom.grid(row=1, column=1, padx=5, pady=5)
    tk.Label(add_window, text="Age :").grid(row=2, column=0)
    spinbox_age = tk.Spinbox(add_window, from_=18, to=65, width=5)
    spinbox_age.grid(row=2, column=1, padx=5, pady=5)
    tk.Label(add_window, text="Matricule :").grid(row=3, column=0)
    entry_matricule = tk.Entry(add_window)
    entry_matricule.grid(row=3, column=1)
    tk.Label(add_window, text="Nbr d'heures :").grid(row=4, column=0)
    spinbox_nbr_heures = tk.Spinbox(add_window, from_=0, to=100, width=5)
    spinbox_nbr_heures.grid(row=4, column=1, padx=5, pady=5)
    tk.Label(add_window, text="Tarif Horaire :").grid(row=5, column=0)
    spinbox_tarif_horaire = tk.Spinbox(add_window, from_=0, to=1000, increment=10, width=5)
    spinbox_tarif_horaire.grid(row=5, column=1, padx=5, pady=5)
    tk.Button(add_window, text="Enregistrez", command=save_ajout).grid(row=6, column=0)
    tk.Button(add_window, text="Annuler", command=cancel).grid(row=6, column=1)
def modifier():
    def save_modification():
        if not validate_entries(entry_nom, entry_prenom, entry_matricule):
            return
        selected_item = tree.selection()
        if selected_item:
            employee = Employee(
                entry_nom.get(),
                entry_prenom.get(),
                spinbox_age.get(),
                entry_matricule.get(),
                spinbox_nbr_heures.get(),
                spinbox_tarif_horaire.get()
            )
            tree.item(selected_item, values=employee.to_list())
        modify_window.destroy()
    def cancel():
        modify_window.destroy()
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo("Erreur", "Aucune ligne sélectionnée.")
        return
    values = tree.item(selected_item, "values")
    modify_window = tk.Toplevel(root)
    modify_window.title("Modifier")
    tk.Label(modify_window, text="Nom :").grid(row=0, column=0)
    entry_nom = tk.Entry(modify_window)
    entry_nom.grid(row=0, column=1, padx=5, pady=5)
    entry_nom.insert(0, values[0])
    tk.Label(modify_window, text="Prenom :").grid(row=1, column=0)
    entry_prenom = tk.Entry(modify_window, font=("Arial", 10))
    entry_prenom.grid(row=1, column=1, padx=5, pady=5)
    entry_prenom.insert(0, values[1])
    tk.Label(modify_window, text="Age :").grid(row=2, column=0)
    spinbox_age = tk.Spinbox(modify_window, from_=18, to=65, width=5)
    spinbox_age.grid(row=2, column=1)
    spinbox_age.delete(0, tk.END)
    spinbox_age.insert(0, values[2])
    tk.Label(modify_window, text="Matricule :").grid(row=3, column=0)
    entry_matricule = tk.Entry(modify_window)
    entry_matricule.grid(row=3, column=1)
    entry_matricule.insert(0, values[3])
    tk.Label(modify_window, text="Nbr d'heures :").grid(row=4, column=0)
    spinbox_nbr_heures = tk.Spinbox(modify_window, from_=0, to=1000, increment=10, width=5)
    spinbox_nbr_heures.grid(row=4, column=1)
    spinbox_nbr_heures.delete(0, tk.END)
    spinbox_nbr_heures.insert(0, values[4])
    tk.Label(modify_window, text="Tarif Horaire :").grid(row=5, column=0)
    spinbox_tarif_horaire = tk.Spinbox(modify_window, from_=0, to=1000, increment=10, width=5)
    spinbox_tarif_horaire.grid(row=5, column=1)
    spinbox_tarif_horaire.delete(0, tk.END)
    spinbox_tarif_horaire.insert(0, values[5])
    tk.Button(modify_window, text="Enregistrez", command=save_modification).grid(row=6, column=0)
    tk.Button(modify_window, text="Annuler", command=cancel).grid(row=6, column=1)
def supprimer():
    def delete():
        matricule_to_delete = entry_matricule.get()
        found = False
        for item in tree.get_children():
            if tree.item(item, "values")[3] == matricule_to_delete:  
                tree.delete(item)
                found = True
                break
        if not found:
            messagebox.showinfo("Erreur", "Matricule non trouvé.")
        delete_window.destroy()
    def cancel():
        delete_window.destroy()
    delete_window = tk.Toplevel(root)
    delete_window.title("Supprimer")  
    tk.Label(delete_window, text="Matricule :").grid(row=0, column=0)
    entry_matricule = tk.Entry(delete_window)
    entry_matricule.grid(row=0, column=1)
    tk.Button(delete_window, text="Supprimer", command=delete).grid(row=1, column=0)
    tk.Button(delete_window, text="Annuler", command=cancel).grid(row=1, column=1)
root = tk.Tk()
root.title("Gestion des Employés")
btn_ajouter = tk.Button(root, text="Ajouter", command=ajouter)
btn_ajouter.grid(row=0, column=0)
btn_modifier = tk.Button(root, text="Modifier", command=modifier)
btn_modifier.grid(row=0, column=1)
btn_supprimer = tk.Button(root, text="Supprimer", command=supprimer)
btn_supprimer.grid(row=0, column=2)
btn_save = tk.Button(root, text="Sauvegarder", command=save_data)
btn_save.grid(row=0, column=3)
btn_import = tk.Button(root, text="Importer", command=load_data)
btn_import.grid(row=0, column=4)
columns = ("Nom", "Prenom", "Age", "Matricule", "Nbr d'heures", "Tarif Horaire", "Salaire")
tree = ttk.Treeview(root, columns=columns, show="headings", style="Custom.Treeview")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.grid(row=1, column=0, columnspan=6)

root.mainloop()