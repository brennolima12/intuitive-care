Testes de Nivelamento da Intuitive Care, sendo 4 testes e uma pasta para cada.

Na pasta 1, tem o script que faz o download dos anexos solicitados pelo link, e faz a sua compactação, deixando o arquivo zip na própria pasta.

Na pasta 2, tem o script extrai os dados do pdf indicado, fazendo a transformação para um arquivo csv com os dados e depois faz sua compactação, 
também deixando o arquivo zip na própria pasta.

Na pasta 3, tem o script em MySQL que normalizada o endcoding, cria tabelas com os dados solicitados e também tem as queries para o que foi solicitado de busca. 
Necessário usar MySQL para rodar os scripts, pois são arquivos sql.

Na pasta 4, tem a API, integrada ao banco de dados criado para o teste 3, nela se tem 2 endpoints, uma para listar os dados do arquivo passado da questão anterior, 
e o endpoint da busca pedida no 4.2. Além disso na pasta teste tem o frontend pedido, em vue.js.

Para finalizar o link da coleção de postman pedidos no teste 4: 
https://brennolima.postman.co/workspace/Brenno-Lima's-Workspace~fc7bde8c-7d2d-403a-8e9f-0c1f5367bab8/collection/43707170-0839667e-b1fb-4954-bd2f-cfbaf4f212f3?action=share&creator=43707170
