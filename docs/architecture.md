# Arquitetura Tecnica

## Visao geral

Arquitetura modular em monorepo:

```text
Next.js Web -> FastAPI API -> PostgreSQL
                         -> Object Storage
                         -> AI Gateway
                         -> Audit Log
```

O backend concentra as regras sensiveis de dominio. O frontend nunca decide sozinho se um instrumento pode ser usado ou se um relatorio pode ser finalizado.

## Fronteiras de contexto

- Identidade e acesso: usuarios, papeis, permissoes, sessoes e MFA.
- Cadastro clinico/institucional: avaliados, responsaveis, escola e profissionais externos.
- Consentimento e LGPD: termos, finalidades, bases legais, validade e revogacao.
- Avaliacao e intervencao: anamnese, sessoes, instrumentos, resultados e matriz de habilidades.
- Documentos: modelos, relatorios, versoes, assinaturas, exportacoes e devolutivas.
- IA assistiva: sugestoes, lacunas, reescrita e revisao, sempre com origem dos dados.
- Auditoria: eventos imutaveis de leitura, escrita, exportacao, compartilhamento e IA.

## Principios de seguranca por design

- Menor privilegio por perfil.
- Segregacao por organizacao.
- Nao exposicao de dados sensiveis em metricas do dashboard.
- Auditoria de acesso e exportacao.
- Criptografia de campos sensiveis e anexos.
- Revisao humana obrigatoria antes de documentos finais.
- Bloqueio de instrumentos conforme autorizacao, perfil e restricao.

## API inicial

- `GET /health`: saude do servico.
- `GET /protocols`: lista base de protocolos.
- `POST /protocols/{id}/validate-use`: verifica se um profissional pode usar determinado protocolo.
- `POST /reports/validate-finalization`: valida prerequisitos para finalizar relatorio.
- `GET /reports/templates/full`: retorna estrutura do relatorio completo.

## Evolucao recomendada

1. Persistencia real com SQLAlchemy/Alembic.
2. Autenticacao e autorizacao com politicas centralizadas.
3. Editor de documentos por blocos, com versoes.
4. Exportadores DOCX/PDF assinaveis.
5. AI Gateway com mascaramento, minimizacao e registro de prompts/respostas.
6. Eventos de auditoria append-only.
