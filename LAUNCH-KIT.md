# 🚀 InstaPilot AI — launch kit

Everything below is ready to post. **You post it** — accounts are yours, and these
communities ban anything that looks automated or astroturfed.

---

## ⛔ First: the one thing blocking you

**The repo has no screenshots.** Ten images in the README are all badges.

For a visual product, "show me what it looks like" is the first question every visitor
has, and on r/selfhosted a post without screenshots reliably dies. This matters more
than every post below combined.

**Before launching, capture 4–6 shots:**

| Shot | Why it earns the star |
|---|---|
| The dashboard home | Proves it's real software, not a script |
| The calendar / schedule view | Shows the "set it and walk away" promise |
| A generated Short (or a short screen recording) | The actual output — the most persuasive thing you have |
| A generated carousel / image card | Same, and cheap to show |
| Settings → AI Setup | The "describe your brand in a sentence" magic moment |
| The theme picker mid-switch | Ten themes is a visible, tweetable detail |

Put them near the **top** of the README, right under the tagline. A 10–15 second GIF of
a Short being generated is worth more than any paragraph.

⚠️ **Blur or swap out** any real handle, follower count, or account name first.

---

## 📅 When to post

- **Tuesday–Thursday, 8–10am US Eastern.** Avoid Fri/Sat entirely.
- **One platform at a time**, a day or two apart. Simultaneous posting reads as spam.
- Be free for the next 4 hours to answer every comment. **Reply speed is the whole game** —
  an unanswered thread dies, and comment velocity is what drives the star burst that
  Trending measures.

---

## 1️⃣ r/selfhosted — your best single shot

Big, active, and exactly your audience: people who want to run things on their own keys.
Read their self-promotion rules first; lead with the self-hosted angle, not the AI angle.

> **Title:** I built a self-hosted AI content manager for Instagram + YouTube Shorts — your accounts, your API keys, MIT
>
> I got tired of the "AI social media manager" SaaS products that want $50/month and hold
> your accounts hostage, so I spent seven months building one that runs entirely on my own
> infrastructure.
>
> It runs one or more "brands" (a paired Instagram + YouTube account) end to end: invents a
> topic, writes the copy, designs branded image cards and carousels, renders a vertical
> Short with mood-matched royalty-free music and optional AI voiceover, publishes on a
> per-weekday schedule, cross-posts the Short as an Instagram Reel, and replies to comments
> and DMs — including voice notes, which it transcribes and answers aloud.
>
> Self-hosting specifics, since that's what matters here:
>
> - **No keys bundled.** Every API key is yours; `.env.example` ships blank.
> - Postgres + Next.js, deploys with Docker or Railway. Runs fine on modest hardware — I
>   built the whole thing on a two-core laptop with no GPU.
> - White-label from the settings UI: name, niche, persona, handles, ten themes. Nothing
>   niche-specific is hardcoded.
> - Won't double-post, won't reply to itself, recovers after a crash.
> - Every AI provider has fallbacks, so one rate-limited day doesn't cost a day of posting.
>
> It is genuinely not finished — there's no test suite yet, and I've flagged that as the
> top "good first issue" rather than pretending otherwise.
>
> MIT: https://github.com/ys941/instapilot-ai
>
> Happy to answer anything about the Meta Graph API side, which was by far the worst part.

---

## 2️⃣ Hacker News — "Show HN"

Highest ceiling, highest variance. HN rewards a personal story and punishes marketing language.

> **Title:** Show HN: Self-hosted AI that runs an Instagram and YouTube channel unattended

**First comment (post immediately after submitting):**

> I'm a medical laboratory technologist, not a developer by training. I started learning to
> code because the software I used at the bench was miserable, and this is what came out of
> seven months of nights — 198 hours, about a quarter of them between midnight and 5am, on a
> two-core laptop with no GPU.
>
> It runs a content brand end to end: topic → copy → branded cards → vertical Short with
> voiceover → publish to Instagram and YouTube → cross-post the Reel → reply to comments and
> DMs. All on your own accounts and API keys; nothing routes through a service of mine.
>
> The hard parts weren't the AI bits, which are mostly prompt plumbing. They were:
>
> - **Idempotency.** Making absolutely sure it never publishes twice or replies to itself,
>   including after a crash mid-cycle.
> - **The Meta Graph API.** Permissions, token lifetimes, and webhook HMAC verification took
>   longer than the entire video renderer.
> - **Prompt injection.** Inbound DMs are untrusted input — someone can and will try to make
>   your bot say something. Replies are constrained so a message can't steer them.
> - **Degrading gracefully.** No music available → silent Short. Provider rate-limited →
>   fallback. It should never stop posting because one thing broke.
>
> Weak spots, honestly: no test suite (top good-first-issue), and the analytics only report
> what happened rather than suggesting anything.
>
> Happy to go into detail on any of it.

