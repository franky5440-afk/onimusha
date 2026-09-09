# Hero 視覺（鬼武者）

自 nioh3 `docs/hero-redesign` 六層效果移植；人物／色票改為惡鬼劍戟（墨黑＋緋紅＋暗金）。

## 現況

- **正式站主視覺**：`static/hero-onimusha.webp` — 目前為**佔位圖**（非 Capcom IP）
- Nelli A／B：**Frank 已否決**，未接入
- **下一版方向**：鬼面造型 OK；色調可近被否決的 A；姿勢／構圖**不可像** nioh3。Nelli 重繪中
- 品牌色票：`brand-tokens.md`（已寫進 `static/style.css` `:root`）
- 產圖 prompt：`onimusha-hero-prompt.md`（由 samurai→onimusha 改編）

| 檔案 | 用途 |
|---|---|
| `onimusha-hero-prompt.md` | 產主視覺 prompt ＋ 硬條件 |
| `brand-tokens.md` | CSS 變數與標題 mood |
| `hero-template.html` | 共用模板結構（圖片佔位） |
| `samurai-hero-prompt.md` | nioh3 原文（對照用，勿當本站色票） |

主視覺本體只放 `static/hero-onimusha.webp`（建議 1600×900、`aspect-ratio: 16 / 9`）。

## 正式站接法

| 檔案 | 內容 |
|---|---|
| `static/hero-onimusha.webp` | 主視覺，全 repo 唯一一份 |
| `templates/index.html` | `<section class="hero">` + Cormorant／Noto Serif + `hero.js` |
| `static/style.css` | hero 樣式；三處 `url("hero-onimusha.webp")` |
| `static/hero.js` | 視差、光塵 |
| `NELLI_HERO.md` | 硬約束與換圖清單 |

### 換圖檢查清單

- CSS 三處：`.hero-wall`、`.hero-img`、`.hero-detail i`
- `.hero-img { aspect-ratio: 16 / 9; }`（換比例時同步）
- `.hero-halo` 對準金色圓盤；`.hero-detail i` 框住頭部
- 跑 `node tests/site_contract.mjs`
