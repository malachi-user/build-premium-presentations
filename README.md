# build-premium-presentations

Premium, studio-grade presentations and interactive web decks: content-first narrative & fact-checking, visual object composition, color-per-concept art direction, Hebrew RTL & English LTR typography, cinematic motion, presenter controls, animated characters, and an automated structural + zero-AI-tell QA gate.

An agent skill for [Claude Code](https://claude.com/claude-code) and Codex. `SKILL.md` sits at the repository root, so installing is a single `git clone`.

## Key capabilities

- **Content-first & fact-checked:** one-by-one discovery, 3 opening hook options (story, question, verified statistic), strict **30-word slide body ceiling**, **≥50% non-bullet slides**, and verified sources kept separate from slide canvas clutter.
- **Every slide is a visual object, not a list:** translates metrics into giant animated counters, stages into lighting rails, dialogues into typing chat mockups, case studies into tabbed folders, and concept clusters into core-and-wire hubs.
- **Color-per-concept & compositional buildups:** each concept gets a consistent semantic color across tiles, wires, and ambient glows; every click transforms the composition rather than appending bullet lines.
- **Zero AI-tells enforcement:** automated `scripts/check_deck.py` flags em-dashes (`—`), middle dots (`·`), trailing arrows, unresolved `[VERIFY]`/`[לאמת]` markers, slides exceeding the 30-word body budget, and CDN scripts missing Subresource Integrity (SRI).
- **RTL/Hebrew & LTR/English ready:** logical CSS, mixed-direction `<bdi>` isolation, curated free Hebrew font pairings, and animated character pipeline.

## Live demo

A Hebrew RTL launch deck with a live neural background, animated counters, a reactive mascot, and a simulated WhatsApp chat: [`examples/binart-launch-deck`](examples/binart-launch-deck/).

## Install

### Claude Code

```bash
# For all your projects
git clone https://github.com/malachi-user/build-premium-presentations.git ~/.claude/skills/build-premium-presentations

# Or for a single project
git clone https://github.com/malachi-user/build-premium-presentations.git <project>/.claude/skills/build-premium-presentations
```

### Codex

```bash
git clone https://github.com/malachi-user/build-premium-presentations.git ~/.codex/skills/build-premium-presentations
```

Restart the agent session after installing so it discovers the skill.

## What's inside

```text
build-premium-presentations/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── deck-starter/            # RTL/LTR Reveal.js starter with SRI, pointer halo & reduced-motion path
├── examples/
│   └── binart-launch-deck/      # Full 8-slide Hebrew RTL interactive launch deck
├── references/
│   ├── character-animation.md   # Mascot/character generation & WebP/GIF loop pipeline
│   ├── design-directions.md     # Art direction lanes, color-per-concept & zero-AI-tell visual rules
│   ├── motion-and-interaction.md# Compositional buildups, pointer halo, canvas performance & reduced motion
│   ├── narrative-and-speaker.md # One-by-one discovery, 3 hooks, fact-checking, 30-word rule & presenter UX
│   ├── quality-gates.md         # Structural, copy-tell, SRI, browser & live-event verification gates
│   ├── slide-patterns.md        # Content-to-visual object translation table & markup conventions
│   └── typography-and-rtl.md    # Display/body roles, 28px floor, Hebrew font pairings & RTL isolation
├── scripts/
│   ├── scaffold_deck.py         # Scaffold a new RTL or LTR web deck from the bundled starter
│   └── check_deck.py            # Automated structural, SRI, 30-word budget & zero-AI-tell preflight
├── README.md
└── LICENSE
```

## License

MIT. No private business material is included.
