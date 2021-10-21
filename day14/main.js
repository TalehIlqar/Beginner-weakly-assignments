let bookbase = [
    {
    "name":  "Sefiller",
    "muellif" : "Viqtor Huqo",
    "img" : "sefiller.jpeg"

},

{
    "name":  "Icognito",
    "muellif" : "Elegman",
    "img" : "Inkognito.png"
},


{
    "name":  "Etiraf",
    "muellif" : "Talstoy",
    "img" : "Etiraf_(Lev_Tolstoy).jpg"
},


{
    "name":  "Beyaz geceler",
    "muellif" : "Dostayevski",
    "img" : "Dostoyevski_Beyaz_Geceler_mini.png"
},


{
    "name":  "Herb ve sulh",
    "muellif" : "Tolstoy",
    "img" : "herbsulh.jpeg"
},



{
    "name":  "Qadinlar Veneradan Kishiler Marsdan",
    "muellif" : "Deyl Karnegi",
    "img" : "kishiler.jpg"
}


]

let booklg = bookbase.length;

let arr = [];

$("#plus").click(function(){
    if (parseInt($("#inputadd").val()) != booklg){
        $("#inputadd").val(function(i,c){
            // console.log(c);
            return parseInt(c) + 1
            
        })
        let r = Math.floor(Math.random()*bookbase.length)
        // console.log(a);
        $("#row").append(`
        <div class="pt-4 col-12 col-md-6  col-lg-4 d-flex justify-content-center last">
    <div class="card mt-3 mb-3" style="width: 10rem;">
    <img class="card-img-top" src="../assets/images/${bookbase[r].img}" alt="Card image cap">
    <div class="card-body">
    <h5 class="card-title">${bookbase[r].name}</h5>
    <p class="card-text">${bookbase[r].muellif}</p>
    <a href="#" class="btn btn-primary bg-info">Ətraflı</a>
    </div>
    </div>`)
    arr.push(bookbase[r]);
    // console.log(arr)
    bookbase.splice(r,1);    
}   

});


$("#minus").click(function(){
    if (parseInt($("#inputadd").val()) != 0){
        $("#inputadd").val(function(i,c){
            return parseInt(c) - 1
            
        })
    }

    if (bookbase.length != 6){
        bookbase.push(arr.pop())
    }

    $(".last").last().remove()
});





$("#bashla").click(function(){    
    if ($("#bashla").text() == ("Başla")){
        $("#calc").removeClass("d-none")
        $("#bashla").text("Bitir").removeClass("btn-warning").addClass("btn-danger")
    }
    else{
        $("#calc").addClass("d-none")
        $("#bashla").text("Başla").removeClass("btn-danger").addClass("btn-warning")
    }})
    $("#hesabla").click(function () {
    $('#alert1').removeClass("d-none")
    let result = $(("#page")).val() / $(("#day")).val();
        if (isNaN($("#page").val())==true || isNaN($("#day").val())==true || $("#page").val()== 0 || $("#day").val() == 0 || isNaN(result) || result == Infinity){
        $('#alert1').text('Hesablamada səhv baş verdi!')
        $("#alert1").addClass("alert-danger")
    }
    else {
        $('#alert1').text(`Hər gün ən az ${result} səhifə oxumalısız`)
        $("#alert1").addClass("alert-success")
    }})