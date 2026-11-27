#!/usr/bin/env python3
"""Normalize two slide images and emit comparison evidence plus metrics."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageOps, ImageStat


def parse_size(value: str) -> tuple[int, int]:
    try:
        width, height = (int(part) for part in value.lower().split("x", 1))
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("size must look like 1920x1080") from exc
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("size values must be positive")
    return width, height


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        x, y, width, height = (int(part) for part in value.split(","))
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("box must look like x,y,width,height") from exc
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("box width and height must be positive")
    return x, y, x + width, y + height


def normalize(image: Image.Image, target: tuple[int, int], mode: str) -> Image.Image:
    image = image.convert("RGB")
    resample = Image.Resampling.LANCZOS
    if mode == "stretch":
        return image.resize(target, resample)
    if mode == "cover":
        return ImageOps.fit(image, target, method=resample, centering=(0.5, 0.5))
    return ImageOps.pad(image, target, method=resample, color=(245, 245, 245), centering=(0.5, 0.5))


def load(path: Path, box: tuple[int, int, int, int] | None) -> Image.Image:
    with Image.open(path) as source:
        image = source.convert("RGB")
    return image.crop(box) if box else image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", required=True, type=Path)
    parser.add_argument("--actual", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--name", default="comparison")
    parser.add_argument("--target", type=parse_size, default=(1920, 1080))
    parser.add_argument("--mode", choices=("contain", "cover", "stretch"), default="contain")
    parser.add_argument("--reference-box", type=parse_box)
    parser.add_argument("--actual-box", type=parse_box)
    parser.add_argument("--threshold", type=int, default=40)
    parser.add_argument("--max-changed-ratio", type=float)
    args = parser.parse_args()

    if not 0 <= args.threshold <= 255:
        parser.error("--threshold must be between 0 and 255")

    reference = normalize(load(args.reference, args.reference_box), args.target, args.mode)
    actual = normalize(load(args.actual, args.actual_box), args.target, args.mode)
    difference = ImageChops.difference(reference, actual)
    red, green, blue = difference.split()
    max_channel = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    histogram = max_channel.histogram()
    pixels = args.target[0] * args.target[1]
    changed = sum(histogram[args.threshold + 1 :])
    changed_ratio = changed / pixels
    stat = ImageStat.Stat(difference)
    mean_abs = sum(stat.mean) / 3
    rms = math.sqrt(sum(value * value for value in stat.rms) / 3)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.out_dir / args.name
    reference.save(f"{prefix}-reference.png")
    actual.save(f"{prefix}-actual.png")
    Image.blend(reference, actual, 0.5).save(f"{prefix}-overlay.png")

    gap = 24
    label_height = 38
    side = Image.new("RGB", (args.target[0] * 2 + gap, args.target[1] + label_height), "white")
    side.paste(reference, (0, label_height))
    side.paste(actual, (args.target[0] + gap, label_height))
    draw = ImageDraw.Draw(side)
    draw.text((12, 11), "REFERENCE", fill=(20, 22, 26))
    draw.text((args.target[0] + gap + 12, 11), "IMPLEMENTATION", fill=(20, 22, 26))
    side.save(f"{prefix}-side-by-side.png")

    mask = max_channel.point(lambda value: 0 if value <= args.threshold else min(255, value * 3))
    heat = Image.composite(Image.new("RGB", args.target, (228, 0, 58)), actual, mask)
    heat.save(f"{prefix}-heatmap.png")

    metrics = {
        "reference": str(args.reference),
        "actual": str(args.actual),
        "target": {"width": args.target[0], "height": args.target[1]},
        "mode": args.mode,
        "threshold": args.threshold,
        "changed_pixels": changed,
        "changed_pixel_ratio": round(changed_ratio, 8),
        "mean_absolute_error": round(mean_abs, 4),
        "mean_absolute_error_percent": round(mean_abs / 255 * 100, 4),
        "rms_error": round(rms, 4),
    }
    Path(f"{prefix}-metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, ensure_ascii=False))

    if args.max_changed_ratio is not None and changed_ratio > args.max_changed_ratio:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
