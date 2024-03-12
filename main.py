import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openpyxl
from email.mime.application import MIMEApplication
from email.encoders import encode_base64
import ollama
import re


def envoyer_email(destinataire, sujet, expediteur, username, mot_de_passe, company):
    # Créer un objet MIMEMultipart pour le message
    prompt_finale = prompt(destinataire, company)
    message = MIMEMultipart()
    message['From'] = expediteur
    message['To'] = destinataire
    text = ""
    text = generation_ollama(prompt_finale)
    subject = re.search(r"Subject:(.*)", text)
    subject = subject.group(1).strip()
    message['Subject'] = subject
    text = re.sub(r"Subject:(.*)", "", text)

    # Ajouter le contenu du message
    message.attach(MIMEText(text, 'plain'))
    
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
    nom = []
    for row in feuille.iter_rows(min_row=4, max_row=5, min_col=2, max_col=2):
        for cell in row:
            nom.append(cell.value + '\n')
    
    entreprise = []
    for row in feuille.iter_rows(min_row=4, max_row=5, min_col=3, max_col=3):
        for cell in row:
            entreprise.append(cell.value + '\n')
    for i in adresse_mail:
        # Appeler la fonction envoyer_email avec les paramètres appropriés
        destination = 'candidature stage ' + nom[adresse_mail.index(i)]
        company = entreprise[adresse_mail.index(i)]
        envoyer_email(i, destination,"Antonin Urbain", "anto.urbain@gmail.com", 'hhcj pxns haim adya', company)

def contenu():
    # Créer un objet MIMEMultipart pour le contenu du message
    contenu = MIMEMultipart()

    # Créer les objets MIMEApplication pour les fichiers PDF
    with open("ANTONIN URBAIN.pdf", "rb") as opened:
        openedfile = opened.read()
    with open("Copie de ANTONIN URBAIN.pdf", "rb") as opened2:
        openedfile2 = opened2.read()
    
    attachedfile = MIMEApplication(openedfile, _subtype="pdf", _encoder=encode_base64)
    attachedfile2 = MIMEApplication(openedfile2, _subtype="pdf", _encoder=encode_base64)
    attachedfile.add_header('content-disposition', 'attachment', filename="ANTONIN URBAIN.pdf")
    attachedfile2.add_header('content-disposition', 'attachment', filename="ANTONIN URBAIN EN.pdf")
    contenu.attach(attachedfile)
    contenu.attach(attachedfile2)
    
    return contenu

def prompt(name, company):
    text = "My name is Antonin Urbain, my email is anto.urbain@gmail.com and my phone numbers is 07 83 19 45 78. I am a fast learner and i like programmation and new technology.I am actually in first year of ingeneering at ESEO, i am looking for an internship for 4 month from mid july to november. don't write any subject in the mail. The mail reader is named "+name+". The mail should be formal and polite. and i want to make them know that i know their company named" + company 
    return text

def extract(output):
    text = ""
    text += output['response']
    return text

def generation_ollama(prompt):
    client = ollama.Client()
    output = client.generate('mistral', prompt)
    return (extract(output))

envoyer_email_classeur()