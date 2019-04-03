
var myimg = document.getElementById('mypics');

imgarray = ['static/blog/img/sport.jpg', 'static/blog/img/education.jpg', 'static/blog/img/entertainment.jpg',
          'static/blog/img/lifestyle-font.jpg','static/blog/img/fash_world.jpg', 'static/blog/img/tech.jpg'];

imgindex = 0;

function changeImg(){
  myimg.setAttribute("src", imgarray[imgindex]);
  imgindex++;
  if(imgindex >= imgarray.length){
    imgindex = 0;
  }
}

setInterval(changeImg, 7000)
