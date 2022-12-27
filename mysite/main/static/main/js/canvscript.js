var canvas;
var ctx;
var width = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var height = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;

function init()
{
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
    canvas.width = width;
    canvas.height = height;
    canvasW = canvas.width;
    canvasH = canvas.height;
}

init();

ctx.fillStyle = "green";
ctx.fillRect(0, 0, width, height);