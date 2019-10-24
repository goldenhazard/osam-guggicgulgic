IoT_Guggicgulgic
===================

# 1. 프로젝트 이름
------------------
## 상병 자비스 (Corporal Jarvis)

# 2. 프로젝트 개요
--------------------
## 2.1 프로젝트 Overview

#### 실제 군 내에서 전화를 교환해주거나 전화를 받는 보직을 임하게 되면, 업무와 전혀 관계없는 일과 관련된 전화가 오는 경우가 매우 흔합니다.
저희 프로젝트 **상병 자비스**는 **Google Speech Recognition** 음성인식모듈과 **Chatbot**에 의한 답변학습을 활용하여, 위와 같은 발신자의
음성을 인식해, 그에 대한 답변을 전화기 하드웨어의 화면에 디스플레이해주는 AI기반 IoT 군 전화기입니다.

# 3. 상병 자비스 블록다이어그램
-------------------------
#### 링크 올려드리겠습니다.
[Block Diagram of Jarvis](https://www.draw.io/?state=%7B%22ids%22:%5B%221iwCvxclkZYj36zZODpW1UAqr17ZMdT-A%22%5D,%22action%22:%22open%22,%22userId%22:%22101443275628626820839%22%7D#G1iwCvxclkZYj36zZODpW1UAqr17ZMdT-A)
사진도 올려드리겠습니다.
![Block_Diagram](https://user-images.githubusercontent.com/54850462/67497036-53b07780-f6b8-11e9-8f18-d50d27cbe45f.jpg)

# 4. 상병 자비스 매뉴얼
----------------------
#### 사용자의 관점에서 서술하겠습니다.
1) 수화기를 들면 LCD의 Backlight가 켜지고 LCD 화면에는 **Corporal Jarvis**라는 서비스 이름이 출력됩니다.

2) RFID 카드를 RFID 센서가 부착되어 있는 전화기의 하드웨어에 대면, 삑 소리와 함께 사용자의 음성이 웹으로 보내지고
   RFID 카드를 때면 삐빅 소리와 함께 음성 전송이 종료됩니다. 음성 전송 중에는 LCD에 **로딩 중**을 의미하는 애니메이션이
   보여집니다.
   
3) RFID를 태그할 동안 입력된 음성에 대한 답변이 LCD에 디스플레이되며, 답변의 사이즈가 16byte를 넘을 경우 Autoscroll을 지원해
   문구가 LCD에 슬라이드됩니다.
   
4) 입력된 질문과 출력된 답변은 사용자의 앱 UI에 메신저 형식으로 표시되고, 서버의 repository에 자동저장됩니다.

5) RFID가 센서에 입력되면 휴대폰의 카메라가 웹으로 사용자의 캡쳐사진을 보내주며, 그 이후 카메라의 촬영화면이 웹에 스트리밍됩니다.

# 5. 상병 자비스 동작코드 및 구조

## 5.1 





