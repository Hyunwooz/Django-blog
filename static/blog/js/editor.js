const Editor = toastui.Editor;

const editor = new Editor({
    el: document.querySelector('#editor'),
    height: '600px',
    initialEditType: 'markdown',
    previewStyle: 'vertical',
    hooks: {
        addImageBlobHook: (blob, callback) => {
            // blob : Java Script 파일 객체
            //console.log(blob);

            // 쿠키로드
            const getCookie = function(name){
                const value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
                return value? value[2] : null;
            }

            const csrf_token = getCookie('csrftoken');

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

            // const imgUpload = async () => {
            //     const result = await fetch("/blog/imageupload/", {
            //         method: "POST",
            //         headers: {
            //             'X-CSRFToken' : csrf_token
            //         },
            //         body: formData,
            //         redirect: "follow",
            //     })
            //     .then((res) => {
            //         url += data.filename;
            //         callback(url, '사진 대체 텍스트 입력');
            //     })
            //     .catch((err) => {
            //         callback('image_load_fail', '사진 대체 텍스트 입력');
            //     });
            // };

            
        }
    }
});