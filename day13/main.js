function like() {
    let likes = document.getElementById("like")
    if (likes.classList.contains("fa-thumbs-up")) {
        likes.classList.replace("fa-thumbs-up", "fa-thumbs-down")
        likes.classList.replace("text-primary", "text-danger")
    }
    else {
        likes.classList.replace("fa-thumbs-down", "fa-thumbs-up")
        likes.classList.replace("text-danger", "text-primary")
    }
}




function heart() {

    let hearts = document.getElementById("heart")
    if (hearts.classList.contains("text-secondary")) {
        hearts.classList.replace("text-secondary", "text-danger")
        alert("Beyendiniz")
    }
    else {
        hearts.classList.replace("text-danger", "text-secondary")
        alert("Beyenmediniz")
    }
}





function button() {
    let buttons = document.getElementById("button");
    // let badges = document.getElementById("badge");
    let alert = document.getElementById('alert')
    let alertdiv = document.getElementById("alertdiv")
    let kitabadd = document.getElementById("kitabadd")
    let kitabprice = document.getElementById("kitabprice")
    let xuchuncu = document.getElementById("xuchuncu")
    let toplamqiymet = document.getElementById("toplamqiymet")
    let AZN = document.getElementById("AZN")

    if (buttons.classList.contains("bg-info")) {
        buttons.classList.replace("bg-info", "bg-secondary")
        alertdiv.classList.replace("alert-warning", "alert-danger")
        AZN.innerText = "AZN"
        alert.innerText = "1"
        kitabadd.innerText = "Incognito"
        kitabprice.innerText = "12"
        xuchuncu.classList.add("fa-times")
        buttons.setAttribute("value", "Sebetden chixar");
        $("#modal1").modal()
        hesabla()

    }
    else {
        buttons.classList.replace("bg-secondary", "bg-info")
        alertdiv.classList.replace("alert-danger", "alert-warning")
        alert.innerText = "2"
        kitabadd.innerText = ""
        kitabprice.innerText = ""
        toplamqiymet.innerText = "37 AZN"
        xuchuncu.classList.remove("fa-times")
        buttons.setAttribute("value", "Sebete elave et");
        $("#modal2").modal()
    }
}




function xbirinci() {

    let xbirincidiv = document.getElementById("xbirincidiv")
    xbirincidiv.innerHTML = ""
    hesabla()

}

function xikinci() {
    let xikincidiv = document.getElementById("xikincidiv")
    xikincidiv.innerHTML = ""
    hesabla()

}

function xuchuncu() {
    let xuchuncudiv = document.getElementById("xuchuncudiv")
    xuchuncudiv.innerHTML = ""
    hesabla()

}




function hesabla() {
    let All_prices = document.querySelectorAll(".price");
    let arr = [];
    sum = 0;
    for (let i = 0; i < All_prices.length; i++) {
        // console.log(arr.length)
        let valuseprice = All_prices[i].innerText
        // console.log(valuseprice)
        if (valuseprice != '') {
            arr.push(parseInt(valuseprice))
            // console.log(arr)
        }
    }
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i]
        console.log(sum)
    }
    document.querySelector("#sum").innerHTML = sum
    document.querySelector("#badge").innerText = arr.length
    if (arr.length == 0) {
        document.querySelector("#badge").style.display = "none"
    }
}
hesabla()

