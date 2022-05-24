
var ticket_number_div = document.getElementById("ticket_no");
var cal_price_div = document.getElementById("price")
var seat_price = document.getElementById("seat-price").value
ticket_number_div.addEventListener("input",(e) =>{
    if (ticket_number_div.value < 0) ticket_number_div.value = 0;
    value_ticket=ticket_number_div.value;
    cal_price_div.value = value_ticket*seat_price;
})