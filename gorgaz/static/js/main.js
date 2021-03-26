"use strict";

$(document).ready(function () {
    let dogovor = document.querySelectorAll(".dogtr");
    Array.from(dogovor).forEach(function (tr_dogovor) {
        tr_dogovor.addEventListener('click', function (e) {
            e.preventDefault();
            let dog_id = e.target.getAttribute("data-id");
            document.location.href = `/dogovor/${dog_id}`;
        });
    });

    $("#id_filter").on("keyup", function() {
        let value = $(this).val().toLowerCase();
        $("#cities option").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        });

    $( "#id_address_city" ).autocomplete( {
            source: "/city-autocomplete/",
            delay: 100,
        });

    $( "#id_address_street" ).autocomplete( {
            source: "/street-autocomplete/",
            delay: 100,
        });
});


function fiz_change() {
    if (document.getElementById("id_fiz").checked) $("#fiz_label").text("Физлицо");
    else $("#fiz_label").text("Юрлицо");
}

function active_change() {
    if (document.getElementById("id_active").checked) $("#active_label").text("Действующий");
    else $("#active_label").text("Расторгнут");
}

//function get_cities() {
//    let url = '/city-autocomplete/?q=' + $("#id_address_city").val().toLowerCase();
//    fetch(url).then(function(response) {
//        response.json().then(function(data) {
//            console.log('data', data)
//            return data;
//        });
//    });
//}
//
//function get_streets() {
//    let url = '/street-autocomplete/?q=' + $("#id_address_street").val().toLowerCase();
//    fetch(url).then(function(response) {
//        response.json().then(function(data) {
//            return data;
//        });
//    });
//}
