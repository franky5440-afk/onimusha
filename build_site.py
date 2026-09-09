#!/usr/bin/env python3
"""Build static Pages artifact: merge JSON data + convert story MD → HTML JSON."""
import json
import re
import shutil
from pathlib import Path

import markdown as md_lib

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
SITE = BASE / "site"
STORY_SRC = BASE / "content" / "story"

SECTIONS = [
    "guides_zh", "guides_en", "guides_ja",
    "videos_hot_zh", "videos_hot_en", "videos_hot_ja",
    "videos_new_zh", "videos_new_en", "videos_new_ja",
    "bahamut",
    "tweets_zh", "tweets_en", "tweets_ja",
    "meta",
]

# Reader chapters (ordered). 目錄大綱 / 全稿 stay in content/story for maintenance only.
STORY_PUBLISH = [
    "00_前言與劇透警告.md",
    "01_京都初刃.md",
    "02_血河甦生.md",
    "03_鬼武者之約.md",
    "04_裂隙淨化.md",
    "05_鏡中歧路.md",
    "06_籠手佳人.md",
    "07_白衣真名.md",
    "08_道狂暗影.md",
    "09_屈辱一戰.md",
    "10_人性試煉.md",
    "11_酒吞童子.md",
    "12_嵐山危殆.md",
    "13_祭與犧牲.md",
    "14_鬼門洞開.md",
    "15_鬼門宮殿.md",
    "16_餘燼追獵.md",
    "99_人物小傳與時間線.md",
]

MD = md_lib.Markdown(extensions=["tables", "fenced_code", "nl2br", "sane_lists"])


def chapter_id(filename: str) -> str:
    stem = Path(filename).stem
    m = re.match(r"^(\d+)", stem)
    return f"ch-{m.group(1)}" if m else f"ch-{stem}"


def chapter_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return fallback


def build_story() -> dict:
    """Convert published chapter markdown → HTML payload for the 劇情小說 tab."""
    chapters = []
    if not STORY_SRC.is_dir():
        return {
            "title": "鬼武者：劍之道｜章回小說",
            "chapters": [],
            "error": "content/story 目錄不存在",
        }

    for fname in STORY_PUBLISH:
        path = STORY_SRC / fname
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        title = chapter_title(raw, Path(fname).stem)
        MD.reset()
        html = MD.convert(raw)
        chapters.append({
            "id": chapter_id(fname),
            "file": fname,
            "title": title,
            "html": html,
        })

    return {
        "title": "鬼武者：劍之道｜章回小說體全稿",
        "subtitle": "原創敘事改寫 · 非官方劇本",
        "chapters": chapters,
        "chapter_count": len(chapters),
    }


def main():
    merged = {}
    for name in SECTIONS:
        p = DATA / f"{name}.json"
        merged[name] = json.loads(p.read_text(encoding="utf-8")) if p.exists() else ([] if name != "meta" else {})

    story = build_story()

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "data").mkdir(parents=True)
    payload = json.dumps(merged, ensure_ascii=False)
    (DATA / "site.json").write_text(payload, encoding="utf-8")
    (SITE / "data" / "site.json").write_text(payload, encoding="utf-8")

    story_payload = json.dumps(story, ensure_ascii=False)
    (DATA / "story.json").write_text(story_payload, encoding="utf-8")
    (SITE / "data" / "story.json").write_text(story_payload, encoding="utf-8")

    shutil.copy(BASE / "templates" / "index.html", SITE / "index.html")
    shutil.copytree(BASE / "static", SITE / "static")
    print(
        f"site built: {sum(len(merged[k]) for k in merged if k.startswith('guides'))} guides, "
        f"{sum(len(merged[k]) for k in ('videos_hot_zh', 'videos_hot_en', 'videos_new_zh', 'videos_new_en'))} videos, "
        f"story chapters={story.get('chapter_count', 0)}"
    )


if __name__ == "__main__":
    main()
