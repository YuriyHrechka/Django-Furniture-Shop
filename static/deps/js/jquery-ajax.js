// Коли html документ готовий (промальований)
$(document).ready(function () {
    // беремо в змінну елемент розмітки з id jq-notification для сповіщень від ajax
    var successMessage = $("#jq-notification");

    // // Ловимо подію кліку по кнопці додати до кошика
    // $(document).on("click", ".add-to-cart", function (e) {
    //     // Блокуємо його базову дію
    //     e.preventDefault();

    //     // Беремо елемент лічильника в значку кошика і беремо звідти значення
    //     var goodsInCartCount = $("#goods-in-cart-count");
    //     var cartCount = parseInt(goodsInCartCount.text() || 0);

    //     // Отримуємо id товару з атрибута data-product-id
    //     var product_id = $(this).data("product-id");

    //     // З атрибута href беремо посилання на контролер django
    //     var add_to_cart_url = $(this).attr("href");

    //     // робимо post-запит через ajax без перезавантаження сторінки
    //     $.ajax({
    //         type: "POST",
    //         url: add_to_cart_url,
    //         data: {
    //             product_id: product_id,
    //             csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    //         },
    //         success: function (data) {
    //             // Повідомлення
    //             successMessage.html(data.message);
    //             successMessage.fadeIn(400);
    //             // Через 7 сек прибираємо повідомлення
    //             setTimeout(function () {
    //                 successMessage.fadeOut(400);
    //             }, 7000);

    //             // Збільшуємо кількість товарів у кошику (промальовка у шаблоні)
    //             cartCount++;
    //             goodsInCartCount.text(cartCount);

    //             // Змінюємо вміст кошика на відповідь від django (новий промальований фрагмент розмітки кошика)
    //             var cartItemsContainer = $("#cart-items-container");
    //             cartItemsContainer.html(data.cart_items_html);

    //         },

    //         error: function (data) {
    //             console.log("Помилка при додаванні товару до кошика");
    //         },
    //     });
    // });




    // // Ловимо подію кліку по кнопці видалити товар із кошика
    // $(document).on("click", ".remove-from-cart", function (e) {
    //     // Блокуємо його базову дію
    //     e.preventDefault();

    //     // Беремо елемент лічильника в значку кошика і беремо звідти значення
    //     var goodsInCartCount = $("#goods-in-cart-count");
    //     var cartCount = parseInt(goodsInCartCount.text() || 0);

    //     // Отримуємо id кошика з атрибута data-cart-id
    //     var cart_id = $(this).data("cart-id");
    //     // З атрибута href беремо посилання на контролер django
    //     var remove_from_cart = $(this).attr("href");

    //     // робимо post-запит через ajax без перезавантаження сторінки
    //     $.ajax({

    //         type: "POST",
    //         url: remove_from_cart,
    //         data: {
    //             cart_id: cart_id,
    //             csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    //         },
    //         success: function (data) {
    //             // Повідомлення
    //             successMessage.html(data.message);
    //             successMessage.fadeIn(400);
    //             // Через 7 сек прибираємо повідомлення
    //             setTimeout(function () {
    //                 successMessage.fadeOut(400);
    //             }, 7000);

    //             // Зменшуємо кількість товарів у кошику (промальовка)
    //             cartCount -= data.quantity_deleted;
    //             goodsInCartCount.text(cartCount);

    //             // Змінюємо вміст кошика на відповідь від django (новий промальований фрагмент розмітки кошика)
    //             var cartItemsContainer = $("#cart-items-container");
    //             cartItemsContainer.html(data.cart_items_html);

    //         },

    //         error: function (data) {
    //             console.log("Помилка при додаванні товару до кошика");
    //         },
    //     });
    // });




    // // Тепер + - кількості товару
    // // Обробник події для зменшення значення
    // $(document).on("click", ".decrement", function () {
    //     // Беремо посилання на контролер django з атрибута data-cart-change-url
    //     var url = $(this).data("cart-change-url");
    //     // Беремо id кошика з атрибута data-cart-id
    //     var cartID = $(this).data("cart-id");
    //     // Шукаємо найближчий input із кількістю
    //     var $input = $(this).closest('.input-group').find('.number');
    //     // Беремо значення кількості товару
    //     var currentValue = parseInt($input.val());
    //     // Якщо кількість більше одного, то лише тоді робимо -1
    //     if (currentValue > 1) {
    //         $input.val(currentValue - 1);
    //         // Запускаємо функцію визначену нижче
    //         // із аргументами (id кошика, нова кількість, кількість зменшилась або збільшилась, url)
    //         updateCart(cartID, currentValue - 1, -1, url);
    //     }
    // });

    // // Обробник події для збільшення значення
    // $(document).on("click", ".increment", function () {
    //     // Беремо посилання на контролер django з атрибута data-cart-change-url
    //     var url = $(this).data("cart-change-url");
    //     // Беремо id кошика з атрибута data-cart-id
    //     var cartID = $(this).data("cart-id");
    //     // Шукаємо найближчий input із кількістю
    //     var $input = $(this).closest('.input-group').find('.number');
    //     // Беремо значення кількості товару
    //     var currentValue = parseInt($input.val());

    //     $input.val(currentValue + 1);

    //     // Запускаємо функцію визначену нижче
    //     // із аргументами (id кошика, нова кількість, кількість зменшилась або збільшилась, url)
    //     updateCart(cartID, currentValue + 1, 1, url);
    // });

    // function updateCart(cartID, quantity, change, url) {
    //     $.ajax({
    //         type: "POST",
    //         url: url,
    //         data: {
    //             cart_id: cartID,
    //             quantity: quantity,
    //             csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    //         },

    //         success: function (data) {
    //              // Повідомлення
    //             successMessage.html(data.message);
    //             successMessage.fadeIn(400);
    //              // Через 7 сек прибираємо повідомлення
    //             setTimeout(function () {
    //                  successMessage.fadeOut(400);
    //             }, 7000);

    //             // Змінюємо кількість товарів у кошику
    //             var goodsInCartCount = $("#goods-in-cart-count");
    //             var cartCount = parseInt(goodsInCartCount.text() || 0);
    //             cartCount += change;
    //             goodsInCartCount.text(cartCount);

    //             // Змінюємо вміст кошика
    //             var cartItemsContainer = $("#cart-items-container");
    //             cartItemsContainer.html(data.cart_items_html);

    //         },
    //         error: function (data) {
    //             console.log("Помилка при додаванні товару до кошика");
    //         },
    //     });
    // }
});