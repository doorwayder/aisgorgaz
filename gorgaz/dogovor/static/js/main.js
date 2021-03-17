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


function pay_type_change() {
    if (document.getElementById("id_pay_type").checked) $("#pay_type_label").text("Наличные");
    else $("#pay_type_label").text("Безнал");
}

function delete_payment(payment_id) {
    if (confirm('Вы действительно хотите удалить платеж?')) {
        document.location.href = `/delpay/${payment_id}`;
    }
}