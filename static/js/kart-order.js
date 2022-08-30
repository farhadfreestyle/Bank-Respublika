const select = document.getElementById('filial-or-kuryer');
select.addEventListener('change', function handleChange(event) {
  var location = document.getElementById('chosen-location');
  var filial = document.querySelector('.chosen-filial')
  
  console.log(typeof event.target.value);
  if (event.target.value === 'Kuryerlə'){
    location.style.display = 'block'
    filial.style.display = 'none'
  }

  else if (event.target.value === 'Filialdan'){
    location.style.display = 'none'
    filial.style.display = 'block'
  }
  
});



const card_name = document.getElementById('selected-card-name');
card_name.addEventListener('change', function handleChange(event) {


var my_value =  event.target.value;
if (my_value =='NeoKart Standard'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/NEO/Cards%20(2).png" alt="" height="135px" width="215px">'
}

else if (my_value =='NeoKart Premium'){

  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/NEO/Cards.png" alt="" height="135px" width="215px">'
}

else if (my_value =='Mover Visa Platinium'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/Mover%20Visa%20Premium.png" alt="" height="135px" width="215px">'
}

else if (my_value =='Mover Visa Classic'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/Mover%20Visa%20Classic.png" alt="" height="135px" width="215px">'
}


else if (my_value =='Digital Card (Rəqəmsal Kart)'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/DG_new_screen/card%20thumbs%20for%20website.png" alt="" height="135px" width="215px">'
}

else if (my_value =='MasterCard Debit'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/debet.png" alt="" height="135px" width="215px">'
}

else if (my_value =='MasterCard Platinum'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/MC%20Platinum.png" alt="" height="135px" width="215px">'
}

else if (my_value =='MasterCard World Elite'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/world%20elite.png" alt="" height="135px" width="215px">'
}


else if (my_value =='MasterCard Wblack Edition PP'){
  document.querySelector('.card-picture').innerHTML= '<img src = "https://www.bankrespublika.az/uploads/cards/black_edition.png" alt="" height="135px" width="215px">'
}



});