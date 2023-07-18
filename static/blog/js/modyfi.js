const Editor = toastui.Editor;
const $save_btn = document.querySelector('.post_save');
const $thumbnail_btn = document.querySelector('.post_thumbnail');

const getCookie = function(name){
    const value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return value? value[2] : null;
}

const csrf_token = getCookie('csrftoken');
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

let thumbnail = null;
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
    const title = document.querySelector('.post_title').value
    const category = document.querySelector('.post_category').value
    let post = {
        "title": title,
        "content": editor.getHTML(),
        "category": category,
    }

    if (thumbnail != null) {
        post["thumbnail"] = '/media/'+ thumbnail
    } else {
        post["thumbnail"] = "blank"
    }

    let link =  document.location.href;
    let blog_idx = link.indexOf('blog');
    link = link.substring(blog_idx+4)
    let pk = link.replace(/\//g, '')

    $.ajax({
        type: 'POST',
        url: '/blog/edit/'+pk,
        data: post,
        dataType: 'json',
        timeout: 600000,
        beforeSend : function(xhr){
            xhr.setRequestHeader("X-CSRFToken",csrf_token);
        },
        success: function(data) {
            alert('글이 수정되었습니다.')
            location.href = '/blog/'+pk
        },
        error: function(e) {
            alert(e)
        }
    });
}

$save_btn.addEventListener('click',postSave)
$thumbnail_btn.addEventListener('change',thumbnailFunc)