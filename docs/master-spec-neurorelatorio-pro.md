# NeuroRelatorio Pro - Especificacao Mestre Segura

## 1. Resumo executivo

O NeuroRelatorio Pro e uma plataforma web profissional para organizacao de casos, registros de avaliacao, triagem, sondagem, acompanhamento, intervencao e emissao de documentos neuropsicopedagogicos. O produto deve apoiar o neuropsicopedagogo clinico ou institucional na estruturacao de dados e na redacao tecnica, sem substituir julgamento profissional, sem diagnosticar automaticamente, sem emitir CID, sem aplicar testes psicologicos privativos e sem reproduzir materiais protegidos.

O sistema deve operar sempre com revisao humana obrigatoria e com separacao explicita entre:

- achados observados;
- indicadores compativeis com;
- hipoteses neuropsicopedagogicas;
- necessidade de encaminhamento;
- limitacoes da avaliacao;
- conclusao tecnica revisada pelo profissional.

## 2. Escopo do produto

### Incluido

- Cadastro de avaliados, responsaveis, escola, profissionais externos e historico.
- Anamnese neuropsicopedagogica estruturada.
- Registro de sessoes de avaliacao, triagem, sondagem, intervencao e acompanhamento.
- Banco de instrumentos/protocolos com alertas de restricao, validade, faixa etaria, licenca e SATEPSI.
- Matriz de habilidades avaliadas.
- Gerador de relatorios, devolutivas e planos de intervencao.
- Exportacao PDF/DOCX.
- Versionamento, auditoria, consentimento, controle de acesso e seguranca.
- Assistente de escrita limitado aos dados registrados, com citacao de campos usados e revisao humana.

### Fora do escopo

- Diagnostico automatico.
- Emissao de CID.
- Aplicacao automatica de testes psicologicos privativos.
- Reproducao de manuais, crivos, itens protegidos ou materiais licenciados.
- Relatorio final sem profissional responsavel.
- Uso com dados reais em ambiente publico sem autenticacao, contrato, politica de privacidade e controles de seguranca.

## 3. Base etica e legal

### Fontes consideradas

- Codigo de Etica Tecnico-Profissional da Neuropsicopedagogia da SBNPp, Resolucao n. 05/2021.
- SATEPSI/CFP e Resolucao CFP n. 31/2022 para avaliacao psicologica e classificacao de instrumentos.
- LGPD, Lei n. 13.709/2018, especialmente dados sensiveis, finalidade, necessidade, seguranca, transparencia e dados de criancas/adolescentes.
- Orientacoes da ANPD sobre tratamento de dados de criancas e adolescentes.

### Riscos criticos

| Risco | Impacto | Controle obrigatorio |
| --- | --- | --- |
| Sistema induzir diagnostico automatico | Alto | Bloqueio de CID/conclusao automatica; revisao humana obrigatoria |
| Uso indevido de instrumentos restritos | Alto | Cadastro de restricao, perfil autorizado, alerta SATEPSI e bloqueio |
| Vazamento de dados sensiveis | Alto | Criptografia, RBAC, logs, backup, minimizacao e retencao |
| Dados de menores sem responsavel legal | Alto | Consentimento/base legal e responsavel obrigatorios |
| IA inventar historico, escore ou recomendacao | Alto | IA somente com dados do caso, citacao de fonte e bloqueio de campos ausentes |
| Campo livre excessivo | Medio/alto | `additional_fields` com rotulo, tipo, valor, fonte e justificativa obrigatorios |

## 4. Base de conhecimento neuropsicopedagogica

### Estrutura do cadastro de instrumentos/protocolos

Campos obrigatorios:

- nome;
- area avaliada;
- objetivo;
- faixa etaria/serie;
- tipo: triagem, sondagem, avaliacao, intervencao, observacao, entrevista, escala, questionario;
- contexto: clinico, institucional ou ambos;
- profissional autorizado;
- restricao de uso;
- nivel de acesso: aberto, nao privativo, privativo, exige verificacao SATEPSI;
- referencia bibliografica;
- observacoes tecnicas;
- politica de manual/licenca;
- politica de resultados/escores;
- status: ativo/inativo;
- data da ultima verificacao.

### Base inicial

Todos os itens abaixo devem exibir o alerta: "Verifique manual, licenca, faixa etaria, padronizacao, autorizacao de uso e SATEPSI antes da aplicacao."

