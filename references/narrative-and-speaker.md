# Narrative, content rules, fact-checking, and presenter experience

## 1. One-by-one discovery & reading source materials first

- Read all user-supplied files, data, and visuals completely before asking any clarifying questions.
- When key context is missing (objective, audience, duration, tone, core takeaway, slide count, or brand URL/logo), ask **one question at a time** and wait for the answer so each response shapes the next question.

## 2. Three non-negotiable content rules

1. **Max ~30 words per slide body ("No wall of text!"):**
   - The slide body (excluding the slide title) must not exceed roughly **30 words**.
   - Audiences read a crowded slide instead of listening to the speaker. If a critical idea needs more words, tighten the phrasing or split it across two slides. Never shrink body text below `28px` to cram more text.
2. **Slide variety (≥50% non-bullet slides):**
   - At least **half of the slides** (rounded up) must be built around a single strong statement, short passage, giant metric, or verified quote — never a continuous stream of bullet lists.
3. **Strict fact-checking & source separation:**
   - Every statistic, number, date, or quote placed on a slide must be verified against a reliable primary source (or marked explicitly as user-provided internal data).
   - If a claim cannot be verified, mark it `[VERIFY: <claim>]` / `[לאמת: <הנתון>]` or `[COMPLETE: <missing info>]` / `[להשלים: <מה חסר>]` during drafting and ask the user whether to replace, remove, or rephrase it. Never ship unresolved markers in a final deck.
   - **Never clutter the slide canvas with citation URLs or bibliography lines.** Keep full sources (organization/publication, year, link) in the speaker notes or a separate sources block delivered alongside the deck.

## 3. Build the argument & offer three opening hooks

Capture: audience, context, duration, objective, one remembered message, desired action, proof available, presenter credibility, and likely objections.

For **Slide 1 (the opening hook)**, propose **3 distinct opening variants** for the user to choose from:
1. **Story / relatable scenario:** use the presenter's real story if provided; otherwise write a second-person scenario the audience immediately recognizes (without inventing fake names).
2. **Provocative question:** a sharp question that exposes the core tension or cost of the status quo.
3. **Verified surprising statistic:** a verified number that reframes the topic at a glance.

Use this default timing shape across the deck when no stronger structure fits:

- **Opening (~15%):** earn attention, establish relevance, and state what the audience will gain.
- **Body (~70%):** organize around at most three memorable ideas, each with proof, example, demo, story, or contrast.
- **Close (~15%):** synthesize, make the action specific, and close a loop opened at the start.

Plan an attention change every 5–10 minutes: a question, story, live interaction, striking visual, physical pause, demo, short clip, or temporary blank screen.

## 4. Slide-plan schema

For every slide record:

| Field | Purpose |
|---|---|
| ID | Stable code/notes reference independent of slide order |
| Job | The single thing this slide must accomplish |
| Message | One sentence the audience should understand (body ≤ 30 words) |
| Visual object | What the audience *sees* (the concrete visual object, chart, mockup, or photograph) |
| Buildup | How each click transforms the visual composition (never just "add another bullet line") |
| Speaker beat | What the presenter says/does, plus verified source citation if the slide has a stat/quote |
| Time | Target minutes or seconds |
| Fallback | Backup if a demo, link, network, or audience interaction fails |

The sum of slide timings must match the talk duration. Also define a shortened route: which slides/fragments can be skipped without breaking the argument.

## 5. Presenter controls

For web decks, prefer:

- Arrow/space navigation plus visible progress and slide number (`direction: ltr` on `.slide-number` in RTL decks so `2 / 14` does not flip to `14 / 2`).
- Left click to advance only outside interactive elements (`a, button, input, [data-no-advance]`, or active text selection).
- Right click (`contextmenu`) to go back only in presentation mode (preserve browser menu in edit mode).
- `F` for fullscreen, `T` for theme toggle (when dual-theme), and a documented blank-screen shortcut.
- A subtle per-slide `data-time-hint` visible to the presenter without competing with content.
- Hash URLs for direct access to a slide during rehearsal.

## 6. Speaker notes

Write notes as actionable beats, not an essay:

1. Purpose.
2. Suggested wording.
3. Interaction or pause.
4. Proof/demo cues & verified source citation.
5. Transition sentence.
6. Target time.
7. Fallback or cut instruction.
