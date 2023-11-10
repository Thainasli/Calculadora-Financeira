from flask import Flask, render_template, request
import os

app = Flask(__name__)

def validar_renda(renda):
    return 1000 <= renda <= 10000

@app.route('/', methods=['GET', 'POST'])
def index():
    show_result = False
    error_message = None
    
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
        else:
            error_message = "Renda fora do limite especificado. Tente novamente."

    return render_template('index.html', 
                           show_result=show_result,
                           renda=request.form.get('renda', ''),
                           valor_emprestimo=request.form.get('valor_emprestimo', ''),
                           meses_pagamento=request.form.get('meses_pagamento', ''),
                           prestacao_mensal=f'{prestacao_mensal:.2f}' if show_result else '',
                           custo_total=f'{custo_total:.2f}' if show_result else '',
                           taxa_juros_porcentagem=f'{taxa_juros_porcentagem:.2f}' if show_result else '',
                           error_message=error_message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
