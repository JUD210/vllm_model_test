# LLM API 사용 가이드

### 1. FastAPI 서버 실행

1. **모델 경로 수정**  
   `fastAPIWithoutCache.py` 파일에서 `model_path` 값을 사용할 모델 경로로 수정.

2. **서버 실행**  
    - 터미널에서 다음 명령어로 서버 실행:

    ```bash
    python3 fastAPIWithoutCache.py
    ```

    - **백그라운드 실행 및 로그 저장**  
    백그라운드에서 실행하고 로그를 저장하려면:

    ```bash
    nohup python3 fastAPIWithoutCache.py >> fastAPIWithoutCache.log &
    ```


### 2. 로컬 컴퓨터에서 서버 실행 시 (외부 접근 설정)

- 로컬에서 서버를 실행할 경우 **Ngrok**으로 외부 접근 설정을 추가.


### 3. API 서버 호출하기

- 다른 컴퓨터에서 API 서버를 호출하려면 다음 방법을 사용:
  - **Python**: `callAPI.py`로 호출
  ```bash
  $ python3 callAPI.py "안녕? 이름이 뭐니?"

  Latency: 8.880962371826172 seconds
  LLM response: {"text":" 어쩌구 저쩌꾸 (영문)"}
  ```
  - **Flutter**: `my_flutter_webapp`에서 호출
