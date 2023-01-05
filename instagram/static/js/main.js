

$(document).on("scroll", function () {
if ($(document).scrollTop() > 50) {
        $(".navigation").addClass("shrink");
    } else {
        $(".navigation").removeClass("shrink");
    }
    });

$('#post-submit').submit(function(event){
    event.preventDefault();
    event.stopImmediatePropagation();
    formData = new FormData(this);
    $.ajax({
        url: $('#post-submit').attr('action'),
        enctype: 'multipart/form-data',
        method: "POST",
        processData: false,
        contentType: false,
        data: formData,
        success: function(data){
            console.log(data);
            console.log(data.status);
            alert('Пост опубликован');
        },
        error: function(data){
            console.log(data.responseJson),
            alert('ошибка')}
        })
    return false
    })

let getPost = function(post){
    $.ajax({
        url : `http://127.0.0.1:8000/api/posts/${post.pk}`,
        method: "GET",
        success: function(data){
            console.log(data)
        },
        error: function(data){
            console.log(data)
        }
    })
}