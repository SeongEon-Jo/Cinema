# 롯데시네마 재개봉 프로젝트 - LIKELION 8기 X LOTTE (2020)<br><br>HUFS(Seoul)

---

## 1. 프로젝트 소개

>
### 1.1 주제 
- 롯데의 유통, 물류, 제조 서비스 중에서 현재 불편함을 느끼는 부분을 스스로 도출하거나, 롯데그룹에 새롭게 제안하고 싶은 주제를 자유롭게 개발하는 방향

>
### 1.2 프로젝트 소개
- 롯데시네마 재-개봉 프로젝트는 코로나 19로 타격을 입고 있는 영화관과 연달은 개봉연기로 볼거리가 부족한 관객들을 위해 우리지역에서 상영할 영화들을 관객들이 직접 투표해 관람을 이끌어 낼 수 있는 서비스입니다. 관객들은 홈페이지에 접속해 재개봉 했으면 하는 영화를 직접 투표할 수 있습니다. 투표율 TOP 10 작품 뿐만 아니라, 검색을 통해 찾는 작품에 투표할 수 있습니다.  중복투표는 불가하나 다중투표는 가능합니다. 관리자는 지역별 투표율을 한 눈에 볼 수 있으며, 이를 다음 주/달/분기에 상영할 재개봉 영화에 반영할 수 있습니다. 재개봉이 확정되면 홈페이지와 롯데시네마 공식 인스타그램 계정을 통해 공지합니다. 이를 통해 상영관의 활용도를 높임과 더불어 SNS 계정 홍보를 통한 마케팅 효과를 기대할 수 있습니다.

>
### 1.3 팀원
|이름|담당|
|:---:|:---:|
|윤영택|팀장 및 백엔드(영화 데이터 수집 및 분류)|
|조성언|백엔드(메인 페이지 & 영화 카테고리별 추천)|
|김민채|UI/UX & 로고 제작|
|고명주|프론트엔드|
|정은아|PPT제작 및 기능 개선|

---
## 2. 프로젝트 정보
## 2.1 영화 데이터
>
- 연도별 데이터를 수집하려 했으나 데이터의 양이 너무 방대한 관계로 네이버에서 상위 2000개의 영화 데이터를 가져왔다.
- 장르별 추천 기능을 위해 장르 객체를 미리 만들어 놓은 후에 연결시켜주었다.
![영화_데이터_코드](https://user-images.githubusercontent.com/29058347/96351999-cfda7100-10fa-11eb-895a-b1b2c7f589b2.png)

## 2.2 주요 기능
>
## 사용자
### 1. 이메일 인증을 통한 회원가입
![이메일_인증](https://user-images.githubusercontent.com/29058347/96223316-ab7e7780-0fc8-11eb-9e11-873241f0c4e0.JPG)
![이메일_인증_코드](https://user-images.githubusercontent.com/29058347/96351917-f77d0980-10f9-11eb-9be4-7a8ab6fe222d.png)<br>
### 2. 영화 검색(네이버 영화 기준 평점 상위 2000개)
![검색](https://user-images.githubusercontent.com/29058347/96223331-b33e1c00-0fc8-11eb-818b-79100523a49a.JPG)<br>
### 3. 카테고리별 랜덤 영화 추천
![추천](https://user-images.githubusercontent.com/29058347/96223370-c0f3a180-0fc8-11eb-8d36-d55d8e6cb38a.jpg)<br>
### 4. 재개봉을 원하는 영화에 투표
![투표](https://user-images.githubusercontent.com/29058347/96223328-b0432b80-0fc8-11eb-89c0-281a8904dac3.JPG)<br>

>
## 관리자
### 1. 지역별 투표 현황 확인
![투표현황](https://user-images.githubusercontent.com/29058347/96223344-b933fd00-0fc8-11eb-92d4-5c546765c409.JPG)<br>
### 2. 중복 투표 방지
#### 중복투표 방지를 위해 Django Model의 ManyToManyField를 이용했다.
![모델](https://user-images.githubusercontent.com/29058347/96351939-314e1000-10fa-11eb-8fda-b24af4c0f478.png)<br>
#### 투표시 해당 유저가 voted_users필드에 존재하는지 확인한다.
![코드](https://user-images.githubusercontent.com/29058347/96352062-6eff6880-10fb-11eb-8234-e948e04cbe28.png)<br>
### 3. 투표 대상에서 제외 + 상영 확정하는 권한
![제외_상영_확정](https://user-images.githubusercontent.com/29058347/96223341-b6390c80-0fc8-11eb-92ce-5c1408d217af.JPG)<br>


---
## 3. 후기 및 개선점

>
### 3.1 아쉬웠던 점 
- 프로젝트 주제 변경으로 인해 시간적인 여유가 없었던 점
- REST API를 이용해 백과 프론트를 분리하지 않아서 템플릿 문법을 적용하는 데 시간이 낭비되었다.
- 반응형을 부분적으로 구현하지 못한 부분이 있었다.

>
### 3.2 개선방향 & 확장
- 더 많은 영화 데이터를 수집·분류하고 그에 따라 발전된 검색 엔진을 구현한다.
- 사용자의 성향과 키워드에 따른 추천 알고리즘을 구현한다.
- 관리자가 유의미한 정보를 얻을 수 있도록 통계 및 분석 기능을 향상시킨다.
- 비밀번호 분실시 이메일을 통해 비밀번호를 찾을 수 있게 한다.
- UI/UX를 향상시킨다.
