// Restart Game Button
var restart = document.querySelector('#b');

// Grab all the squares
var squares = document.querySelectorAll("td");


// Clear Squares Function
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }

}
restart.addEventListener('click',clearBoard)

var flag = true;

function changeMarker() {
  // if(this.textContent === '') {
  //   this.textContent = 'X';
  // } else if (this.textContent === 'X') {
  //   this.textContent = 'O';
  // } else {
  //   this.textContent = '';
  // }
  if(flag) {
    this.textContent = 'X';
    flag = false;
  } else {
    this.textContent = 'O';
    flag = true;
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click', changeMarker);
}
