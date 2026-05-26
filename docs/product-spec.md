# NeuroRelatorio Pro - Especificacao do Produto

## 1. Resumo executivo

O NeuroRelatorio Pro e uma plataforma web para neuropsicopedagogos clinicos e institucionais organizarem atendimentos, avaliacoes, triagens, sondagens, intervencoes e documentos tecnicos. O sistema centraliza cadastro do avaliado, anamnese, sessoes, protocolos, matriz de habilidades, evidencias, planos de intervencao, devolutivas e relatorios exportaveis em PDF/DOCX.

A diretriz fundamental e que o produto nao substitui julgamento profissional. Ele estrutura dados, alerta lacunas, organiza evidencias e apoia a escrita tecnica, mas bloqueia finalizacao automatica sem revisao humana, identificacao do responsavel tecnico e verificacoes eticas.

## 2. Escopo do produto

### Incluido no MVP

- Cadastro de avaliados, responsaveis, escola, profissionais externos e documentos.
- Anamnese neuropsicopedagogica extensivel.
- Registro de sessoes de avaliacao, triagem, sondagem, intervencao e acompanhamento.
- Banco de protocolos com alertas de validade, licenca, faixa etaria, autorizacao e SATEPSI.
- Matriz de habilidades avaliadas por dominio.
- Abas preenchiveis com opcoes pre-definidas, permitindo tambem adicionar `campo44` quando o profissional precisar registrar um dado nao previsto.
- Gerador de relatorio com versoes preliminar/final.
- Plano de intervencao individual e institucional.
- Devolutivas para familia, escola e equipe multiprofissional.
- Trilhas de auditoria, consentimento, controle de acesso e exportacao segura.

### Fora do escopo

- Diagnostico automatico.
- Emissao de CID.
- Aplicacao ou reproducao de testes psicologicos privativos.
- Armazenamento de manuais protegidos sem licenca.
- Promessa de resultado, prognostico taxativo ou conclusao sem evidencias registradas.

## 3. Base etica e legal

O sistema deve incorporar alertas e bloqueios baseados em:

- Codigo de Etica Tecnico-Profissional da Neuropsicopedagogia da SBNPp, especialmente delimitacao clinica/institucional, habilitacao profissional, limites de instrumentos e encaminhamento quando necessario.
- LGPD, com atencao reforcada a dados sensiveis, criancas e adolescentes, finalidade, necessidade, transparencia, seguranca, consentimento e controle de acesso.
- SATEPSI/CFP para verificacao de instrumentos psicologicos, privativos, nao privativos, favoraveis, desfavoraveis ou nao avaliados.
- Sigilo profissional, revisao humana obrigatoria e manutencao de evidencias.

