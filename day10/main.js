let lose = 0;
let win = 0;
let alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
let index = Math.floor(Math.random() * alfabet.length)
let request = alfabet[index]

for (i = 0; i < 5; i ++) {
    let guess = prompt("get letter")
    if (guess == request) {
        win ++
        break
    }
    else{
        lose ++
    }
}
console.log(`win: ${win}`)
console.log(`lose: ${lose}`)