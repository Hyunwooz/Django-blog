export const getCookie = function(name){
    const value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return value? value[2] : null;
}

// 썸네일 이미지 저장
// export const thumbnailSave = (thumbnail,csrf_token) =>{
//     const formData = new FormData();
//     formData.append('image', thumnnail);
    
//     $.ajax({
//         type: 'POST',
//         enctype: 'multipart/form-data',
//         url: '/blog/imageupload/',
//         data: formData,
//         dataType: 'json',
//         processData: false,
//         contentType: false,
//         cache: false,
//         timeout: 600000,
//         beforeSend : function(xhr){
//             xhr.setRequestHeader("X-CSRFToken",csrf_token);
//         },
//         success: function(data) {
//             // console.log('Result: 성공')
//             let thumbnailUrl = data.url
//             return thumbnailUrl
//         },
//         error: function(e) {
//             // console.log(e)
//             return e.toString()
//         }
//     });
// }