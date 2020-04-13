#! python


def tag_bloco(texto, classe="sucess"):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Realização de Testes (Assertions)
    assert tag_bloco('Incluido com Sucesso!') == \
        '<div class="sucess">Incluido com Sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
    print(tag_bloco('bloco'))
