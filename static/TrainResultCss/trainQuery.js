const root_box = document.getElementById("result-box");

async function fetching(){
    // const trainPro = await fetch("http://127.0.0.1:8000/api/train_query/SIRSA/HISAR%20JN").then(data => data.json());
    // const pricePro = await fetch('http://127.0.0.1:8000/api/quota_price/').then(data => data.json())
    let querSet = Promise.all([
        fetch(`http://127.0.0.1:8000/api/train_query/${root_box.getAttribute("data-train-to")}/${root_box.getAttribute("data-train-from")}`).then(data => data.json()),
        fetch('http://127.0.0.1:8000/api/quota_price/').then(data => data.json())
    ]).then(e => domManipulation(e[0],e[1])).then((e) => allSineHide())
}

let train = fetching()
function domManipulation(trainObj,price_list){
    
    let train;
    // console.log(price_list,trainObj)
    for(train in trainObj){
        if((trainObj[train][1].Distance - trainObj[train][0].Distance) > 0){

        root_box.innerHTML += `<div class="individual-set">
            <h3>${trainObj[train][0].Train_No}</h3>
            <div class="timing-box"><span>${trainObj[train][0].Arrival_time} </span>${trainObj[train][0].Station_Code}--- <span>${trainObj[train][1].Arrival_time} </span>${trainObj[train][1].Station_Code}</div>
            <div class="seat-type">
                <div class="seat-summary">
    <!--------------seat SL -------------------------------------------!>
                    <div id="tn-${trainObj[train][0].Train_No}-sl" class="seat">
                        <div class="js-shine-box shine-box"></div>
                        <div class="flex">
                            <div class="seat-name">Sl</div>
                            <div class="price">${price_list[0].Seat_SL*(trainObj[train][1].Distance - trainObj[train][0].Distance)/10}</div>
                        </div>
                        <div class="seat-available success">Available  <span>${trainObj[train][0].Seat_SL}</span> </div>
                    </div>


    <!--------------seat 1A -------------------------------------------!>
                    <div id="tn-${trainObj[train][0].Train_No}-1a" class="seat">
                        <div class="js-shine-box shine-box"></div>
                        <div class="flex">
                            <div class="seat-name">1A</div>
                            <div class="price">${price_list[0].Seat_1A*(trainObj[train][1].Distance - trainObj[train][0].Distance)/10}</div>
                        </div>
                        <div class="seat-available success">Available <span>${trainObj[train][0].Seat_1A}</span> </div>
                    </div>



    <!--------------seat 2A -------------------------------------------!>
                    <div id="tn-${trainObj[train][0].Train_No}-2a" class="seat">
                        <div class="js-shine-box shine-box"></div>
                        <div class="flex">
                            <div class="seat-name">2A</div>
                            <div class="price">${price_list[0].Seat_2A*(trainObj[train][1].Distance - trainObj[train][0].Distance)/10}</div>
                        </div>
                        <div class="seat-available success">Available <span>${trainObj[train][0].Seat_2A}</span> </div>
                    </div>



    <!--------------seat 3A -------------------------------------------!>
                    <div id="tn-${trainObj[train][0].Train_No}-3a" class="seat">
                        <div class="js-shine-box shine-box"></div>
                        <div class="flex">
                            <div class="seat-name">3A</div>
                            <div class="price">${price_list[0].Seat_3A*(trainObj[train][1].Distance - trainObj[train][0].Distance)/10}</div>
                        </div>
                        <div class="seat-available fail">Not Available <span>${trainObj[train][0].Seat_3A}</span> </div>
                    </div>
                </div>
                </div>
                <div id="detail-${trainObj[train][0].Train_No}-sl" class="list-seat-type hidden">
                <div id="menu-SL" class="seat-detail">
                    <ul>
                        <li><span class="date"></span><span class="detail-seat">Tue</span><span
                                class="detail-price"><a href="">Book
                                    245</a></span></li>
                    </ul>
                </div>
            </div>`
        // console.log(trainObj)
    }}
      return trainObj;
}


function allSineHide(){
    const summerySeat = document.querySelectorAll(".seat-summary .seat");
// const seat_type = document.querySelectorAll(".list-seat-type");
const all_shine_box = document.querySelectorAll(".js-shine-box");
// const name = '#1234455-sl .js-shine-box'
// let shine = document.querySelector(`#${name} .js-shine-box`);

for (let i = 0; i < summerySeat.length; i++) {
  summerySeat[i].addEventListener("click", clickEvent);
  all_shine_box[i].classList.remove("shine-box");
  console.table(all_shine_box[i])
}
}




























// const train = await fetch("http://127.0.0.1:8000/api/train_query/SIRSA/HISAR%20JN").then(
//     e => e.json() ).then( e => domManipulation(e))

    // for (i = 0; i < 10; i++) {
    //     console.log(train_json[i]);
    // }
// return train_json;
// console.log(train_json);
// return trainObj
async function trainQuery(){
const price_list_promise = await fetch('http://127.0.0.1:8000/api/quota_price/')
const price_list_json = await price_list_promise.json()
const train = await fetch("http://127.0.0.1:8000/api/train_query/SIRSA/HISAR%20JN")
const trainObj = await train.json()
domManipulation(trainObj,price_list_json)
return trainObj
}

async function quotaPrice(){
    
    return price_list_json
}

function htmlTags(querySet){
    // console.log(querySet)
}





// let value = trainQuery()
// console.log(value)
// domManipulation()