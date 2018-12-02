(function () {
    function toJSONString(form) {
        var objekatTim = {};
        var prviClan = {};
        var drugiClan = {};
        var treciClan = {};
        var cetvrtiClan = {};
        var nizClanova = [];

        var informOTimu = $(".opsteInformacije, :input").not(".cetvrtiClan")
        var clanoviTima = $(".clanTima, :input").not(".cetvrtiClan")
        

        for (var i = 0; i < informOTimu.length; ++i) {
            var element = informOTimu[i];
            var kljucTim = element.name;
            var vrednostTima = element.value;

            if (vrednostTima == "") {
                throw("Sve vrednosti moraju biti popunjene")
            }

            if (kljucTim == "name" || kljucTim == "description" || kljucTim == "photo_url") {
                objekatTim[kljucTim] = vrednostTima;
            }

        }

        for (var y = 0; y < clanoviTima.length; ++y) {
            var clan = clanoviTima[y];
            var kljucClan = clan.name;
            var vrednostClan = clan.value;
            var clanId = clan.id;

             if (vrednostClan == "") {
                throw("Sve vrednosti moraju biti popunjene")
             }

            console.log(clanoviTima[0]);

            if (clanId == "first_name1" || clanId == "last_name1" || clanId == "email1" || clanId == "phone_number1" || clanId == "school1" || clanId == "city1") {
                prviClan[kljucClan] = vrednostClan;
                nizClanova[0] = prviClan;
            }

            if (clanId == "first_name2" || clanId == "last_name2" || clanId == "email2" || clanId == "phone_number2" || clanId == "school2" || clanId == "city2") {
                drugiClan[kljucClan] = vrednostClan;
                nizClanova[1] = drugiClan;
            }

            if (clanId == "first_name3" || clanId == "last_name3" || clanId == "email3" || clanId == "phone_number3" || clanId == "school3" || clanId == "city3") {
                treciClan[kljucClan] = vrednostClan;
                nizClanova[2] = treciClan;
            }

            nizClanova[0] = prviClan;
            nizClanova[1] = drugiClan;
            nizClanova[2] = treciClan;

            

        }
        
        var selClan4 = $("input.cetvrtiClan")
        var clan4one = false
        var clan4all = true
        for (var i = 0; i < selClan4.length; i++) {
            if (selClan4[i].value != "") {
                clan4one = true
            }
            if (selClan4[i].value == "") {
                clan4all = false
            }
        }

        if (clan4one == true && clan4all == false) {
            throw("Cetvrti clan mora biti ili ceo popunjen, ili ceo prazan!")
        }

        if (clan4all == true) {

            for (var i = 0; i < selClan4.length; i++) {
                cetvrtiClan[selClan4[i].name] = selClan4[i].value
            }

            nizClanova[3] = cetvrtiClan
        }

        objekatTim["team_members"] = nizClanova;
        return JSON.stringify(objekatTim);
    }

    document.addEventListener("DOMContentLoaded", function () {
        var form = document.getElementById("forma");
        var output = document.getElementById("output");

        // $(".cetvrtiClan").css("display", "none")

        form.addEventListener("submit", function (e) {
            e.preventDefault();
            try {
            var json = toJSONString(this);
            output.innerHTML = json;

            posaljiNaServer(json);

            odvediNaListuTimova();
            } 
            catch (err){
                alert(err)
            }

        }, false);

    });

})();

function odvediNaListuTimova() {
    var dugmeZaListuTimova = document.getElementById('listaTimova');
    dugmeZaListuTimova.style.visibility = 'visible';
    //dugmeZaListuTimova.addEventListener("click", window.open('https://hzsradionice.github.io/prviTest/probniHttp/index.html', '_blank'));
}

function posaljiNaServer(json) {
    var req = new XMLHttpRequest();
    var base = "http://localhost:5000/teams/"
    req.open('POST', base, true)
    req.setRequestHeader('Content-Type', 'application/json')

    req.onload = function (e) {
        if (req.readyState === 4) {
            if (req.status === 201) {
                console.log(req.responseText);
                alert('Tim prijavljen!')
            }
            if (req.status === 400) {
                 alert()
            } else {
                console.error(req.statusText);
            }
        }
    };

    req.send(json)
    
    
    var tim = req.response;
    var nazivTima = tim['name'];
    var uuidTima = tim['team_uuid'];
    
    window.localStorage.setItem(nazivTima, uuidTima);
    

}









/*
let req = new XMLHttpRequest();
const base = "http://142.93.173.116:5000/teams/"
req.open('POST', base, true)
req.setRequestHeader('Content-Type', 'application/json')

req.onload = function (e) {
    if (req.readyState === 4) {
        if (req.status === 201) {
            console.log(req.responseText);
        } else {
            console.error(req.statusText);
        }
    }
};

req.send(JSON.stringify({
    "description": "ALOOO 😞",
    "id": 1,
    "name": "NOVI",
    "photo_url": "NOVINOVINOVI DRUGI damo",
    "team_members": [
        {
            "city": "Bitni grad",
            "email": "NOVI",
            "first_name": "jMarkosss",
            "id": 1,
            "last_name": "NOVINOVINOVI",
            "phone_number": "+381293813",
            "school": "Gimn mldsss",
            "team_id": 1
        },
        {
            "city": "Bg sss",
            "email": "teammember@dqoweoq.rs",
            "first_name": "21k312 DRUGI",
            "id": 2,
            "last_name": "Member",
            "phone_number": "+139138333",
            "school": "Teh schsss",
            "team_id": 1
        }
    ],
    "team_uuid": "ae98b051-be1f-472a-af17-798bb28a11d6"
}))
*/