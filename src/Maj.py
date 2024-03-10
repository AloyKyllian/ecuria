
import win32com.client
import os
import shutil

def raccourci(path, nom):
    bureau = os.path.join(os.path.expanduser("~"), "Desktop")
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(os.path.join(bureau, nom.replace(".exe", "")+".lnk"))
    shortcut.Targetpath = path + "\\" + nom.replace(".exe", "")+"\\" + nom
    print(path + "\\" + nom.replace(".exe", "")+"\\" + nom)
    # shortcut.Targetpath = r"C:\\Users\\33621\\Documents\\cheval_python\\ecuria\\ecuria 1.5\\ecuria v1.5.exe"
    shortcut.WorkingDirectory = path + "\\" + nom.replace(".exe", "")
    print(path + "\\" + nom.replace(".exe", ""))
    # shortcut.WorkingDirectory = r"C:\\Users\\33621\\Documents\\cheval_python\\ecuria\\ecuria 1.5"
    shortcut.save()

# taskbar_path = os.path.join(os.path.expanduser("~"), r"AppData\\Roaming\\Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\TaskBar\\testdfs.lnk")
# shutil.copy2(os.path.join(bureau, "testdfs.lnk"), taskbar_path)


# taskbar_path = os.path.join(bureau, "Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar")
# shutil.copy2(os.path.join(bureau, "testdfs.lnk"), taskbar_path)

# Exemple d'utilisation
# shortcut_path = os.path.join(os.path.expanduser("~"), "Desktop", "testdfs.lnk")
# pin_to_taskbar(shortcut_path)
# import os
# import shutil

# def create_shortcut(source_path, shortcut_name):
#     # Vérifier si le fichier source existe
#     if not os.path.exists(source_path):
#         print("Le fichier source n'existe pas.")
#         return

#     # Vérifier si le raccourci existe déjà
#     shortcut_path = os.path.join(os.path.expanduser("~"), "Desktop", shortcut_name + ".lnk")
#     if os.path.exists(shortcut_path):
#         print("Le raccourci existe déjà.")
#         return

#     try:
#         # Créer le raccourci
#         shutil.copy2(source_path, shortcut_path)
#         print("Le raccourci a été créé avec succès.")
#     except Exception as e:
#         print("Une erreur s'est produite lors de la création du raccourci :", str(e))

# # Exemple d'utilisation
# source_file = "C:\\Users\\33621\\Documents\\cheval_python\\ecuria\\ecuria 1.5\\ecuria v1.5.exe"
# shortcut_name = "Mon Raccourci"

# create_shortcut(source_file, shortcut_name)




# import os
# import subprocess
# # chemin vers le fichier .exe
# fichier_exe = "C:\\Users\\33621\\Documents\\cheval_python\\ecuria\\ecuria 1.5\\ecuria v1.5.exe"

# # chemin vers le bureau
# bureau = os.path.join(os.path.expanduser("~"), "Desktop")

# # création du raccourci
# with open(os.path.join(bureau, "Raccourci vers Mon_Programme.lnk"), "wb") as f:
#     pass
# os.chmod(os.path.join(bureau, "Raccourci vers Mon_Programme.lnk"),  0o644)
# subprocess.call(["cmd", "/c", "mklink", "/d", os.path.join(bureau, "Raccourci vers Mon_Programme.lnk"), fichier_exe])