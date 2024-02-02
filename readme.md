# DeploymentSession

### 피로그래밍 17기 배포 세션1, 배포 세션 2 레퍼지토리

<b>실습 내용 - 배포 세션 1</b> : [https://even-plain-88c.notion.site/1-abeefa387a864b0faf430fbfb8012bc5](https://www.notion.so/1-abeefa387a864b0faf430fbfb8012bc5)
<br>

<b>실습 내용 - 배포 세션 2</b> : [https://even-plain-88c.notion.site/2-220813-4c55e7d14fd24985b95fecbab09625ac](https://even-plain-88c.notion.site/2-220813-4c55e7d14fd24985b95fecbab09625ac)
<br>

<b>실습 목표</b> :

① 배포에 대해 이해한다.<br>
② AWS EC2 를 사용하여 직접 프로젝트를 배포한다.

<br>
실습 화면 :
<div align=center>
    <img width="39.5%" alt="스크린샷 2022-08-04 오후 11 17 06" src="https://user-images.githubusercontent.com/62539910/182874039-56138a3e-f511-462e-932e-12c4dbc088f2.png">
    <img width="40%" alt="스크린샷 2022-08-04 오후 11 17 34" src="https://user-images.githubusercontent.com/62539910/182874053-f884812a-9e83-494c-a483-42219bdb48f3.png">
</div>


---

<br>

### 브랜치 목록

① master : 실제 실습에서 사용할 브랜치
    
② deployment-session-1 : 방명록 작성 프로젝트가 구현되어 있는 브랜치. 개발 모드에 적합하게 구현되어 있음
    
③ deployment-session-1-with-security : deployment-session-1의 내용에서 배포하기 전 수행해야 하는 보안 조치를 취한 브랜치. 배포 모드에 적합하게 구현되어 있음

<br>    

### 실행

```java
"""
git, python3, venv 등은 이미 설치되어 있다고 가정.
"""

// 해당 레퍼지토리 클론
$ git clone https://github.com/KYBee/DeploymentSessionPiro17.git

// 클론받은 레퍼지토리로 이동
$ cd DeploymentSessionPiro17

// 가상환경 생성
$ python3 -m venv venv

// 가상환경 실행
$ source venv/bin/activate

// 필요한 모듈 설치
$ pip3 install -r requirements.txt

// makemigrations
$ python3 manage.py makemigrations

// migrate
$ python3 manage.py migrate

// 서버 실행
$ python3 manage.py runserver

```
