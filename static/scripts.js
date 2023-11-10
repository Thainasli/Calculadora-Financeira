function calcularEmprestimo() {
    var renda = parseFloat(document.getElementById('renda').value);
    var valor_emprestimo = parseFloat(document.getElementById('valor_emprestimo').value);
    var meses_pagamento = parseInt(document.getElementById('meses_pagamento').value);

    var taxa_juros_mensal = 0.03;
    var taxa_juros_porcentagem = taxa_juros_mensal * 100;
    var juros_cobrado = valor_emprestimo * taxa_juros_mensal * meses_pagamento;
    var prestacao_mensal = (valor_emprestimo + juros_cobrado) / meses_pagamento;
    var custo_total = valor_emprestimo + juros_cobrado;

    document.getElementById('prestacao-mensal').textContent = prestacao_mensal.toFixed(2);
    document.getElementById('custo-total').textContent = custo_total.toFixed(2);
    document.getElementById('taxa-juros').textContent = taxa_juros_porcentagem.toFixed(2) + "%";

    document.getElementById('result-container').style.display = 'block';
}
