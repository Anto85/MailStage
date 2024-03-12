import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.encoders import encode_base64
import re

output = {
    'model': 'mistral',
    'created_at': '2024-03-12T16:51:40.3913433Z',
    'response': " Subject: Application for Four-Month Internship at [Company Name]\n\nDear Hiring Manager,\n\nI hope this message finds you well. I was excited to discover that [Company Name] is currently offering a four-month internship opportunity starting from mid-July. As a first-year engineering student at ESEO with a strong interest in programming and new technology, I believe that this position would provide an excellent opportunity for me to gain valuable experience and contribute to your team.\n\nI have always admired [Company Name] for its innovative approach and commitment to excellence in the field of technology. I am confident that I can bring a fresh perspective and strong work ethic to your team, as well as a keen desire to learn and grow.\n\nMy academic background includes courses in programming languages such as Java, C++, and Python. In addition, I have gained hands-on experience through various projects and group assignments, including developing web applications using HTML, CSS, and JavaScript. I am also proficient in using tools such as Git for version control and Agile methodologies for software development.\n\nFurthermore, I have a strong analytical mindset and excellent problem-solving skills, which I believe would be an asset to your team. I am a quick learner and am always eager to take on new challenges.\n\nI am confident that my skills and experiences align well with the requirements of this internship. I look forward to the opportunity to contribute to [Company Name] and learn from the talented individuals within your organization.\n\nIf you require any further information or have any questions, please do not hesitate to contact me. My email address is anto.urbain@gmail.com, and my phone number is 07 83 19 45 78. I am available at your earliest convenience to discuss my application in more detail.\n\nThank you for considering my application. I look forward to the opportunity to join your team and contribute to [Company Name]'s continued success.\n\nSincerely,\n\nAntonin Urbain",
    'done': True,
    'context': [733, 16289, 28793, 28705, 315, 837, 264, 4102, 27205, 1079, 304, 613, 737, 2007, 28719, 352, 304, 633, 5514, 28723, 28737, 837, 2590, 297, 907, 879, 302, 4155, 1860, 2131, 438, 413, 1151, 28762, 325, 19185, 302, 13176, 304, 5227, 1711, 557, 613, 837, 2526, 354, 396, 3875, 4760, 302, 28705, 28781, 2102, 477, 4725, 461, 3089, 298, 24107, 28723, 415, 9636, 8847, 349, 5160, 28747, 28723, 415, 9636, 1023, 347, 9907, 304, 27057, 28723, 304, 613, 947, 298, 1038, 706, 873, 369, 613, 873, 652, 2496, 5160, 907, 28725, 613, 2169, 586, 1008, 562, 613, 949, 28742, 28707, 2111, 586, 3754, 1871, 28725, 868, 613, 1347, 586, 21594, 354, 272, 2496, 28725, 304, 613, 1985, 684, 586, 6266, 304, 586, 9021, 1024, 456, 613, 1492, 586, 9636, 395, 586, 3754, 1871, 714, 1984, 1141, 349, 8999, 262, 500, 9312, 426, 28725, 586, 4927, 349, 396, 532, 28723, 5354, 426, 28818, 23769, 28723, 675, 304, 586, 4126, 5551, 349, 28705, 28734, 28787, 28705, 28783, 28770, 28705, 28740, 28774, 28705, 28781, 28782, 28705, 28787, 28783, 28723, 733, 28748, 16289, 28793, 25558, 28747, 12482, 354, 9611, 28733, 15605, 3560, 4760, 438, 733, 24673, 6620, 28793, 13, 13, 28757, 644, 382, 5549, 13111, 28725, 13, 13, 28737, 3317, 456, 2928, 12397, 368, 1162, 28723, 315, 403, 9534, 298, 5191, 369, 733, 24673, 6620, 28793, 349, 5489, 9055, 264, 2308, 28733, 10976, 3875, 4760, 5701, 5615, 477, 4725, 28733, 28798, 3089, 28723, 1136, 264, 907, 28733, 4395, 13320, 5716, 438, 413, 1151, 28762, 395, 264, 2967, 2145, 297, 16292, 304, 633, 5514, 28725, 315, 3091, 369, 456, 2840, 682, 3084, 396, 8099, 5701, 354, 528, 298, 8356, 12302, 2659, 304, 14951, 298, 574, 1918, 28723, 13, 13, 28737, 506, 1743, 5055, 1360, 733, 24673, 6620, 28793, 354, 871, 16827, 4431, 304, 13106, 298, 7154, 636, 297, 272, 1834, 302, 5514, 28723, 315, 837, 10689, 369, 315, 541, 2968, 264, 6138, 10403, 304, 2967, 771, 7511, 294, 298, 574, 1918, 28725, 390, 1162, 390, 264, 20005, 8646, 298, 2822, 304, 2333, 28723, 13, 13, 5183, 11860, 5414, 5532, 12318, 297, 16292, 14028, 1259, 390, 11639, 28725, 334, 1680, 28725, 304, 21366, 28723, 560, 4518, 28725, 315, 506, 14018, 3038, 28733, 266, 2659, 1059, 4118, 7028, 304, 2071, 28025, 28725, 2490, 10423, 4686, 8429, 1413, 13987, 28725, 17922, 28725, 304, 26281, 28723, 315, 837, 835, 1957, 4065, 297, 1413, 7040, 1259, 390, 27903, 354, 2751, 2602, 304, 3786, 546, 2038, 8776, 354, 3930, 4099, 28723, 13, 13, 28765, 324, 620, 4452, 28725, 315, 506, 264, 2967, 13305, 745, 2273, 673, 304, 8099, 2700, 28733, 28713, 18390, 6266, 28725, 690, 315, 3091, 682, 347, 396, 13458, 298, 574, 1918, 28723, 315, 837, 264, 2936, 27205, 1079, 304, 837, 1743, 15381, 298, 1388, 356, 633, 10369, 28723, 13, 13, 28737, 837, 10689, 369, 586, 6266, 304, 9021, 8753, 1162, 395, 272, 8296, 302, 456, 3875, 4760, 28723, 315, 913, 3814, 298, 272, 5701, 298, 14951, 298, 733, 24673, 6620, 28793, 304, 2822, 477, 272, 21712, 6992, 2373, 574, 6666, 28723, 13, 13, 3381, 368, 2699, 707, 3629, 1871, 442, 506, 707, 4224, 28725, 4665, 511, 459, 10816, 9647, 298, 3754, 528, 28723, 1984, 4927, 2962, 349, 396, 532, 28723, 5354, 426, 28818, 23769, 28723, 675, 28725, 304, 586, 4126, 1474, 349, 28705, 28734, 28787, 28705, 28783, 28770, 28705, 28740, 28774, 28705, 28781, 28782, 28705, 28787, 28783, 28723, 315, 837, 2632, 438, 574, 21864, 20185, 298, 3342, 586, 4993, 297, 680, 8291, 28723, 13, 13, 15896, 368, 354, 9868, 586, 4993, 28723, 315, 913, 3814, 298, 272, 5701, 298, 5175, 574, 1918, 304, 14951, 298, 733, 24673, 6620, 28793, 28742, 28713, 5317, 2288, 28723, 13, 13, 28735, 1814, 263, 723, 28725, 13, 13, 13389, 266, 262, 500, 9312, 426],
    'total_duration': 94101055500,
    'load_duration': 3666299100,
    'prompt_eval_count': 180,
    'prompt_eval_duration': 2098953000,
    'eval_count': 442,
    'eval_duration': 88334970000}



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

def envoyer_email(destinataire, expediteur, text):
    # Créer un objet MIMEMultipart pour le message
    message = MIMEMultipart()
    message['From'] = expediteur
    message['To'] = destinataire

    subject = re.search(r"Subject:(.*)", text)
    subject = subject.group(1).strip()
    message['Subject'] = subject
    text = re.sub(r"Subject:(.*)", "", text)
    text = re.sub(r"\n\n", "", text,1)
    print(text)

    # Ajouter le contenu du message
    message.attach(MIMEText(text, 'plain'))
    
    message.attach(contenu())

    
    # Établir une connexion avec le serveur SMTP de Gmail
"""  serveur_smtp = smtplib.SMTP('smtp.gmail.com', 587)
serveur_smtp.starttls()

# Se connecter au compte Gmail
serveur_smtp.login(username, mot_de_passe)

# Envoyer le message
serveur_smtp.send_message(message)

# Fermer la connexion
serveur_smtp.quit()"""


envoyer_email("jean", "anto", output['response'])