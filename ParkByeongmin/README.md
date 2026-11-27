# PARK BYEONGMIN
# Linux System Monitor

## 1. 프로젝트 개요

Python과 오픈소스 라이브러리 psutil을 활용하여 시스템 자원 사용량을 실시간으로 모니터링하는 프로그램입니다.

Linux 시스템 모니터링 도구인 top을 참고하여 CPU, 메모리, 디스크 및 프로세스 정보를 터미널 환경에서 확인할 수 있도록 구현하였습니다.

## 2. 주요 기능

- CPU 사용률 실시간 모니터링
- RAM 사용률 모니터링
- 디스크 저장 공간 사용률 모니터링
- CPU 사용률 상위 5개 프로세스 출력
- 자원 사용률 임계치 초과 경고
- CSV 기반 시스템 상태 로그 저장
- Linux /proc 파일시스템 직접 파싱
- 시스템 가동 시간 및 평균 부하 출력

## 3. 실행 화면

<img width="441" height="558" alt="실행화면" src="https://github.com/user-attachments/assets/eaab9974-8d54-4ecd-93b6-9ed1bc2c037d" />


## 4. 개발 환경 및 사용 패키지

- Python:3.11.9

- psutil:
Name: psutil
Version: 7.2.2
Summary: Cross-platform lib for process and system monitoring.
Home-page: https://github.com/giampaolo/psutil
Author: Giampaolo Rodola
Author-email: g.rodola@gmail.com
License: BSD-3-Clause
Location: C:\Users\mk980\Desktop\OpenSource_TermProject\.venv\Lib\site-packages
Requires: 
Required-by: 


- IDE: Visual Studio Code
  
- Version Control: Git, GitHub

- OS: Windows / Linux

## 5. 설치 및 실행 방법

cd ParkByeongmin/LinuxSystemMonitor
pip install -r requirements.txt
python main.py
Ctrl+C를 입력하여 프로그램을 종료할 수 있습니다.

## 6. 프로젝트 구조

| 파일 | 역할 |
|---|---|
| main.py | 프로그램 실행 및 화면 출력 |
| monitor.py | 시스템 자원 및 프로세스 정보 수집 |
| logger.py | CSV 로그 저장 |
| linux_info.py | Linux /proc 파일시스템 파싱 |
| requirements.txt | 의존성 관리 |

## 7. 자원 사용률 경고 기준

| 자원 | 임계치 |
|---|---:|
| CPU | 80% |
| RAM | 85% |
| DISK | 90% |

## 8. 참고 자료

- psutil 공식 문서: https://psutil.readthedocs.io/
- Linux proc filesystem: https://docs.kernel.org/filesystems/proc.html
- Python 공식 문서: https://docs.python.org/3/

## 9. 제한사항

Windows 환경에서 기본 모니터링, 경고 및 CSV 로그 저장 기능의 동작을 확인하였습니다. Linux /proc 파싱 기능은 Linux 전용으로 구현하였으며 실제 Linux 환경에서의 실행 검증은 수행하지 않았습니다.
