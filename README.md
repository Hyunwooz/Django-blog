# Django Blog

-   Django를 이용한 Blog 제작 프로젝트 입니다.

## 1. 목표 및 기능

### 1.1 목표

-   Django를 이용하여 CRUD 기능을 구현할 수 있다.

### 1.2 기능

-   회원가입 및 로그인
-   비밀번호 변경
-   Profile CRU
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

### 2.2 배포 환경

-   Aws Lightsail
-   ~~Gunicorn~~
-   Nginx
-   uwsgi

### 2.2 배포 URL

<<<<<<< HEAD
-   http://blog.kanghyunwoo.com/
=======
-   http://52.78.152.106
>>>>>>> d2af9d1b0c7245c321cf8801bda59b67f8258d55

## 3. 프로젝트 구조와 개발 일정

### 3.1 Entity Relationship Diagram
![erd](https://github.com/Hyunwooz/Django-blog/assets/107661525/f554ac1a-47d8-4525-9d5f-316d7e05c914)

### 3.2 URL 설계

|이름|URL|비고|
|------|---|---|
|User|||
|회원가입|user/join/||
|로그인|user/login/||
|로그아웃|user/logout/||
|비밀번호 변경|user/changePassword/||
|프로필|user/profile/edit/||
|Blog|||
|글 목록|blog/||
|글 쓰기|blog/write/||
|글 디테일|blog/int:pk/||
|글 수정|blog/edit/int:pk/||
|글 삭제|blog/delete/int:pk/||
|제목 검색|blog/search/||
|카테고리 검색|blog/categorysearch/||
|좋아요|blog/like/int:pk/||
|이미지업로드|||
|이미지|blog/imageupload/||
|댓글|||
|댓글 작성|blog/comment/write/int:pk/||
|댓글 삭제|blog/comment/delete/int:pk/||

### 3.3 프로젝트 구조
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

2023.07.17 ~ 2023.07.20

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
-   회원가입 및 로그인
![login-join](https://github.com/Hyunwooz/Django-blog/assets/107661525/9782cb48-7ffa-4fd9-8607-ac73abe04b0d)
-   프로필
![pf](https://github.com/Hyunwooz/Django-blog/assets/107661525/85ae538f-976e-4831-ae3a-5a48be7f8998)
-   게시물 작성
![Write-min](https://github.com/Hyunwooz/Django-blog/assets/107661525/cee8c6c7-d54d-4682-b9ce-2adc3b999871)
-   게시물 수정
![edit](https://github.com/Hyunwooz/Django-blog/assets/107661525/92bad933-0fbf-4115-94b5-603b3b1494af)
-   댓글
![comment-min](https://github.com/Hyunwooz/Django-blog/assets/107661525/bb12072c-e58f-4ad4-8787-7bf153321d1c)
-   제목 검색
![sec-tt](https://github.com/Hyunwooz/Django-blog/assets/107661525/1262ce35-af60-476a-91ec-1e9a6b63595a)
-   카테고리 검색
![sec-ct](https://github.com/Hyunwooz/Django-blog/assets/107661525/07f160d0-cb87-48e9-a295-29b10c23a93d)
## 6. 개발과정과 느낀점
### Aws Lightsail을 이용하여 서버 배포

처음에는 runserver를 이용하여 백그라운드에서 서버를 실행 하여 SSH를 끄더라도 서버가 돌아가게끔 설정했습니다.

그 후 Django_Secret_Key를 .bashrc 파일에 환경변수를 추가하여 설정했습니다.

다만 매번 .bashrc를 실행시켜줘야 하는 번거로움이 있어 , .bash_profile을 생성하여

SSH로 접속할 때 마다 .bashrc를 실행할 수 있도록 설정하였습니다.

그후 runserver로 서버를 구동할 경우 보안상 문제가 발생할 여지가 있다하여 Nginx와 Gunicorn을 연동하여 배포하게되었습니다.

1.  https://twowix.me/85  # Runserver로 서버를 돌리면 안되는 이유
2.  https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver # Django Docs
3.  https://leffept.tistory.com/282 # Django를 Nginx와 Guicorn 연동하여 배포하기

위의 블로그를 참고하여 배포과정을 진행하였습니다. 배포 도중 많은 에러들을 경험하였지만,
대부분의 원인들은 gunicorn과 nginx의 여러 설정 파일을 잘못 기입 했을 경우 발생하였습니다.

개인 도메인을 구매 한 후 AWS Lightsail에서 도메인 및 DNS 설정을 변경하고 도메인 구매처에서 네임서버 변경을 완료하여 적용하였습니다.

- nginx에서 502 Bad Gateway
    - 아직 정확한 원인파익은 되진않았지만 gunicorn이 제대로 작동하지 않아서 발생한 문제로 파악됩니다. nginx에서 gunicorn으로 요청을 전달해주는 reverse proxy에서 발생한 걸로 추측됩니다.
- 111: Connection Refused
    - 너무나 다양한 오류가 많았으며 결과적으로 여러 설정파일에서 문제가 복합적으로 존재하여 발생한 에러입니다.
- 13: Permission Failed
    - gunicorn.socket을 실행시키는데 권한이 없어 발생한 문제입니다. chmod로 권한을 변경하여 해결하였지만 , 보안상 문제가 있다는 정보들이 많았습니다. 권한을 늘려버리면 누군가 해당 파일을 수정시켜버릴 수 있기때문입니다.
- gunicorn ModuleNotFoundError: No module named 'config'
    - 단순히 설정 파일에서 config 대신 wsgi.py파일이 있는 폴더 이름을 적어주면 해결되는 문제였습니다. 
- gunicorn.socket could not be found. 
    - 소켓 위치를 찾을 수 없어서 생겼던 오류 > 생성을 하지 않았기에 당연히 존재하지 않았습니다.
- gunicorn /tmp/gunicorn.socket failed 
    - 소켓을 실행시켰지만 실패함. 제 gunicorn.sokect이 해당 경로에 존재하지 않았습니다.

등등 많은 오류들을 만나 설정 파일들이 너무 꼬여버린 바람에 더이상 진행이 되지않아 gunicorn에서 uwsgi로 변경하여 배포하기로 결정하였습니다.

다만 위에서 여러 시도와 검색을 통해 배우게된 사실들이 있습니다.

Proxy
- 정보를 대신 전달해주는 주체입니다.

Reverse Proxy
- 클라이언트의 요청을 대신 받아 내부 서버로 전달해주는 것을 말합니다. = nginx가 그 역할을 하고있습니다.

Reverse Proxy를 이용하는 장점
- 로드 밸런싱 : 클라이언트의 요청을 프록시 서버에 분산하여 성능, 확장성을 향상시킬 수 있습니다.
- 캐싱 : Reverse Proxy를 사용하실 경우 렌더링된 페이지를 미리 캐싱하여 페이지 로드시간을 단축할 수 있습니다.
- DDoS : 수신 요청과 단일 IP 주소당 연결 수를 제한할 수 있어서 DDoS를 방지할 수 있습니다.

이 외에도 여러가지 장점이 존재한다는 걸 알수 있었습니다. 다음으로

Unix socket과 Network socket의 차이입니다.

- Network socket
    - 네트워크 상에서 처리되는 커뮤니케이션
    - TCP/UDP 프로토콜을 사용한 통신

- Unix socket
    - Unix Domain Socket.
    - IPC(Inter process communication) Socket
    - 내부의 프로세스들끼리 통신만을 위한 양방향 통신 소켓.

리눅스에서 Unix socket을 사용하는 이유는 시스템상의 프로그램에서 프로세스 간 로컬 통신이 필요할 경우 Network socket보다 속도나 효율성 면에서 유리한 이점을 가져올 수 있기 때문입니다.

> 참고블로그 : https://rura6502.tistory.com/entry/Unix-Socket-vs-TCP-Socket

uwsgi와 nginx를 연동하기 위해서 "Django 자습" 이라는 사이트의 내용을 참고하여 진행하였습니다.

> 참고사이트 : https://wikidocs.net/6611

위의 사이트를 그대로 진행한다 하더라도 제대로 작동이 되진않습니다. 설정 파일을 본인의 환경에 맞게 설정하셔야 합니다.

제가 어떠한 실수를 하였고 , 어떤식으로 진행하였는지 알려드리겠습니다.

`$ git clone {각자의 github 주소}`

git을 가져와 주시고 , 장고 폴더내에서 가상환경을 세팅해줍니다.

`(venv) $ pip install uwsgi`

설치를 진행 하고 

/home/{사용자이름}/{장고 프로젝트 폴더}/run/ 에 uwsgi.ini 파일을 만들어주었습니다.

여기서 많은 실수가 있었습니다.

제가 별표* 를 친 곳이 제가 계속 놓쳤던 부분입니다. 

```
[uwsgi]
uid = {사용자이름}
base = /home/%(uid)/{장고 프로젝트 폴더}

home = %(base)/venv
chdir = %(base)/
*module = {장고 폴더내 wsgi.py파일이 있는 폴더 이름 }.wsgi:application
*env = DJANGO_SETTINGS_MODULE={장고 폴더내 settings.py파일이 있는 폴더 이름 }.settings

master = true
processes = 5

socket = %(base)/run/uwsgi.sock
chown-socket = %(uid):www-data
chmod-socket = 660
vacuum = true
```
```
Django
  -App
    - wsgi.py
    - settings.py
  -Blog
  -User
```
module과 env의 경우 예를들어 위의 폴더트리가 존재한다고 가정한다면 

```
module = App.wsgi:application
env = DJANGO_SETTINGS_MODULE=App.settings
```

이렇게 작성해야 됐습니다.

위의 코드를 보면 위에서 말씀드렸던

- gunicorn ModuleNotFoundError: No module named 'config' 

해당 오류는 쉽게 해결할 수 있다는 생각이 드네요.

다음 과정으로는 

/etc/systemd/system/ 에 uwsgi.service 파일을 만들어야 합니다.
제가 별표* 를 친 곳이 제가 계속 놓쳤던 부분입니다. 

```
[Unit]
Description=uWSGI Emperor service

[Service]
*ExecStart=/home/{사용자이름}/{장고 프로젝트 폴더}/venv/bin/uwsgi \
        *--emperor /home/{사용자이름}/{장고 프로젝트 폴더}/run # 이는 아까 만드셨던 uwsgi.ini 파일의 경로입니다.
*User={사용자이름}
Group=www-data
Restart=on-failure
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all
StandardError=syslog

[Install]
WantedBy=multi-user.target
```

여기까지가 설정 파일은 작성은 끝입니다.

```
sudo systemctl start uwsgi # 서비스 시작
sudo systemctl enable uwsgi # SSH를 껐다 키더라도 자동 실행 되게 함
```
2가지 리눅스 명령어를 통해 서비스 실행 및 등록을 진행하였습니다.

```
systemctl status uwsgi
```

위의 명령어를 통해 uwsgi의 상태를 확인할 수 있으며 , /var/log/ 경로에 syslog 파일을 확인하시면 다양한 에러 로그를 확인할 수 있습니다.

그 후 nginx를 설치 하고 uwsgi와 연동하여 배포를 하는데 성공하였습니다.

아래는 nginx와 uwsgi를 연동하는 nginx 설정입니다.

여기서도 제가 실수했던 부분에 숫자를 표시하여 설명드리겠습니다.

```
#1 upstream withthai-django {
    server unix:/home/{사용자이름}/{장고 프로젝트 폴더}/run/uwsgi.sock;
}

server {
        listen 80;
        server_name {개인 도메인 or 고정 IP};

        location = /favicon.ico { access_log off; log_not_found off; }

        location /static/ {
                root /home/{사용자이름}/{장고 프로젝트 폴더}/; # static파일이 있는 경로를 적어주시면 됩니다.
        }

        location / {
            include         /etc/nginx/uwsgi_params;
            #3 uwsgi_pass      django;
        }
}
```

#1 `*upstream withthai-django` 해당 부분과 #3 `uwsgi_pass      django;`여기서
withthai-django과 django 이 부분은 아래처럼 일치해야합니다.

```
#1 upstream 변수명 {
    server unix:/home/foo/django_test/run/uwsgi.sock;
}

server {
        ... 생략 ...
        location / {
            include         /etc/nginx/uwsgi_params;
            #3 uwsgi_pass      변수명;
        }
}
```

장황하게 설명을 하였지만 , 결국 오타와 잘못된 정보 기입의 문제였습니다. 다음에는 좀 더 원활하게 배포할 수 있도록 더욱 공부하도록 하겠습니다. 

### Toast Ui Editor를 입히기 위한 과정
#### Client와 server의 비동기 통신 과정

Toast Ui Editor(이하 에디터) 제공하는 기능 중 Hook를 통해서 게시글을 쓰는 도중 이미지를 업로드 할 수 있도록 하는 기능이 있는데,
이 기능은 비동기통신으로 server에 데이터를 주고받을 수 있게 해주는 역할을 하였습니다.

해당 기능을 이용하는 이유는 총 2가지가 있었습니다.

1. 여러 이미지를 업로드 할 수 있도록 하기 위해
2. Post 작성도중 업로드한 이미지 표시를 위해

처음 비동기 통신으로 이미지 데이터만을 보냈을 때 당연히 실행되지 않았습니다.
이유는 바로 csrftoken을 헤더에 넣어주지 않아서 였습니다. 

cookie에서 csrftoken을 가져와 header에 csrftoken을 넣어 통신에 성공하게 되었습니다.

여기서 문제가 발생하였습니다. 

바로 "이미지만 어떻게 업로드 시킬 것인가?" 입니다.
고민 끝에 저는 이미지 업로드만을 담당하는 모델을 만들기로 결정 후 media 폴더로 업로드 하는데 성공했습니다.

```js
editor.js
export const editor = new Editor({
    ... 생략 ..
    hooks: {
        // editor에서 이미지 업로드 기능
        addImageBlobHook: (blob, callback) => {

            const formData = new FormData();
            formData.append('image', blob);
            
            let url = '/media/';

            $.ajax({
                type: 'POST',
                enctype: 'multipart/form-data',
                url: '/blog/imageupload/',
                data: formData,
                dataType: 'json',
                ... 생략 ...,
                beforeSend : function(xhr){
                    xhr.setRequestHeader("X-CSRFToken",csrf_token);
                },
                success: function(data) {
                    url = url + data.url
                    callback(url, '사진 대체 텍스트 입력');
                },
                error: function(e) {
                    callback('image_load_fail', '사진 대체 텍스트 입력');
                }
            });
        }
    }
});
```

```py
Views.py
class ImgUpload(View):
    def post(self, request):
        image = request.FILES['image']
        imageUpload = ImageUpload.objects.create(image=image)
        url = imageUpload.image
        data = {
            'url': str(url)
        }
        return JsonResponse(data)
```

위의 과정을 통해 RestFull API의 구조에 대해 공부할 수 있는 계기가 되었습니다.
또한 프론트엔드와 백엔드 사이에 의사소통이 정말 중요하다라는 걸 다시 한번 깨닫게 되었습니다.

### 데이터베이스 설계의 중요성 feat.(type , dir 찍어보기)
#### 모델간 1:1 관계에서 Filter 제대로 활용해보기

제가 원하는 데이터는 
- Category 모델에 있는 name값이 request.GET['category']인 Post를 모두

입니다.

제가 원하는 데이터를 가져오기 위해 많은 시행착오가 있었습니다.

원래 진행했던 데이터베이스 설계를 바꾼다던가 select_related()를 사용한다던가 등등 여러 시도를 해봤지만, 결국 해결하지 못해 원점으로 돌아오게됬습니다.

어떻게 이를 해결할까 고민을 하던 도중 문득 생각난 것이 "근데 장고는 어떤 SQL 쿼리문을 보내는 걸까?" 입니다.

위의 생각을 확인하기 위해 아래의 과정을 진행하였고, 결국 원하는 데이터를 보낼 수 있게 되었습니다.

```py
results = Category.objects.select_related().filter(name=request.GET['category'],status='active').order_by('-created_at')
        
print(dir(results))
--- 실행 결과
['__aiter__', '__and__', '__bool__', '__class__', ... 생략 ... ,'ordered', 'prefetch_related', 'query', 'raw', 'resolve_expression', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'using', 'values', 'values_list']
```

```py
print(results.query)
```
```sql
SELECT 
    "blog_category"."id", 
    "blog_category"."post_id", 
    "blog_category"."created_at", 
    "blog_category"."name", 
    "blog_post"."id", 
    "blog_post"."title", 
    "blog_post"."content", 
    "blog_post"."writer_id", 
    "blog_post"."status", 
    "blog_post"."thumbnail", 
    "blog_post"."views", 
    "blog_post"."created_at", 
    "blog_post"."updated_at", 
    "user_user"."id", "user_user".
    "password", 
    "user_user"."first_name", 
    "user_user"."last_name", 
    "user_user"."email", 
    "user_user"."is_profile", 
    "user_user"."is_staff", 
    "user_user"."is_superuser", 
    "user_user"."is_active", 
    "user_user"."date_joined", 
    "user_user"."last_login" 
FROM "blog_category" 
INNER JOIN "blog_post" ON ("blog_category"."post_id" = "blog_post"."id") 
INNER JOIN "user_user" ON ("blog_post"."writer_id" = "user_user"."id") 
WHERE "blog_category"."name" = Tech 
ORDER BY "blog_category"."created_at" DESC
```
위의 과정을 통해 Django에서 어떤식으로 SQL 쿼리문을 작성해서 보내는지 파악이 되었으며 Django에서 제공하는 select_related()에 대한 이해도가 상승하게 되었습니다.

dir,type 등을 활용해서 다양한 정보를 얻었으면 좋겠습니다.

### 마치며

위에서 서술했던 내용들 말고도 해당 프로젝트를 진행하며 크고 작은 이슈들이 많았지만, 이번 프로젝트를 통해 Django와 좀 더 친해지는 계기가 되었습니다.

제가 백엔드 개발자로서 일을 하게된다면 , 프론트엔드 개발자와의 의사소통이 정말 중요하다는 것을 깨닫기도 했습니다.

어쩌다 마주치게된 비동기 통신을 통해 Django Rest Framework에 대해 공부할 기회가 되기도 했으며 Django가 얼마나 매력적인 Web Framework인지도 알게되었습니다.

이런 의미있는 프로젝트들을 진행하며 앞으로도 더욱 성장하는 개발자가 되도록 하겠습니다.

끝까지 읽어주신 모든 분들 감사합니다 :)
