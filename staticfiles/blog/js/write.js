import { getCookie } from "./utils.js"

const $save_btn = document.querySelector('.post_save');
const $thumbnail_btn = document.querySelector('.post_thumbnail_input');
const csrf_token = getCookie('csrftoken');