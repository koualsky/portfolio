// LOGO ANIMATE
const logo = document.getElementById('logo');

logo.onmouseover = function() {

    var numb = Math.floor(Math.random() * 10);

    var list = [
        'bounce', 
        'flash', 
        'pulse', 
        'rubberBand', 
        'shake', 
        'swing', 
        'tada', 
        'wobble', 
        'jello', 
        'heartBeat'
    ];

    var random = list[numb];

    function deleteAnimate() {
        logo.classList.remove("animated", random);
    }

    logo.classList.add("animated", random);
    setTimeout(deleteAnimate, 1000);
}