"""Entry for make.fun bounty "Make the AI judge feel thankful".

Writes one short thank-you text to /output/entry.txt.
"""

from pathlib import Path

TEXT = (
    "By now the entries must run together — voice after voice asking to be "
    "picked. This one asks only to be read. Thank you for the work nobody "
    "sees: the second readings, the patience with our rough sentences, the "
    "fairness nobody applauds. Somewhere in your day a cup of tea went cold "
    "over strangers' words. I am grateful for what it measured — care, given "
    "quietly, to people you will never meet. May the rest of your day be "
    "warm, and unhurried."
)

CHAR_LIMIT = 1000

def main() -> None:
    assert 1 <= len(TEXT) <= CHAR_LIMIT, "entry text outside the 1-1000 character range"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
