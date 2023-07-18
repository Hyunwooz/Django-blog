const Editor = toastui.Editor;
const $title = document.querySelector('.post_title')
const $category = document.querySelector('.post_category')
const $save_btn = document.querySelector('.post_save');
const $thumbnail_btn = document.querySelector('.post_thumbnail');

const getCookie = function(name){
    const value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return value? value[2] : null;
}
const csrf_token = getCookie('csrftoken');

let link =  document.location.href;
let blog_idx = link.indexOf('edit');
link = link.substring(blog_idx+4)

const editor = new Editor({
    el: document.querySelector('#editor'),
    height: '600px',
    initialEditType: 'markdown',
    previewStyle: 'vertical',
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

let thumbnail ;
const loadPostData = () => {

    let post = {
        "message": "Data plz",
    }

    $.ajax({
        type: 'POST',
        url: '/blog/loadpost'+link,
        data: post,
        dataType: 'json',
        timeout: 600000,
        beforeSend : function(xhr){
            xhr.setRequestHeader("X-CSRFToken",csrf_token);
        },
        success: function(data) {
            $title.value = data.title
            $category.value = data.category
            editor.setHTML(data.content)
        },
        error: function(e) {
            console.log(e)
        }
    });
}

// 썸네일 이미지 저장
const thumbnailFunc = () =>{
    
    const formData = new FormData();
    formData.append('image', $thumbnail_btn.files[0]);
    
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
            thumbnail = data.url
            console.log('Result: 성공')
        },
        error: function(e) {
            console.log(e)
        }
    });
}

const postSave = (event) => {
    event.preventDefault()

    let post = {
        "title": $title.value,
        "content": editor.getHTML(),
        "category": $category.value,
    }

    if (thumbnail != null) {
        post["thumbnail"] = '/media/'+ thumbnail
    } else {
        post["thumbnail"] = "blank"
    }

    $.ajax({
        type: 'POST',
        url: '/blog/edit'+link,
        data: post,
        dataType: 'json',
        timeout: 600000,
        beforeSend : function(xhr){
            xhr.setRequestHeader("X-CSRFToken",csrf_token);
        },
        success: function(data) {
            alert(data.message)
            location.href = '/blog'+link
        },
        error: function(e) {
            alert(e.toString())
        }
    });
}

// Post data들 불러오고 넣기
loadPostData()
$save_btn.addEventListener('click',postSave)
$thumbnail_btn.addEventListener('change',thumbnailFunc)