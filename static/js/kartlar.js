var checked = document.querySelectorAll('#card-checkbox')

each = document.querySelectorAll('.each-card')

zero =  document.querySelector('.card1')

first = document.querySelector('.card2')

second = document.querySelector('.card3')


var count = document.querySelector(".muqaise-count")

var one1 = document.querySelector('.one1 button')
var one2 = document.querySelector('.one2 button')
var one3 = document.querySelector('.one3 button')
var one4 = document.querySelector('.one4 button')

var two1 = document.querySelector('.two1 button')
var two2 = document.querySelector('.two2 button')
var two3 = document.querySelector('.two3 button')
var two4 = document.querySelector('.two4 button')

var three1 = document.querySelector('.three1 button')
var three2 = document.querySelector('.three2 button')
var three3 = document.querySelector('.three3 button')



var four1 = document.querySelector('.four1 button')
var four2 = document.querySelector('.four2 button')
var four3 = document.querySelector('.four3 button')


checked.forEach(element => {
   
    element.addEventListener('click',function() {
        var checkboxes = $('input:checkbox:checked').length
        count.innerText = checkboxes
    })
  });


  one1.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    one2.style.backgroundColor = 'white'
    one3.style.backgroundColor = 'white'
    one4.style.backgroundColor = 'white'
    each.forEach(element => {
   
        element.style.display = 'block'
        })
    first.style.display = 'none'
    zero.style.display = 'none'
    

   


  })

  one2.addEventListener('click', function(){
    one2.style.borderLeft = '50px'
    one2.style.backgroundColor = 'rgb(218, 216, 216)'
    one1.style.backgroundColor = 'white'
    one3.style.backgroundColor = 'white'
    one4.style.backgroundColor = 'white'
  })


  one3.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    one2.style.backgroundColor = 'white'
    one1.style.backgroundColor = 'white'
    one4.style.backgroundColor = 'white'

    each.forEach(element => {
   
        element.style.display = 'none'
        })

  })


  one4.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    one2.style.backgroundColor = 'white'
    one1.style.backgroundColor = 'white'
    one3.style.backgroundColor = 'white'
  })



  two1.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    two2.style.backgroundColor = 'white'
    
    
    each.forEach(element => {
   
        element.style.display = 'block'
        })
    first.style.display = 'none'
    zero.style.display = 'none'
    

  })

  two2.addEventListener('click', function(){
    two2.style.borderLeft = '50px'
    two2.style.backgroundColor = 'rgb(218, 216, 216)'
    two1.style.backgroundColor = 'white'
    
    
  })










  three1.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    three2.style.backgroundColor = 'white'
    three3.style.backgroundColor = 'white'
    each.forEach(element => {
   
        element.style.display = 'block'
        })
    first.style.display = 'none'
  
  })

  three2.addEventListener('click', function(){
    three2.style.borderLeft = '50px'
    three2.style.backgroundColor = 'rgb(218, 216, 216)'
    three1.style.backgroundColor = 'white'
    three3.style.backgroundColor = 'white'
    
  })


  three3.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    three1.style.backgroundColor = 'white'
    three2.style.backgroundColor = 'white'
  
  })







  four1.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    four2.style.backgroundColor = 'white'
    four3.style.backgroundColor = 'white'

    each.forEach(element => {
   
        element.style.display = 'block'
        })
    first.style.display = 'none'
    zero.style.display = 'none'
   
  })

  four2.addEventListener('click', function(){
    four2.style.borderLeft = '50px'
    four2.style.backgroundColor = 'rgb(218, 216, 216)'
    four1.style.backgroundColor = 'white'
    four3.style.backgroundColor = 'white'
   
  })


  four3.addEventListener('click', function(){
    this.style.borderLeft = '50px'
    this.style.backgroundColor = 'rgb(218, 216, 216)'
    four2.style.backgroundColor = 'white'
    four1.style.backgroundColor = 'white'
   
  })


