# KRXA LOCAL BUILD v3 CANON

이 폴더가 현재 정본입니다.

## 의미

- v1: 기본 골격
- v2: 실행 엔진
- v3_CANON: 기본 골격 + 실행 엔진 + 정본 기준판

앞으로 작업은 이 폴더 하나에서만 진행합니다.

## 실행

```bat
python run_krxa.py status
python run_krxa.py run-m2m
python run_krxa.py recover
python run_krxa.py reset
```

또는:

```bat
KRXA_RUN.bat
KRXA_RUN_M2M.bat
KRXA_RESET.bat
```

## 핵심 구조

```text
core/
samples/m2m/user/
samples/m2m/dev/
samples/m2m/verify/
scripts/
build/
run_krxa.py
```

## 원칙

내 컴퓨터에서 완성하고, 저장소에는 완성본을 올린다.
Google Drive는 제작소가 아니라 업로드/보관소다.
