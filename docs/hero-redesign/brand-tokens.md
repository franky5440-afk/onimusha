# 鬼武者：劍之道 攻略武庫 — 品牌色票與標題字級

站名：**鬼武者：劍之道 攻略武庫**

## CSS 變數建議（暗黑血戰版，可對調 nioh3 的 ivory/ink）

```css
:root {
  /* 基底 */
  --ink: #0b0a0c;           /* 墨黑頁底／盔甲主色 */
  --charcoal: #1a1714;      /* 次級底、卡片底 */
  --mist: #2a2622;          /* 單一色調背景牆 */

  /* 重音 */
  --crimson: #9b1c1c;       /* 緋紅（斗篷／繩／眼） */
  --crimson-hot: #c23a2e;   /* hover／強調 */
  --gold: #b8923a;          /* 暗金（halo／飾金） */
  --gold-soft: #d4b56a;     /* 標題掃光、連結 */

  /* 文字 */
  --text: #f2ebe3;          /* 主文（暖象牙，對深底） */
  --text-dim: #a89f94;      /* 次文 */
  --scrim: rgba(11, 10, 12, 0.55); /* 左下淡遮罩，護襯線標題 */

  /* 玻璃卡 */
  --glass: rgba(26, 23, 20, 0.45);
  --glass-border: rgba(184, 146, 58, 0.22);
}
```

## 標題／字級 mood（短）

| 用途 | 建議 | 備註 |
|---|---|---|
| 站名主標 | 襯線顯示字（類 Cormorant / Noto Serif TC），**clamp(2.4rem, 5vw, 4.2rem)**，字重 600–700，`--text`，可加極淡 `--gold` 掃光 | 繁中：「鬼武者：劍之道」＋副標「攻略武庫」小一級 |
| 副標／英譯 | 無襯線大寫追蹤 `0.12em`，`--gold-soft`，約主標 40% | 可選 `ONIMUSHA · WAY OF THE SWORD` |
| 區塊標題 | Noto Sans TC / system-ui，1.25–1.5rem，`--text` | |
| 內文 | 1rem / 1.65，`--text-dim` | |
| 情緒關鍵字 | 肅殺、惡鬼、劍戟、暗金緋紅；**不要**可愛／賽博霓虹 | |

## 本批圖檔

| 檔 | 用途 | 尺寸 |
|---|---|---|
| `hero-onimusha.webp`（＝A） | **主推**接站 | 1600×900 |
| `hero-onimusha-a.webp` | 紅鬼面＋煙塵翼 | 1600×900 |
| `hero-onimusha-b.webp` | 緋紅戰旗張開更滿 | 1600×900 |
