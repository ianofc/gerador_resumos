Gerador de Resumos

Uma aplicação web simples desenvolvida em Python com Flask que utiliza a API da OpenAI (ChatGPT) para gerar resumos de textos automaticamente. Ideal para estudantes, profissionais e pesquisadores que precisam sintetizar informações rapidamente.



Funcionalidades

Envio de textos ou documentos para resumo.

Geração de resumos claros e objetivos com base em IA.

Interface simples e fácil de usar.

Integração com a API da OpenAI para processamento de linguagem natural.



Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

Python 3.x instalado.

Conta na OpenAI e uma chave de API válida para acessar o ChatGPT.

As bibliotecas necessárias instaladas:

pip install flask openai




Como usar

1. Clone o repositório:

git clone https://github.com/seuusuario/gerador_resumos.git


2. Navegue até o diretório do projeto:

cd gerador_resumos


3. Configure a chave da API da OpenAI:

Crie um arquivo .env no diretório raiz e adicione:

OPENAI_API_KEY=sua-chave-da-api-aqui



4. Execute a aplicação:

python app.py


5. Acesse a aplicação no navegador em http://127.0.0.1:5000.


6. Insira o texto ou envie um documento e clique em "Gerar Resumo" para receber o resultado.





Tecnologias utilizadas

Python: Linguagem principal.

Flask: Framework web para criação da API.

OpenAI API: Para integração com o modelo ChatGPT.



Estrutura do Projeto

app.py: Código principal da aplicação Flask.

templates/: Contém os arquivos HTML para a interface web.

index.html: Página principal da aplicação.


static/: Diretório para arquivos estáticos (CSS, JS, imagens).




Melhorias Futuras

Suporte para mais formatos de documentos (PDF, DOCX).

Opção de personalização do nível de detalhamento do resumo.

Integração com ferramentas de produtividade, como Google Docs ou Notion.

Armazenamento de textos e resumos em um banco de dados (PostgreSQL).



Contribuições

Contribuições são bem-vindas! Se tiver sugestões ou melhorias, abra uma issue ou envie um pull request.

