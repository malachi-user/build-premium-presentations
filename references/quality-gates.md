# Quality gates

## 1. Structural & Security Gate (`scripts/check_deck.py`)

Run `python3 "<skill-directory>/scripts/check_deck.py" <deck-dir>` before delivery. Every counter below must pass:

- **Valid HTML & Reveal contract:** `<!doctype html>`, `<html lang="..." dir="rtl|ltr">`, viewport meta, `Reveal.initialize(...)`, `.slides` container, unique semantic `<section id="...">` IDs, and `prefers-reduced-motion` media query.
- **Asset resolution & secret scan:** all local `src`/`href` paths resolve inside the deck root; zero embedded API keys, tokens, `.env` values, or private URLs.
- **Subresource Integrity (SRI) or vendored assets:** every external CDN `<script>` and `<link rel="stylesheet">` (e.g. `cdn.jsdelivr.net` for Reveal.js or GSAP) has `integrity="sha384-..." crossorigin="anonymous"`, or the files are vendored locally.
- **Clean production file:** `index.html` contains no leaked local edit-mode toolbar; any local editor copy (`index.local.html`, `.work/`) is excluded via `.vercelignore` / `.gitignore`.

## 2. Copy-Tell, Fact-Check & Word-Budget Gate

Checked automatically by `scripts/check_deck.py` and verified visually:

- **Zero AI tells in visible slide text:**
  - `0` em-dashes (`—`) or en-dashes (`–`) in visible copy.
  - `0` middle dots (`·`) in visible copy.
  - `0` trailing arrows (`→`, `←`, `➜`) at the end of lines.
  - `0` unresolved verification markers (`[לאמת...]`, `[להשלים...]`, `[VERIFY...]`, `[TODO...]`).
- **30-word slide body ceiling:** no slide's body text (excluding `h1`/`h2` titles, `.notes`, and `.credit`) exceeds ~30 words.
- **≥50% non-bullet slides:** at least half the slides are built around a statement, quote, counter, mockup, or photograph rather than bullet points.
- **Fact-checked sources:** every number, statistic, date, and quote has a verified source recorded in speaker notes or the separate sources block.

## 3. Browser & Visual Render Gate

Render every slide at `1920×1080`, `1440×900`, and `1366×768` (plus mobile `390×844` when shared as a web link).
> **Linux server note:** when running headless Chrome/Playwright as `root` on Linux for screenshots or PDF/PPTX export, pass `--no-sandbox` when `os.geteuid() == 0` so Chrome does not refuse to launch.

- Capture every slide after transitions settle, plus intermediate buildup steps for any slide where a later step covers an earlier one (e.g. `.verdict` overlays, expanding photos, switching tabs).
- Check horizontal and vertical overflow, clipping, overlaps, and off-canvas controls.
- Confirm `.reveal .slides section` uses Reveal's positioning (`min-height: 100%` or inner `.slide-shell`, never `position: relative; height: 100vh` on the `<section>`).
- In RTL decks, confirm `.slide-number` has `direction: ltr` so slide numbers render as `2 / 14` rather than `14 / 2`.
- Verify computed font family (`28px` minimum body text size for projection), asset loading, zero console errors, and zero failed network requests.
- Test both dark and light themes (if a theme toggle is provided) and ensure `color-scheme: dark` / `light` updates with the theme.
- Test without reduced motion and with `prefers-reduced-motion: reduce`.
- Test keyboard arrows/space, left-click advance, right-click back, fullscreen (`F`), links, focus rings, and touch swipe.

## 4. Live-Event Resilience Gate

- Offline/vendored build or tested venue network.
- Static PDF/PPTX fallback and local demo screenshots/video.
- Presenter notes, per-slide `data-time-hint`, and emergency shortened route.
- Links and QR codes verified from an actual phone on a public network.
