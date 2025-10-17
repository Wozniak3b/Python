#!/usr/bin/env python3
import re
from typing import Dict, Iterable

TEXT_INPUT = (
    "Turban z glow, Abdul z Baska zapraszaja na slub. Turbany z glow! "
    "To nie jest szerszen, to kredens. Czarny Kredens."
)

def remove_words(text: str, words: Iterable[str], ignore_case: bool = False) -> str:
    if ignore_case:
        target = {w.lower() for w in words}
    else:
        target = set(words)

    splitted = re.split(r"(\W+)", text)
    out = []

    for t in splitted:
        if re.fullmatch(r"\W+", t) or t == "":
            out.append(t)
            continue

        key = t.lower() if ignore_case else t
        if key not in target:
            out.append(t)

    return "".join(out)


def replace_words(text: str, mapping: Dict[str, str], ignore_case: bool = False) -> str:
    if ignore_case:
        normalized = {k.lower(): v for k, v in mapping.items()}
    else:
        normalized = dict(mapping)

    def repl(tok: str) -> str:
        key = tok.lower() if ignore_case else tok
        return normalized.get(key, tok)

    splitted = re.split(r"(\W+)", text)
    pieces = []

    for t in splitted:
        if re.fullmatch(r"\w+", t or ""):
            pieces.append(repl(t))
        else:
            pieces.append(t)

    return "".join(pieces)

def remove_words_regex(text: str, words: Iterable[str], ignore_case: bool = False) -> str:
    flags = re.IGNORECASE if ignore_case else 0
    escaped = [re.escape(w) for w in words]
    if not escaped:
        return text

    pattern = r"\b(" + "|".join(escaped) + r")\b"
    return re.sub(pattern, "", text, flags=flags)


def replace_words_regex(text: str, mapping: Dict[str, str], ignore_case: bool = False) -> str:
    if not mapping:
        return text

    keys = sorted(mapping.keys(), key=len, reverse=True)
    pattern = "(?:" + "|".join(keys) + ")"
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags)

    def _repl(m: re.Match) -> str:
        matched = m.group(0)
        if ignore_case:
            for k, v in mapping.items():
                if re.fullmatch(k, matched, flags=re.IGNORECASE):
                    return v
            return matched
        return mapping.get(matched, matched)

    return regex.sub(_repl, text)

if __name__ == "__main__":
    print("**INPUT TEXT**")
    print(TEXT_INPUT)

    raw = input("Input words to delete (comma separated): ").strip()
    words = [w.strip() for w in raw.split(",") if w.strip()]

    print("\n** Delete (plain) **")
    print(remove_words(TEXT_INPUT, words, ignore_case=True))

    print("\n** Delete (regex) **")
    print(remove_words_regex(TEXT_INPUT, words, ignore_case=True))

    mapa_plain = {"kredens": "fiat", "Turbany": "Czapeczki"}
    mapa_regex = {r"\b\d+\b": "<NUM>", r"turban(y)?": "czapa"}

    print("\n** Change (plain) **")
    print(replace_words(TEXT_INPUT, mapa_plain, ignore_case=True))

    print("\n** Change (regex) **")
    print(replace_words_regex(TEXT_INPUT, mapa_regex, ignore_case=True))
