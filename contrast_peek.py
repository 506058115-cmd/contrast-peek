#!/usr/bin/env python3
"""Calculate the WCAG contrast ratio between two hexadecimal colors."""

import argparse
import sys


def terminal_safe(value):
    return "".join(
        char if char.isprintable() else char.encode("unicode_escape").decode("ascii")
        for char in value
    )


def parse_color(value):
    digits = value[1:] if value.startswith("#") else value
    if len(digits) == 3:
        digits = "".join(char * 2 for char in digits)
    if len(digits) != 6 or any(char not in "0123456789abcdefABCDEF" for char in digits):
        raise ValueError("颜色必须是 #RGB 或 #RRGGBB 格式。")
    return "#" + digits.upper(), tuple(
        int(digits[index:index + 2], 16) / 255 for index in (0, 2, 4)
    )


def luminance(rgb):
    channels = tuple(
        channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
        for channel in rgb
    )
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def main(argv=None):
    parser = argparse.ArgumentParser(description="离线计算两种 HEX 颜色的 WCAG 对比度。")
    parser.add_argument("colors", nargs="*", metavar="COLOR", help="前景色和背景色，如 #123 #abcdef")
    args, extra = parser.parse_known_args(argv)
    if extra or len(args.colors) != 2:
        print("用法：contrast_peek.py 前景色 背景色（格式为 #RGB 或 #RRGGBB）", file=sys.stderr)
        return 2

    try:
        foreground, foreground_rgb = parse_color(args.colors[0])
        background, background_rgb = parse_color(args.colors[1])
    except ValueError as error:
        print(f"contrast-peek: {terminal_safe(str(error))}", file=sys.stderr)
        return 2

    first, second = luminance(foreground_rgb), luminance(background_rgb)
    ratio = (max(first, second) + 0.05) / (min(first, second) + 0.05)
    print(f"前景色 {foreground} · 背景色 {background}")
    print(f"对比度 {ratio:.2f}:1")
    print(f"普通文字 AA（≥ 4.5:1）：{'通过' if ratio >= 4.5 else '未通过'}")
    print(f"大号文字 AA（≥ 3:1）：{'通过' if ratio >= 3 else '未通过'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
