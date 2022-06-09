pergunta = {
    'questão 1': {
        'pergunta': 'Qual das alternativas a seguir, o clientes não entende a modalegem',
        'alternativas': {'a': 'Orientado a Objeto', 'b': 'Estruturado', 'c': 'Métodos Formais'},
        'resposta': 'c'
    },
    'questão 2': {
        'pergunta': 'Um dos problemas do modelo_________ é descobrir o fim, de qual modelo estamos falando',
        'alternativas': {'a': 'Cascata', 'b': 'Espiral', 'c': 'Prototipagem'},
        'resposta': 'b',
    }, 'questão 3': {
        'pergunta': 'Uma classe que não pode ser instanciada  é chamada de?',
        'alternativas': {'a': 'Classe filha', 'b': 'Classe abstrata', 'c': 'Classe sem métodos'},
        'resposta': 'b',
    }, 'questão 4': {
        'pergunta': '__________ é o diagrama que possui os mesmos elementos do de sequencia',
        'alternativas': {'a': 'Robustez', 'b': 'Atividades', 'c': 'Classe'},
        'resposta': 'a',
    }, 'questão 5': {
        'pergunta': 'O que são Sprints nas metodologias ágeis',
        'alternativas': {'a': 'São padrões de projeto ', 'b': 'São documentos de projetos',
                         'c': 'São ciclos de Desenvolvimento'},
        'resposta': 'c',
    },
}
nota = 0
for pergunta_k, pergunta_v in pergunta.items():  # pergunta_k: chave, pergunta_v: conteudo
    print(f'{pergunta_k}: {pergunta_v["pergunta"]}:')

    for alt, opc in pergunta_v['alternativas'].items():
        print(f'{alt}) {opc}')

    res = input('escolha uma alternativa: ')
    if res == pergunta_v['resposta']:  # Verifica ser a resposta está certa
        print('Alternatica correta\n')
        nota += 2
    else:
        print('Alternatica incorreta\n')

print('nota final: ', nota)
cont = input('Digite [Sim] se deseja visualizar a gararito: ')
if cont == 'Sim' or cont == 'sim':
    for pergunta_k, pergunta_v in pergunta.items():
        print(f'{pergunta_k}: {pergunta_v["resposta"]}')
