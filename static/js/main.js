function enviarPesquisa() {
    var atendimento = document.querySelectorAll('.atendimento')
    var limpeza = document.querySelectorAll('.limpeza')
    var conforto = document.querySelectorAll('.conforto')
    var cafe = document.querySelectorAll('.cafe')
    var internet = document.querySelectorAll('.internet')
    var custo_beneficio = document.querySelectorAll('.custo_beneficio')
    var localizacao = document.querySelectorAll('.localizacao')
    var listaDeItens = [atendimento, limpeza, conforto, cafe, internet, custo_beneficio, localizacao]
    var votos = new Array()


    var nome_cliente = document.getElementById('nome').value;
    var num_apto = document.getElementById('num_apto').value;

    var sugestao = document.getElementById('sugestao').value;

//    var nome_cliente = input_nome.value
//    var num_apto = input_num.value




    // Iterador para os RadioButtons.
    // Acrescenta cada item selecionado na lista "votos"
    for (let contador1 = 0; contador1 < listaDeItens.length; contador1++) {
        for (let contador2 = 0; contador2 < listaDeItens[contador1].length; contador2++){
            if (listaDeItens[contador1][contador2].checked) {
                votos.push(`${listaDeItens[contador1][contador2].id}`)
            }
        }
    }

    var regexAvaliacao = /(-ms|-s|-ps|-i)/g
    var listaItem = new Array()
    var listaAvaliacao = new Array()

    listaAvaliacao.push(nome_cliente)
    listaAvaliacao.push(num_apto)


    // Regex para encontrar os resultados das votações na lista "votos"
    for (var contRegex = 0; contRegex < votos.length; contRegex++) {
        var encontrarAv = votos[contRegex].match(regexAvaliacao)
        var strAv = encontrarAv.toString()
        var replaced = strAv.replace('-','')
        listaAvaliacao.push(replaced)
    }

    listaAvaliacao.push(sugestao)

    fetch("/pesquisa?" + new URLSearchParams({listaAvaliacao}))
    console.log(listaAvaliacao)
    alert('Pesquisa enviada com sucesso! Muito obrigado por participar. :)')
    document.location.reload(true)

}