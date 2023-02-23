# Case Grupo Boticário

# Case 1

### Cenário Atual

Estamos passando por um processo de transformação digital, onde o seu papel será
definir a arquitetura de referência para plataforma de dados do Grupo Boticário e ser uma
referência técnica para engenheiros e analistas de dados.
No cenário atual, utilizamos SAP Hana como nosso repositório principal de data
warehouse. Existem processos de ETL que fazem ingestão de dados de 50 transacionais.
Mais de 90% das bases são de origem transacionais de diferentes DBMS’s (DB2, MS SQL
etc) e estão alocados em ambiente on-premises.
Além do SAP Hana, a empresa possui algumas aplicações hospedadas em nuvens
públicas como Microsoft Azure e Amazon Web Services.
Dentro da empresa, o tratamento e o consumo dos dados são tratados em silos, onde
diferentes unidades de negócios acabam utilizando diferentes ferramentas para processar,
analisar dados e apresentar dados. Algumas ferramentas que podemos citar como exemplo
são Jupyter Notebook, Qlick, Qlick Sense.
Outro aspecto importante está ligado a governança de dados, onde aspectos como
acesso a dados sensíveis, catalogação e permisionamento carecem de melhorias.

### O que a boticário espera ?

1. Definir uma arquitetura de referência com tecnologias de alguma nuvem
pública, preferencialmente AWS ou GCP. Considerando os seguintes
requisitos:
- Permear as camadas de ingestão, processamento, armazenamento, consumo,
análise, segurança e governança;
- Substituição gradativa do cenário on-premises atual;
- Incorporação de componentes e tecnologias que permitam a analisarmos dados
em tempo real;
- Que a arquitetura considere componentes que a habilitem a empresa organizar e
fornecer dados para diferentes fins, tais como: Analytics, Data Science, API’s e
serviços para integrações com aplicações. Ressaltando que necessariamente
precisaremos manter a comunicação on-premises x cloud para diversas
finalidades.

### Solução
![60f3cfa9-f5bd-4efe-a807-ff5b1832de53](https://user-images.githubusercontent.com/66088183/220826985-06e01541-f58a-41c2-b45d-70bb446b268e.jpeg)

# Case 2

Junto com este descritivo, você está recebendo 3 arquivos com dados aleatórios de
vendas de 2017 a 2019.
Para a execução deste teste, você pode utilizar as ferramentas que estiver mais
familiarizado, seguindo apenas as seguintes premissas:
1. Os dados necessariamente devem ser armazenados em tabelas de banco de
dados (MySQL, PostgreSQL, BigQuery, MS SQL, Oracle etc) e não em arquivos
ou planilhas;
2. Você deve necessariamente utilizar as linguagens SQL e Python nos
processos de carga, consulta e transformação dos dados;
3. Utilizar uma ferramenta que lhe permita criar os processos de ETL ou DAG’s
para ingestão e transformação de dados;
4. Você deve implementar um controle de versionamento para seus códigos.

### O que precisa ser feito:

Junto com este descritivo, você está recebendo 3 arquivos com dados aleatórios de
vendas de 2017 a 2019.
Para a execução deste teste, você pode utilizar as ferramentas que estiver mais
familiarizado, seguindo apenas as seguintes premissas:
1. Os dados necessariamente devem ser armazenados em tabelas de banco de
dados (MySQL, PostgreSQL, BigQuery, MS SQL, Oracle etc) e não em arquivos
ou planilhas;
2. Você deve necessariamente utilizar as linguagens SQL e Python nos
processos de carga, consulta e transformação dos dados;
3. Utilizar uma ferramenta que lhe permita criar os processos de ETL ou DAG’s
para ingestão e transformação de dados;
4. Você deve implementar um controle de versionamento para seus códigos.

### Desenvolvimento

Para o desenvolvimento para resolução desse case foi usado as ferramendas do Google Cloud: Pub/Sub, Cloud Function, BigQuery e Composer.

1. Cloud Composer fazendo a orquestração do processo iniciando mandando uma mensagem em um tópico no Pub/Sub e com isso iniciando a Cloud Function.
2. Cloud Function pegando os arquivos no Google Sheets e inserindo no BigQuery
3. E por fim, com Cloud Composer rodando uma procedure criando as tabelas consolidadas.

