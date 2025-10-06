import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# from Log import LoggerCounter

# logger = LoggerCounter(name="Mail").logger


def envoyer_email(destinataire, piece_jointe, nom_piece_jointe, sujeti, mail):
    sujet = sujeti
    corps = " "
    
    # Création de l'objet MIMEMultipart
    msg = MIMEMultipart()
    msg["From"] = "ecuria.excel@gmail.com"
    msg["To"] = destinataire
    msg["Subject"] = sujet

    # Ajout du corps du message
    msg.attach(MIMEText(corps, "plain"))

    # Ajout de la pièce jointe
    with open(piece_jointe, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f"attachment; filename={nom_piece_jointe}"
        )
        msg.attach(part)

    # Connexion au serveur SMTP de Gmail
    serveur_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    serveur_smtp.starttls()

    # Authentification avec votre compte Gmail
    serveur_smtp.login("ecuria.excel@gmail.com", "ldos hxcw kado lnly")

    # Envoi de l'e-mail
    try:
        err = serveur_smtp.sendmail("ecuria.excel@gmail.com", destinataire, msg.as_string())
        print("E-mail envoyé avec succès à %s", destinataire)
    except Exception as e:
        err = f"Erreur lors de l'envoi de l'email (vérifier l'adresse du destinataire : {destinataire})"
        print(err + " | Exception: %s", e)
    finally:
        serveur_smtp.quit()
    return err


# if __name__ == "__main__":
#     # Exemple d'utilisation
#     user = "Lena"
#     mail = ["aloykyllian31520@gmail.com"]
#     sujeti = "Test"
#     corps = "Bonjour,\n\nVoici un e-mail envoyé depuis Python."
#     piece_jointe = "C:/Users/aloyk/Downloads/ecuria 1.83/ecuria 1.83/parametre.zip"
#     nom_piece_jointe = "parametre.zip"

#     err = False
#     try:
#         erreur = envoyer_email(user, piece_jointe, nom_piece_jointe, sujeti, mail)
#     except Exception as e:
#         err = True
#         logger.error("Erreur lors de l'envoi du planning : %s", e)

#     if not err:
#         logger.info("Le planning a été envoyé avec succès!")
