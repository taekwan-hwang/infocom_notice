
# 숭실대학교 전자정보공학부 공지사항 플러스친구
본 문서는 [숭실대학교 전자정보공학부 공지사항](http://infocom.ssu.ac.kr/rb/?c=2/38)을 크롤링하고, 이를 카카오톡 플러스친구에 추가된 이용자들에게 제공하는 플러스친구의 개발 환경, 설치 과정 등을 명세합니다.

## 1. 개발 환경

 * Amazon Web Service (EC2, Ubuntu 16.04 LTS)
 * Python 3.5.2
 * Git, Github

## 2. 사용 모듈

* phantomjs==2.1.3-dev-release
* django==2.0.1
* djangorestframework==3.7.7
* selenium==3.8.0
* bs4==0.0.1
* beautifulsoup4==4.6.0
* urllib3==1.7.1 
* apscheduler==3.5.1

## 3. 환경 설정

#### 1. 의존성 설치 

 * python 설치
  ~~~~
  sudo add-apt-repository ppa:jonathonf/python-3.6
  sudo apt-get update
  sudo apt-get install python3.6
  ~~~~
  
 * phantomjs 설치 및 환경변수 등록
  ~~~~
  wget https://github.com/ariya/phantomjs/releases/download/2.1.3/phantomjs
  cp phantomjs /usr/bin
  ~~~~
     
 * phantomjs 의존성 설치
  ~~~~
  sudo apt-get install libfontconfig
  ~~~~
  
#### 2. Git Repository clone

  ~~~~
  git clone https://github.com/taekwan-hwang/infocom_notice.git
  ~~~~
  
#### 3. python 패키지 설치 

  ~~~~
  cd infocom_notice
  pip install -r requirements.txt
  ~~~~
  
#### 4. 첫 DB마이그레이션 및 설정

  ~~~~
  python manage.py makemigrations
  python manage.py migrate
  ~~~~
  
#### 5. 카카오 계정 설정
* main/sender/datafield.py 파일을 생성해주어야 합니다. 
EMAIL 과 PASSWORD 필드가 존재하여야 하며 각각은 카카오 계정 이메일과 비밀번호입니다.
* 이 정보들은 해당 계정으로 만든 플러스친구에 등록된 이용자에게 메시지를 보내는 데 사용됩니다.
 
 ex)main/sender/datafield.py
 ~~~~
  EMAIL='{your_kakao_email}'
  PASSWORD='{your_kakao_password}'
 ~~~~
* 또한 main/scheduled_task.py 에서 KakaoSender 생성자를 호출할 때, kakaoPath를 설정해 주어야 합니다.

ex)main/scheduled_task.py

 ~~~~
 ln[18]: sender = KakaoSender(kakaoPath='https://center-pf.kakao.com/_hfvhC')
 ~~~~
 
## 4. 서버 시작
 ~~~~
 python manage.py runserver {your_server_ip}:{port}
 ~~~~
 
## 5. 동작 확인 
 * 카카오톡 플러스친구 자동응답 API에선 http://host-ip:port/keyboard에 대한 반응을 필수로 요구한다.
 * 단 이 프로젝트에서는 main/으로 시작되니 다음과 같이 입력해야한다.
   ~~~~
   curl -XGET 'http://host-ip:port/main/keyboard/'
   {"type":"text"}
   ~~~~
 * {"type":"text"} 와 같이 응답이 왔다면 정상적으로 설정되었다.
 
 
