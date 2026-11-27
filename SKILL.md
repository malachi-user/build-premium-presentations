---
name: build-premium-presentations
description: Design, build, redesign, or polish premium presentations and interactive web decks with strong narrative, fact-checked content, visual object composition, professional typography, cinematic or restrained motion, presenter controls, animated characters, and rigorous visual and copy-tell QA. Use for slide decks, talks, pitches, workshops, Reveal.js/HTML presentations, RTL/Hebrew decks, speaker notes, presentation templates, or when a deck feels generic, static, crowded, or visually weak.
---

# Build Premium Presentations

Create a presentation as one coherent system: fact-checked message, visual object composition, art direction, typography, motion, interaction, speaker experience, and verification. Prefer a Reveal.js/HTML web deck when rich interaction, animation, responsive projection, or editable source is valuable. Preserve the requested format when editing PowerPoint, Keynote, Google Slides, Canva, or an existing deck.

## Runtime portability

Use this skill in both Claude Code and Codex. Resolve the skill directory from the loaded `SKILL.md`; never assume the current working directory is the skill directory. Run bundled scripts and read references/assets from that resolved directory.

Use only tools that exist in the current environment. For character or AI scene generation, use Codex `image_gen` when it is available. In Claude Code, use a configured image generation tool or another user-approved image workflow. For real people, places, historical events, products, or documents, use real free-licensed photography (e.g. Wikimedia Commons) with attribution rather than AI images.

## Workflow

1. **Inspect all source material first.** Read attached files, data, and visuals completely before asking questions. Preserve the original when adapting an existing deck.
2. **One-by-one discovery (when context is missing).** Establish the audience, venue, duration, objective, one remembered message, presenter, delivery format, language/direction, slide count, brand assets (URL or logo file), and technical constraints. Ask **one focused question at a time** rather than overwhelming the user with a questionnaire. Skip questions already answered by the source material.
3. **Fact-check & plan the narrative before styling.**
   - Verify every external statistic, number, date, or quote against a reliable source. Flag any unverified claim explicitly (`[VERIFY: ...]` / `[לאמת: ...]`, `[COMPLETE: ...]` / `[להשלים: ...]`) and ask the user how to handle it — never invent numbers, quotes, or attributions.
   - Propose **3 distinct opening hooks** for Slide 1 (a real story or second-person scenario, a provocative question, or a verified surprising statistic).
   - Write a slide-by-slide plan (what the audience sees + how the buildup transforms the slide) and timing budget. Wait for user approval when working interactively. Read [references/narrative-and-speaker.md](references/narrative-and-speaker.md).
4. **Commit to one art direction & semantic color system.**
   - Extract brand colors and logo from the user's website URL or logo file when provided; otherwise choose a direction tailored to the topic and audience.
   - Assign **one consistent color per recurring concept** (used across its card, connecting wire, badge, and ambient glow) while keeping slide titles clean white/ink.
   - Define type roles (display, body, optional quote/mono), spacing, materials, imagery strategy (real photos vs. AI illustrations), motion energy, and one or two signature moments. Read [references/design-directions.md](references/design-directions.md) and [references/typography-and-rtl.md](references/typography-and-rtl.md).
5. **Turn every explanation into a visual object, not a bullet list.**
   - Select slide patterns by communication job so every slide is a picture of the idea (metric → giant animated counter, stages/dates → rail with lighting stops, dialogue → typing chat mockup, case study → tabbed folder, concept cluster → core + color-coded nodes + wires, key message → verdict overlay or underlined punchline).
   - **30-word slide body rule:** Keep slide body text (excluding the title) to **at most ~30 words**. If an idea doesn't fit, tighten it or split it into two slides; never shrink body text below `28px`.
   - **Slide variety rule:** At least **50% of slides** must be built around a single strong sentence, short passage, or verified quote rather than bullet points. Never place three dense/diagram slides in a row — alternate with "moment" slides. Read [references/slide-patterns.md](references/slide-patterns.md).
