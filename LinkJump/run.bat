@echo off
for /f "delims=: tokens=2" %%j in ('ipconfig ^| find /i "IPv4" ') do echo 请在浏览器地址栏中输入 %%j:8000
cd .\resource\
python -m http.server
PAUSE