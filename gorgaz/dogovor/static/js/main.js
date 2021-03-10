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

    $( "#id_address_city" ).autocomplete( {
            source: [],
        });

    $( "#id_address_street" ).autocomplete( {
            source: [],
        });

    $("#id_filter").on("keyup", function() {
        let value = $(this).val().toLowerCase();
        $("#cities option").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        });

    $("#id_address_city").on("keyup", function() {
        let value = $(this).val().toLowerCase();
        get_cities(value);
        });

    $("#id_address_street").on("keyup", function() {
        let value = $(this).val().toLowerCase();
        get_streets(value);
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

function get_cities(str) {
    let url = '/city-autocomplete/?q=' + str
    console.log('url', url)
    fetch(url).then(function(response) {
        response.json().then(function(data) {
            $( "#id_address_city" ).autocomplete( {
            source: data,
            });
        });
    });
}

function get_streets(str) {
    let url = '/street-autocomplete/?q=' + str
    fetch(url).then(function(response) {
        response.json().then(function(data) {
            $( "#id_address_street" ).autocomplete( {
            source: data,
            });
        });
    });
}

