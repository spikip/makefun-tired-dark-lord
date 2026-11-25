"""Entry for the make.fun bounty "The Tired Dark Lord: A 100-Word Villain
Monologue".

The tiredness lives in the voice, not in a plain statement: torches kept
like office hours, a scheme postponed for tea, a villain who pawned his
amulet to pay the goblin landlord. The program writes a monologue of
exactly 100 words to /output/entry.txt,
spoken by a fantasy villain who is secretly just very tired. The gate
allows 1 to 600 characters of UTF-8 text, so the monologue is checked
against that cap and its word count before it is written.
"""

import os

ENTRY = (
    "They light the torches for me, as if I keep office hours. I used to "
    "arrive with thunder; now I arrive with a list, and the list is mostly "
    "errands. The amulet of endless night? I pawned it. The goblin landlord "
    "does not accept prophecies, and the mountain's rent was due. My grand "
    "scheme \u2014 the eclipse, the coronation, the whole dark ballet "
    "\u2014 is set for Tuesday, unless it rains. It will rain. It always "
    "rains on Tuesdays. Conquering the realm can wait until I have sat down "
    "with tea. The realm is not going anywhere. I checked. Twice."
)

MAX_CHARS = 600
WORD_TARGET = 100
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    words = len(text.split())
    assert words == WORD_TARGET, (
        f"entry is {words} words, target is {WORD_TARGET}"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters, {words} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
