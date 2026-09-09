# onimusha 專案規範

鬼武者：劍之道（Onimusha: Way of the Sword）攻略聚合站。Flask 本機版 + GitHub Pages 線上版共用同一套前端與資料。
本檔只列專案特有規則；架構改編自 nioh3 模板。

## 產品常數

- 標題 ZH：鬼武者：劍之道 攻略武庫
- 標題 EN：Onimusha: Way of the Sword Guide Hub
- 本機 Port：**8767**
- 巴哈 bsn：**217**
- 官方 X：`onimusha_capcom`（JP）、`OnimushaGame`（EN）
- 官方站：https://www.capcom-games.com/onimusha/ws/
- Pages：https://franky5440-afk.github.io/onimusha/
- Hero：`static/hero-onimusha.webp`（目前為佔位；A/B 否決；v2 待選 C slash／D maskcrop — 見 `NELLI_HERO.md`）

## 語言

一律使用繁體中文回覆。程式碼、指令、變數名稱維持英文。

## 架構與資料流

```
scraper.py ──> data/*.json ──> build_site.py ──> site/（靜態站，Pages artifact）
                     │
                     └──> app.py（Flask 本機版，直接讀 data/）
```

- `data/*.json` 是唯一資料來源，所有內容只能存放在本工作區
- `site/` 是建置產物，已列入 `.gitignore`，**絕不 commit**；Pages 用 `actions/upload-pages-artifact` 上傳，不是 gh-pages branch
- 攻略庫（`guides_*.json`）是**累積式**：URL 正規化去重後併入，永不清空；X 推文區（`tweets_*.json`）同為累積式但每語言上限 250 筆（超出裁最舊）；影片區與巴哈區是每日覆寫快照
- `meta.json` 記錄各區最後更新時間，`_last_run` 是完整掃描時間
- 空陣列／空物件時前端必須 graceful（`empty-msg`），scraper 來源失敗時保留舊資料、不覆蓋成空檔

## 語言分區規則（不可破壞）

三區 zh / en / ja 由 `detect_lang()` 判定：

1. 標題或摘要含**平/片假名** → ja
2. 網域以 `.jp` 結尾 → ja
3. 含 CJK 字元 → zh
4. 其餘 → en

影片區的 `keep()` 過濾同邏輯：ja 要有假名；zh 必須「含 CJK 且**無**假名」。新增任何抓取來源都要套用此規則，避免日文混入中文區。

## 各來源已知陷阱

### yt-dlp（v2026.08+）
- **沒有 `ytsearchdate` 前綴**了；而且 `sp=CAI%3D`（上傳時間排序）**已被 YouTube 靜默忽略**
- 找「最新影片」的正解：flat 搜尋結果自帶 `channel_id`，改抓候選頻道的上傳 RSS
- flat playlist 搜尋自帶 `view_count`，但**沒有 upload_date**
- flat 搜尋結果會混入**播放清單項目**（id 是 PL…），組 pool 時只收 id 長度 11 的影片
- 影片縮圖**不下載、不入 repo**：前端直連 `https://i.ytimg.com/vi/{video_id}/mqdefault.jpg`

### DuckDuckGo（ddgs）
- 同一批 query **短時間內重跑**會回空或 429/403——不是程式壞掉
- 中文 `region="tw-zh"`、英文 `us-en`、日文 `jp-jp`

### 巴哈姆特
- `RSS.php` 已失效，只能解析 `B.php?bsn=217` HTML
- 帶 `.b-list__summary__mark` 的置頂/公告/精華**跳過**
- 解析失敗時保留舊資料並記 log，不要覆蓋成空檔

### X（Twitter）
- 免費讀取：syndication + ddgs `site:x.com`
- syndication **極敏感於連續請求**：每天各打官方帳號一次（`@onimusha_capcom`、`@OnimushaGame`），失敗就保留舊資料
- ddgs 結果仍要過 `GAME_TERMS` 關鍵字過濾；`tweets_*.json` 以 tid 去重累積，每語言上限 250 筆

## Git 與部署流程

1. push 前做機密掃描（勿掃 `venv/`）
2. **push 之後線上不會自動更新**，必須手動觸發：`gh workflow run deploy.yml --ref main`
3. 雲端 bot 每天 UTC 00:00 會產生 "daily data update" commit。本機 push 若撞到 `data/*.json` 衝突：

```bash
git pull --rebase
git checkout --theirs -- data/
git add data/ && git -c core.editor=true rebase --continue && git push
```

4. repo 保持 public（免費 Pages）；首次需人工把 Pages source 設為 GitHub Actions

## 驗證清單

1. `./venv/bin/python -c "import ast; ast.parse(open('scraper.py').read())"`
2. `node --check static/app.js`
3. `node tests/site_contract.mjs`（需本機 Chrome）
4. scraper 後檢查各區筆數與語言誤配 = 0
5. `./start.sh` 後 curl：`/` 200、`/data/site.json` 可解析（port **8767**）
6. push 後觸發 workflow，確認 run success

## 其他約定

- 本機 cron 與雲端 Actions 雙排程並存是刻意設計，不要移除其中一個
- `venv/`、`logs/`、`site/` 都不入 git
- Hero 換圖規則見 `NELLI_HERO.md`：佔位可上線；Nelli 成品須 Frank 核准後才覆寫 `static/hero-onimusha.webp`
