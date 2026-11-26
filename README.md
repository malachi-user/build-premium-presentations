# build-premium-presentations

Premium, studio-grade presentations and interactive web decks: narrative, art direction, typography, cinematic motion, presenter controls, animated characters and a strict visual-QA gate. RTL/Hebrew ready, with a live deployable demo.

An agent skill for [Claude Code](https://claude.com/claude-code) and Codex. `SKILL.md` sits at the repository root, so installing is a single `git clone`.

## Live demo

A Hebrew RTL launch deck with a live neural background, animated counters, a reactive mascot and a simulated WhatsApp chat: [`examples/binart-launch-deck`](examples/binart-launch-deck/).

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
├── assets/
├── examples/
├── references/
├── scripts/
├── README.md
└── LICENSE
```

## License

MIT. No private business material is included.
