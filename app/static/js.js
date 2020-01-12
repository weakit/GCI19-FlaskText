function open_link(tag) {
    var url = $(tag).children().children().html().slice(0, -4).replace(' ', '_');
    window.open(url);
    console.log(url);
}

$(document).ready(function () {
    bsCustomFileInput.init()
    if (Boolean($("#alert").length))
        setTimeout(function(){
            $("#alert").fadeOut(200);
            $("#alert").remove();
        }, 3000);
})
