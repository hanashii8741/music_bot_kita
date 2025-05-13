# 베이스 이미지로 Python 3.11을 사용
FROM python:3.11

# 시스템 패키지 설치 (C 컴파일러 및 Python 헤더 포함)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    libffi-dev

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt .

# requirements.txt 파일을 기반으로 의존성 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 애플리케이션 복사
COPY . .

# 애플리케이션 실행
CMD ["python", "main.py"]