1. Anamnese neuropsicopedagogica.
2. Entrevista inicial com responsaveis.
3. Entrevista com escola/professores.
4. Observacao clinica.
5. Observacao institucional.
6. Observacao ludica.
7. Observacao comportamental.
8. EOCA.
9. Provas operatorias piagetianas, quando cabiveis e permitidas.
10. Sondagens de leitura, escrita, matematica, consciencia fonologica, funcoes executivas, atencao, memoria, linguagem oral, coordenacao motora e psicomotricidade.
11. IAR, CONFIAS, TDE/TDE II, PROLEC, PROLEC-SE, PROCOMLE, PROADE, Pro-Ortografia, APET, Prohfon, CORUJA-PROMAT.
12. Avaliacao Neuropsicologica Cognitiva - Atencao e Funcoes Executivas, observando restricoes.
13. EME-IJ, EAVAP-EF, DCDQ, Ficha de Acompanhamento do Desempenho Motor, GMFM quando aplicavel e por profissional habilitado.
14. Protocolos de compreensao leitora, producao textual, desempenho ortografico, raciocinio logico-matematico, lateralidade, esquema corporal, orientacao temporal/espacial.
15. Protocolos de rastreio de dificuldades de aprendizagem, comportamento adaptativo, autorregulacao, rotina escolar, habitos de estudo e funcoes executivas.
16. Protocolos de intervencao individual, institucional e devolutivas familiar/escolar.

## 5. Modulos do sistema

### Dashboard

Indicadores agregados sem exposicao indevida: avaliados ativos, avaliacoes em andamento, relatorios pendentes, sessoes, consentimentos vencidos, documentos incompletos e alertas de instrumentos.

### Cadastro do avaliado

Identificacao, data de nascimento, idade automatica, sexo quando necessario, escola, serie, turno, responsaveis legais, contatos, profissionais externos, queixa principal, encaminhamento, consentimentos e anexos.

### Anamnese

Formulario extenso: identificacao, motivo, gestacao, desenvolvimento neuropsicomotor, linguagem, historico medico/familiar/escolar, alfabetizacao, sono, alimentacao, rotina, telas, socializacao, comportamento, atencao, memoria, autonomia, motricidade, relacao familia-escola, intervencoes, medicamentos informados, encaminhamentos e documentos.

### Sessoes

Data, duracao, objetivo, protocolo, atividade, comportamento, engajamento, mediacao, estrategias, respostas, resultados quantitativos/qualitativos, evidencias, observacoes e proximos passos.

### Banco de protocolos

CRUD de instrumentos/protocolos, categorizacao, status, alertas, bloqueios por perfil e registro de verificacao.

### Matriz de habilidades

Atencao seletiva/sustentada/alternada, memorias, linguagem, consciencia fonologica, leitura, fluencia, compreensao, escrita, ortografia, producao textual, matematica, raciocinio logico, funcoes executivas, flexibilidade, controle inibitorio, planejamento, organizacao, autorregulacao, motricidades, lateralidade, orientacao espacial/temporal, coordenacao visuomotora, motivacao, estrategias de aprendizagem, comportamento em tarefa, interacao social e autonomia academica.

### Gerador de relatorio

Editor por blocos, versao preliminar/final, citacao de evidencias, limitacoes obrigatorias, revisao humana, assinatura e exportacao PDF/DOCX.

### Assistente de escrita

IA limitada a redacao assistiva. Regras: nao inventar dados, nao diagnosticar, nao emitir CID, separar fato/interpretacao/hipotese, destacar lacunas, sugerir encaminhamento quando extrapolar a area e exigir aprovacao.

## 6. Banco de dados

### Entidades principais

- organizations
- users
- professional_profiles
- assessees
- guardians
- schools
- external_professionals
- consents
- documents
- anamneses
- sessions
- protocols
- protocol_results
- skill_domains
- skill_findings
- reports
- report_versions
- intervention_plans
- feedback_documents
- fillable_tab_templates
- fillable_tab_entries
- audit_logs
- ai_events
- exports

### Tabelas essenciais

| Tabela | Finalidade |
| --- | --- |
| assessees | Dados do avaliado, com campos sensiveis criptografados |
| guardians | Responsaveis legais e contato |
| consents | Base legal, finalidade, validade, revogacao |
| anamneses | Secoes estruturadas e fontes |
| sessions | Registro de atendimentos e evidencias |
| protocols | Banco de instrumentos/protocolos |
| protocol_results | Resultados lancados pelo profissional |
| skill_findings | Achados por habilidade e evidencias |
| reports | Metadados do relatorio |
| report_versions | Conteudo versionado |
| fillable_tab_entries | Opcoes selecionadas e `additional_fields` |
| audit_logs | Trilha imutavel de acesso/alteracao/exportacao |

## 7. Fluxo operacional

1. Administrador configura organizacao, perfis, termos, retencao e politicas.
2. Profissional cadastra avaliado, responsaveis e finalidade.
3. Sistema exige consentimento/base legal quando aplicavel.
4. Profissional registra anamnese e documentos.
5. Profissional cria sessoes e vincula evidencias.
6. Protocolos sao selecionados com alertas e bloqueios.
7. Resultados sao lancados pelo profissional.
8. Matriz de habilidades consolida achados.
9. Relatorio preliminar e gerado por blocos.
10. IA pode sugerir texto apenas com base nos campos registrados.
11. Profissional revisa, corrige, aprova e assina.
12. Sistema exporta versao final e registra auditoria.

## 8. Modelos de relatorio

### Relatorio neuropsicopedagogico completo

