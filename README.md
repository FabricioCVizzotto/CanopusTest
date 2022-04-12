Este é um projeto que visa ser avaliado pela empresa Canopus Online.

As tecnologias usadas foram python para o back-end e a framework django, 
que lida com a estruturação do CRUD pela sessão de ADMIN,
Criação de usuário ADMIN, gerenciamento de requests e urls, 
ORM para gerência do banco de dados utilizando python, 
entre outras funcionalidades de back-end.
Tendo em vista que não fora requisitado que estas funcionalidades não fossem auxiliadas por uma framework
tomei a liberdade de usar estas funcionalidades preset da ferramenta.
Portanto para que o sistema funcione é necessário que o host dele tenha instalado o python 3.10 instalado, e o django 4 (latest)
e utilizando o pip se instale os outros requisitos de back-end descritos no documento requirements.txt
usando o comando na pasta raiz do projeto:
python -m pip install -r requirements.txt
e em seguida o comando na pasta raiz do projeto:
python manage.py runserver
que disponibilizará o projeto no endereço localhost:8000 pelo browser da máquina host.

O banco de dados está anexo ao próprio projeto do git, bem como as imagens que usei de exemplo, para facilitar os testes.
O usuário padrão ficou estabelecido como sem necessidade de login.
O usuário administrador registrado em banco de dados é o de usuário admin, senha 123 estas configurações de segurança são
fracas mas como é um projeto apenas demonstrativo tomei a liberdade de utilizá-las.
acessível pela URL localhost:8000/admin/
Lá é possível realizar todas as operações de CRUD em imagens e carrosseis(que traduzi para o inglês como banners).

Para o front-end HTML, CSS e JS, que são tecnologias padrão, 
Como requisitado a funcionalidade do carrossel foi implementada inteiramente por CSS.
Considerei utilizar a Vue.js framework para adicionar mais reatividade no front-end,
mas como não agregaria na proposta principal do projeto optei por não usá-la.
