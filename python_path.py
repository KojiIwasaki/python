from pathlib import Path

terms = {'for':0, 'if':0, 'else':0}
path = Path()
for filepath in path.glob('*.py'):
    with open(filepath, encoding='utf-8') as rfile:
        text = rfile.read()
    for term in terms:
        cnt = text.count(term)
        terms[term] += cnt

print(terms)