let form_section = [
    '#train-detail',
    '#train-detail-2',
    '#personal-detail',
]



function allBackBtnFun(e){
    pos_number = e.getAttribute("data-pos");
    index_number = pos_number - 1;
    console.log(index_number - 1, form_section[index_number -1])
    document.querySelector(form_section[index_number]).style.left = "50%";
    document.querySelector(form_section[index_number-1]).style.left = "0%";
}
function allNextBtnFun(e){
    pos_number = e.getAttribute("data-pos");
    index_number = pos_number - 1;
    // console.log(index_number + 1, form_section[index_number + 1])
    document.querySelector(form_section[index_number]).style.left = "-50%";
    document.querySelector(form_section[index_number +1]).style.left = "0%";
}

function sumbitTheForm(){
    document.querySelector("#form-csrf").submit();
}