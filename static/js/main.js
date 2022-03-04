function enviarPesquisa() {
    var atendimento = document.querySelectorAll('.atendimento')
    var limpeza = document.querySelectorAll('.limpeza')
    var conforto = document.querySelectorAll('.conforto')
    var cafe = document.querySelectorAll('.cafe')
    var internet = document.querySelectorAll('.internet')
    var custo_beneficio = document.querySelectorAll('.custo_beneficio')
    var localizacao = document.querySelectorAll('.localizacao')
    var listaDeItens = [atendimento, limpeza, conforto, cafe, internet, custo_beneficio, localizacao]
    var votacao = new Array()
    for (let contador1 = 0; contador1 < listaDeItens.length; contador1++) {
        for (let contador2 = 0; contador2 < listaDeItens[contador1].length; contador2++){
            if (listaDeItens[contador1][contador2].checked) {
                votacao.push(`${listaDeItens[contador1][contador2].id}`)
            }
        }
    }
    var regexAvaliacao = /(-ms|-s|-ps|-i)/g
    var listaItem = new Array()
    var listaAvaliacao = new Array()
    for (var contRegex = 0; contRegex < votacao.length; contRegex++) {
        var encontrarAv = votacao[contRegex].match(regexAvaliacao)
        str = encontrarAv.toString()
        repl = str.replace('-','')
        listaAvaliacao.push(repl)
    }
    window.alert(`${listaAvaliacao}`)
}

