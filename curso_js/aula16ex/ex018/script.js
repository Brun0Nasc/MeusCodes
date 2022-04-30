let valores = []
let res = document.getElementById('res')
function adicionar(){
    res.innerHTML = ''
    let num = document.getElementById('num')
    let sel = document.getElementById('selnum')
    let n = Number(num.value)
    if(num.value.length == 0 || num.value < 1 || num.value > 100 || valores.indexOf(n) != -1){
        alert('Valor inválido ou já adicionado')
    } else{
        valores.push(n)
        let item = document.createElement('option')
        item.text = `Valor ${n} adicionado.`
        sel.appendChild(item)
    }
    num.value = ''
    num.focus()
}

function finalizar(){
    let somador = 0
    if (valores.length == 0){
        alert('Adicione algum valor!')
    } else {
        for (let pos in valores){
            somador += valores[pos]
        }
        let media = somador / valores.length
        let max = valores.reduce(function(a, b) {return Math.max(a, b)})
        let min = valores.reduce(function(a, b) {return Math.min(a, b)})
        res.innerHTML = `<p>Ao todo, temos ${valores.length} números cadastrados.</p>`+
        `<p>O maior valor informado foi ${max}.</p>`+
        `<p>O menor valor informado foi ${min}</p>`+
        `<p>Somando todos os valores, temos ${somador}</p>`+
        `<p>A média dos valores digitados é ${media}</p>`
    }
}