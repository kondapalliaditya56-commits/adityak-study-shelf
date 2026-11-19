Study Shelf (installable offline app)

1. Upload this whole folder to any static host that gives you an https link.
   Easiest: Netlify Drop (app.netlify.com/drop), Cloudflare Pages (Upload assets) or GitHub Pages.
2. Open the https link on your tablet in Chrome (Android) or Safari (iPad).
   Android Chrome: menu > Install app (or Add to Home screen).
   iPad Safari: Share > Add to Home Screen.
3. Open it once while online. After that it works without internet, including every image.
When new chapters or notebooks are added, upload the new folder over the old one. The app shows a 'Reload to use it' note when the update has downloaded. Your progress stays on the tablet; use Backup on the shelf to keep a copy.

CALENDAR SYNC
calendar.json is refreshed every ~15 minutes by .github/workflows/cal-sync.yml from the
private iCal address of Google Calendar (repo secret CAL_ICS_URL). Study Shelf reads it
when the live connector is not available (laptop, phone, installed app).

READ ALOUD
readaloud.js adds a speaker button (bottom left) to every notebook page. Tap it to hear the page
from where you are; select text and tap Listen to hear only that. After generating new pages,
run: python3 tools/add_readaloud.py

SEARCH CHECK
python3 tools/audit_search.py checks that every search result opens an existing page and section.

HOME SCREEN
index.html has five tabs (Today, Recall, Learn, Notebooks, Progress; links like index.html#books work).
search-all.json (search across all notebooks) and mnemonics.json (mnemonic of the day) are built by
python3 tools/build_search_all.py and python3 tools/build_mnemonics.py. Re-run both after notebooks change.

READ ALOUD VOICES
The speaker button ranks the voices on the device and picks the most natural Indian English one (Edge: Neerja or Prabhat; iPhone and iPad: Rishi or Veena Enhanced; Android: Google English India). Change it in the panel. Tips are under 'More natural voices'.
