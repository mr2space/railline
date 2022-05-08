const root_box = document.getElementById("result-box");
const root = ReactDOM.createRoot(root_box);


async function trainQuery(){
const train = await fetch("http://127.0.0.1:8000/api/train_no/1705/").then(
    e => e.json() ).then( e => domManipulation(e))

    // for (i = 0; i < 10; i++) {
    //     console.log(train_json[i]);
    // }
// return train_json;
// console.log(train_json);
}

function domManipulation(train){
    let i = 0
    let html = <div></div>
    for(i = 0;i<10;i++){
        html += <div 
    }
}
trainQuery()
// domManipulation()