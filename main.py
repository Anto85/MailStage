import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openpyxl
from email.mime.application import MIMEApplication
from email.encoders import encode_base64
import ollama


def envoyer_email(destinataire, sujet, expediteur, username, mot_de_passe):
    # Créer un objet MIMEMultipart pour le message
    message = MIMEMultipart()
    message['From'] = expediteur
    message['To'] = destinataire
    message['Subject'] = sujet

    # Ajouter le contenu du message
    message.attach(MIMEText("""
    Bonjour,

    Veuillez trouver ci-joint le fichier ANTONIN URBAIN.pdf.
    Je vous envoie également une copie avec un texte de motivation en prime.

    Cordialement,
    Votre nom
    """, 'plain'))
    
    message.attach(contenu())

    # Établir une connexion avec le serveur SMTP de Gmail
    serveur_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    serveur_smtp.starttls()

    # Se connecter au compte Gmail
    serveur_smtp.login(username, mot_de_passe)

    # Envoyer le message
    serveur_smtp.send_message(message)

    # Fermer la connexion
    serveur_smtp.quit()
    
def envoyer_email_classeur():
    # Ouvrir le fichier Classeur1.xlsx
    classeur = openpyxl.load_workbook('Classeur1.xlsx')
    feuille = classeur.active

    # Récupérer le contenu du message à partir de la feuille de calcul
    adresse_mail = []
    for row in feuille.iter_rows(min_row=4, max_row=5, min_col=6, max_col=6):
        for cell in row:
            adresse_mail.append(cell.value + '\n')
    for i in adresse_mail:
        # Appeler la fonction envoyer_email avec les paramètres appropriés
        envoyer_email(i, "candidature stage","Antonin Urbain", "anto.urbain@gmail.com", 'hhcj pxns haim adya')

def contenu():
    # Créer un objet MIMEMultipart pour le contenu du message
    contenu = MIMEMultipart()

    # Créer les objets MIMEApplication pour les fichiers PDF
    with open("ANTONIN URBAIN.pdf", "rb") as opened:
        openedfile = opened.read()
    attachedfile = MIMEApplication(openedfile, _subtype="pdf", _encoder=encode_base64)
    attachedfile.add_header('content-disposition', 'attachment', filename="ANTONIN URBAIN.pdf")
    contenu.attach(attachedfile)
    

    return contenu


def extract(output):
    text = ""
    text += output['response']
    return text

client = ollama.Client()
output = client.generate('mistral', "Tell me a joke")
print(output)
print(extract(output))


envoyer_email_classeur()