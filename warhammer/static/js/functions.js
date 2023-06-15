function onload()
{
    var parts = window.location.search.substr(1).split("&");
    var $_GET = {};
    for (var i = 0; i < parts.length; i++) 
    {
        var temp = parts[i].split("=");
        $_GET[decodeURIComponent(temp[0])] = decodeURIComponent(temp[1]);
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
