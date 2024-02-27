import tkinter as tk
from tkinter import filedialog
from subprocess import Popen

# fenêtre principale
root = tk.Tk()
root.title("Launcher Doom avec Gestion des Mods et Chemins")
root.geometry("600x500")

# creation des variables Tkinter
path_to_doom_exe = tk.StringVar(value="C:/chemin/vers/Doom.exe")
mods_folder = tk.StringVar(value="C:/chemin/vers/mods")
def launch_doom():
    selected_mods = [mods_listbox.get(idx) for idx in mods_listbox.curselection()]
    mod_paths = [f'"{mods_folder.get()}/{mod}"' for mod in selected_mods]  # Utiliser le chemin depuis l'objet StringVar
    doom_command = [path_to_doom_exe.get()] + mod_paths
    Popen(doom_command)

def add_mod():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("WAD files", "*.wad"), ("All files", "*.*")))
    if filename:
        mods_listbox.insert(tk.END, filename.split("/")[-1])

def select_doom_path():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Doom Executable",
                                           filetypes=(("Executable files", "*.exe"), ("All files", "*.*")))
    if filename:
        path_to_doom_exe.set(filename)  # Mettre à jour la variable avec le nouveau chemin

def select_mods_folder():
    directory = filedialog.askdirectory(title="Select Mods Folder")
    if directory:
        mods_folder.set(directory)  # Mettre à jour la variable avec le nouveau chemin

# stocker les chemins
path_to_doom_exe = tk.StringVar(value="C:/chemin/vers/Doom.exe")  # Valeur initiale, modifiable 
mods_folder = tk.StringVar(value="C:/chemin/vers/mods")  # Valeur initiale, modifiable 


# Configuration pour le chemin de Doom
tk.Label(root, text="Chemin d'accès à Doom:").pack()
tk.Entry(root, textvariable=path_to_doom_exe, width=50).pack()
tk.Button(root, text="Parcourir...", command=select_doom_path).pack()

# Configuration pour le dossier des mods
tk.Label(root, text="Dossier des Mods:").pack()
tk.Entry(root, textvariable=mods_folder, width=50).pack()
tk.Button(root, text="Parcourir...", command=select_mods_folder).pack()

# Liste pour afficher les mods
mods_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
mods_listbox.pack(pady=10)

# Bouton pour ajouter des mods à la liste
add_mod_button = tk.Button(root, text="Ajouter Mod", command=add_mod)
add_mod_button.pack(pady=5)

# Bouton pour lancer Doom avec les mods sélectionnés
launch_button = tk.Button(root, text="Lancer Doom avec Mods", command=launch_doom)
launch_button.pack(pady=20)

# Démarrer l'interface utilisateur
root.mainloop()