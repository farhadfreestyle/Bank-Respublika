var myHeaders = new Headers();
myHeaders.append("apikey", "p8sNj6vbnnKaJv2c9DJEZPb5EKEmFx7u");


spans =document.getElementsByTagName('span')

var requestOptions = {
  method: 'GET',
  redirect: 'follow',
  headers: myHeaders
};

fetch("https://api.apilayer.com/fixer/latest?symbols=AZN&base=EUR", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error))




fetch("https://api.apilayer.com/fixer/latest?symbols=AZN&base=GBP", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error))




  fetch("https://api.apilayer.com/fixer/latest?symbols=AZN&base=RUB", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error))
     


  fetch("https://api.apilayer.com/fixer/latest?symbols=AZN&base=USD", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error))
     