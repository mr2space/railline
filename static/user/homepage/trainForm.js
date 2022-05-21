        const search = document.getElementById("origin-input")
        const destination_input = document.getElementById("destination-input")
        const box = document.querySelectorAll(".suggestions");


function boxUpdate(html,id=null){
    if(id == null){
        for(i=0;i<box.length;i++){
            box[i].innerHTML = html
        }
        return []
    }
    let selected_box = document.getElementById(`${id}-suggestion`)
    selected_box.innerHTML = html;
}

async function codeQuerry(){
    let status = await fetch(`http://127.0.0.1:8000/api/station_code`);
    stationCodeJson = await status.json();
}

codeQuerry()
const stationSearch = async (text,e) =>{
    if(text.length<2){
            return []
        }
    let matches = stationCodeJson.filter(ele =>{
        let regex = new RegExp(`^${text}`,'gi');
        return ele.Station_Name.match(regex) || ele.Station_Code.match(regex)
    })
    try{
    const html = matches.slice(0,7).map(
        match =>
            `<li onclick="listClickEvent(this,'${e}')" data-parent-id='${e}' data-code='${match.Station_Code}' >${match.Station_Name} (${match.Station_Code} )</li>`
    ).join('')
    boxUpdate(html,e);
     }
     catch{
        console.log("error in data")
 }
}

search.addEventListener("input",()=> stationSearch(search.value,search.id));
destination_input.addEventListener("input", () => stationSearch(destination_input.value, destination_input.id));
boxUpdate('')

function listClickEvent(e,element_id){
    nam = this.name;
    console.log(e.getAttribute('data-code'));
    document.getElementById(element_id).value = e.getAttribute('data-code')
    boxUpdate('')
}
