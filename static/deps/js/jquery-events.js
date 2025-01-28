// Коли HTML-документ готовий (відмальований)
$(document).ready(function () {
    // Беремо з розмітки елемент за id - сповіщення від django
    var notification = $('#notification');
    // І через 7 сек. прибираємо
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // При кліці на значок кошика відкриваємо спливаюче (модальне) вікно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Подія кліку на кнопку закриття вікна кошика
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обробник події радіокнопки вибору способу доставки
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Приховуємо або відображаємо input для введення адреси доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});