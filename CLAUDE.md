# From The End (FTE)

Law-of-Assumption-Projekt (Neville Goddard / "from the end"): Audio-Tracks und Practices, zuerst für Kevin selbst, später als App und YouTube-Kanal. Gebaut mit Airtable + n8n + Discord, mit KI-"Mitarbeitern" (Researcher, Writer, Reviewer, Producer, Supervisor), die im Hintergrund arbeiten.

## Warum es das Projekt gibt (Leitregel)
1. Es soll Menschen wirklich helfen und Kevin Sinn und den gewünschten Lebensstil geben.
2. Kevin ist der größte Tester: Alles, was gebaut wird (Content, Features), muss auch ihm selbst bei seiner LoA-Praxis helfen. **Diese Regel gilt für jede Entscheidung.**
3. Selbst wenn alles scheitert, bleibt das Know-how für ein Angebot "KI-Mitarbeiter für Kleinunternehmer" bei seinen Kunden.

Kein Schönreden: Der Erfolgsfall ist nicht garantiert (Zeit ist das echte Risiko, Arbeit an Kundenprojekten konkurriert). Bei Schwächen in Plänen widersprechen, nicht zustimmen.

## Arbeitsweise mit Kevin
- Deutsch, "du". Kurz, direkt, vollständige Outputs, keine Platzhalter.
- **Erst den bestehenden Zustand lesen** (Airtable-Schema, n8n-Workflows per MCP), dann handeln. Nie aus dem Gedächtnis annehmen, was existiert. Keine neuen Tabellen/Felder anlegen, ohne vorher zu prüfen, ob es sie schon gibt.
- Terminal-Befehle komplett und copy-paste-fähig.
- Nichts Irreversibles (löschen, publizieren, Audio/Video erzeugen, Credits verbrauchen) ohne seine Freigabe.

## Architektur
- **Airtable = Single Source of Truth** (Base "From The End"), alle Tools austauschbar. Team-Plan, 50.000 Records pro Base. Forschung und eigener Content bleiben bewusst in **einer** Base (Links über Tabellen).
- **n8n** (n8n.oceandiveloper.com): alle Workflows. Deterministische Sub-Workflows sind die "Tools", Agenten (Supervisor, Researcher, Writer, Reviewer) orchestrieren sie nur dort, wo Urteilsvermögen nötig ist.
- **Discord** (Server "From The End"): Benachrichtigungen, Freigaben, ein Channel pro Mitarbeiter. Aktuell Incoming Webhooks, später ein Bot für Zwei-Wege (Freigabe-Buttons, Änderungswünsche per Formular).
- Audio: ElevenLabs (Stimme "James") → Bunny Storage/CDN (`from-the-end-audio.b-cdn.net`).
- Transkripte: TranscriptAPI (1.000 Credits, sparsam einsetzen). Video-/Kanaldaten: YouTube Data API v3.
- Claude API für Analyse/Skripte.

## IDs (zur Orientierung, Schema immer live per MCP prüfen)
- Airtable Base: `appIr46GFzpjhPyzV`
- Tabellen: Sources `tblmnHPjID3udL8ft`, Channels `tbloriljxsEbTU7L9`, Competitor Videos `tblr45nOywfFRIElD`, Agent Runs `tblRS4Rd6RsLDgjpE`, Personal Tracks `tblUbBe02AXXGAXtl`. Weitere (Topics, Methods, Insights, Scripts/Tracks): per MCP lesen.
- n8n-Credentials: "From The End Airtable", "YouTube Data API V3", "TranscriptAPI From The End". Keine Secrets ins Repo.

