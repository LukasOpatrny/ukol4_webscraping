import requests
from bs4 import BeautifulSoup

# URL stránky, kterou chceš scrapovat
url = "https://www.csfd.cz/tvurce/180726-lukas-opatrny/prehled/"

# Hlavička, aby server neházel 429 (blokace robotů)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# Stažení stránky
response = requests.get(url, headers=headers)
response.raise_for_status()  # zastaví skript při chybě

# Parsování HTML
soup = BeautifulSoup(response.text, "html.parser")

# --- 1) VÝPIS JEDNÉ SKUPINY PRVKŮ (například odkazů)
links = soup.find_all("a")  # najde všechny <a> tagy
print("Prvních 20 odkazů na stránce:")
for link in links[:20]:
    print("-", link.get("href"))

print("\n---\n")

# --- 2) NALEZENÍ ELEMENTU S KONKRÉTNÍM TEXTEM
hledane_jmeno = "Lukáš Opatrný"

# hledá text v libovolném tagu – vrátí první výskyt
element = soup.find(string=lambda t: t and hledane_jmeno in t)

# --- 3) VÝPIS NADŘAZENÉHO TAGU A JEHO TEXTU
if element:
    parent = element.parent  # vezme nadřazený HTML tag
    print("Nadřazený tag:", parent.name)
    print("Text uvnitř:")
    print(parent.get_text(strip=True))
else:
    print("Text s jménem nebyl nalezen.")
