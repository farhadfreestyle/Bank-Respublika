var ferdi = document.querySelector(".compage-container .button-container .buttons .ferdi")
var koor = document.querySelector(".koor")

var whole = document.querySelector('.card-cotainer')


window.addEventListener('load', function(){
    ferdi.style.borderBottom = "2px solid #475ED0";
    ferdi.style.color = '#475ED0'


})

ferdi.addEventListener('click', function(){
    ferdi.style.borderBottom = "2px solid #475ED0";
    ferdi.style.color = '#475ED0'
    koor.style.borderBottom = "none";
    koor.style.color = 'black'
    whole.style.display = 'block'
    


})


koor.addEventListener('click', function(){
    ferdi.style.borderBottom = "none";
    ferdi.style.color = 'black'
    koor.style.borderBottom = "2px solid #475ED0";
    koor.style.color = '#475ED0'
    whole.style.display = 'none'


})