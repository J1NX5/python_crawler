# Verwende das offizielle Python-Image als Basis
FROM python:3.8

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen (requirements.txt) in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Codes in das Arbeitsverzeichnis
COPY . .

# Führe den Python-Crawler aus
CMD ["python", "scapy", "crawl", "my_spider"]