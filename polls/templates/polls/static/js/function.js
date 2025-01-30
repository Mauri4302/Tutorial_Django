var fecha = document.getElementById("fecha");


function updateClock(){
    actual = new Date();
    hora = actual.getHours()
    minuto = actual.getMinutes()
    segundo = actual.getSeconds()
    mes = actual.getMonth()
    dia = actual.getDay()
    anno = actual.getFullYear()

    showHour =dia+" - "+mes+" - "+anno+" - " +hora+" : "+minuto+" : "+segundo
    fecha.textContent = showHour

    setTimeout("updateClock()", 1000)

}

updateClock()

var django = document.getElementById('django')
var reloj = document.getElementById('clock')
function updateDjangoClock(){
    update = django.textContent
    reloj.textContent = update

    setTimeout("updateDjangoClock()", 1000)
}

updateDjangoClock()