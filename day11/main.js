function myHeart() {
    document.getElementById("heartfirst").style.display = "none";
    document.getElementById("heart").style.display = "block";
    document.getElementById("heart").style.color = "red";
    alert("Beyendiniz")
}

function myfirstHeart() {
    document.getElementById("heartfirst").style.display = "block";
    document.getElementById("heart").style.display = "none";
    document.getElementById("heartfirst").style.color = "black";
    alert("Beyenmediniz")
}



function myLike() {
    document.getElementById("likefirst").style.display = "none";
    document.getElementById("like").style.display = "block";
}


function myfirstLike() {
    document.getElementById("likefirst").style.display = "block";
    document.getElementById("like").style.display = "none";
}


function addBasket() {

    // let mebleg = document.querySelectorAll('.mebleg')
    // let sum = 0
    // mebleg.forEach(e => {
    //     x = e.innerHTML
    //     sum += parseInt(x)
    // });
    // document.getElementById("mysum").innerHTML = `${sum} AZN`



    let addbutton = document.getElementById("addbutton");
    let alertPrice = document.getElementById("alertPrice");







    if (addbutton.classList.contains("bg-info")) {
        addbutton.classList.replace("bg-info", "bg-secondary");
        addbutton.innerHTML = "Səbətdən çıxar"
        alertPrice.innerHTML = "1"
        alertt.classList.replace("alert-warning", "alert-danger")
        $('#myModal').modal('toggle')

    }
    else {
        addbutton.classList.replace("bg-secondary", "bg-info")
        addbutton.innerHTML = "Səbətə əlavə et"
        alertPrice.innerHTML = "2"
        alertt.classList.replace("alert-danger", "alert-warning")
        $('#myModal2').modal('toggle')
        // if (alertPrice.innerHTML == "1") {
        //     alertt.classList.replace("alert-warning", "alert-danger")
        // }
        // else {
        //     alertt.classList.replace("alert-danger", "alert-warning")
        // }
    }
}

let mebleg = document.querySelectorAll('.mebleg')
let sum = 0
mebleg.forEach(e => {
    let x = e.innerHTML
    sum += parseInt(x)
});
document.getElementById("mysum").innerHTML = `${sum} AZN`





let redx = document.querySelectorAll(".redx")
redx.forEach(e => {
    // console.log(e)
    e.addEventListener("click", function (el) {
        small_parent = el.target.parentElement
        small_parent.parentElement.style.display = "none";
    })
});


