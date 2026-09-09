# Nelli Hero — 硬條件與現況

## 現況（2026-09-09）

| 項目 | 狀態 |
|---|---|
| `static/hero-onimusha.webp` | **佔位圖**（抽象暗金／墨黑色塊，非 Capcom IP、非 Nelli 成品） |
| Nelli A（`hero-onimusha-a`） | **Frank 已否決** — 不得接進 `static/` |
| Nelli B（`hero-onimusha-b`） | **Frank 已否決** — 不得接進 `static/` |
| 品牌色票 | **已套用**於 `static/style.css` `:root`（見 `docs/hero-redesign/brand-tokens.md`） |
| 下一版 | Nelli **重繪中** — 等新圖再換 |

## Frank 下一版藝術方向（給 Nelli / 文件用）

- **鬼面造型 OK**
- **色調**可接近被否決的 A（墨黑／緋紅／暗金）
- **姿勢／構圖不可像 nioh3**（不要複製武士大理石雕像那套 layout）
- 接站前仍以佔位圖＋品牌色票為準；新圖到了再換檔與微調 halo／detail

## 路徑與尺寸硬約束

| 條件 | 值 |
|---|---|
| 正式路徑 | **唯一** `static/hero-onimusha.webp`（全 repo 只留一份） |
| 建議尺寸 | **1600×900**（16:9） |
| `.hero-img` `aspect-ratio` | **`16 / 9`**（換直式圖時必須同步改） |
| CSS 三處 | `.hero-wall` / `.hero-img` / `.hero-detail i` 皆指向 `hero-onimusha.webp` |
| `.hero-halo` | `top` 對準圖中金色圓盤 |
| `.hero-detail i` | `background-position` 框住頭部 |
| 標題 mood | 襯線 `clamp(2.4rem, 5vw, 4.2rem)`；肅殺惡鬼劍戟 — 不要可愛／霓虹 |

## 換圖檢查清單

1. 覆寫 `static/hero-onimusha.webp`（勿另開第二份主視覺）
2. 確認 CSS 三處檔名、`aspect-ratio`、halo、detail crop
3. `python build_site.py` 後跑 `node tests/site_contract.mjs`（若環境有 Chrome）
4. 文件：本檔與 README 標明「目前為哪一版／佔位」

產圖 prompt 見 `docs/hero-redesign/onimusha-hero-prompt.md`。
