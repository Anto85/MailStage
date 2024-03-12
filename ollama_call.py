import ollama

def extract(output):
    text = ""
    text += output['response']
    return text

client = ollama.Client()
text = "I am a fast learner and i like programmation and new technology.I am actually in first year of ingeneering at ESEO (school of electronic and informatic), i am looking for an internship of 4 month from mid july to november. The mail reader is named:. The mail should be formal and polite. and i want to make them know that i know their company named first, i present my self but i don't give my contact information, then i show my motivation for the company, and i talk about my skills and my experiences after this i sign my mail with my contact information : My name is Antonin Urbain, my email is anto.urbain@gmail.com and my phone numbers is 07 83 19 45 78." 
output = client.generate('mistral', text)
print(output)
