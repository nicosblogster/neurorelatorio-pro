# NeuroRelatorio Pro

Plataforma web inicial para organizacao, avaliacao, intervencao e emissao de relatorios neuropsicopedagogicos com revisao humana obrigatoria.

Este repositorio nasce como um starter arquitetural: documentacao de produto, base de conhecimento inicial, regras de negocio sensiveis, backend FastAPI e prototipo textual em Next.js.

## Principios do produto

- O sistema apoia o profissional, mas nao diagnostica sozinho.
- A IA nao inventa historico, resultados, escores, hipoteses ou encaminhamentos.
- Todo relatorio exige revisao e aprovacao do profissional responsavel.
- Instrumentos restritos, privativos ou dependentes de licenca/manual devem ser bloqueados ou alertados conforme perfil e autorizacao.
- Dados de criancas, adolescentes e informacoes de saude/aprendizagem sao tratados como dados sensiveis ou de protecao reforcada.

## Estrutura

```text
neurorelatorio-pro/
  apps/
    api/        Backend FastAPI com regras de dominio e seeds iniciais
    web/        Prototipo Next.js do painel profissional
  docs/         Especificacao, arquitetura, LGPD, modelos e roadmap
  docker-compose.yml
  .env.example
```

## Instalacao rapida

### Streamlit

Versao recomendada para publicar rapidamente a ferramenta a partir do GitHub.

```powershell
cd C:\projetos\neurorelatorio-pro
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Abra `http://localhost:8501`.

Para publicar no Streamlit Community Cloud:

1. Envie este repositorio para o GitHub.
2. Acesse `https://share.streamlit.io/`.
3. Escolha o repositorio `nicosblogster/neurorelatorio-pro`.
4. Em **Main file path**, informe `streamlit_app.py`.
5. Clique em deploy.

### Backend

```powershell
cd C:\projetos\neurorelatorio-pro\apps\api
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Abra `http://localhost:8000/docs`.

Endpoints iniciais relevantes:

- `GET /reports/fillable-tabs`: lista todas as abas preenchiveis com opcoes pre-definidas e suporte a `campo44`.
- `POST /reports/fillable-tabs/validate`: valida se o preenchimento usa apenas opcoes permitidas e se `campo44` possui rotulo, tipo, valor, fonte e justificativa.

Exemplo de payload: `examples/fillable_tabs_submission.json`.

### Frontend

O repositorio tambem inclui um prototipo estatico inicial em `apps/web` para validar as abas preenchiveis sem instalar dependencias:

```powershell
cd C:\projetos\neurorelatorio-pro\apps\web
py -3 -m http.server 3000
```

Abra `http://localhost:3000`.

Fluxo disponivel no prototipo:

- todas as abas de relatorio com opcoes pre-definidas;
- opcao `Adicionar campo44` em cada aba;
- exigencia de rotulo, valor, fonte e justificativa para `campo44`;
- previa textual do rascunho;
- copia do rascunho e exportacao JSON.

Quando o frontend Next.js for scaffoldado, manter o mesmo contrato de dados de `apps/api/app/seed/fillable_tabs.json`.

Planejado para a versao Next.js:

```powershell
cd C:\projetos\neurorelatorio-pro\apps\web
npm install
npm run dev
```

Abra `http://localhost:3000`.

## Documentos principais

- [Especificacao do produto](docs/product-spec.md)
- [Arquitetura tecnica](docs/architecture.md)
- [Modelo de dados](docs/data-model.md)
- [Seguranca e LGPD](docs/security-lgpd.md)
- [Modelos de relatorio e intervencao](docs/report-templates.md)
- [Roadmap](docs/roadmap.md)

## Nota clinica e juridica

Esta base e um apoio de engenharia e redacao tecnica. A validacao final deve ser feita por profissional habilitado, considerando legislacao vigente, normas profissionais aplicaveis, manuais, licencas, SATEPSI quando pertinente e limites de atuacao neuropsicopedagogica.
