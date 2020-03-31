with open('sample.txt', encoding='utf-8') as rfile:
    text = rfile.read()

print(text)

with open('output.txt', mode='w', encoding='utf-8') as wfile:
    wfile.write(text)