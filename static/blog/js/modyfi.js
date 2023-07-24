import { getCookie } from "./utils.js"
import { editor } from "./editor.js";

const Editor = toastui.Editor;
const $title = document.querySelector('.post_title_input')
const $category = document.querySelector('.post_category_input')
const $save_btn = document.querySelector('.post_save');
const $img_div = document.querySelector('.thumbnail_preview')
const $thumbnail_btn = document.querySelector('.post_thumbnail_input');

const csrf_token = getCookie('csrftoken');

let link =  document.location.href;
let blog_idx = link.indexOf('edit');
link = link.substring(blog_idx+4)

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
            if (data.thumbnail) {
                $img_div.style.height = '30rem'
                let img = $img_div.querySelector("img");
                img.setAttribute("src", data.thumbnail);
            }
        },
        error: function(e) {
            console.log(e)
        }
    });
}

let thumbnail ;
// 썸네일 이미지 저장
const thumbnailFunc = (event) =>{

    previewImage(event)

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

const previewImage = (event) => {
    let reader = new FileReader();

    $img_div.style.height = '30rem'
    reader.onload = function (event) {
        let img = $img_div.querySelector("img");
        img.setAttribute("src", event.target.result);
    };
    reader.readAsDataURL(event.target.files[0]);
};

// Post data들 불러오고 넣기
loadPostData()
$save_btn.addEventListener('click',postSave)
$thumbnail_btn.addEventListener('change',thumbnailFunc)