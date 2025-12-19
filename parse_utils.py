import re

def clean_text(s: str) -> str:
    if not s:
        return ""
    return re.sub(r"\s+", " ", s).strip()

def extract_duration(text: str) -> str:
    if not text:
        return ""
    m = re.search(r"\b\d+\s*min\b", text)
    return m.group(0) if m else ""

def extract_price(text: str) -> str:
    if not text:
        return ""
    m = re.search(r"\b\d[\d\s]*\s*kr\b", text)
    return m.group(0) if m else ""

