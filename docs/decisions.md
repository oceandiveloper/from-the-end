# Entscheidungen

| Entscheidung | Grund |
|---|---|
| YouTube-Kanal vor App testen | Billiger, mit KI skalierbar, baut Publikum für die App auf. 90-Tage-Checkpoint vorher festlegen. |
| Kanal vor allem als Marketing, Werbeeinnahmen als Bonus | Monetarisierung braucht Zeit (1.000 Abos, 4.000 Stunden), YouTube geht gegen generische Massenware vor. |
| Discord statt Slack/Telegram | Nur Kevin liest mit, Free-Plan ohne Verlaufslimit, Kunden nutzen Discord/WhatsApp/Signal/Telegram, kein Slack. |
| Eine Airtable-Base für Forschung und Content | Verknüpfung Competitor Video → Source → Script ist nur in einer Base möglich. Team-Plan reicht (50k Records). |
| Nur Shortlist von Konkurrenz-Videos speichern | Base klein halten; Rest per API bei Bedarf. |
| Agenten-Kommunikation anfangs sichtbar | Kevin soll beurteilen, ob sie sinnvoll oder Rauschen ist. Logging später reduzieren. |
| Sub-Workflows als Tools, Agenten nur für Urteilsaufgaben | Kosten und Nachvollziehbarkeit. |
| Grok Bot nur als optionales Experiment (SuperGrok, ein Monat) | Hosted, Lock-in, keine Modellwahl, US-Compute. Hauptpipeline bleibt n8n. |
| Eigene Web-App statt Airtable (Entscheidung 2026-11-08) | Kevin will lernen, Web-Apps mit Claude Code zu bauen und zu hosten, um es später Kunden anzubieten. Lernchance wiegt schwerer als Zeitaufwand. Airtable zwingt die Struktur vor. Hosting auf bestehendem RunCloud (Backups, Datenbanken vorhanden). Ersetzt die Zeile "Eine Airtable-Base" oben, sobald migriert. |
| Telegram-Bot als Eingang (2026-11-08) | iPhone-Shortcut war zu umständlich, Kevin pusht Videos sonst nicht mehr. Bot ist privat (nur Kevins Chat-ID), kein zweiter Bot bis zur App. Ob Telegram Discord ganz ersetzt, ist offen. |
| Bot und Tracks immer auf Englisch (2026-11-08) | Kanal und Content werden englisch. Gilt auch, wenn Kevin Deutsch schreibt oder spricht. |
| Vom Endprodukt her bauen: Abend-, Morgen-, Midday-Tracks (2026-11-09) | Neville: Momente vor dem Einschlafen und nach dem Aufwachen. Videos dienen nur noch als Rohmaterial (Sätze, Bilder) für diese Formate, nicht als Selbstzweck. Generische Analysen haben Kevin nicht inspiriert. |
| Abend-Tracks aus Modulen (2026-11-09) | Revision wechselt mit dem Tag, die Szene bleibt (ein Wunsch, über Wochen). Module einmal vertonen, Zusammensetzen kostet keine Credits. |
| Abend-Varianten vormischen statt Mixer auf dem Server (2026-11-09) | Vier Revisionen = vier MP3s, Speicher kostet fast nichts. Spart Server-Umbau (ffmpeg, Skripte in n8n) und macht den Bot einfach: er wählt nur eine Datei. Neu prüfen, wenn Kombinationen explodieren (z.B. mehrere Szenen × Revisionen). |
| Kevins Vision Board ist die Quelle für Identitätssätze (2026-11-09) | Eigene Worte wirken stärker als erfundene. Bleibt sichtbar, soll später Teil der öffentlichen FTE-Geschichte werden. Beträge vom Board kommen nie in Tracks. |
| Stimme und Hintergrund getrennt (2026-11-09) | Kevin mag den generierten Ambient nicht, Geschmack beim Hintergrund ist individuell. Voice-only ist der Master, die App mischt einen wählbaren Hintergrund (oder keinen) beim Abspielen. Spart auch Speicher (kein Track × Hintergrund). |
| Positionierung: Selbstexperiment statt Guru (2026-11-10) | Kevin testet nacheinander die gängigen LoA-Methoden an sich (Experiments, je 7 Tage, ~90 Tage) und dokumentiert es täglich als kurzen Clip. Nische: LoA für Leute, bei denen Visualisieren nicht funktioniert (Kevin sieht nur kurze Standbilder). Thema ist der Prozess zum Erfolg, nicht die Technik. Kein Scheitern-Framing, keine Versprechen, nur innere Zeichen als Fortschritt. |
| Echter Content, KI im Hintergrund (2026-11-10) | Menschen folgen Menschen; faceless KI-LoA-Content ist überlaufen und wird von YouTube abgewertet. Kevin liefert Clips und Geschichte, KI liefert Tagesimpulse, Transkripte, später Schnitt/Titel. Erst 2 Wochen privat aufnehmen, dann entscheiden. |
| Selbstexperiment im selben Telegram-Bot (2026-11-10) | Ein Eingang für alles, Trennung über Befehle (/today, /clip, /next) statt zweitem Bot. Kein zusätzliches Setup, Kevin muss nicht zwischen Chats wechseln. |
| Background Tracks mit Nutzungsrecht pro Loop (2026-11-10) | Hintergründe kommen aus mehreren Quellen mit unterschiedlichen Lizenzen (ElevenLabs Music, Envato Elements, Uppbeat, MusicGen lokal). Feld "Usage Rights" (Private only / YouTube only / Public OK / Check) entscheidet, wo ein Loop laufen darf; die App nimmt nur "Public OK". Kostenloses MusicGen ist CC-BY-NC, daher immer "Private only". |