## Workflows (Stand Anfang Oktober 2026; per n8n-MCP verifizieren)
1. **Save Video Source**: Webhook `fte-save-video-source` (iOS-Share-Sheet-Shortcut, Frage "Why this, right now?" wird als Notiz gespeichert). Duplikat-Check, legt Source an, ruft 2 und 3, Discord-Meldung `#fte-sources`.
2. **Pull Meta Data (YouTube)**: Titel, Kanal, Daten, verknüpft/legt Channel an.
3. **Pull Transcript (YouTube)**: TranscriptAPI → Transcript, Dauer, Wortzahl (lange Transkripte: Feld ~99.999 Zeichen, Volltext als Anhang). Manueller Webhook `fte-sources-pull-transcript`.
4. **Pull Channel Profile (YouTube)**: Channel-ID, Abonnenten, Videoanzahl, Beschreibung (ID/Handle/Name als Fallback).
5. **Analyze Source**: Claude → Key Points, Personal Relevance, Coverage Note (gegen Topics/Methods), optional Suggested Method; Post in `#fte-sources`.
6. **Personal Track (Stuck Moment)**: iOS-Diktat → Claude-Skript (~1.000 Wörter) → ElevenLabs → Bunny → Discord `#fte-personal`. Webhook `fte-personal-tracks-new`.
7. **Pull Channel Videos (YouTube)** (neu, noch ungetestet): Kanalstatistik + alle Uploads, Shortlist (Top 20 Views, Top 10 Trending, 10 Neueste) → Competitor Videos, Log in Agent Runs. Webhook `fte-channels-pull-videos`.
0. **Telegram Bot** (`nmVilblsg7oeJMaC`, Bot `from_the_end_bot`, nur Kevins Chat-ID `8045566023`): YouTube-Link → "Why this, right now?" mit Buttons (Something specific / Analyze / Apply to me / Just save / Discard), Antwort auch per Sprache (ElevenLabs STT) oder Text → ruft WF1 mit `mode` + `chatId`. `/morning`, `/reset` schicken die Tracks direkt (Map `DAILY` im Node "Route Update"), `/evening` (Work/Family/Money/Calm) und `/padel` (Before/After) zeigen Buttons (Map `MENUS` + Nodes "Ask Evening"/"Ask Padel"), `/today`, `/clip`, `/next` steuern das Selbstexperiment (WF11–13; Videos/runde Videos gehen immer als Clip, Sprachnachricht/Text nur direkt nach `/clip`), `/help` listet die Befehle, `/tracks` listet Personal Tracks mit Audio, `/tN` schickt das Audio. **Alles im Bot auf Englisch**, auch wenn Kevin Deutsch schreibt.
8. **Voice Track Segments** (`47UGddXwiWjcdPVM`): Webhook `fte-tracks-voice-segments` mit `{trackId, speed, segments[{key,text,previousText,nextText}]}` → ElevenLabs "James" pro Abschnitt → Bunny `tracks/{trackId}/{key}.mp3`. Pausen und Ambient werden danach mit ffmpeg gemischt (aktuell lokal mit `scripts/`, siehe `docs/tracks/README.md`).
9. **Upload Audio File** (`gGf3JiVAgJqCakPO`): Webhook `fte-upload-audio?path=tracks/...mp3`, Header `x-fte-token` (Token nicht im Repo), Datei multipart → Bunny.
10. **Extract Statements** (`HMY7W8UzaoLnlWF2`, aktiv seit 2026-11-10): Webhook `fte-sources-extract-statements` mit `{recordId, force?, maxStatements?}`. Claude zerlegt das vorhandene Source-Transkript in max. 20 Aussagen (Wortlaut exakt), ordnet Typ + Form zu → Tabellen **Statements** `tblfj3u0PqdiOswXx` und **Statement Types** `tblAm1AmccZf2n1IA` (neue Typen per Typecast, Kern wird nachgetragen), Log in Agent Runs. Keine TranscriptAPI-Credits. Hintergrund: `docs/aussagetypen-minitest.md`.
11. **Experiment Today** (`hHH75yRjkWQRfygF`): Webhook `fte-experiment-today` `{chatId}`. Aktives Experiment (Tabelle **Experiments** `tblmpPKd6W4w1v3Qf`) + letzte Clips → Claude schreibt Übung, Clip-Fokus, Stichworte, Einstiegssatz für den Tag → Telegram. Zeitzone der Workflows 11–13: Europe/Berlin.
12. **Save Experiment Clip** (`lJGoMnQSQxYOZLKu`): Webhook `fte-experiment-clip` `{chatId, kind video|voice|text, fileId, text}`. Telegram-Download (max. 20 MB) → Bunny `clips/` + ElevenLabs STT → **Experiment Log** `tblFz9rNuW3RfNJ2m` (mit Experiment + Tag) → Bestätigung mit Transkript.
13. **Experiment Next** (`4yV40Pk3WxZkUJ82`): Webhook `fte-experiment-next`. Aktives Experiment → Done, nächstes Queued (kleinste Order) → Active mit Start heute, dann WF11.

Änderungen an 1 und 5 (2026-11-08): WF1 liest `mode`/`chatId`; `mode=keep` holt nur Metadaten (kein Transkript, keine Analyse); Duplikat-Meldung geht an Telegram, wenn `chatId` gesetzt. WF5 schickt die Analyse zusätzlich an Telegram (kompakt, einklappbare Quotes, immer Englisch) und hängt neue Methoden an, statt die Verknüpfung zu überschreiben.

## n8n-/Airtable-Konventionen (aus Fehlern gelernt)
- Sub-Workflows: Trigger "Called by Workflow" + manueller Backfill-Webhook, dann "Normalize Input".
- Airtable Update: `id` gehört in `columns.value`, `matchingColumns: ["id"]`. Fehlt das, schreibt n8n in den falschen Record.
- **Typecast immer an** (sonst scheitern Selects/Links still).
- AKTION-/ACTIONS-Felder werden **am Ende** des Workflows zurückgesetzt, nie am Anfang.
- Echte Workflow-IDs in Execute-Workflow-Nodes, keine Platzhalter.
- Airtable "Search" liefert Felder auf oberster Ebene (nicht unter `fields`).
- Discord-Webhook-Nachrichten pushen nicht aufs Handy, daher `@mention`; iOS "Mobile Notification Delay" auf Never.
- Je Aktion ein eigener Workflow, kein kombinierter Mega-Workflow.

## Inhaltsregeln für LoA-Content
- LoA dreht sich um **Identität und inneren Zustand**, nicht um das Wie. Persönliche Tracks enthalten keine Strategien, Pläne, Beträge oder Zusicherungen, dass etwas klappt.
- Tracks sprechen immer mit "you", nie "he"/"she" (geschlechtsneutral, Kevin will sie auch an Frauen testen). Revision: alten Moment von außen sehen, neue Version von innen erleben.
- Identitätssätze nur über Kevin selbst, kein Gefühl behaupten, das er gerade nicht hat, höchstens dreimal pro Track.
- Quelle für Kevins Identität und Ziel-Zustand: `docs/kevin-2.0.md` (sein Vision Board Level 1 → Level 100, mit Foto). Identitätssätze möglichst in seinen eigenen Worten von dort nehmen. Kevin will das Board später öffentlich zeigen, als Teil der FTE-Geschichte.
- Jeder Content für andere muss auch für Kevin selbst funktionieren.

## Prozess und offene Punkte
Siehe `docs/process.md`, `docs/decisions.md`, `docs/open-items.md`.
