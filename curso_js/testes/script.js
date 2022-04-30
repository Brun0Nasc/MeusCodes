function submeter() {
    var pontos = 0
    var q1 = document.getElementById('q1a')
    var q2 = document.getElementById('q2c')
    var q3 = document.getElementById('q3b')
    var q4 = document.getElementById('q4d')
    if (q1.checked) {
        var q1indi = document.getElementById('q01')
        q1indi.style.color = 'green'
        pontos++
    } else {
        var q1indi = document.getElementById('q01')
        q1indi.style.color = 'red'
    }
    if (q2.checked) {
        var q2indi = document.getElementById('q02')
        q2indi.style.color = 'green'
        pontos++
    } else {
        var q2indi = document.getElementById('q02')
        q2indi.style.color = 'red'
    }
    if (q3.checked) {
        var q3indi = document.getElementById('q03')
        q3indi.style.color = 'green'
        pontos++
    } else {
        var q3indi = document.getElementById('q03')
        q3indi.style.color = 'red'
    }
    if (q4.checked) {
        var q4indi = document.getElementById('q04')
        q4indi.style.color = 'green'
        pontos++
    } else {
        var q4indi = document.getElementById('q04')
        q4indi.style.color = 'red'
    }

    document.getElementById('f1').innerText = ''
    document.getElementById('f2').innerText = ''
    document.getElementById('f3').innerText = ''
    document.getElementById('f4').innerText = ''
    var acertos = document.getElementById('pontuacao')

    if (pontos == 0) {
        acertos.innerHTML = `Você não acertou nenhuma :(`
    } else if (pontos < 4){
        acertos.innerHTML = `Você acertou ${pontos} questões`
    } else {
        acertos.innerHTML = `Parabéns! Você acertou todas! :D`
    }
}