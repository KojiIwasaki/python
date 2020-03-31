from pathlib import Path

path = Path()
for filepath in path.glob('*.py'):
    print(filepath)