# csl_confirm
사용자에게 보여줄 정보를 회원가입 혹은 어드민이 추가한 후 정보를 보여줄 수 있음.

# 시작
1. pip install django
2. python manage.py runserver


# 기능
1. admin
   1. 127.0.0.1:8000/admin
   2. admin/csladmin
   3. 사용자 추가
   4. 사용자별 점수 추가
   5. 과목명 추가
   6. 업로드 기능 이용(csv 파일 가능) 아래 양식(컬럼명 변경시 뷰 자동 변경)
        >학번,국어,정보,수학,영어,inform5,inform6,inform7,inform8,inform9,inform10
        >a1,1100,200,300,400,500,600,700,800,900,1000
        >a2,2100,200,300,400,500,600,700,800,900,1001
        >a3,3100,200,300,400,500,600,700,800,900,1002

2. 사용자
   1. 회원가입
   2. 자신의 점수 조회
   
3. 화면
![](/imgs/1.png){: width="400"}
![](/imgs/2.png){: width="400"}
![](/imgs/3.png){: width="400"}
![](/imgs/4.png){: width="400"}
![](/imgs/5.png){: width="400"}



