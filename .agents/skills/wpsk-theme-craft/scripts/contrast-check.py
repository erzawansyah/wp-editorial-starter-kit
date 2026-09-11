#!/usr/bin/env python3
"""WCAG 2.x contrast checker for wpsk-theme-craft.

Usage:
    python contrast-check.py "#FFFFFF" "#777777"
    python contrast-check.py FFFFFF 777777

Prints the contrast ratio and a PASS/FAIL verdict for normal text (4.5:1)
and large text (3:1, 18px+ per WCAG AA). Exit code 0 only when both
verdicts pass, so scripts can chain on it.
"""

import os
import re
import sys

NAMED_COLORS = {"black": (0, 0, 0), "white": (255, 255, 255)}


def parse_hex(value):
    value = value.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if not re.fullmatch(r"[0-9A-Fa-f]{6}", value):
        raise ValueError(f"expected a hex color like #FFFFFF, got {value!r}")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def parse_pairing(pairing):
    """Turn 'White on #333333' or '#555555 on black' into two RGB tuples."""
    colors = []
    for token in re.split(r"\s+on\s+", pairing):
        token = token.strip()
        match = re.search(r"#[0-9A-Fa-f]{3,6}", token)
        if match:
            colors.append(parse_hex(match.group(0)))
        elif token.lower() in NAMED_COLORS:
            colors.append(NAMED_COLORS[token.lower()])
        else:
            raise ValueError(f"cannot parse {token!r} from pairing {pairing!r}")
    if len(colors) != 2:
        raise ValueError(f"expected two colors in pairing {pairing!r}")
    return tuple(colors)


def linearize(channel):
    c = channel / 255.0
    if c <= 0.03928:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (linearize(ch) for ch in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color_a, color_b):
    lum_a, lum_b = luminance(color_a), luminance(color_b)
    lighter, darker = sorted((lum_a, lum_b), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def check(color_a, color_b):
    ratio = contrast_ratio(color_a, color_b)
    normal_pass = ratio >= 4.5
    large_pass = ratio >= 3.0
    print(f"Ratio: {ratio:.2f}:1")
    print(f"Normal text (>=4.5:1): {'PASS' if normal_pass else 'FAIL'}")
    print(f"Large text  (>=3.0:1): {'PASS' if large_pass else 'FAIL'}")
    return 0 if (normal_pass and large_pass) else 1


def main():
    if len(sys.argv) < 3:
        print("Usage: python contrast-check.py <color1> <color2>")
        print("Example: python contrast-check.py '#FFFFFF' '#1E293B'")
        sys.exit(2)
    try:
        c1 = parse_hex(sys.argv[1])
        c2 = parse_hex(sys.argv[2])
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(2)
    sys.exit(check(c1, c2))


if __name__ == "__main__":
    main()
