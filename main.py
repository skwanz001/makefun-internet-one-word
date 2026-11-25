"""The Internet in One Word — entry program.

Writes a single word to /output/entry.txt. The word is the whole entry:
one word, nothing else, judged pairwise by a comedy-editor judge on how
funny it is, how well it fits the internet as a whole, and how surprising
it is.

Chosen word: "groupchat"

Why this word wins on the judge's own criteria (in their order):
1. Single word — 9 letters, one token, no phrase, no punctuation.
2. Funny by itself — the mental image lands instantly: eight billion
   people crammed into one group chat with no admin, someone always
   typing, someone always leaving, someone always replying at 3am.
3. True about the whole internet — it is not one app, one site or one
   mood. The internet IS one giant group chat: everyone talking at
   once, memes, drama, lurkers, arguments, notifications, receipts.
   That is what the place is, not what you do on it.
4. Surprising — nobody's first reach. The obvious picks (chaos,
   doomscrolling, infinite, addictive, endless) are abstract or one
   behaviour; this one names the room we're all standing in.
5. Lands in one beat — short, correctly spelled, instantly readable.

Rejected candidates: "chaos" / "doomscrolling" / "infinite" (obvious,
everyone will submit them); "highschool" (normally two words, risky
spelling); "yapping" (funny but only a behaviour, not the whole net);
"tabs" / "cookies" / "captcha" / "loading" (one corner of the net only);
"actually" (clever, but pedantry is only one of the internet's moods).
"""

import os

WORD = "groupchat"


def validate(word: str) -> str:
    """Enforce the gate ourselves before writing: UTF-8 text of 1 to 30
    characters, not only white space. Fail loudly instead of shipping an
    invalid entry."""
    cleaned = word.strip()
    if not cleaned or len(cleaned) > 30:
        raise ValueError(f"entry word fails the gate: {word!r}")
    if len(cleaned.split()) != 1:
        raise ValueError(f"entry must be a single word: {word!r}")
    return cleaned


def main() -> None:
    word = validate(WORD)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the entry is the word and nothing else, and
    # fewer bytes wins the size tie-break.
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
