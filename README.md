# 系辦交叉查榜資料抓取工具操作說明

## 功能
從交叉查榜網站抓取考生資料及志願系所，整理成excel檔案。

## 檔案
Github link: https://github.com/FooJiaYin/NTHUCS-crosscheck-crawler
- userconfig.csv：設定檔案名稱、組別名稱和鏈接
- crawler.bat：執行爬蟲程式（crawler-excel-combine.py）
- install.bat：安裝環境
- source：User不會用到的文件
    - crawler-csv-separate.py：把資料匯出成分開的csv檔案，需要手動輸入鏈接和檔名（沒用到）
    - crawler-excel-combine.py：把資料匯出成同意一個excel檔，鏈接和分頁名稱需要從links.csv修改
    - get-pip.py：安裝pip
    - requirements.txt：需要安裝的modules

## 環境需求
1. Python 3（不支援Python 2）
    - 安裝python：https://medium.com/@ChunYeung/給自學者的python教學-1-如何安裝python-126f8ce2f967
2. modules（可用pip安裝）
    - 第一次執行時，雙點`install.bat`，以安裝pip和所需的modules

## 使用步驟
1. 雙點`userconfig.csv`，用excel打開。設定檔案名稱、組別名稱和鏈接。
    - 第一行是輸出的檔案名稱（不含`.xlsx`）。預設為`result.xlsx`。
    - 接下來幾行，左邊是組別名稱，右邊是對應的網址
    - 可以自行修改/增加

2. 雙點`crawler.bat`，程式會開始執行。

3. 耐心等待幾秒後，文件夾會出現excel檔，名稱如同`userconfig.csv`中所設定。

## 注意事項
- 考生姓名尚未登記在榜上，因此程式沒有加入考生姓名，日後如要更新考生姓名，請聯絡我進行修改。
- 爬蟲程式強烈依賴網站排版，如果網站排版更改，程式會失效，請聯絡我進行修改。

工作辛苦了～加油！ ``\(^o^)/``
有問題請聯繫嘉尹：candy23198@gmail.com