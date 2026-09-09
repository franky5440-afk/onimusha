# 鬼武者：劍之道 攻略武庫 · Onimusha: Way of the Sword Guide Hub

**線上版：https://franky5440-afk.github.io/onimusha/**

本機自用攻略聚合站。所有資料僅存放於本工作區 `data/`，每日由排程自動更新。

- 線上版：GitHub Actions 每日 UTC 00:00（台北 08:00）雲端執行 `scraper.py` → 建置靜態站 → 自動發布 GitHub Pages，並將資料 commit 回本 repo
- 本機版：cron 每天 08:00 執行 `update.sh`，Flask 服務於 `http://127.0.0.1:8767`
- 官方站：https://www.capcom-games.com/onimusha/ws/

## 啟動網站

```bash
./start.sh          # 啟動於 http://127.0.0.1:8767
./stop.sh           # 停止
```

首次使用需先建環境：

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## 分頁功能

| 分頁 | 內容 | 資料檔 |
|------|------|--------|
| 攻略庫 | 全網搜尋文字／圖文攻略，累積式攻略庫，分中文區、English、日本語，再依 Boss、配裝、武器、新手、流程、收集、白金、情報等類別分區 | `data/guides_{zh,en,ja}.json` |
| 熱門影片 TOP10 | YouTube 每日熱門攻略影片（依觀看數），分中文、英文、日文區 | `data/videos_hot_{zh,en,ja}.json` |
| 最新影片 | YouTube 每日最新發布攻略影片各 10 部，分中文、英文、日文區 | `data/videos_new_{zh,en,ja}.json` |
| 巴哈討論區 | 巴哈姆特鬼武者哈啦區（bsn=217）最新 10 篇討論（已排除置頂公告） | `data/bahamut.json` |
| X 推文 | X（Twitter）上含「鬼武者／Onimusha」的相關推文與官方 @onimusha_capcom、@OnimushaGame 動態，累積式，分中文、英文、日文區 | `data/tweets_{zh,en,ja}.json` |

頂部搜尋框可跨全部內容（攻略＋影片＋討論＋推文）以關鍵字搜尋。

## Hero 主視覺

- Live art = **C2b dual** → `static/hero-onimusha.webp`（1600×900；取代 C slash；dual-wield 修正不良雙端刀柄）。
- Nelli **A／B 已否決**；**D 未採用**。
- 布局：無 `.hero-halo`、標題／玻璃疊**右側暗區**、`.hero-img` 維持 `aspect-ratio: 16 / 9`、品牌色票不變。詳見 [NELLI_HERO.md](NELLI_HERO.md)。

## 每日更新

- 雲端：GitHub Actions schedule（`.github/workflows/deploy.yml`），可手動觸發：`gh workflow run deploy.yml`
- 本機：cron 可設定每天 08:00 執行 `update.sh`；手動更新：`./update.sh`

更新來源：
- 攻略庫：DuckDuckGo 網頁搜尋（ddgs）
- YouTube：yt-dlp（不需 API key）
- 巴哈姆特：HTML 解析（bsn=217）
- X 推文：ddgs 站內搜尋（site:x.com）＋ syndication 官方帳號時間軸（免 API key；推文日期由 status id 直接換算）

語言分區判定：標題或摘要含假名、或網域為 .jp → 日文區；含中日韓字元 → 中文區；其餘 → 英文區。三區各自獨立累積，不會互相混雜。

## 專案結構

```
onimusha/
├── app.py                     # Flask 本機伺服器（127.0.0.1:8767）
├── scraper.py                 # 每日爬蟲：攻略庫 / YouTube 熱門+最新 / 巴哈討論 / X
├── build_site.py              # 彙整 data/*.json → site/ 靜態站（Pages artifact）
├── start.sh / stop.sh         # 本機網站啟停
├── update.sh                  # cron 每日更新入口（scraper + build）
├── requirements.txt
├── AGENTS.md                  # 維護規範（給 AI 助手看的工作守則）
├── NELLI_HERO.md              # Hero 硬條件與換圖檢查清單
├── templates/index.html       # 單頁前端
├── static/style.css, app.js, hero.js, hero-onimusha.webp
├── .github/workflows/deploy.yml  # 每日雲端爬蟲 + Pages 自動部署
└── data/
    ├── guides_{zh,en,ja}.json
    ├── videos_hot_{zh,en,ja}.json
    ├── videos_new_{zh,en,ja}.json
    ├── bahamut.json
    ├── tweets_{zh,en,ja}.json
    ├── meta.json
    ├── site.json
    └── (縮圖不存放，前端直連 i.ytimg.com)
```

## GitHub Pages

首次上線請在 repo Settings → Pages 將 Source 設為 **GitHub Actions**（本 repo 已附 `deploy.yml`）。MCP 無 Pages 設定 API 時需人工開一次。

## 疑難排解

- **攻略庫掃不到新資料**：DuckDuckGo 有速率限制，同批關鍵字短時間內重跑會被擋，等隔天排程即可
- **push 被拒**：雲端 bot 每天會 commit 新資料，先 `git pull --rebase`；若 `data/*.json` 衝突，以本地較新資料為準（`git checkout --theirs -- data/`）再 `rebase --continue`
- **線上沒更新**：push 不會自動發布，需 `gh workflow run deploy.yml --ref main`
- **巴哈解析失敗**：scraper 會保留前一日資料並記錄於 `logs/scraper.log`，不會覆蓋成空檔
- **空資料**：前端對空陣列有 `empty-msg` 降級，不會崩潰；骨架可先上線再等首次 scraper

維護此專案的完整工作規範見 [AGENTS.md](AGENTS.md)。

## 日誌

- `logs/scraper.log` — scraper 完整記錄
- `logs/cron.log` — cron 執行輸出
- `logs/server.log` — 網站伺服器輸出

## 授權

本專案採用 [Apache License 2.0](LICENSE)。歡迎自由使用、修改、二次開發或商用，但需保留原始著作權聲明，並在你修改過的檔案中註明有修改；衍生專案請標明來源於此 repo。架構改編自 [nioh3](https://github.com/franky5440-afk/nioh3) 模板。
