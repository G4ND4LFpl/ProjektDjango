function onload()
{
    var parts = window.location.search.substr(1).split("&");
    var $_GET = {};
    for (var i = 0; i < parts.length; i++) 
    {
        var temp = parts[i].split("=");

        if (temp[0] != "") $_GET[decodeURIComponent(temp[0])] = decodeURIComponent(temp[1]);
        else $_GET["selector"] = "pl";
    }

    let selector = document.getElementById("lang_selector");
    selector.value = $_GET["selector"];
    selector.style = "display: inline-block;"
}
function changeLang()
{
    var from = document.getElementById("lang_form");
    from.submit();
}
function openimg(img_info)
{
    if (screen.width >= 576)
    {
        let window = document.getElementById("window");
        window.style = "display: block;";
    
        let image_name = document.getElementById("image_name");
        image_name.innerHTML = img_info.title;
    
        let image = document.getElementById("imagefull");
        image.src = img_info.src.replace("_min","");
        image.alt = img_info.alt;
    }
}
function closeimg()
{
    document.getElementById("window").style = "display: none;";
}
