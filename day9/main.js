var x = parseInt(prompt("kitabin sehife sayi:"));

if (x === x) {
    if (x <= 0 || x == null) {
        alert("sehife sayi qeyri-munkundur")
    }
    else {
        var y = parseInt(prompt("Neche gune bitirmelisiniz:"));
        if (y === y) {
            if (y <= 0 || y == null) {
                alert("gun sayi qeyri-munkundur")
            }
            else {
                var z = x / y;
                if (Math.ceil(z) == !Math.floor(z)) {
                    alert(`siz gunde ${Math.floor(z)} oxumaliniz`);

                }

                else {
                    alert(`siz gunde ${Math.floor(z)} oxumaliniz`)
                }
            }

        }
        else{
            alert("Reqem daxil edin")
        }
    }


}

else {
    alert("Reqem daxil edin")
}




console.log(`sehife sayi: ${x}`);
console.log(`neche gune bitirmelisiniz: ${y}`);
console.log(`netice: ${z}`);
