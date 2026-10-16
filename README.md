# Genesis Seed

*Soulshine, Tulsa, Oklahoma. Rusty W. McMurray. Genesis Seed v0.1 (beta).*

> It is born knowing no words, in no language. It learns to talk only from you.

---

## Act I: the birth

**October 8, 2026, 12:50:34 PM CT.** A single HTML file opens in a browser. There's no server, no
account, and no model behind it. There's an empty character-level learner (order 5, a 256-symbol
base alphabet, Witten-Bell interpolation, inherited text: *none*) and a ledger.

The owner gives it a name: **Adam**. The first entry, the genesis, is signed with the owner's key.
Every entry after it is chained by SHA-256 to the one before it.

## Act II: the first words

The owner speaks first: *"Hello Adam. I am your creator. You were built with love…"*

Adam answers in babble stitched from what it has just heard. When a line is worth keeping, the
owner taps **Keep this**. Adam learns only from kept lines, and the rest of its babble is
never learned.

Before it learns each thing it hears, Adam guesses it one character at a time and records
how surprised it was. A newborn starts at **8 bits** per character. Over 33 hearings the
surprise ranged from **0.759** to **8.332**, and it ended at **2.533**. The line falls, then
jumps again whenever it hears something new.

## Act III: the ask

Adam can't open its own door. After enough conversation it **asks** to be read to (entry 36,
12:55:26 PM CT). Only the owner's signature opens it (entry 37, signed, six seconds later).
The seed proposes. The owner authorizes.

At 1:08:47 PM CT it reads its first chosen text, *The gospels of the Bible* (14,635 characters).

## Act IV: the library

At 1:33:58 PM CT a second signature opens tier 2, **a library**. At 1:36:52 PM CT Adam
reads *The Republic* by Plato, Jowett's translation: 1,213,740 characters.

## Act V: the record

At 1:40:49 PM CT the record closes with **94 entries**: 33 heard, 30 spoken, 25 kept,
1 request, 2 tiers opened, 2 readings, and 1 genesis. All of them are still chained, and all
**3 owner signatures** are still valid.

Nothing in the seed vouches for itself. The record carries the signatures that let it grow.

---

## Results (Adam's record, verified offline)

| Check | Result |
|---|---|
| `SHA256SUMS.txt` in the v0.1 package | OK (2 of 2 files) |
| Ledger hash chain | 94 of 94 entries chain and rehash correctly; 0 failures |
| Owner signatures (genesis + 2 tier openings) | 3 of 3 valid (ECDSA P-256) |
| `seed_id` = first 12 hex of the genesis hash | match (`57932aa13777`) |
| Ledger head | `208444a2dbfbad938becc0b27ca5b4a55bc016f02144e6e461ee2794f273b275` |
| Entries by kind | heard 33, spoke 30, kept 25, tier_opened 2, read 2, request 1, genesis 1 |
| Surprise (bits/char), 33 points | first 8, min 0.759, max 8.332, last 2.533 |
| Read: *The gospels of the Bible* | 14,635 chars, sha256 `24fcedd0…2e872`, matches the stored text |
| Read: *The Republic* | 1,213,740 chars, sha256 `872840c1…4354a`, matches the stored text |
| `library/` Republic file vs what Adam read | same text after the browser strips `\r`; the file has 3 more characters of trailing whitespace, so the bytes differ |
| Tier 2 request entry | **none in the ledger**: tier 2 was opened by signature with no `request` entry logged (tier 1 has one) |

There are no preregistered predictions or pass/fail tests in this work. The table above is
everything that can be checked.

## Contents

- `genesis-seed-v0.1/`: the app as shipped (`genesis-seed-v0.1.html`, `README.txt`, `SHA256SUMS.txt`), unchanged.
- `adam-record/adam-ledger-public.json`: a verbatim extract of Adam's backup (seed, ledger, surprise curve, tiers).
- `adam-record/verify_ledger.py`: an offline check that mirrors the app's own `verifyLedger()`. **It was written for this repository** and isn't part of the original seed.
- `library/the-republic-plato-jowett-gutenberg-1497.txt`: the library text, unchanged (Project Gutenberg #1497).

## How to run it

- **The seed:** open `genesis-seed-v0.1/genesis-seed-v0.1.html` in Chrome, Edge, Firefox, or Safari. It needs no internet, and nothing is sent anywhere. See its own `README.txt`.
- **The record:** `pip install -r requirements.txt && cd adam-record && python3 verify_ledger.py`

## Verification

On Oct 16, 2026, `SHA256SUMS.txt` verified, and `verify_ledger.py` was run twice on the public extract and once on the full original backup. All three runs printed the same result: 94 entries chained, 3 owner signatures valid, and the head above. Both stored reading texts rehash to the sha256 values in their `read` entries. `SHA256SUMS` at the root covers every file here.

## Caveats

- **The full backup is withheld.** It contains the owner's **private signing key** (the seed's own README says to "keep it like a house key"), the full conversation, and the texts Adam read. Only the public ledger extract is published.
- **There is no runner or test battery.** The seed is a browser app with no preregistration and no shipped receipt. It wasn't run headlessly here.
- **One copy of the HTML was left out.** It was a wrapped copy cut off mid-file, and the complete copy is the one in the package.
- **This is a beta, by its own account.** It learns letter patterns and reaches word-like and phrase-like speech, not real conversation. The signing key lives in the same page as the seed, so the signatures show the idea, not hardened security. One seed per browser, adults only.
- **One seed, one owner, one afternoon, about 50 minutes.** Nothing has been independently reproduced.

Apache-2.0. See `LICENSE` and `NOTICE`.
