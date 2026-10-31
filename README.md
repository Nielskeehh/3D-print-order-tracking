# Printjes – 3D-print bestellingen

Simpele iPad-app (PWA) om 3D-print bestellingen bij te houden. Alles staat lokaal op de iPad (IndexedDB), er is geen server of account nodig.

## Online zetten (GitHub Pages)
1. Maak op github.com een nieuwe **public** repository, bijv. `Printjes`.
2. *Add file → Upload files* → sleep deze bestanden erin: `index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png` → *Commit changes*.
3. *Settings → Pages* → Source: *Deploy from a branch*, branch `main`, map `/ (root)` → *Save*.
4. Na ±1 minuut staat de app op `https://<gebruikersnaam>.github.io/Printjes/`.

## Op de iPad installeren
Open de link in **Safari** → deelknop → **Zet op beginscherm**. Daarna opent hij als losse app, ook zonder internet.

## Back-up
Tandwiel ⚙️ → *Back-up maken* (met foto's) → bewaren in Bestanden/iCloud. Zelfde plek om terug te zetten.

## Updates
Bij elke wijziging aan een bestand: in `sw.js` `CACHE_NAME` ophogen (`printjes-v1` → `printjes-v2`) en `sw.js` meeuploaden, anders blijft de iPad de oude versie tonen.
De gegevens van je dochter staan niet in deze bestanden en blijven bij een update gewoon bewaard.
