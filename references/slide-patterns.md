# Slide patterns by communication job (Content-to-Visual translation)

Select patterns because they turn an idea into a visual object; change composition between neighboring slides.

## Content-to-Visual Translation Table

| What is in the content | What to build on the slide |
|---|---|
| **Opening question or hook statement** | **Moment slide:** the sentence alone, giant (`70–110px`), with a symbolic object, ambient canvas, or full-bleed photo behind it, and a second beat revealed on click |
| **3–5 concepts / types / components / agents** | **Core & satellites (Hub):** central core/self node in the middle, a color-coded glowing card for each concept (`--c`), and SVG wires stretching from the core to each node in sequence |
| **Term and definition** | **Dictionary card:** giant term, secondary Latin/technical name in `<bdi>`, and a crisp definition below |
| **Case study / story with stages** | **Tabbed file/folder:** paper/glass folder with tabs that highlight per click while pages swap in place (`.stack`) |
| **Dialogue (customer/agent, user/system)** | **Chat mockup:** phone or chat window with typing indicator dots (`...`) before each message arrives, followed by an "under the surface" breakdown |
| **Famous or verified quote** | **Portrait/moment + quote:** full-bleed or half-bleed real photograph of the person/moment, then the quote in a large display/serif face |
| **Key statistic or metric** | **Giant animated counter:** dominant number (`data-count`) that counts up on entry, unit label, and a one-line interpretation below (source kept in notes/sources block) |
| **Dates, milestones, or sequential steps** | **Rail / timeline:** horizontal or vertical track (`.rail`) with stations/stops that light up one by one on click |
| **Before / after or two contrasting sides** | **State shift or split reveal:** the same image transforming (e.g. warm to cold, sepia to color) or an asymmetric 7/5 contrast layout |
| **Real person, place, event, or document** | **Real photograph:** full-bleed with readability shade, half-bleed, or tilted archival print gallery (`.print-photo`) with Wikimedia Commons attribution |
| **Core takeaway / final verdict** | **Verdict overlay or punchline:** dark blurred overlay dropping over the slide with a giant statement (`.verdict`), or a closing line with an animated underline (`.punch`) |
| **Dense text that cannot be cut further** | **Never shrink the font.** Split into compositional stages: a lead title that rises to the top on click 1, earlier items dimming as new ones arrive (`.dim-past`), or in-place swapping panels (`.stack`) |

## Additional pattern notes

- **Character beat:** point, react, celebrate, warn, or transition via `data-mascot`; never park a mascot in the exact same pose on every slide.
- **CTA / Closing loop:** return to the opening question or visual motif, present one specific action (button, link, or QR code), and leave one memorable line — never end with a generic "Thank You / תודה על ההקשבה" slide.

## Markup conventions for web decks

- Give each `<section>` a stable semantic `id`.
- Put timing in `data-time-hint` and optional behavior in data attributes such as `data-effect`, `data-mascot`, `data-stagger`, and `data-accent`.
- Use Reveal `.fragment` (or staged buildup classes) for narrative sequence; avoid fragile selectors tied to slide numbers.
- Keep the default DOM state accessible and visible if optional animation scripts fail.
- Notice on reveal.js CSS: never set `position: relative` or `height: 100vh` directly on `.reveal .slides section` (it overrides Reveal's `position: absolute` and stacks slides vertically off-screen); use `min-height: 100%` or an inner `.slide-shell` container instead.
- Mark interactive controls with `data-no-advance`.
