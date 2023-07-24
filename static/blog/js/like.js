import { getCookie } from "./utils.js"

const $post_like_btn = document.querySelectorAll('.post_like_btn')
const csrf_token = getCookie('csrftoken');

const likeFunc = (event) => {
    event.preventDefault()
    let btn = event.target

    if (btn.tagName == 'I') {
        btn = btn.parentNode
    }

    const icon = btn.querySelector('i')
    const pk = btn.id

    $.ajax({
        type: 'POST',
        url: 'like/'+pk+'/',
        dataType: 'json',
        timeout: 600000,
        beforeSend : function(xhr){
            xhr.setRequestHeader("X-CSRFToken",csrf_token);
        },
        success: function(data) {
            let message = data.message
            if (icon.classList.value == "fa-regular fa-heart"){
                icon.classList = "fa-solid fa-heart"
            } else {
                icon.classList = "fa-regular fa-heart"
            }
        },
        error: function(e) {
            console.log(e)
        }
    });
}


$post_like_btn.forEach(element => {
    element.addEventListener('click',likeFunc)
});