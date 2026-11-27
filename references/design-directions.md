# Design directions, color-per-concept, and visual language

Choose one art-direction lane, then adapt it to the brand. Do not combine unrelated visual languages.

| Lane | Best for | Palette/material | Motion |
|---|---|---|---|
| Dark cinematic | Tech, AI, launches, creative keynotes | Tinted near-black (`#0a0f1f` / `#0F172A`), electric/warm accent (`#14B8A6` / `#F59E0B`), grain, restrained glass, deep imagery | Purposeful entrances, particles/neural canvas, one major spectacle |
| Editorial minimal | Ideas, culture, leadership, premium services | Bone/ink, one muted accent, strong serif/sans typography, full-bleed photography | Slow fades, masks, calm parallax |
| Warm human | Education, community, personal brand, workshops | Cream/earth or deep night-blue with warm gold/coral, tactile shapes, friendly imagery | Soft springs, gentle reveals, character moments |
| Bold brutalist-lite | Youth, design, campaigns | High contrast, one loud color, off-grid type, solid blocks | Snappy cuts, marquees, cursor play |
| Corporate clean | Sales, boards, technical or institutional work | White/navy/charcoal, restrained accent, diagrams and proof | Minimal fades; clarity is the premium signal |

## Five core visual principles

1. **Every explanation becomes an object, not a block of text.**
   - Concept cluster → central core with color-coded glowing cards and connecting SVG wires.
   - Customer/user dialogue → realistic chat window with typing indicator (`...`) and underlying layers.
   - Metric → giant animated counter (`data-count`, `150–260px` at 1080p) with a one-line caption below.
   - Timeline / process → horizontal or vertical rail with stops that light up sequentially.
   - Case study / multi-part story → folder/file with switching tabs.
2. **Color-per-concept.**
   - Assign each distinct concept its own semantic color token (`--c`). Repeat that exact color on its icon tile, connecting wire, border glow, and heading, while keeping main slide titles neutral white/ink. Color tells the viewer what belongs to what without extra words.
3. **The buildup builds the picture — never just adds another text line.**
   - Every click must change the composition: a card flies out from the core and a wire stretches to it; a half-screen photo expands to full-screen (`width: 100%`) as a quote lands over it; a tab switches; a dark blur layer (`.verdict`) drops with the takeaway sentence.
4. **Background with depth, never flat black.**
   - Use a deep tinted gradient base with two soft radial glows tuned to the active slide's concept colors (`--ga`, `--gb`), an ambient low-density neural/particle canvas, or a full-bleed photograph with a directional readability shade (`.shade-b`, `.shade-t`, `.shade-all`).
5. **Pacing and rhythm.**
   - Never place three dense diagram/card slides in a row. After a dense slide, insert a "moment" slide: a full-bleed photograph, a single giant statement (`70–110px`), or one dominant counter. Opening, climax, and closing slides should always feel like "moments".

## Real photography vs. AI imagery

- **Real people, historical events, places, products, or documents:** always use **real photography** (e.g., free-licensed / Public Domain / CC0 photos from Wikimedia Commons). Include a clean `<div class="credit">Photographer, license, Wikimedia Commons</div>` caption (without middle dots).
- **Abstract concepts, atmosphere, or scenes with no real photograph:** use AI-generated imagery with **one consistent style sentence** appended to every prompt across the deck so all images belong to the same visual series.
- **Presentation treatments for imagery (avoid generic boxed pictures):**
  - Full-bleed with slow Ken Burns zoom + directional gradient shade under text.
  - Half-screen bleed merging seamlessly into the slide background (optionally expanding to full-bleed on the final click).
  - Zoom into a specific detail on click (`transform: scale(...)` with `transform-origin` on the detail).
  - Same image shifting state (warm-to-cold filter or sepia-to-color transition for before/after).

## Strict Zero-AI-Tell Visual Rules (Avoid)

- **No em-dashes (`—`) or en-dashes (`–`)** in visible slide text (replace with comma, colon, period, or line break).
- **No middle dots (`·`)** as decorative separators.
- **No trailing arrows (`→`, `←`)** at the end of lines.
- **No emojis inside slide titles or bullet points** (use Lucide/SVG icons instead).
- **No small eyebrow label above every single slide title** — use eyebrows only when they carry essential context, not as a mechanical template on every slide.
- **No three identical cards in a row** across consecutive slides.
- **No hollow/outlined display text** (`-webkit-text-stroke`) — always use solid fill.
- **No unrequested gradient/colored highlight word in every title** (unless the user explicitly asks for title highlights).
- **No default purple-pink AI gradient glow.**
