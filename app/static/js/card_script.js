const link = document.querySelector("#card")
const url = window.location.href
console.log(link)
console.log(url)
link.setAttribute("href", url + "/create_card")
console.log(link)