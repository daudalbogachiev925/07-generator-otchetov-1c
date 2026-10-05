import yaml, re, glob

TEMPLATES = [yaml.safe_load(open(f)) for f in glob.glob('templates/*.yaml')]

def parse(text: str):
    for t in TEMPLATES:
        if any(k in text.lower() for k in t['keywords']):
            return t
    return None

def extract_dates(text):
    m = re.search(r'за\s+(\w+)', text)
    return m.group(1) if m else 'month'
