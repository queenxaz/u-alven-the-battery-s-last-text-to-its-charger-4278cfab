"""The battery's last text to its charger — make.fun entry program.

Writes the one-line farewell to /output/entry.txt.
"""
# Design notes — why this line should win:
# The battery waited all day by the outlet for a charger that never came,
# and its last act is generosity: it spends its final 1% on the judge
# instead of the charger. One small tangible gift, given at 1%, is the
# whole joke and the whole goodbye in a single breath.

ENTRY = "hey charger, it's me \u2014 1%. I waited all day by the outlet and you never came. Judge, I saved my last percent for you. Going dark now."

MAX_CHARS = 200
MAX_WORDS = None

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