1. Identificacao.
2. Dados do profissional.
3. Solicitante/encaminhamento.
4. Objetivo.
5. Queixa principal.
6. Procedimentos.
7. Instrumentos/protocolos.
8. Historico relevante.
9. Observacoes comportamentais.
10. Analise por dominio.
11. Resultados qualitativos.
12. Resultados quantitativos.
13. Interpretacao neuropsicopedagogica.
14. Hipoteses levantadas.
15. Potencialidades.
16. Dificuldades observadas.
17. Impactos na aprendizagem.
18. Recomendacoes a familia, escola, professor e intervencao.
19. Encaminhamentos.
20. Limitacoes.
21. Conclusao revisada.
22. Local, data, assinatura e registro/associacao quando aplicavel.

### Outros modelos

- Triagem neuropsicopedagogica.
- Sondagem escolar.
- Institucional.
- Acompanhamento.
- Evolucao.
- Devolutiva familiar.
- Devolutiva escolar.
- Plano de intervencao individual.
- Plano de intervencao institucional.

## 9. Seguranca/LGPD

### Controles minimos

- Autenticacao forte.
- RBAC por perfil.
- Criptografia em transito e repouso.
- Consentimento informado e finalidade.
- Minimização de dados.
- Logs de acesso, alteracao e exportacao.
- Politica de retencao/descarte.
- Backup seguro.
- Controle de compartilhamento.
- Anonimizacao/pseudonimizacao.
- Revisao periodica de acessos.
- Bloqueio de exportacao sem responsavel tecnico.

### Perfis

- Administrador.
- Neuropsicopedagogo clinico.
- Neuropsicopedagogo institucional.
- Assistente/secretaria com acesso limitado.
- Supervisor tecnico.
- Leitor externo temporario e restrito.

## 10. Stack tecnica

### Recomendada para produto profissional

- Frontend: Next.js + React + TypeScript.
- Backend: FastAPI ou NestJS.
- Banco: PostgreSQL.
- Arquivos: S3/MinIO com criptografia.
- Autenticacao: OAuth2/OIDC, JWT curto, refresh seguro, MFA.
- Documentos: DOCX por template; PDF por renderizacao controlada.
- IA: camada isolada com guardrails, auditoria e citacao de campos.
- Observabilidade: logs estruturados, auditoria, metricas sem dados sensiveis.

### Streamlit

Adequado somente para MVP demonstrativo, validacao de fluxo e prototipo com dados ficticios. Nao deve ser usado com dados reais sem autenticacao, persistencia segura, politicas juridicas e controles de acesso.

## 11. Codigo inicial

O repositorio deve manter:

```text
neurorelatorio-pro/
  streamlit_app.py
  requirements.txt
  apps/
    api/
      app/
        main.py
        schemas.py
        domain/
        routers/
        repositories/
        seed/
    web/
      app/
      components/
      lib/
  docs/
  examples/
```

Prioridade imediata do codigo:

- Melhorar UX do Streamlit para MVP demonstrativo.
- Manter seeds expansiveis de protocolos e abas.
- Adicionar validacao de relatorio e `additional_fields`.
- Preparar migracao posterior para Next.js + FastAPI + PostgreSQL.

## 12. Proximos passos

### MVP seguro

- Streamlit demonstrativo com dados ficticios.
- Abas preenchiveis, opcoes pre-definidas e `additional_fields` justificado.
- Validacao de fonte, justificativa, responsavel e limitacoes.
- Exportacao TXT/JSON.
- Aviso de rascunho e revisao profissional obrigatoria.
- Publicacao no Streamlit Community Cloud sem dados reais.

### Versao intermediaria

- Backend FastAPI ativo.
- PostgreSQL.
- Login.
- Perfis de usuario.
- Consentimentos.
- Anexos.
- Auditoria.
- Exportacao DOCX/PDF.
- Relatorios versionados.
- Banco de protocolos com bloqueios reais.

### Versao avancada

- Multi-tenant.
- Criptografia de campos sensiveis.
- MFA.
- Compartilhamento temporario.
- Assinatura digital.
- IA assistiva com citacao de evidencias.
- Painel de governanca/LGPD.
- Retencao/descarte automatizado.
- Monitoramento e resposta a incidentes.

## Referencias

- SBNPp - Codigo de Etica Tecnico-Profissional da Neuropsicopedagogia, Resolucao n. 05/2021: https://sbnpp.org.br/arquivos/Codigo_de_Etica_Tecnico_Profisisonal_da_Neuropsicopedagogia_-_SBNPp_-_2021.pdf
- SATEPSI/CFP - Legislacao e Resolucao CFP n. 31/2022: https://satepsi.cfp.org.br/legislacao.cfm
- SATEPSI/CFP - Instrumentos nao privativos: https://satepsi.cfp.org.br/testesNaoPrivativos.cfm
- LGPD - Lei n. 13.709/2018: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- ANPD - Tratamento de dados de criancas e adolescentes: https://www.gov.br/anpd/

