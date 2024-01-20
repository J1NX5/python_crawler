# Verwende das offizielle Python-Image als Basis
FROM python:3.8-alpine

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

RUN apk --no-cache add build-base libffi-dev

# Kopiere die Anforderungen (requirements.txt) in das Arbeitsverzeichnis
COPY requirements.txt .

# Pip auf den neusten Stand bringen
RUN python -m pip install --upgrade pip

# Installiere die Python-Abhängigkeiten
RUN pip install -r requirements.txt

# Kopiere den Rest des Codes in das Arbeitsverzeichnis
COPY . .

# Führe den Python-Crawler aus bzw my_spider
CMD ["python", "scapy", "crawl", "my_spider"]