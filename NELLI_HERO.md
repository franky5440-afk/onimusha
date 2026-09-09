# Nelli Hero — 硬條件與現況

## 現況（2026-09-09）

| 項目 | 狀態 |
|---|---|
| `static/hero-onimusha.webp` | **Live = C（slash）** 1600×900；鬼面武士偏左、右側暗區放標題 |
| Nelli A（`hero-onimusha-a`） | **Frank 已否決** — 不得接進 `static/` |
| Nelli B（`hero-onimusha-b`） | **Frank 已否決** — 不得接進 `static/` |
| Nelli D（maskcrop） | **未採用** |
| 品牌色票 | **已套用**於 `static/style.css` `:root`（見 `docs/hero-redesign/brand-tokens.md`）— 接 C **不變** |
| `.hero-halo` | **已關閉**（`display: none`） |
| 標題／玻璃 | **右側暗區**（`justify-items: end` + 右向墨黑 scrim／vignette） |

## 藝術方向（定稿）

- **鬼面造型 OK**；墨黑／緋紅／暗金
- 構圖為 **slash**（人物偏左、刀光、右側負空間）— 非 nioh3 置中白甲
- A／B 已否決；D 未用

## 路徑與尺寸硬約束

| 條件 | 值 |
|---|---|
| 正式路徑 | **唯一** `static/hero-onimusha.webp`（全 repo 只留一份） |
| 建議尺寸 | **1600×900**（16:9） |
| `.hero-img` `aspect-ratio` | **`16 / 9`**（換直式圖時必須同步改） |
| CSS 三處 | `.hero-wall` / `.hero-img` / `.hero-detail i` 皆指向 `hero-onimusha.webp` |
| `.hero-halo` | **關閉**（C 無金色圓盤） |
| `.hero-detail i` | `background-position` 約 `35% 15%/200%`（框住鬼面頭盔） |
| 標題 mood | 襯線 `clamp(2.4rem, 5vw, 4.2rem)`；肅殺惡鬼劍戟 — 不要可愛／霓虹；疊右側暗區 |

## 換圖檢查清單

1. 覆寫 `static/hero-onimusha.webp`（勿另開第二份主視覺）
2. 確認 CSS 三處檔名、`aspect-ratio`、halo、detail crop、標題左右
3. `python build_site.py` 後跑 `node tests/site_contract.mjs`（若環境有 Chrome）
4. 文件：本檔與 README 標明「目前為哪一版／佔位」

產圖 prompt 見 `docs/hero-redesign/onimusha-hero-prompt.md`。
