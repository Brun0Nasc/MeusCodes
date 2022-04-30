function contar() {
    let inicio = document.getElementById('inicio')
    let fim = document.getElementById('fim')
    let passo = document.getElementById('passo')
    let res = document.getElementById('res')
    
    if(inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        res.innerHTML = `Impossível contar...`
    } else {
        res.innerHTML = `Contando:<br>`
        let i = Number(inicio.value)
        let f = Number(fim.value)
        let p = Number(passo.value)

        if(p === 0){
            alert('Passo inválido. Vou considerar como 1')
            p = 1
        }
        if (i <= f){
            while(i <= f){
                res.innerHTML += `${i} &#128073 `
                i += p
            }
        } else{
            while(f <= i){
                res.innerHTML += `${i} &#128073 `
                i -= p
            }
        }
        res.innerHTML += `&#127937`
    }
}