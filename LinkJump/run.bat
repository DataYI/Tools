@echo off
for /f "delims=: tokens=2" %%j in ('ipconfig ^| find /i "IPv4" ') do echo �����������ַ�������� %%j:8000
cd .\resource\
python -m http.server
PAUSE