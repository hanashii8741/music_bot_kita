# Python 3.11을 기반으로 하는 이미지 사용
FROM python:3.11

# 시스템 패키지 설치 (C 컴파일러 및 Python 헤더 포함)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    libpq-dev \
    libncurses5-dev \
    libreadline-dev \
    libbz2-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    tk-dev \
    libncursesw5-dev \
    liblzma-dev \
    libffi-dev \
    libssl-dev


RUN pip install --upgrade pip
# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt .

# pip 업그레이드 및 의존성 설치
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 애플리케이션 복사
COPY . .

# 애플리케이션 실행
CMD ["python", "main.py"]
