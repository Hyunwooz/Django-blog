const Editor = toastui.Editor;
const $save_btn = document.querySelector('.post_save')

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

const postSave = (event) => {
    event.preventDefault()
    const title = document.querySelector('.post_title').value
    const category = document.querySelector('.post_category').value
    
    const post = {
        "title": title,
        "content": editor.getHTML(),
        "category": category,
    }

    $.ajax({
        type: 'POST',
        url: '/blog/write/',
        data: post,
        dataType: 'json',
        timeout: 600000,
        beforeSend : function(xhr){
            xhr.setRequestHeader("X-CSRFToken",csrf_token);
        },
        success: function(data) {
            alert('글이 저장되었습니다.')
            location.href = '/blog/'
        },
        error: function(e) {
            alert(e)
        }
    });
}

$save_btn.addEventListener('click',postSave)