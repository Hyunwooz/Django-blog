import { getCookie } from "./utils.js"
import { editor } from "./editor.js";

const $save_btn = document.querySelector('.post_save');
const $thumbnail_btn = document.querySelector('.post_thumbnail_input');
const $title = document.querySelector('.post_title_input')
const $category = document.querySelector('.post_category_input')

const csrf_token = getCookie('csrftoken');

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
$thumbnail_btn.addEventListener('change',thumbnailFunc)