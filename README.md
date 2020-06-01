# 系辦交叉查榜資料抓取工具操作說明

## 功能
從交叉查榜網站抓取考生資料及志願系所，整理成excel檔案。

## 檔案
Github link: https://github.com/FooJiaYin/NTHUCS-crosscheck-crawler
- phase1-config.csv, phase2-config.csv：設定檔案名稱、組別名稱和鏈接
- phase1-crawler.bat：執行第一階段爬蟲程式（crawler-excel-combine.py）
- phase2-crawler.bat：執行第二階段爬蟲程式（crawler-phase2.py），抓取錄取結果與分發結果
- install.bat：安裝環境
- source：User不會用到的文件
    - crawler-csv-separate.py：把資料匯出成分開的csv檔案，需要手動輸入鏈接和檔名（沒用到）
    - crawler-excel-combine.py：把資料匯出成同一個excel檔，鏈接和分頁名稱需要從phase1-userconfig.csv修改
    - crawler-phase2.py：抓取錄取結果與分發結果，鏈接和分頁名稱需要從phase2-userconfig.csv修改
    - get-pip.py：安裝pip
    - requirements.txt：需要安裝的modules
    - name-id-甲組, name-id-乙組, name-id-丙組, name-id-APCS組APCS：由於第二階段的准考證號為圖片，需要從第一階段的抓取結果去比對，因此先整理出名字和准考證號的組合方便查詢


## 環境需求
1. Python 3（不支援Python 2）
    - 安裝python：https://medium.com/@ChunYeung/給自學者的python教學-1-如何安裝python-126f8ce2f967
2. modules（可用pip安裝）
    - 第一次執行時，雙點`install.bat`，以安裝pip和所需的modules

## 使用步驟
1. 雙點`phase1-config.csv`（`phase2-config.csv`），用excel打開。設定檔案名稱、組別名稱和鏈接。
    - 第一行是輸出的檔案名稱（不含`.xlsx`）。預設為`phase1-result.xlsx`。
    - 接下來幾行，左邊是組別名稱，右邊是對應的網址
    - 可以自行修改/增加

2. 雙點`phase1-crawler.bat`（`phase2-crawler.bat`），程式會開始執行。

3. 耐心等待幾秒後，文件夾會出現excel檔，名稱如同`phase1-config.csv`（`phase2-config.csv`）中所設定。

4. 第二階段執行完畢後會出現`Success`提示。

## 注意事項
- 第一階段：考生姓名尚未登記在榜上，因此第一階段程式沒有加入考生姓名，日後如要更新考生姓名，請聯絡我進行修改，或是直接從csv中貼上。
- 爬蟲程式強烈依賴網站排版，如果網站排版更改，程式會失效，請聯絡我進行修改。

工作辛苦了～加油！ ``\(^o^)/``
有問題請聯繫嘉尹：candy23198@gmail.com