Fontes verificadas: [Resolucao SBNPp n. 05/2021](https://www.sbnpp.org.br/arquivos/Codigo_de_Etica_Tecnico_Profisisonal_da_Neuropsicopedagogia_-_SBNPp_-_2021.pdf), [SATEPSI/CFP](https://satepsi.cfp.org.br/), [ANPD sobre criancas e adolescentes](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-divulga-enunciado-sobre-o-tratamento-de-dados-pessoais-de-criancas-e-adolescentes) e [portal gov.br de LGPD](https://www.gov.br/pt-br/lgpd/lei-geral-de-protecao-de-dados-lgpd).

## 4. Base de conhecimento neuropsicopedagogica

A base inicial de protocolos fica em `apps/api/app/seed/protocols.json` e usa os campos:

- nome;
- area avaliada;
- objetivo;
- faixa etaria/serie;
- tipo;
- contexto;
- profissional autorizado;
- restricao de uso;
- nivel de acesso: aberto, nao privativo, privativo ou exige verificacao no SATEPSI;
- referencia bibliografica;
- observacoes tecnicas;
- politica de anexo de manual/licenca;
- politica de lancamento de resultados/escores.

Regra central: o sistema guarda resultados inseridos pelo profissional, mas nao reproduz itens, crivos, manuais ou materiais protegidos.

## 5. Modulos do sistema

### Dashboard

Exibe indicadores agregados: total de avaliados, avaliacoes em andamento, relatorios pendentes, sessoes, consentimentos vencidos, documentos incompletos e alertas sem expor dados sensiveis indevidos.

### Cadastro do avaliado

Inclui identificacao, escola, serie, turno, responsaveis legais, contatos, profissionais externos, queixa principal, encaminhamento, consentimentos e anexos.

### Anamnese

Formulario extenso: motivo da avaliacao, gestacao, desenvolvimento neuropsicomotor, linguagem, historico medico/familiar/escolar, alfabetizacao, sono, alimentacao, rotina, telas, socializacao, comportamento, atencao, memoria, autonomia, motricidade, relacao familia-escola, intervencoes anteriores, medicamentos informados, encaminhamentos e documentos.

Todas as abas preenchiveis da anamnese devem apresentar opcoes pre-definidas para agilizar o preenchimento, padronizar linguagem tecnica e reduzir omissoes. Cada aba tambem deve permitir a inclusao de `campo44`, usado como campo adicional configuravel pelo profissional quando as opcoes existentes forem insuficientes. O `campo44` deve registrar rotulo, tipo de resposta, valor informado, fonte da informacao e justificativa de inclusao.

### Sessoes

Cada sessao registra data, duracao, objetivo, protocolo, atividade, comportamento, engajamento, mediacao, estrategias, respostas, resultados quantitativos/qualitativos, evidencias, observacoes e proximos passos.

Todas as abas preenchiveis de sessoes devem conter opcoes pre-definidas para objetivo, tipo de atividade, comportamento observado, nivel de mediacao, engajamento, resultados qualitativos e proximos passos. A opcao `Adicionar campo44` deve estar disponivel em cada aba para dados complementares nao contemplados no modelo-base.

### Banco de protocolos

Permite cadastrar, editar, ativar, desativar, categorizar e bloquear uso inadequado de instrumentos restritos.

### Matriz de habilidades

Mapeia dominios como atencao, memoria, linguagem, leitura, escrita, matematica, funcoes executivas, motricidade, orientacao, motivacao, comportamento, interacao social e autonomia academica.

### Gerador de relatorio

Gera versoes preliminares a partir de dados registrados, separando fato, interpretacao, hipotese, recomendacao e limitacao. Exportacao so ocorre apos validacao.

### Modelos de relatorio

Inclui relatorio clinico completo, triagem, sondagem escolar, institucional, acompanhamento, evolucao, devolutivas, plano individual e plano institucional.

Todas as abas preenchiveis dos modelos de relatorio devem conter campos com opcoes pre-definidas e a opcao `Adicionar campo44`. O assistente de escrita so pode usar valores selecionados, textos inseridos pelo profissional ou dados do `campo44` explicitamente preenchidos e vinculados a fonte/evidencia.

### Assistente de escrita

Sugere redacao tecnica ou acessivel, destaca lacunas, nao inventa dados, exige fontes registradas e revisao humana.

Quando encontrar `campo44`, o assistente deve trata-lo como dado informado pelo profissional, citando a aba de origem e a fonte registrada. Se `campo44` estiver vazio, o assistente deve ignora-lo e nao preencher o conteudo por inferencia.

### Seguranca e LGPD

Aplica autenticacao, RBAC, logs, consentimento, criptografia, politicas de retencao, compartilhamento controlado, anonimização e registro de finalidade.

## 6. Banco de dados

O modelo relacional proposto esta em `docs/data-model.md`. O banco principal recomendado e PostgreSQL, com armazenamento externo seguro para anexos e exportacoes.

Entidades centrais:

- usuarios, profissionais, perfis e organizacoes;
- avaliados, responsaveis, escola e contatos;
- consentimentos, documentos e anexos;
- anamneses, sessoes, protocolos e resultados;
- matriz de habilidades e achados por dominio;
- relatorios, versoes, aprovacoes e exportacoes;
- planos de intervencao;
- logs de auditoria e eventos de IA.

## 7. Fluxo operacional

1. Administrador configura organizacao, perfis, termos e politicas.
2. Profissional cadastra avaliado e responsaveis.
3. Sistema exige consentimento e finalidade antes de registros sensiveis.
4. Profissional preenche abas usando opcoes pre-definidas e, quando necessario, adiciona `campo44` com fonte e justificativa.
5. Profissional preenche anamnese e documentos apresentados.
6. Profissional agenda e registra sessoes.
7. Protocolos sao selecionados com alerta de autorizacao, manual e SATEPSI.
8. Resultados sao lancados como observacao direta, relato familiar, relato escolar ou instrumento.
9. Matriz de habilidades consolida achados e evidencias.
10. Assistente sugere texto sem inventar dados.
11. Profissional revisa, edita, assina e aprova.
12. Sistema gera versao final e exportacao segura.
13. Toda alteracao fica auditada.

## 8. Modelos de relatorio

Os modelos-base estao em `docs/report-templates.md` e seguem a estrutura:

- identificacao;
- dados do profissional;
- solicitante/encaminhamento;
- objetivo;
- queixa;
- procedimentos;
- historico relevante;
- observacoes;
- resultados por dominio;
- interpretacao neuropsicopedagogica;
- hipoteses;
- potencialidades e dificuldades;
- impactos na aprendizagem;
- recomendacoes;
- encaminhamentos;
- limitacoes;
- conclusao revisada;
- local, data, assinatura e registro quando aplicavel.

## 9. Seguranca/LGPD

Politica completa em `docs/security-lgpd.md`.

Controles minimos:

- autenticacao forte;
- perfis e permissoes granulares;
- criptografia em transito e repouso;
- segregacao por organizacao/tenant;
- consentimento de responsavel legal para menores quando aplicavel;
- minimizacao de dados;
- auditoria imutavel;
- revisao de acesso periodica;
- exportacao com marca d'agua opcional;
- expiracao de links compartilhados;
- plano de resposta a incidente.

## 10. Stack tecnica

Recomendacao inicial:

- Frontend: Next.js, React, TypeScript.
- Backend: FastAPI, Python, Pydantic.
- Banco: PostgreSQL.
- Arquivos: S3/MinIO com criptografia e politica de retencao.
- Autenticacao: JWT/OAuth2 com MFA em producao.
- Documentos: geracao DOCX via templates e PDF por pipeline de renderizacao.
- IA: API isolada por camada de seguranca, sem acesso direto irrestrito aos dados.
- Observabilidade: logs estruturados, trilhas de auditoria e metricas tecnicas sem dados sensiveis.

## 11. Codigo inicial

O starter inclui:

- API FastAPI com endpoints de saude, protocolos e validacao de relatorio.
- Seeds de protocolos e matriz de habilidades.
- Regras de dominio para bloqueios eticos.
- Prototipo Next.js do dashboard e fluxos principais.
- Docker Compose para PostgreSQL e MinIO.

## 12. Proximos passos

1. Validar juridicamente termos, consentimentos e politica de privacidade.
2. Definir cadastro profissional e comprovacao de habilitacao.
3. Implementar autenticação real, multi-tenant e banco PostgreSQL.
4. Criar editor de anamnese e sessoes.
5. Implementar gerador DOCX/PDF com templates auditaveis.
6. Criar camada de IA com prompt seguro, RAG do caso e trilha de revisao.
7. Executar testes com profissionais em ambiente controlado.
