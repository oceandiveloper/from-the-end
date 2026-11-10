# Offene Punkte

## Als Nächstes (Stand 2026-11-10)
- Selbstexperiment läuft: Baseline (VVIQ + Board) ab 2026-11-10, dann 12 Methoden à 7 Tage (Airtable Experiments). Kevin morgens `/today`, abends Clip per `/clip`, nach Tag 7 Verdict setzen und `/next`. Reihenfolge in Airtable frei änderbar (Order).
- Clip-Upload mit echtem Video/Sprachnachricht testen (bisher nur Text getestet). Grenze 20 MB pro Datei (Telegram-Bot-API).
- Nach 2 Wochen: Clips sichten (Feld Usable), entscheiden, ob/wie öffentlich gestartet wird. Liste innerer Zeichen "close to the result" aus Videos zusammenstellen (keine äußeren Zeichen).
- BotFather-Menü um today, clip, next ergänzen.
- Kevin testet die Tracks (Morning, Midday, Evening ×4, Padel ×2) ein paar Tage, Feedback zu Sätzen, Tempo, Ambient.
- Neuer Fluss (mehr Inhalt, Pausen nur bei Atem/Szene/Sätzen): Kevin hört Padel After v2. Passt es, alle anderen Tracks genauso neu schreiben und vertonen (Morning, Midday, Padel Before, Abend-Module). Credits: grob 25.000 Zeichen.
- Kevin legt das Befehlsmenü in BotFather an (`/setcommands`: morning, reset, evening, padel, tracks, help).
- `/tracks` wird lang (8 Tracks). Wenn es nervt: nur Tracks ohne festen Befehl listen oder nach Gruppe sortieren.
- Morgen-Track: v1 steht (Sätze 1, 6, 9). Nächster Schritt: täglich rotierende drei Sätze.
- Video-Prozess neu: Analyse (WF5) ersetzen durch "Kandidaten herausziehen" (Lines / Phrases / Concepts, ohne Deutung) → Kevin wählt per Nummer in Telegram → Bibliothek in "Quotes / Statements" (braucht Felder Source, Type, Status, Timestamp, Own Version, Methods; vorher Freigabe). Zweck: Bausteine für Revision- und Szenen-Module. Fremde Sätze nie wörtlich in eigene Audios, Own Version nutzen.
- Bot: Ideen/Notizen ohne Link speichern.
- "Apply to me" im Bot braucht eine eigene Ausgabe (aktuell gleiche Analyse wie "Analyze").
- Hintergrund: der selbst erzeugte ffmpeg-Ambient taugt nicht (Kevin, 2026-11-09). Bot spielt vorerst nur Stimme. Bessere Hintergründe finden (2–4 Optionen, z.B. Regen, Meer, warmes Pad/Klavier), Lizenz für App + YouTube prüfen. In der App: Stimme + wählbarer Hintergrund (oder keiner), getrennt abgespielt.
- Airtable Personal Tracks: "Audio URL" zeigt jetzt auf die Voice-only-Datei. Für die App evtl. eigenes Feld für die Hintergrund-Version (vorher Freigabe).
- Workflow 7 (Pull Channel Videos) auf einem kleinen Kanal testen (z.B. Neville Creation), erst dann alle.
- Transkripte für die Shortlist holen (TranscriptAPI-Credits beachten, Agent Runs loggen). Nummer 8 ist inzwischen an "Voice Track Segments" vergeben.
- Wettbewerbsanalyse: Top 50 je Kanal, Muster bei Titeln, Hooks, Längen, Themenlücken → Insights.
- Mehr kleine AI-Kanäle (5k bis 50k Abos) recherchieren; Stichprobe ist zu stark Richtung große Human-Kanäle.
- Narc Pattren und Grace & Victory: Content Origin prüfen, Abos passen nicht zu den Views (vermutlich Kollaboration/Netzwerk).
- Discord-Bot einrichten (Zwei-Wege, Freigabe mit Formular), `fte-approvals` anlegen.
- Feld "Content Origin" pro Competitor Video (Lookup vom Kanal als Start).

## Aufräumen
- Alte Base "LoA YouTube Research" in Airtable löschen (leer, ersetzt).

## Später
- Researcher- und Supervisor-Zeitpläne.
- Freemium-Regel für Premium-Tracks, Notfall-Skript für Widerstandszustände.
- Optional: Grok Bot als Experiment für den Researcher (X-Suche).
- 90-Tage-Checkpoint für den YouTube-Test (Views pro Video, Zuschauerbindung, Abos pro 1.000 Views).
