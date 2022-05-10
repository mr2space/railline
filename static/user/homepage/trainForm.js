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


const stationSearch = async (text,e) =>{
        if(text.length<3){
            
            return []
        }
    const stationName = await fetch(`https://indianrailways.p.rapidapi.com/findstations.php?station=${text}`, {
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "indianrailways.p.rapidapi.com",
		"x-rapidapi-key": "cf23647522mshd5acd9e46e038c6p10558bjsn5820f55667fb"
	}
})
    const state = await stationName.json();
    console.log(state)
    try{
    const html = state.stations.slice(0,7).map(
        match =>
            `<li onclick="listClickEvent(this,'${e}')" data-parent-id='${e}' data-code='${match.stationCode}' >${match.stationName} (${match.stationCode} )</li>`
    ).join('')
    boxUpdate(html,e);
    console.log(html)
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
