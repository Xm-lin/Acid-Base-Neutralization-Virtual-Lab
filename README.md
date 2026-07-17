# 🧪 酸鹼滴定虛擬實驗室 (Acid-Base Titration Virtual Lab)

### ⚗️ 輕量化的純 Python 互動式模擬系統，與雲端試算表即時連動的化學實驗室！

---

## 📌 目錄 (Table of Contents)

* [🎯 專案介紹 (Overview)](https://www.google.com/search?q=%23-%E5%B0%88%E6%A1%88%E4%BB%8B%E7%B4%B9-overview)
* [🌟 專案特色 (Features)](https://www.google.com/search?q=%23-%E5%B0%88%E6%A1%88%E7%89%B9%E8%89%B2-features)
* [🖼️ 畫面展示 (Demo)](https://www.google.com/search?q=%23%25EF%25B8%258F-%E7%95%AB%E9%9D%A2%E5%B1%95%E7%A4%BA-demo)
* [🏗️ 軟體架構與系統流程 (Architecture & Workflow)](https://www.google.com/search?q=%23%25EF%25B8%258F-%E8%BB%9F%E9%AB%94%E6%9E%B6%E6%A7%8B%E8%88%87%E7%B3%BB%E7%B5%B1%E6%B5%81%E7%A8%8B-architecture--workflow)
* [📂 檔案結構 (Project Structure)](https://www.google.com/search?q=%23-%E6%AA%94%E6%A1%88%E7%B5%90%E6%A7%8B-project-structure)
* [📦 模組詳細說明 (Modules)](https://www.google.com/search?q=%23-%E6%A8%A1%E7%B5%84%E8%A9%B3%E7%B4%B0%E8%AA%AA%E6%98%8E-modules)
* [🔬 化學原理與 pH 計算 (Theory & Algorithm)](https://www.google.com/search?q=%23-%E5%8C%96%E5%AD%B8%E5%8E%9F%E7%90%86%E8%88%87-ph-%E8%A8%88%E7%AE%97-theory--algorithm)
* [🎨 UI 介面設計 (UI Design)](https://www.google.com/search?q=%23-ui-%E4%BB%8B%E9%9D%A2%E8%A8%AD%E8%A8%88-ui-design)
* [⚙️ 安裝方式 (Installation)](https://www.google.com/search?q=%23%25EF%25B8%258F-%E5%AE%89%E8%A3%9D%E6%96%B9%E5%BC%8F-installation)
* [🖥️ 使用方法 (Usage)](https://www.google.com/search?q=%23%25EF%25B8%258F-%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95-usage)
* [📋 系統需求 (Requirements)](https://www.google.com/search?q=%23-%E7%B3%BB%E7%B5%B1%E9%9C%80%E6%B1%82-requirements)
* [🚀 未來擴充方向 (Future Roadmap)](https://www.google.com/search?q=%23-%E6%9C%AA%E4%BE%86%E6%93%B4%E5%85%85%E6%96%B9%E5%90%91-future-roadmap)
* [📝 開發心得 (Development Insights)](https://www.google.com/search?q=%23-%E9%96%8B%E7%99%BC%E5%BF%83%E5%BE%97-development-insights)
* [📄 授權條款 (License)](https://www.google.com/search?q=%23-%E6%8E%88%E6%AC%8A%E6%A2%9D%E6%AC%BE-license)
* [🙏 鳴謝與作者資訊 (Acknowledgements & Contact)](https://www.google.com/search?q=%23-%E9%B3%B4%E8%AC%9D%E8%88%87%E4%BD%9C%E8%80%85%E8%B3%87%E8%A8%8A-acknowledgements--contact)

---

## 🎯 專案介紹 (Overview)

本專案是一款專為理化教學與自主學習設計的**互動式酸鹼滴定虛擬實驗室**。它解決了傳統理化實驗室中「藥品消耗、設備限制、強酸強鹼操作危險性」等痛點。使用者可以在完全安全的數位環境下，自由調配不同的酸鹼液與指示劑，進行高擬真的滴定實驗模擬。

---

## 🌟 專案特色 (Features)

* **純 Python 輕量化**：免去下載動輒上百 MB 的封裝執行檔，保持程式碼完全透明安全，極速下載、即開即玩。
* **智慧動態 pH 計算核心**：內建非線性化學公式，精確處理「強酸+強鹼」、「強酸+弱鹼」、「弱酸+強鹼」、「弱酸+弱鹼」四種經典組合，完美模擬緩衝溶液區與鹽類水解。
* **雲端資料庫動態連動**：化學試劑的特性與常數完全託管於 Google Sheets，啟動時背景自動同步最新參數，無縫支援離線快取機制。
* **高擬真即時反饋**：
* 支持 6 種主流酸鹼指示劑（酚酞、甲基橙、溴瑞香草酚藍、甲基紅、百里酚藍、酚紅），燒杯內液體顏色隨當前 pH 值即時演變。
* 動態繪製 pH 突躍曲線，並在滴定達到中和點時**自動捕捉並標註「Equivalence Point (當量點)」**。



---

## 🖼️ 畫面展示 (Demo)

```text
[ 預留位置：請在此處插入參數設定選單 option.py 的截圖或 GIF ]
[ 預留位置：請在此處插入主實驗室 main.py 動態滴定與突躍曲線的截圖或 GIF ]

```

---

## 🏗️ 軟體架構與系統流程 (Architecture & Workflow)

### 1. 系統流程圖 (System Workflow)

```text
[ 啟動 main.py ]
       │
       ▼
[ data.py：背景更新 ] ───(連網成功)───► 下載雲端 Google Sheets 存為 data.xlsx
       │                                     │
       │(連網失敗)                           ▼
       └─────────────────────────────► 讀取本地 data.xlsx 快取並解析
                                             │
                                             ▼
                                   [ option.py：設定選單 ] ◄───► 讀取 說明書.txt
                                             │
                                         (Confirm)
                                             │
                                             ▼
                                   [ main.py：主實驗室 ] ◄────► [ beaker.py：動態反應與顯色 ]
                                                                [ ui.py     ：自訂元件渲染 ]

```

### 2. 演算法與資料流程 (Data Flow)

* 當使用者點擊滴定或觸發自動滴定時，系統會計算滴入的莫耳數。
* 資料傳入 `pH_update` 核心計算公式，動態回傳最新 pH 值。
* `beaker.py` 根據最新 pH 值與選定指示劑更新顏色。
* `main.py` 將 pH 歷史資料繪製成即時曲線，並偵測斜率突變點以標記當量點。

---

## 📂 檔案結構 (Project Structure)

```text
.
├── code/
│   ├── main.py        # 實驗室主程式進入點、主畫面渲染與動態 pH 運算核心
│   ├── option.py      # 第一階段：化學試劑、指示劑與參數配置選單介面
│   ├── beaker.py      # 燒杯物件（管理液體體積、莫耳數與指示劑顏色狀態變化）
│   ├── data.py        # 雲端資料庫串接（Google Sheets 匯出及本地 Excel 讀取）
│   └── ui.py          # 通用 UI 元件（自訂矩形按鈕、三角形變速按鈕渲染與事件處理）
├── images/
│   ├── beaker.png     # 燒杯視覺素材
│   └── burette.png    # 滴定管視覺素材
├── manual/
│   ├── manual.md      # 實驗操作說明書 (Markdown 版本)
│   └── manual.txt     # 實驗操作說明書 (純文字版本)
├── .gitignore         # Git 忽略檔案設定（排除本地運行產生的 data.xlsx 快取）
└── README.md          # 專案首頁說明文件（本檔案）

```

---

## 📦 模組詳細說明 (Modules)

* **`main.py` (主程式與核心算法)**：負責 Pygame 主循環、即時滴定數據卡渲染、pH 刻度尺視覺化、以及即時 pH 突躍曲線的繪製。內建完整的酸鹼中和平衡運算邏輯。
* **`option.py` (參數設定選單)**：獨立的設定介面。利用自訂的幾何演算法（如三角形點選判定機制 `point_in_triangle`）來精準擷取使用者的切換事件，引導使用者配置酸、鹼、指示劑、模式與初始體積。
* **`beaker.py` (燒杯反應模擬)**：封裝了燒杯的物理與化學狀態。動態計算當前累積體積、總莫耳數，並內建 6 種指示劑的變色範圍邏輯，決定燒杯液體的漸層與顯色。
* **`data.py` (雲端資料庫串接)**：利用 `urllib.request` 連線 Google Sheets API 將雲端資料匯出為 XLSX。若連線失敗，則透過 `try-except` 捕捉 Exception，自動降級讀取本地快取，確保系統的高可用性。
* **`ui.py` (通用介面元件)**：自訂圖形化按鈕元件，支持矩形與三角形（變速按鈕）形狀。內建滑鼠懸停變色（hover）與點擊縮放（pressed）的視覺反饋邏輯。

---

## 🔬 化學原理與 pH 計算 (Theory & Algorithm)

本系統非單純的線性模擬，而是基於真實化學平衡常數（$K_a, K_b, K_w$）進行動態非線性聯立方程求解：

### 1. 強酸 + 強鹼 ($HCl + NaOH$)

完全電離，pH 值完全由過量的 $H^+$ 或 $OH^-$ 莫耳濃度決定：

* 酸過量：$\text{pH} = -\log_{10}\left(\frac{\text{total\_H} - \text{total\_OH}}{\text{vol}}\right)$
* 鹼過量：$\text{pH} = 14 + \log_{10}\left(\frac{\text{total\_OH} - \text{total\_H}}{\text{vol}}\right)$

### 2. 強酸 + 弱鹼 ($HCl + NH_4OH$) / 弱酸 + 強鹼 ($CH_3COOH + NaOH$)

涉及共軛酸鹼對的平衡。

* **當量點前（緩衝溶液區）**：應用韓德森-哈塞爾巴赫方程（Henderson-Hasselbalch Equation）進行精準計算。
* **當量點時（鹽類水解）**：考慮鹽類的水解常數（如 $K_h = \frac{K_w}{K_a}$），動態計算此時的水解 pH 值。
* **當量點後**：由過量的強酸或強鹼主導 pH 值。

### 3. 弱酸 + 弱鹼 ($CH_3COOH + NH_4OH$)

此時系統 pH 值受限於兩者的相對弱電離常數。當量點時之 pH 依據下列公式估算：


$$\text{pH} = 7 + \frac{1}{2}(\text{p}K_a - \text{p}K_b)$$

---

## 🎨 UI 介面設計 (UI Design)

* **配色方案**：主體採用舒適耐看的復古羊皮紙色（`255, 240, 220`）與科技感功能卡片色（`235, 243, 250`），有效降低長時間觀看實驗畫面的視覺疲勞。
* **動態反饋**：所有按鈕皆具備三態變化（常態、懸停、點擊），燒杯液面高度會根據體積（`volume / max_volume`）進行即時幾何縮放繪製。

---

## ⚙️ 安裝方式 (Installation)

請確保您的電腦已安裝 **Python 3.x** 環境。打開終端機 (Terminal) 或命令提示字元 (CMD)，輸入以下指令安裝所需的第三方套件：

```bash
pip install pygame openpyxl

```

---

## 🖥️ 使用方法 (Usage)

### 1. 啟動實驗室

切換至專案根目錄 (`OH_H`)，在終端機輸入以下指令即可啟動：

```bash
python code/main.py

```

### 2. 本地自動更新

本專案支援 Git 版本控制。若開發者更新了化學公式或 UI 素材，您無需重新下載壓縮檔，直接在根目錄執行以下指令即可完成同步：

```bash
git pull origin main

```

### 3. 實驗操作步驟

1. **設定參數**：在選單中透過左右箭頭配置您的實驗。點擊 **[Manual]** 可彈出閱讀 `說明書.txt`。設定完成後點擊 **[Confirm]** 進入。
2. **進行滴定**：點擊 **[drop]** 可手動精準滴定；點擊 **[Start]** 可開啟連續自動滴定（速度可透過 `speed` 旁的三角形按鈕進行倍率調整）。
3. **觀察與重置**：隨時觀察右側即時產生的突躍曲線與當量點標記。點擊 **[Reset]** 可清空燒杯重來，點擊 **[Back to menu]** 即可返回主選單。

---

## 📋 系統需求 (Requirements)

* **作業系統**：Windows 10/11, macOS, Linux
* **Python 版本**：Python 3.8 或更高版本
* **核心依賴**：
* `pygame >= 2.0.0` (圖形介面與即時渲染)
* `openpyxl >= 3.0.0` (本地 XLSX 資料表解析)



---

## 🚀 未來擴充方向 (Future Roadmap)

* **多重突躍曲線**：支援二元酸（如 $H_2SO_4$, $H_2C_2O_4$）的滴定模擬，繪製雙當量點突躍曲線。
* **數據匯出功能**：實驗結束後，可一鍵將 `ph_history` 與體積數據導出為 CSV 報表，供教學統計分析。
* **動態動畫優化**：加入真實的液滴下落動畫與燒杯內攪拌子旋轉特效。

---

## 📝 開發心得 (Development Insights)

在開發過程中，最大的挑戰在於如何優化**弱酸弱鹼過量與中和點時的非線性 pH 跳變**。傳統的線性模擬無法呈現化學真實的「突躍」特徵。透過導入電離平衡常數與對數方程，並配合 Pygame 每秒高頻率的動態刷新率，最終成功在數位環境下還原出高度擬真的化學反應曲線。

---

## 📄 授權條款 (License)

本專案採用 **MIT 授權條款** 開源。您可以自由地複製、修改、散佈本軟體，甚至用於商業用途，唯須在衍生的專案中包含本專案原作者的著作權聲明。

---

## 🙏 鳴謝與作者資訊 (Acknowledgements & Contact)

* **指導與數據託管**：感謝 Google Sheets 提供的穩定雲端支持。
* **作者**：[Xmlin]
* **專案連結**：[https://github.com/Xm-lin/OH_H-chemical-lab-project-in-pygame]

