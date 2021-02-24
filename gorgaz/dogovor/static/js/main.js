"use strict";


$(document).ready(function () {
    let dogovor = document.querySelectorAll(".dogtr");
    Array.from(dogovor).forEach(function (tr_dogovor) {
        tr_dogovor.addEventListener('click', function (e) {
            e.preventDefault();
            let dog_id = e.target.getAttribute("data-id");
            document.location.href = `dogovor/${dog_id}`;
        });
    });
});

function fiz_change() {
    if (document.getElementById("id_fiz").checked) $("#fiz_label").text("Физлицо");
    else $("#fiz_label").text("Юрлицо");
}