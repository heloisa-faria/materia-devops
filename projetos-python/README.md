# Anotações sobre python
- Atalhos de teclado:
    
    ctrl + l = limpa terminal
    
    botão windows + ponto = abre emojis
    
    Crtl + Shift + C - Abrir novo terminal

<br>

- Comandos no Terminal::
    
    cd - mudar o diretório (pasta).
    
    cp - copiar um arquivo.
    
    ls - listar os arquivos na pasta atual.
    
    mkdir - criar um diretório (nova pasta).
    
    rm - remover um arquivo.
    
    mv - mover um arquivo (pode ser usado também para renomear um arquivo).
    
    rmdir -remover um diretório (pasta).
    
    mv *nomedoarquivo.. -* mover para diretório (pasta) principal (por hierarquia).

<br>

- Modo interativo:
    
    atalhos no terminal →  
    
    $ python;
    
    $ executando o script com a flag -i (python -i app.py).
    
    $ exit() →  para sair 

<br>



# Informações a mais

Constante 

No python NÃO tem a palavras *const* ou *final* que são usadas para definir qual valor é constante (NÃO muda). Deve ser criada a variavel com o nome todo em LETRAS MAÍUSCULAS. 
<br>

Função range

    Recebe 3 argumentos: stop (obrigatorio), start(opcional) e step (opcional)

    range(stop) → range object

    range(start, stop{, step}) → range object
<br>

# Atalhos do Git

- Documentação
    - https://git-scm.com/docs/git/pt_BR
    - https://gitfluence.com/
    
    **git init** → inicializar um repositório Git
    
    **git add .** →
    
    **git commit -m”…” →**
    
    **git push origin main** → enviar alterações do repositório local para o remoto.
    
    **git pull** → git fetch + git merge;
    
    **git fetch** → baixa as alterações do repositorio remoto sem mesclar as branches.
    
    **giit merge** → mescla as alterações da branch local com a branch remota.
    
    **git log** → 
    
    **git diff** → ver as diferenças entre as branches.
    
    **git clone** → clona o repositorio; cria uma cópia de um repositório Git existente.
    
    **git clone** **<url> --branch <nome-da-branch> --single-branch** → para clonar apenas uma branch.
    
    **git status** → 
    
    **git stash** → 
    
    **git list** →
    
    **git restore** → 
    
    **git checkout** → alternar entre branches.
    
    **git config --global user.email [seuemail@exemplo.com](mailto:seuemail@exemplo.com)** → utilizado para configurar o email no Git.
    
    **git commit --amend –m"nova mensagem"** → alterar a mensagem de um commit.