from flask import Flask, render_template, request
import os

app = Flask(__name__)

def validar_renda(renda):
    return 1000 <= renda <= 10000

@app.route('/', methods=['GET', 'POST'])
def index():
    show_result = False
    if request.method == 'POST':
        renda = float(request.form['renda'])
        if validar_renda(renda):
            valor_emprestimo = float(request.form['valor_emprestimo'])
            meses_pagamento = int(request.form['meses_pagamento'])

            taxa_juros_mensal = 0.03  
            taxa_juros_porcentagem = taxa_juros_mensal * 100

            juros_cobrado = valor_emprestimo * taxa_juros_mensal * meses_pagamento
            prestacao_mensal = (valor_emprestimo + juros_cobrado) / meses_pagamento
            custo_total = valor_emprestimo + juros_cobrado
            show_result = True

            return render_template('index.html', 
                                   show_result=show_result,
                                   renda=renda,
                                   valor_emprestimo=valor_emprestimo,
                                   meses_pagamento=meses_pagamento,
                                   prestacao_mensal=prestacao_mensal,
                                   custo_total=custo_total,
                                   taxa_juros_porcentagem=taxa_juros_porcentagem,
                                   error_message=error_message)
        else:
            error_message = "Renda fora do limite especificado. Tente novamente."
    
    return render_template('index.html', 
                           show_result=show_result, 
                           error_message=error_message)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
