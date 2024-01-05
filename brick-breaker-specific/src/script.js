//-------------------------
// GLOBAL VARIABLES
//-------------------------
var x = 200;      // starting horizontal position of ball
var y = 150;      // starting vertical position of ball
var dx = 1;       // amount ball should move horizontally
var dy = -3;      // amount ball should move vertically
// variables set in init()
var ctx, width, height, paddlex, bricks, brickWidth; 
var paddleh = 10; // paddle height (pixels)
var paddlew = 75; // paddle width (pixels)
var canvasMinX = 0; // minimum canvas x bounds
var canvasMaxX = 0; // maximum canvas x bounds
var intervalId = 0; // track refresh rate for calling draw()
var nrows = 7; // number of rows of bricks
var ncols = 6; // number of columns of bricks
var brickHeight = 15; // height of each brick
var padding = 1;  // how far apart bricks are spaced

var ballRadius = 10; // size of ball (pixels)
// change colors of bricks -- add as many colors as you like
var brick_colors = ["maroon", "gold", "orange", "green", "blue", "violet", "pink"];
var paddlecolor = "black";
var ballcolor = "black";
var backcolor = "grey";

var score = 0;      // store the number of bricks eliminated
var paused = false; // keeps track of whether the game is paused (true) or not (false)

//-------------------------
// FUNCTION DECLARATIONS
//-------------------------
// initialize game
function init() {
  //get a reference to the canvas
  ctx = $('#canvas')[0].getContext("2d");
  width = $("#canvas").width();
  height = $("#canvas").height();
  paddlex = width / 2;
  brickWidth = (width/ncols) - 1;
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + width;
  // run draw function every 10 milliseconds to give 
  // the illusion of movement
  init_bricks();
  start_animation();
  update_score_text();
}

function reload() {
  x = 200;      // starting horizontal position of ball
  y = 150;      // starting vertical position of ball
  dx = 1;       // amount ball should move horizontally
  dy = -3;      // amount ball should move vertically
  score = 0;    // score resets
  stop_animation(); // added so the speed doesn't keep increasing
  paused = false; // reset "paused" to false or else if the game was restarted when it was set to true, trying to pause the game will either speed it up or make it the normal pace
  init();
}

// used to draw the ball
function circle(x,y,r) {
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI*2, true);
  ctx.closePath();
  ctx.fill();
}

// used to draw each brick & the paddle
function rect(x,y,w,h) {
  ctx.beginPath();
  ctx.rect(x,y,w,h);
  ctx.closePath();
  ctx.fill();
}

// clear the screen in between drawing each animation
function clear() {
  ctx.clearRect(0, 0, width, height);
  rect(0,0,width,height);
}

// What do to when the mouse moves within the canvas
function onMouseMove(evt) {
  // set the paddle position if the mouse position 
  // is within the borders of the canvas
  if (evt.pageX > canvasMinX && evt.pageX < canvasMaxX) {
    paddlex = Math.max(evt.pageX - canvasMinX - (paddlew/2), 0);
    paddlex = Math.min(width - paddlew, paddlex);
  }
}

function onKeyPress(evt) { 
  paused = !paused;
  pause(); 
}

function pause() {
 if (paused) { // if paused, stop animation 
   stop_animation();
 } else { // if unpaused, begin animation again
   start_animation();
 }
}

// initialize array of bricks to be visible (true)
function init_bricks() {
    bricks = new Array(nrows);
    for (i=0; i < nrows; i++) { // for each row of bricks
        bricks[i] = new Array(ncols);
        for (j=0; j < ncols; j++) { // for each column of bricks
            bricks[i][j] = true;
        }
    }
}

// render the bricks
function draw_bricks() {
  for (i=0; i < nrows; i++) { // for each row of bricks
    for (j=0; j < ncols; j++) { // for each column of bricks
      // set the colors to alternate through
      // all colors in brick_colors array
      // modulus (%, aka remainder) ensures the colors
      // rotate through the whole range of brick_colors
      ctx.fillStyle = brick_colors[(i+j) % brick_colors.length];
      if (bricks[i][j]) {
        rect((j * (brickWidth + padding)) + padding, 
             (i * (brickHeight + padding)) + padding,
             brickWidth, brickHeight);
      } // else if bricks[i][j] is false it's already been hit
    }
  }
}

function draw() {
  // before drawing, change the fill color
  ctx.fillStyle = backcolor;
  clear();
  ctx.fillStyle = ballcolor;
  //draw the ball
  circle(x, y, ballRadius);
  ctx.fillStyle = paddlecolor;
  //draw the paddle
  rect(paddlex, height-paddleh, paddlew, paddleh);
  draw_bricks();

  //check if we have hit a brick
  rowheight = brickHeight + padding;
  colwidth = brickWidth + padding;
  row = Math.floor(y/rowheight);
  col = Math.floor(x/colwidth);
  //if so reverse the ball and mark the brick as broken
  if (y < nrows * rowheight && row >= 0 && col >= 0 && bricks[row][col]) {
    dy = -dy; // dy is direction of ball (vertical) - this switches direction
    bricks[row][col] = false; // all bricks are initialized as true. When one is hit, it changes to false and therefore is no longer drawn
    score+=1; // update score
    update_score_text(); // print updated score
  }
 
  //contain the ball by rebouding it off the walls of the canvas
  if (x + dx > width || x + dx < 0)
    dx = -dx;

  if (y + dy < 0) {
    dy = -dy;
  } else if (y + dy > height - paddleh) {
    // check if the ball is hitting the 
    // paddle and if it is rebound it
    if (x > paddlex && x < paddlex + paddlew) {
      dy = -dy;
      if (x > paddlex && x < paddlex + paddlew/2){
        dx = -1; // if the ball hits the left side of the paddle, the ball goes left
      } else {
        dx = 1;  // if the ball hits the right side of the paddle, the ball goes right. Making it a more responsive game
      }
    }
  }
 if (y + dy > height) {
    //game over, so stop the animation
    stop_animation();
  }
  x += dx;
  y += dy;
}

function update_score_text() {
  $('#score').text("Score: " + score);
}

function start_animation() {
  intervalId = setInterval(draw, 10);
}

function stop_animation() {
  clearInterval(intervalId);
}

//-------------------------
// main functionality begins here
$(document).mousemove(onMouseMove); // register the mouse move function
$(document).keypress(onKeyPress);   // register onKeyPress function
init();                             // initialize & begin game
