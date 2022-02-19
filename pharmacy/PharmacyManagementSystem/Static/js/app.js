$(document).ready(function(){
    $('#id_itemOne_Quantity, #id_itemOne_Unit_Price, #id_itemTwo_Quantity, #id_itemTwo_Unit_Price, #id_itemThree_Quantity, #id_itemThree_Unit_Price, #id_itemFour_Quantity, #id_itemFour_Unit_Price, #id_itemFive_Quantity, #id_itemfive_Unit_Price').keyup(function(){
        var itemOne_Quantity_Text = $('#id_itemOne_Quantity').val();
        var itemOne_Unit_Price_Text = $('#id_itemOne_Unit_Price').val();
        var itemOne_total_Price = itemOne_Quantity_Text * itemOne_Unit_Price_Text

        var itemTwo_Quantity_Text = $('#id_itemTwo_Quantity').val();
        var itemTwo_Unit_Price_Text = $('#id_itemTwo_Unit_Price').val();
        var itemTwo_total_Price = itemTwo_Quantity_Text * itemTwo_Unit_Price_Text

        var itemThree_Quantity_Text = $('#id_itemThree_Quantity').val();
        var itemThree_Unit_Price_Text = $('#id_itemThree_Unit_Price').val();
        var itemThree_total_Price = itemThree_Quantity_Text * itemThree_Unit_Price_Text

        var itemFour_Quantity_Text = $('#id_itemFour_Quantity').val();
        var itemFour_Unit_Price_Text = $('#id_itemFour_Unit_Price').val();
        var itemFour_total_Price = itemFour_Quantity_Text * itemFour_Unit_Price_Text

        var itemFive_Quantity_Text = $('#id_itemFive_Quantity').val();
        var itemFive_Unit_Price_Text = $('#id_itemFive_Unit_Price').val();
        var itemFive_total_Price = itemFive_Quantity_Text * itemFive_Unit_Price_Text

        var total = itemOne_total_Price + itemTwo_total_Price + itemThree_total_Price + itemFive_total_Price +itemFive_total_Price

        $('#id_itemOne_total_price').val(itemOne_total_Price);
        $('#id_itemTwo_total_price').val(itemTwo_total_Price);
        $('#id_itemThree_total_price').val(itemThree_total_Price);
        $('#id_itemFour_total_price').val(itemFour_total_Price);
        $('#id_itemFive_total_price').val(itemFive_total_Price);
        $('#id_total').val(total);
    });

});