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
### Toast Ui Editor를 입히기 위한 과정
#### 어쩌다 만들어진 Client와 server의 비동기 통신 과정

Toast Ui Editor(이하 에디터) 제공하는 기능 중 Hook를 통해서 게시글을 쓰는 도중 이미지를 업로드 할 수 있도록 하는 기능이 있는데,
이 기능은 비동기통신으로 server에 데이터를 주고받을 수 있게 해주는 역할을 하였습니다.

해당 기능을 이용하는 이유는 총 2가지가 있었습니다.

1. 여러 이미지를 업로드 할 수 있도록 하기 위해
2. Post 작성도중 업로드한 이미지 표시를 위해

처음 비동기 통신으로 이미지 데이터만을 보냈을 때 당연히 실행되지 않았습니다.
당연히 될거라 생각했지만 안되니 정말 당황했습니다. 
이유는 바로 csrftoken을 헤더에 넣어주지 않아서 였습니다. 

다만 지난 Django 수업에서 Postman을 이용하여 통신하였던 걸 떠올려 브라우저의 cookie에서 csrftoken을 가져오는 방법을 찾아낸 후 header에 csrftoken을 넣어 통신에 성공하게 되었습니다.

여기서 문제가 또 발생하였습니다. 

바로 "이미지만 어떻게 업로드 시킬 것인가?" 입니다.
고민 끝에 저는 이미지 업로드만을 담당하는 모델을 만들기로 결정 후 media 폴더로 업로드 까지 하는데 성공하였습니다.

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
                processData: false,
                contentType: false,
                cache: false,
                timeout: 600000,
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

위의 과정을 통해 DRF가 어떻게 돌아가게 되는 지에 대해서 약간이나마 이해가 가는 계기가 되었습니다.

또한 프론트엔드와 백엔드 사이에는 의사소통이 엄청 중요하다라는 걸 다시한번 깨닫게되었습니다.

### 데이터베이스 설계의 중요성 feat.(type , dir 찍어보기)
#### 모델간 1:1 관계에서 Filter 제대로 활용해보기

해당하는 Category를 가진 Post들만을 보여주는 데이터를 전송해줄 때 겪었던 일입니다.

제가 원하는 데이터는 
- Category 모델에 있는 name값이 request.GET['category']인 Post를 모두

입니다.

제가 원하는 데이터를 가져오기 위해 많은 시행착오가 있었습니다.

원래 진행했던 데이터베이스 설계를 바꾼다던가 select_related()를 사용한다던가 등등 여러 시도를 해봤지만, 결국 해결하지 못해 원점으로 돌아오게됬습니다.

어떻게 이를 해결할까 고민을 하던 도중 문득 생각난 것이 "근데 장고는 어떤 SQL 쿼리문을 보내는 걸까?" 라는 생각이 들었습니다.

그래서 아래의 과정을 진행해보았고 , 결국 원하는 데이터를 보낼 수 있게 되었습니다.

이걸 읽으시는 분들 한번씩 dir,type 등을 찍어보시는 것을 권장합니다.

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
위의 과정을 통해 Django에서 어떤식으로 SQL 쿼리문을 작성해서 보내는지 파악이 되었으며 Django에서 제공하는 select_related()에 대한 이해또한 상승하게 되었습니다.

다들 dir,type 등을 활용해서 다양한 정보를 얻었으면 좋겠습니다.

### 마치며

위에서 서술했던 내용들 말고도 해당 프로젝트를 진행하며 크고 작은 이슈들이 많았지만, 이번 프로젝트를 통해 Django와 좀 더 친해지는 계기가 되었습니다.

제가 백엔드 개발자로서 일을 하게된다면 , 프론트엔드 개발자와의 의사소통이 진짜 중요하다는 것을 깨닫기도 했습니다.

어쩌다(?) 마주치게된 비동기 통신을 통해 Django Rest Framework에 대한 이해가 조금 상승하기도 했으며 Django가 얼마나 매력적인 웹 프레임워크 인지도 알게되기도 하고 정말 의미있는 프로젝트가 아니였나 싶습니다.

앞으로도 더욱 성장하는 개발자가 되도록 하겠습니다.

끝까지 읽어주신 모든 분들 감사합니다 :)