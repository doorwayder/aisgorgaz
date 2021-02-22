"use strict";


$(document).ready(function () {
    let dogovor = document.querySelectorAll(".dogtr");
    Array.from(dogovor).forEach(function (tr_dogovor) {
        tr_dogovor.addEventListener('dblclick', function (e) {
            e.preventDefault();
            let dog_id = e.target.getAttribute("data-id");
            document.location.href = `dogovor/${dog_id}`;
        });
    });
});