6. **Scaffold a web deck when appropriate:**

   ```bash
   python3 "<skill-directory>/scripts/scaffold_deck.py" ./my-deck --title "Presentation title" --lang en --force
   ```

   Replace `<skill-directory>` with the directory containing this `SKILL.md`. Omit `--force` unless overwriting an intentionally disposable target. The starter is in `<skill-directory>/assets/deck-starter/`.
7. **Build static composition first, then compositional buildups.**
   - Every buildup click/fragment must **transform the visual composition** (a card flies out from the core as a wire stretches to it, a half-bleed photo expands to full screen, a tab switches, a counter runs, a dark verdict layer drops) — never just append "another line, another line".
   - Add mouse response, ambient canvas, counters, or demos only where they clarify sequence or create a deliberate peak. Read [references/motion-and-interaction.md](references/motion-and-interaction.md).
8. **Add a character only when it strengthens identity, explanation, or pacing.** Follow the environment-specific tool selection above. Read [references/character-animation.md](references/character-animation.md).
9. **Add presenter notes, separate sources block, timing hints, keyboard/mouse controls, demo fallbacks, and a shortened route.** Keep citation sources in speaker notes or a dedicated sources block, not cluttering the slide canvas. Read [references/narrative-and-speaker.md](references/narrative-and-speaker.md).
10. **Run structural, copy-tell, and browser QA checks:**

   ```bash
   python3 "<skill-directory>/scripts/check_deck.py" ./my-deck
   ```

   Then read and execute [references/quality-gates.md](references/quality-gates.md). Fix all structural errors, AI tells, word-budget violations, and layout issues before delivery.

## Non-negotiable craft & zero-AI-tell rules

- **One focal point and one job per slide.** Max ~30 words in the slide body (excluding title); no text smaller than `28px` (except photo credits).
- **At least half the slides non-bulleted** (a single statement, quote, giant counter, or visual scene).
- **Zero AI tells in visible slide copy and layout:**
  - **No em-dashes (`—`) or en-dashes (`–`)** in visible slide text (use a comma, colon, period, or line break).
  - **No middle dots (`·`)** as decorative separators in visible slide text.
  - **No trailing arrows (`→`, `←`)** at the end of lines.
  - **No emojis inside slide titles or slide body text** (use SVG/Lucide icons instead; emojis are allowed only inside a simulated WhatsApp/chat bubble when realistic).
  - **No repetitive eyebrow captions** above every single slide title.
  - **No three identical cards in a row** across consecutive slides.
  - **No hollow/outlined display text** (`-webkit-text-stroke`) and no default purple-pink AI glow.
  - **No gradient or colored highlight word in titles** unless explicitly requested by the user.
  - **No unverified numbers or quotes**, and no unresolved `[VERIFY]` / `[לאמת]` / `[להשלים]` markers in the final build.
- **Security & Subresource Integrity (SRI):** When loading Reveal.js, GSAP, or other libraries from a public CDN (`cdn.jsdelivr.net`), include `integrity="sha384-..." crossorigin="anonymous"` attributes, or vendor the files locally.
- **Clean production output:** Keep any local in-browser editor (`index.local.html`, `.work/`) out of the production deployment (`index.html`, `.vercelignore`). Do not copy client secrets, private notes, or unlicensed commercial font files into public output.
- **Verify visually:** Render and inspect every slide (and multi-step buildup states where a later step covers an earlier one) at desktop and projection viewports.

## Format decisions

- Choose Reveal.js/HTML for interactive, cinematic, responsive, linkable, or code-driven decks, with optional PPTX/PDF export via headless Chrome (`--no-sandbox` when running as `root` on Linux).
- Keep PowerPoint/Keynote/Google Slides when offline editing by nontechnical collaborators is the primary need. Export animated characters as GIF/APNG for those tools.
- Use animated WebP plus GIF fallback or a sprite sheet for web characters.
- Vendor pinned Reveal/GSAP/font files for offline or filtered-network venues; otherwise pin exact CDN versions with SRI hashes and test the venue network.

## Delivery contract

Deliver the editable source, a presentation-ready build, speaker notes/timing, a separate verified sources list, attribution/licensing notes for external photos, and a short verification report (`check_deck.py` + visual review).
