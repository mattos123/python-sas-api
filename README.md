# Python SaS API Example - CryptoLens<br />
Exemplo de validação de licenciamento via api cryptolens em python, com interface grafica em pyqt5<br />
<br />
Dependências<br />
licensing<br />
pyinstaller<br />
pyqt5<br />
base64<br />
<br />
O código que compartilho, funciona da seguinte forma, tentamos obtemos retorno da auteticação (rsa x auth x numero de licença), a licença sendo validada, atraves do retorno, permitimos acesso a proxima tela do software (MainWindow), salvamos o texto contido no campo referente a "licença" na interface interativa, e carregamos o valor salvo, toda vez que o programa é aberto. Evitando retrabalho para o usuario. Aprofundando-se na documentacao da cryptolens, você encontrara exemplos de como armazenar licenças para que não seja necessário consumir a api frequentemente, voce pode armazenar informações sobre o licenciamento e reconsultar a api dentro de um intervalo de tempo.
<br />

Crie sua conta no ambiente gestor de licenciamentos, cryptolens. <br />
https://app.cryptolens.io/Account/Register<br />
![image](https://user-images.githubusercontent.com/21156270/229330592-b96bba14-9f8b-401d-b0c0-883bce982173.png)<br />
Após validar sua conta, efetue login e navegue até “Create new product”<br />
![image](https://user-images.githubusercontent.com/21156270/229330597-cd84fdb5-2b09-44a8-8dac-d19bfa8c46b1.png)<br />
Preencha as informações sobre seu produto (software) e clique em “Create”<br />
![image](https://user-images.githubusercontent.com/21156270/229330604-a851a325-9c07-4134-b0b5-9ead7300bfec.png)<br />
Após criar seu produto, entre na página dele para configura-lo, e gerar uma chave<br />
![image](https://user-images.githubusercontent.com/21156270/229330613-e0511f1f-1f56-4a0a-865e-ad1102707875.png)<br />
Com estas configurações básicas, você garante que o cliente seja associado ao produto, após ativar a licença via api, que o tempo concedido pela licença, começará a diminuir após a ativação somente<br />
![image](https://user-images.githubusercontent.com/21156270/229330628-e556ee63-8746-466f-b8ae-69c92f83bd90.png)<br />
Após gerar a licença, clique sobre ela para definirmos alguns parâmetros<br />
![image](https://user-images.githubusercontent.com/21156270/229330766-13b54df1-d6a9-46b5-8a40-e6e662a8bba7.png)<br />
Defina a quantidade de acessos e clique em salvar( defina no mínimo 1), modalidade de licenciamento, e acesso à funções especiais vinculadas a licença<br />
![image](https://user-images.githubusercontent.com/21156270/229330779-64412c25-cb4e-480d-9d6f-09815b077a43.png)<br />
Desta seguinte forma, concluímos a configuração do licenciamento.<br />
![image](https://user-images.githubusercontent.com/21156270/229330786-f6561aa6-fa97-4218-a531-07ab283d3d1f.png)<br />
Temos 1 chave, com permissão de uso em 1 dispositivo, que expira em 1 mês após a ativação, e tem acesso a uma função da licença, “ativação”, você pode criar funções no seu codigo final, que permite acesso somente com permissão através dos “features” da licença acima mencionada, exemplo<br />
Modulo fiscal = f4<br />
A licença tem acesso a f1,f2,f3<br />
Se o usuário tentar acessar o modulo fiscal, a api irá retornar que o f4 = False, assim negando acesso a funcionalidade <br />
Agora definiremos as chaves de acesso e produto, no nosso codigo.<br />
Acesse “security settings”<br />
![image](https://user-images.githubusercontent.com/21156270/229330799-dc01ebfa-c473-4455-8e01-0b8ebaf20899.png)<br />
Copie o conteúdo da sua chave RSA e cole o conteúdo no codigo licensa.py no campo da variável “RSAPubKey” <br />
![image](https://user-images.githubusercontent.com/21156270/229330809-202799d7-b75b-4bbe-ad56-6b3969f63523.png)<br />
Agora acesse “Acess tokens”<br />
![image](https://user-images.githubusercontent.com/21156270/229330819-c72175eb-3c58-4d58-9e94-0bc877d9f3c0.png)<br />
Clique em “Create new acess token”<br />
![image](https://user-images.githubusercontent.com/21156270/229330828-e31e2da5-3aec-4b6a-b392-bec97a8db632.png)<br />
Crie um nome para o token de acesso defina no mínimo a função “activate”, vincule o token de acesso ao produto, e salve<br />
![image](https://user-images.githubusercontent.com/21156270/229330835-07a042e0-1712-4a94-848f-528ae4053098.png)<br />
Pronto, token criado, copie o token gerado<br />
![image](https://user-images.githubusercontent.com/21156270/229330848-dcc3f67a-88cf-47ff-a960-42fb77c48e9f.png)<br />
Copie seu token e cole o conteúdo no codigo licensa.py no campo da variável “auth” <br />
![image](https://user-images.githubusercontent.com/21156270/229330863-100a3b87-3805-4092-bd12-0f2820f3deac.png)<br />
Agora entre em produtos, e selecione seu produto.<br />
![image](https://user-images.githubusercontent.com/21156270/229330866-6b24dd2b-670f-4e8e-82e6-1d7008c5836e.png)<br />
Copie o codigo do seu produto, para o campo da variável “prod_id”<br />
Compilando.<br />
Agora que temos as variáveis definidas dentro do nosso codigo de validação de licenciamento, podemos compilar nossa interface.<br />
Abra o arquivo interface.py em algum terminal de seu ambiente, e envie o comando <br />
pyinstaller --noconsole --onefile interface.py<br />
Aguarde o compilador carregador os nodes utilizados das bibliotecas para um único arquivo executável junto com nosso codigo<br />
![image](https://user-images.githubusercontent.com/21156270/229330872-3727d9c3-e4c3-43e4-806b-ae5992b8d9d2.png)<br />
Codigo fonte compilado, agora temos o executável. Você ira encontrar o executável dentro da pasta “dist” <br />
![image](https://user-images.githubusercontent.com/21156270/229330881-d61bb19e-1508-4415-9854-614a14b2bc1b.png)<br />
![image](https://user-images.githubusercontent.com/21156270/229330997-5f8a4336-1b45-4b37-9fce-7d4f121afb15.png)<br />
Com software pronto. Voltamos ao ambiente cryptolens, e acessamos o painel de clientes,<br />
Quando geramos a licença, dentro do cadastro do produto, informamos um cliente, que ira utilizar a licença.<br />
Esse cliente, fica cadastrado no portal “Customers”<br />
![image](https://user-images.githubusercontent.com/21156270/229330887-e77097ca-05b5-4456-8670-b9622055e20a.png)<br />
Abra o perfil do “Cliente” que você cadastrou junto com a licença.<br />
![image](https://user-images.githubusercontent.com/21156270/229330892-4d9355d4-ab29-4709-9bec-b8c24d0d3d6d.png)<br />
Copie o link do cliente, e envie para seu cliente, poder se cadastrar, se vincular ao licenciamento, e receber a sua licença<br />
Agora, com todos os passos, seguidos corretamente, o cliente ira obter sua chave, e inserir no momento que abre o software.<br />
![image](https://user-images.githubusercontent.com/21156270/229330898-07fa5400-b263-4421-991b-4d502c83dfdd.png)<br />
A partir de agora fica a cargo da sua criatividade utilizar este recurso em seu codigo, implemente-o de tal maneira que atenda sua necessidade.<br />
![image](https://user-images.githubusercontent.com/21156270/229330902-d320e5cb-3cfb-4c32-b144-c2f3070d363a.png)<br />
Após o cliente ativar a licença, você poderá gerenciar através do portal da cryptolens <br />
![image](https://user-images.githubusercontent.com/21156270/229330908-deafdd29-eb55-4d7f-9d73-6c16bc013ae1.png)<br />
Através do portal você poderá gerar formulários de renovação de mensalidade, receber pagamentos via alguns gateways de pagamentos disponíveis na plataforma (paypal etc..)





