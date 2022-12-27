const image_input = document.querySelector("#image_input");
var uploaded_image = "";
var img = new Image();
var canvas=document.getElementById('cv');
var ctx = canvas.getContext("2d");

function drawImageScaled(img, ctx) {
    var hRatio = canvas.width  / img.width    ;
    var vRatio =  canvas.height / img.height  ;
    var ratio  = Math.min ( hRatio, vRatio );
    var centerShift_x = ( canvas.width - img.width*ratio ) / 2;
    var centerShift_y = ( canvas.height - img.height*ratio ) / 2;  
    ctx.clearRect(0,0,canvas.width, canvas.height);
    ctx.drawImage(img, 0,0, img.width, img.height,
                       centerShift_x,centerShift_y,img.width*ratio, img.height*ratio);  
 }

image_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", ()=> {
        uploaded_image = reader.result;
        img.src = reader.readAsDataURL(this.files[0]);
    });
    drawImageScaled(img, ctx);
  })