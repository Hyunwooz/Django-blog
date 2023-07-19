const $old_pw_input = document.querySelector('#id_old_password')
const $new_pw_input = document.querySelector('#id_new_password1')
const $new_pw_input2 = document.querySelector('#id_new_password2')
const uls = document.querySelectorAll('ul')

$old_pw_input.placeholder = 'Old Password'
$new_pw_input.placeholder = 'New Password'
$new_pw_input2.placeholder = 'Check New Password'

// uls.forEach(element => {
//     if (element.className != 'errorlist'){
//         element.remove()
//     }
// });
