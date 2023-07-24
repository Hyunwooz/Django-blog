const $profile_avatar = document.querySelector("#profile-avatar");
const $profile_form = document.querySelector('.user-profile-form')

const previewImage = (event) => {
    let reader = new FileReader();

    reader.onload = function (event) {
        let img = $profile_form.querySelector("img");
        img.setAttribute("src", event.target.result);
    };
    reader.readAsDataURL(event.target.files[0]);
};

$profile_avatar.addEventListener("change", previewImage);
