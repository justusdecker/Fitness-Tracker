# Mitwirken am Projekt (Contributing Guidelines)

Vielen Dank für dein Interesse, dieses Projekt mitzubestalten! Jede Hilfe – egal ob neue Produktdaten, Code-Optimierungen oder UI-Anpassungen – ist herzlich willkommen.

---

## Wo du mitwirken kannst

* **Ernährungstabellen & Produkt-Einträge:** Erfassen neuer Lebensmittel und Nährwertdaten im YAML-Format.
* **Erweiterung von Funktionen:** Neue Features für Tracker, Auswertungen oder Berechnungen.
* **Verbesserung der Benutzeroberfläche (UI):** Optimierung von Layouts, Animationen und User Experience in Flet.
* **Optimierungen & Bugfixes:** Performance-Verbesserungen, Refactoring und Beheben von Fehlern.

---

## GitHub Issues & Workflow

1. **Issue durchsuchen:** Prüfe vor dem Erstellen eines PRs, ob bereits ein passendes **GitHub Issue** existiert.
2. **Issue erstellen:** Wenn du einen Bug findest oder ein neues Feature planst, öffne zuerst ein Issue, um deine Idee kurz abzustimmen.
3. **Pull Request (PR) einreichen:**
   * Forke das Repository und erstelle einen neuen Feature-Branch (`git checkout -b feature/mein-feature`) oder wenn es ein Item Eintrag ist (`git checkout -b item/mein-item`)
   * Committe deine Änderungen mit verständlichen Commit-Nachrichten.
   * Erstelle einen PR mit einer kurzen Beschreibung deiner Änderungen.

---

## Anleitung: Nährwertdaten & Produkte beitragen (`.yml`)

Für die Ernährungstabellen werden Datensätze im Repository als **YAML-Dateien (`.yml`)** abgelegt. Diese werden beim ersten App-Start automatisch in die lokale SQLite-Datenbank importiert und gegen das `Item`-Modell validiert.

### Struktur einer Produkt-Datei

Jeder YAML-Eintrag muss den Attributen des `Item`-Modells entsprechen. 

#### Beispiel für einen YAML-Eintrag:

```yaml
titel: "Haferflocken Zart"
beschreibung: "Vollkorn-Haferflocken extrazart"
zutaten: "100% Vollkorn-Haferflocken"
vorschaubild: "https://example.com/images/haferflocken.jpg"
barcode: "4001234567890"
marke: "MusterMarke"
serviermenge: "50g"
gewicht: "500g"
allergene: "Gluten"
nova_gruppe: "1"
nutri_score: "A"

# Nährwerte (Haupt-Makros) - Werte IMMER mit Einheit angebend (z.B. 370kcal, 7g)
kalorien: "370kcal"
fett: "7g"
davon_gesättigte_fettsäuren: "1.2g"
kohlenhydrate: "59g"
ballaststoffe: "10g"
zucker: "1g"
protein: "13g"
salz: "0.02g"

# --- NutrientSet Sub-Kategorien (Nur erlaubte Keys verwenden!) ---

FETTSÄUREN_UND_ZUCKER:
    einfach_ungesaettigte_fettsaeuren: "2.5g"
    mehrfach_ungesaettigte_fettsaeuren: "2.8g"
    omega_3: "0.1g"
    omega_6: "2.4g"
    trans_fettsaeuren: "0g"
    mehrwertige_alkohole: "0g"

MINERALSTOFFE_SPURENELEMENTE:
    kalium: "350mg"
    kalzium: "54mg"
    magnesium: "130mg"
    eisen: "4.4mg"
    zink: "3mg"

VITAMINE:
    A: "0µg"
    E: "0.6mg"
    K: "0µg"
    C: "0mg"
    D: "0µg"
    B1: "0.5mg"
    B2: "0.15mg"
    B3: "1mg"
    B5: "1.1mg"
    B6: "0.16mg"
    B7: "20µg"
    B9: "87µg"
    B12: "0µg"
    beta_carotin: "0mg"

AMINOSÄUREN:
    bcaa: "2.2g"
    eaas: "4.5g"
    l_glutamin: "1.8g"
    l_arginin: "0.8g"
    l_citrullin: "0g"

PERFORMANCE_SUPPLEMENTS:
    kreatin: "0g"
    beta_alanin: "0g"
    taurin: "0g"
    koffein: "0mg"
    l_carnitin: "0mg"
    l_theanin: "0mg"
    n_acetyl_l_tyrosin: "0mg"
```
