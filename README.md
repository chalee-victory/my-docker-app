# My Docker Web App

간단한 Flask 웹 애플리케이션의 Docker 컨테이너 패키징 예제입니다.

## 실행 방법 (Prerequisites: Docker)

파이썬이나 별도 라이브러리를 설치할 필요 없이 Docker만 설치되어 있으면 즉시 실행 가능합니다.

```bash
# 1. 저장소 복제
git clone [https://github.com/chalee-victory/my-docker-app.git](https://github.com/chalee-victory/my-docker-app.git)
cd my-docker-app

# 2. Docker 이미지 빌드
docker build -t my-web-app .

# 3. 컨테이너 실행
docker run -d -p 5000:5000 --name web-service my-web-app
