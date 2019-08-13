var headOne = document.querySelector('#one');
var headTwo = document.querySelector('#two');
var headThree = document.querySelector('#three');

//Hover (mouseover and mouseout)
headOne.addEventListener('mouseover', function() {
  headOne.textContent = 'Mouse currently over';
  headOne.style.color = 'red';
})

headOne.addEventListener('mouseout', function() {
  headOne.textContent = 'Mouse not on me';
  headOne.style.color = 'blue';
})

//on Click
headTwo.addEventListener('click', function() {
  headTwo.textContent = 'Clicked On';
  headTwo.style.color = 'crimson';
})

//double Click
headThree.addEventListener('dblclick', function() {
  headThree.textContent = 'Double Clicked';
  headThree.style.color = 'green';
})
