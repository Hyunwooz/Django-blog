# Django Blog

-   Django를 이용한 Blog 제작 프로젝트 입니다.

## 1. 목표 및 기능

### 1.1 목표

-   Django를 이용하여 CRUD 기능을 구현할 수 있다.

### 1.2 기능

-   회원가입 및 로그인
-   비밀번호 변경
-   Profile CRD
-   게시글 CRUD ( Toast UI Editor )
-   게시글 조회수 표시
-   댓글 CRD
-   타이틀 Search
-   해당하는 Category Search

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

-   Python == 3.10.4
-   Django == 4.2.3
-   Pillow == 9.5.0

### 2.2 배포 URL

-   준비중

## 3. 프로젝트 구조와 개발 일정

### 3.1 Entity Relationship Diagram
![erd](https://github.com/Hyunwooz/Django-blog/assets/107661525/f554ac1a-47d8-4525-9d5f-316d7e05c914)

### 3.2 프로젝트 구조
```
Django-blog
│
├─App
├─blog
│  ├─migrations
│  ├─templates
│  │  └─blog
├─media
│  ├─blog
│  │  └─media
│  └─user
│      └─media
├─static
│  ├─blog
│  │  ├─assets
│  │  ├─css
│  │  ├─images
│  │  └─js
│  └─user
│      ├─css
│      ├─image
│      └─js
├─staticfiles
│  ├─admin
│  │  ├─css
│  │  ├─img
│  │  └─js
│  ├─blog
│  │  ├─assets
│  │  ├─css
│  │  ├─images
│  │  └─js
│  └─user
│      ├─css
│      ├─image
│      └─js
├─templates
├─user
│  ├─migrations
│  ├─templates
│  │  └─user
└─venv
```
### 3.3 개발 일정

#### 개발 일정

2023.07.17 ~ ing

#### 기술 스택

-   <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
-   <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
-   <img src="https://img.shields.io/badge/Sqlite-F80000?style=for-the-badge&logo=Sqlite&logoColor=white">

## 4. 전체 페이지

-   전체 페이지 UI
![로그인회원가입](https://github.com/Hyunwooz/Django-blog/assets/107661525/83616293-3d40-4fed-9184-3e719be31aab)
![메인](https://github.com/Hyunwooz/Django-blog/assets/107661525/4aaab86a-d4b2-4b19-a255-158ab2de8bd3)
![프로필 비밀번호](https://github.com/Hyunwooz/Django-blog/assets/107661525/8c82b80a-9766-4275-9c1f-b04b31440910)
![서치](https://github.com/Hyunwooz/Django-blog/assets/107661525/b6a9850a-5d88-4fca-b355-24617658eb9a)
![게시물디테일](https://github.com/Hyunwooz/Django-blog/assets/107661525/6fc6274c-d64a-45a9-8949-36e47a3650b9)

## 5. 기능

-   게시물 작성
![Write-min](https://github.com/Hyunwooz/Django-blog/assets/107661525/cee8c6c7-d54d-4682-b9ce-2adc3b999871)
-   게시물 수정
![edit](https://github.com/Hyunwooz/Django-blog/assets/107661525/92bad933-0fbf-4115-94b5-603b3b1494af)

## 6. 개발하며 느낀점

### 마치며

