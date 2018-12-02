document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);

    mid = urlParams.get("id")
    fname = urlParams.get("fname")
    lname = urlParams.get("lname")
    email = urlParams.get("email")
    broj = urlParams.get("broj")
    skola = urlParams.get("skola")
    mesto = urlParams.get("mesto")

    var fnameb = document.getElementById("first_name")
    var lnameb = document.getElementById("last_name")
    var emailb = document.getElementById("email")
    var phoneb = document.getElementById("phone_number")
    var cityb = document.getElementById("city")
    var skolab = document.getElementById("school")

    fnameb.value = fname
    lnameb.value = lname
    emailb.value = email
    phoneb.value = broj
    cityb.value = mesto
    skolab.value = skola

    $("#submit").click(function() {
        var req = new XMLHttpRequest();
        var url = "http://localhost:5000/members/" + mid

        var body = {
            "first_name": fnameb.value,
            "last_name": lnameb.value,
            "email": emailb.value,
            "phone_number": phoneb.value,
            "school": skolab.value,
            "city": cityb.value
        }

        req.open('PUT', url, true)
        req.setRequestHeader('Content-Type', 'application/json')
        req.onload = function (e) {
            if (req.readyState === 4) {
                if (req.status === 200) {
                    console.log(req.responseText);
                    alert("Clan izmenjen!")
                }
                if (req.status === 404) {
                     alert("Clan nije pronadjen")
                } else {
                    console.error(req.statusText);
                }
            }
        };

        req.send(JSON.stringify(body));
    })

})