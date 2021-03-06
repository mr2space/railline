const root_box = document.getElementById("result-box");
async function fetching() {
    let querSet = Promise.all([
        fetch(`http://127.0.0.1:8000/api/train_query/${root_box.getAttribute("data-train-to")}/${root_box.getAttribute("data-train-from")}`).then(data => data.json()),
        fetch('http://127.0.0.1:8000/api/quota_price/').then(data => data.json())
    ]).then(e => domManipulation(e[0], e[1])).then((e) => allSineHide());
};

function divSeatBLackBox(trainObj, price_list, seat_type) {
    inner_HTML_text = '';
        if ((trainObj[1].Distance - trainObj[0].Distance) <= 0) return '';
        inner_HTML_text += `
                <div id="tn-${trainObj[0].Train_No}-${seat_type}" class="seat">
                    <div class="js-shine-box shine-box"></div>
                    <div class="flex">
                        <div class="seat-name">${seat_type.substring(5,7)}</div>
                        <div class="price">${parseFloat(price_list[0][seat_type] * (trainObj[1].Distance - trainObj[0].Distance)).toFixed(2) }</div>
                    </div>
                    <div class="${seatSuccesFail(trainObj[0][seat_type])}">Available <span>${trainObj[0][seat_type]}</span></div>
                </div>`
    return inner_HTML_text;
}
function seatSuccesFail(number){
    if (number > 0) return 'seat-available success';
    if (number <= 0) return 'seat-available fail';
}
function bookingDataDetail(trainObj, price_list, seat_type){
    date_obj = new Date(root_box.getAttribute('data-year'), root_box.getAttribute('data-month'), root_box.getAttribute('data-date'))
    let inner_HTML_text = `
    <div id = "detail-${trainObj[0].Train_No}-${seat_type}" class="list-seat-type hidden" >
        <div id="menu-SL" class="seat-detail">
            <ul>
                <li>
                
                <span class="date">${root_box.getAttribute("data-date")} ${root_box.getAttribute("data-train-month")} ${root_box.getAttribute("data-year")}</span><span class="detail-seat">${root_box.getAttribute("data-train-day")}</span><span
                    class="detail-price" data-form-link="form-${trainObj[0].Train_No}-${seat_type}" onclick="formSubmit(this)"><a href="JavaScript:void(0);">Book
                        ${trainObj[0][seat_type]} </a></span>
        <div class="hidden hidden-form">
        <form id="form-${trainObj[0].Train_No}-${seat_type}" action="/booking/" method="post">
                ${csrf_token}
            <input name="train-no" value="${trainObj[0].Train_No}" type="text">
            <input name="train-id" value="${trainObj[0].id}" type="text">
            <input name="destination" value="${trainObj[1].Station_Code}" type="text">
            <input name="boarding" value="${trainObj[0].Station_Code}" type="text">
            <input name="date" value="${date_obj.toISOString().substring(0, 10)}" type="date">
            <input name="seat_type" value="${seat_type}" type="text">
            <input name="price" value="${price_list[0][seat_type] * (trainObj[1].Distance - trainObj[0].Distance)}" type="text">

        </form>
        </div>
                                       
                    </li>
                </ul>
            </div>
            </div>
    `
    return inner_HTML_text;
}
function individualSetDiv(trainObj,price_list){
    const seat_set = [
        'Seat_SL', 'Seat_1A', 'Seat_2A', 'Seat_3A',
    ]
    let temp = iterationDivSeatBlackBox(seat_set, trainObj, price_list)
    let detail_temp = iterationBookingDataDetail(seat_set, trainObj, price_list)
    let inner_HTML_text =`<div class="individual-set" data-aos="fade-up">
        <h3>${trainObj[0].Train_No}</h3>
        <div class="timing-box"><span>${trainObj[0].Arrival_time} </span>${trainObj[0].Station_Code}--- <span>${trainObj[1].Arrival_time} </span>${trainObj[1].Station_Code}</div>
        <div class="seat-type">
            <div class="seat-summary">
            ${temp}
            </div>
            ${detail_temp}
            </div>
            `
    return inner_HTML_text;
}
function iterationDivSeatBlackBox(seat_set, trainObj, price_list){
    let seat_type;
    inner_HTML_text = ``
    for (seat_type in seat_set){
        inner_HTML_text += divSeatBLackBox(trainObj, price_list, seat_set[seat_type])
    
    }
    return inner_HTML_text;
}
function iterationBookingDataDetail(seat_set, trainObj, price_list){
    let seat_type;
    let inner_HTML_text = ``
    for (seat_type in seat_set) {
        inner_HTML_text += bookingDataDetail(trainObj, price_list, seat_set[seat_type])
    }
    return inner_HTML_text;
}
function domManipulation(trainObj, price_list) {
    let train;
    root_box.innerHTML = '';
    for (train in trainObj) {
        if ((trainObj[train][1].Distance - trainObj[train][0].Distance) <= 0) continue;
        root_box.innerHTML += individualSetDiv(trainObj[train], price_list)
    }
}

let train = fetching()


function allSineHide() {
    const summerySeat = document.querySelectorAll(".seat-summary .seat");
    const all_shine_box = document.querySelectorAll(".js-shine-box");
    for (let i = 0; i < summerySeat.length; i++) {
        summerySeat[i].addEventListener("click", clickEvent);
        all_shine_box[i].classList.remove("shine-box");
        // console.table(all_shine_box[i])
    }
}
function formSubmit(e){
    form_id = e.getAttribute("data-form-link")
    form_DOM = document.querySelector(`#${form_id}`);
    form_DOM.submit();
}