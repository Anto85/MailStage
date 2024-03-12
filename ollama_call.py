import ollama

def extract(output):
    text = ""
    text += output['response']
    return text

client = ollama.Client()
output = client.generate('mistral', "Tell me a joke")
print(output)
print(extract(output))