---

## 3️⃣ X / Twitter — thread

Post the demo GIF in tweet 1. Media is most of the reach.

> **1/** I spent 7 months building an AI that runs an entire Instagram + YouTube channel by itself.
>
> Writes the posts. Designs the cards. Renders the Shorts. Publishes on schedule. Replies to DMs.
>
> Open-sourced it today. MIT. 🧵
>
> *[demo GIF]*

> **2/** It's not a wrapper around a posting API.
>
> Every day, per brand, it invents a topic that doesn't repeat, writes hook/body/CTA, designs
> branded cards, renders a vertical Short with mood-matched music and AI voiceover synced to
> each slide, then publishes to both platforms.

> **3/** The part I'm proudest of: it replies to voice-note DMs.
>
> Transcribes what was said, understands it, and answers back as a real voice note.
>
> In whatever language the sender used — English, Hindi, or romanised Hinglish.

> **4/** It's white-label. Nothing about my niche is hardcoded.
>
> Describe your brand in one sentence in Settings → AI Setup and it generates the entire
> config: niche, persona, handles, topics, schedule.

> **5/** Constraints, for context:
>
> · 2 CPU cores, no GPU
> · no team
> · 198 hours, ~48 of them past midnight
> · I'm a medical lab technologist, not a developer
>
> If you've been telling yourself you need a better machine — you don't.

> **6/** It's yours, free, MIT. No keys bundled, no service of mine in the middle.
>
> Contributions genuinely welcome — there are good first issues open, and the biggest gap
> (a test suite) needs no API keys at all.
>
> https://github.com/ys941/instapilot-ai

---

## 4️⃣ Other places worth a post

| Where | Angle |
|---|---|
| **r/SideProject** | The 7-months-of-nights story — that community rewards the build, not the product |
| **r/opensource** | MIT, no keys bundled, contributions wanted |
| **r/InstagramMarketing** | Purely practical: what it automates, what it costs to run |
| **dev.to / Hashnode** | A technical writeup: "How I made an unattended publisher idempotent" — evergreen traffic |
| **Product Hunt** | Only *after* screenshots exist; needs a gallery to work at all |

---

## 5️⃣ Steady, non-launch stars

Slower but compounding, and they don't depend on a launch-day spike:

- **Awesome lists** — open a PR adding InstaPilot to:
  - `awesome-selfhosted` (has a strict format; read `CONTRIBUTING.md` there carefully)
  - `awesome-ai-agents`
  - `awesome-nextjs`
- **Answer questions.** People ask "how do I automate Instagram posting?" constantly on
  Reddit and Stack Overflow. A genuinely helpful answer that mentions your tool converts far
  better than any launch post.
- **Write the setup guide** (issue #3). It'll pull in search traffic for months.

---

## 📊 What "trending" realistically takes

GitHub Trending ranks by **stars gained in a short window**, not total stars.

- **Trending in TypeScript:** roughly 80–150+ stars in a day
- **Trending overall:** several hundred — realistically needs the HN front page

One strong r/selfhosted post can do 100–300 stars in 24 hours. That is a real shot at the
language board. Overall trending needs HN to break your way, which is genuinely luck.

**Never** buy stars or join star-exchange groups. GitHub detects the patterns, and repos get
flagged and delisted — it's a permanent mark for a temporary number.

---

## ✅ Pre-launch checklist

- [ ] **Screenshots in the README** ← do not launch without this
- [ ] Social preview uploaded (Settings → General → Social preview → `scripts/social-preview.png`)
- [ ] Open the repo in a private window — does it explain itself in 10 seconds?
- [ ] Test the clone-and-run steps on a clean folder, so the first contributor doesn't hit a wall
- [ ] Clear 4 hours to reply to comments
