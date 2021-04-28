"use strict";

$(document).ready(function () {
    let dogovor = document.querySelectorAll(".dogtr");
    let order = document.querySelectorAll(".ordertd");
    Array.from(dogovor).forEach(function (tr_dogovor) {
        tr_dogovor.addEventListener('click', function (e) {
            e.preventDefault();
            let dog_id = e.target.getAttribute("data-id");
            document.location.href = `/dogovor/${dog_id}`;
            });
        });


    Array.from(order).forEach(function (tr_order) {
        tr_order.addEventListener('click', function (e) {
            e.preventDefault();
            let ord_id = e.target.getAttribute("data-id");
            document.location.href = `/order/${ord_id}`;
        });
    });

    $("#id_filter").on("keyup", function() {
        let value = $(this).val().toLowerCase();
        $("#cities option").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
            console.log('data', data)
        });

    $( "#id_address_city" ).autocomplete( {
            source: "/city-autocomplete/",
            delay: 100,
        });

    $( "#id_address_street" ).autocomplete( {
            source: "/street-autocomplete/",
            delay: 100,
        });

    $( "#id_search_name" ).autocomplete( {
            source: "/name-autocomplete/",
            delay: 100,
            minLength: 3,
        });

    let contextMenu = $('.context-menu-open');

    $('.context-menu').on('contextmenu', function (e) {
        e.preventDefault();
        contextMenu.css({top: e.clientY + 'px', left: e.clientX + 'px' });
        let notify_id = e.target.getAttribute("data-id");
        let notify_send = e.target.getAttribute("data-send");
        let ok = document.getElementById("menuOk")
        let err = document.getElementById("menuErr")
        ok.setAttribute('data-id', notify_id);
        err.setAttribute('data-id', notify_id);
        ok.setAttribute('data-send', notify_send);
        err.setAttribute('data-send', notify_send);
        contextMenu.show();
        });

    $(document).on('click', function () {
        contextMenu.hide();
        });
});

function fiz_change() {
    if (document.getElementById("id_fiz").checked) $("#fiz_label").text("Физлицо");
    else $("#fiz_label").text("Юрлицо");
}

function active_change() {
    if (document.getElementById("id_active").checked) {
        $("#active_label").text("Действующий");
        $("#id_terminate_div").toggleClass("invisible");
    }
    else {
        $("#active_label").text("Расторгнут");
        $("#id_terminate_div").toggleClass("invisible");
        let today = new Date().toISOString().substr(0, 10);
        $("#id_terminate_date").val(today);
    }
}


function pay_type_change() {
    if (document.getElementById("id_pay_type").checked) $("#pay_type_label").text("Наличные");
    else $("#pay_type_label").text("Безнал");
}


function completed_change() {
    if (document.getElementById("id_completed").checked) $("#completed_label").text("Выполнен");
    else $("#completed_label").text("Не выполнен");
}


function delete_payment(payment_id) {
    if (confirm('Вы действительно хотите удалить платеж?')) {
        document.location.href = `/delpay/${payment_id}`;
    }
}

function notifyOk() {
    let data_id = document.getElementById("menuOk").getAttribute("data-id");
    let data_send = document.getElementById("menuOk").getAttribute("data-send");
    if (data_send == 1) {
        document.location.href = `/updatenotify1?n=${data_id}&action=1`;
    }
    if (data_send == 2) {
        document.location.href = `/updatenotify2?n=${data_id}&action=1`;
    }
}

function notifyErr() {
    let data_id = document.getElementById("menuErr").getAttribute("data-id");
    let data_send = document.getElementById("menuErr").getAttribute("data-send");
    if (data_send == 1) {
        document.location.href = `/updatenotify1?n=${data_id}&action=0`;
    }
    if (data_send == 2) {
        document.location.href = `/updatenotify2?n=${data_id}&action=0`;
    }
}

function notifyDel() {
    let data_id = document.getElementById("menuErr").getAttribute("data-id");
    let data_send = document.getElementById("menuErr").getAttribute("data-send");
    if (data_send == 1) {
        document.location.href = `/updatenotify1?n=${data_id}&action=2`;
    }
    if (data_send == 2) {
        document.location.href = `/updatenotify2?n=${data_id}&action=2`;
    }
}

function orderDel(order) {
    if (confirm('Удалить наряд № ' + order + "?")) {
        document.location.href = `/delorder/${order}`;
    }
}

function orderPrint(order) {
    window.open(`/printorder/${order}`,'_blank')
}

function onDiscount() {
    let sum = document.getElementById("id_sum").value;
    $('#id_discount').val(Math.ceil(sum*0.2));
    $('#id_amount').val(sum-Math.ceil(sum*0.2));
}

function delRow() {
    alert('...');
}