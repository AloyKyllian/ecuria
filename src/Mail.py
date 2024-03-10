import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def envoyer_email(user, piece_jointe,nom_piece_jointe,sujeti,mail):
    if user == "Lena":
        destinataire = mail[0] #'aloykyllian31520@gmail.com'
    elif user == "Karine":
        destinataire = mail[1] #'thepandou05@gmail.com'
    #delmaslena@gmail.com
    #dunoyerkarine@gmail.com
    
    sujet = sujeti
    corps = ' '
    # Création de l'objet MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = 'ecuria.excel@gmail.com'
    msg['To'] = destinataire
    msg['Subject'] = sujet

    # Ajout du corps du message
    msg.attach(MIMEText(corps, 'plain'))

    # Ajout de la pièce jointe
    attachment = open(piece_jointe, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % nom_piece_jointe)
    msg.attach(part)

    # Connexion au serveur SMTP de Gmail
    serveur_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    serveur_smtp.starttls()

    # Authentification avec votre compte Gmail
    serveur_smtp.login('ecuria.excel@gmail.com', 'ldos hxcw kado lnly')

    # Envoi de l'e-mail
    try:
        err = serveur_smtp.sendmail('ecuria.excel@gmail.com', destinataire, msg.as_string())
        print("E-mail envoyé avec succès !",err)
    except:
        err = "Erreur lors de l'envoie de l'email (veuiller verifier l'adresse du destinataire :"+destinataire+")"
    # Fermeture de la connexion au serveur SMTP
    serveur_smtp.quit()

    
    return err

# Exemple d'utilisation



# envoyer_email(destinataire, sujet, corps, piece_jointe)
 