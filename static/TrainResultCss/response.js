const summerySeat = document.querySelectorAll(".seat-summary .seat");
const seat_type = document.querySelectorAll(".list-seat-type");
const all_shine_box = document.querySelectorAll(".js-shine-box");



function clickEvent() {
  let name = this.id;
  name = name.substring(3);
  // console.log(name, `detail-${name} .js-shine-box`);
  let detail = document.getElementById(`detail-${name}`);
  let shine = document.querySelector(`#tn-${name} .js-shine-box`);
  let status = detail.classList.contains("hidden")
  for (let i = 0; i < seat_type.length; i++) {
   seat_type[i].classList.add("hidden");
   all_shine_box[i].classList.remove("shine-box");
  }
  if (status) {
    detail.classList.remove("hidden");
    shine.classList.add("shine-box");
  } else {
    detail.classList.add(".hide-menu");
    shine.classList.remove("shine-box");
  }
}