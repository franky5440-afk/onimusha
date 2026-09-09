# 鬼武者：劍之道 — Hero 主視覺產圖 Prompt

對齊 franky5440-afk/nioh3 `docs/hero-redesign` 硬條件；調性改為惡鬼／武士／暗金緋紅墨黑。

## 硬條件（不符合的話，nioh3 那組六層效果會壞）

| 條件 | 值 | 為什麼 |
|---|---|---|
| 長寬比 | **建議 16:9**（本批實圖 1600×900）；直式 3:4 也可 | 網頁雙層：模糊背景牆填滿，人物層 `contain` 不裁 |
| 構圖 | **正面、置中、左右對稱** | 左上標題／右中玻璃卡壓在兩側留白 |
| 兩側 | **有張開物填滿**（披風／煙塵／惡鬼翼／戰旗） | 視差有東西可推，畫面不空 |
| 頭部位置 | 畫面**上方約 1/3**、後有**發光圓盤** | `.halo` 呼吸光暈疊在此 |
| 背景 | 極淡或**單一暗調**、無雜物 | 玻璃卡 `backdrop-filter` 才好看 |
| 配色 | **墨黑＋緋紅＋暗金**（對 nioh3 的「暗黑血戰版」） | 比仁王更偏惡鬼劍戟 |
| 邊緣 | 上下左右**約 5% 空白** | 進場 scale；`contain` 下仍保險 |

## Prompt（英文，直接貼）

```
Front-facing centered symmetrical Onimusha demon-samurai warrior, standing tall
and imposing, ornate kabuto helmet with fierce oni horns and dark-gold maedate,
demonic menpo face mask with glowing crimson ember eyes, elaborate blackened
iron and lacquer o-yoroi armor with deep crimson lacings and antique gold crests,
katana held vertically in front with dark gold fittings, enormous billowing
tattered crimson war banners and charcoal smoke spreading wide left and right
like demon wings filling the frame, soft glowing dark-gold sun disc halo behind
the helmet in the upper third, background of swirling charcoal mist on a clean
single-tone near-black void, cinematic studio lighting, hyper-detailed forged
metal and silk, luxury editorial game key art, strictly ink black deep crimson
and dark gold palette only, centered symmetrical composition, 5 percent empty
margin on all edges, no text no watermark, 8k
```

## Negative prompt

```
bright ivory background, white marble, neon, saturated blue, green, purple,
multiple characters, text, watermark, logo, cropped limbs, cluttered background,
low contrast, cartoon, anime chibi, cute, daytime sky, photoreal modern person,
celebrity face, real human portrait
```

## 想微調時只改這幾格

- **更偏惡鬼**：加 `oni wings of ash and crimson energy, yokai mist, faint ghostly ember particles`
- **武器換薙刀／二刀**：`katana held vertically` → `naginata` / `dual katana crossed`
- **略亮背景（利於淺字）**：`near-black void` → `deep charcoal grey mist wall`（仍單一色調）

## 產完怎麼放進去（給 Hedy）

1. 轉 `.webp`，寬約 **1600px**（本批約 145–170KB）
2. 建議檔名：`static/hero-onimusha.webp`（本批主推 A 版；B 為備選）
3. CSS 三處換檔（對齊 nioh3 檢查清單）：`.hero-wall`、`.hero-img`、`.hero-detail i`
4. `.hero-img { aspect-ratio: 16 / 9; }`（本批）；若改直式圖再同步改
5. `.hero-halo` 的 `top` 對準圖裡金色圓盤；`.hero-detail i` 的 `background-position` 框住頭部
6. 換完跑既有 `site_contract` 測試（若站內有）
