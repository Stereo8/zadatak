document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);

    var desc = document.getElementById("description")
    var name = document.getElementById("name")
    var photo = document.getElementById("photo_url")

    desc.value = urlParams.get('opis')
    name.value = urlParams.get('ime')
    photo.value = urlParams.get('link')
    $("#submit2").click(function(button) {

        var uuid = urlParams.get('uuid')
    

        var req = new XMLHttpRequest();
        var url = "http://localhost:5000/teams/" + uuid;
    
        var body = {
            "name" : name.value,
            "description": desc.value,
            "photo_url": photo.value
        }
    
        req.open('PUT', url, true)
        req.setRequestHeader('Content-Type', 'application/json')
    
        req.onload = function (e) {
            if (req.readyState === 4) {
                if (req.status === 200) {
                    console.log(req.responseText);
                    alert("Tim izmenjen!")
                }
                if (req.status === 404) {
                     alert("Tim nije pronadjen")
                } else {
                    console.error(req.statusText);
                }
            }
        };
    
    
        req.send(JSON.stringify(body))
        
    
    });
}); 



