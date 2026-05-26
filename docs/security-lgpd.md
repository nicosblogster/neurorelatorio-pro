# Seguranca, Privacidade e LGPD

## Classificacao de dados

- Dados cadastrais: nome, contato, escola, responsaveis.
- Dados sensiveis ou de protecao reforcada: saude, desenvolvimento, comportamento, aprendizagem, relatorios, resultados de instrumentos, historico familiar e documentos.
- Dados de criancas/adolescentes: sempre exigem cautela reforcada, linguagem clara aos responsaveis e base legal adequada.

## Principios operacionais

- Finalidade: cada caso deve registrar o motivo do tratamento.
- Necessidade: coletar apenas dados pertinentes ao atendimento.
- Transparencia: termo claro para responsaveis e avaliados quando aplicavel.
- Seguranca: criptografia, logs, backups, controle de acesso e segregacao.
- Prevencao: revisao de exportacao, bloqueio de compartilhamento indevido e alertas.
- Responsabilizacao: trilha de auditoria e politicas documentadas.

## Controle de acesso

| Perfil | Permissoes |
| --- | --- |
| Administrador | Configuracao, usuarios, termos, auditoria administrativa |
| Neuropsicopedagogo clinico | Casos clinicos autorizados, sessoes, relatorios e planos |
| Neuropsicopedagogo institucional | Casos institucionais e triagens autorizadas |
| Assistente/secretaria | Agenda e cadastro minimo, sem acesso a relatorios sensiveis por padrao |
| Supervisor tecnico | Revisao, auditoria tecnica e aprovacao quando configurado |
| Leitor externo | Acesso temporario, escopado, com expiracao e log |

## Consentimento

- Menores de idade: exigir responsavel legal cadastrado e termo valido quando essa for a base juridica aplicavel.
- O termo deve conter finalidade, categorias de dados, compartilhamentos, prazo de retencao, direitos do titular e canal de contato.
- Consentimento revogado bloqueia novas operacoes nao justificadas por outra base legal.

## Exportacao e compartilhamento

- Exportacao PDF/DOCX gera evento de auditoria.
- Links externos devem expirar e exigir autenticacao ou token seguro.
- Documentos podem receber marca d'agua com nome do destinatario.
- O sistema deve permitir versao anonimizada para estudo/supervisao, removendo identificadores.

## IA assistiva

- A IA recebe apenas dados necessarios ao texto solicitado.
- Prompts e respostas devem ser auditados sem expor dados alem do necessario.
- Toda resposta deve listar lacunas e fontes usadas.
- Bloquear comandos para diagnostico automatico, CID, prognostico taxativo ou preenchimento inventado.
- Texto gerado permanece como rascunho ate revisao humana.

## Retencao e descarte

- Politica configuravel por organizacao, respeitando obrigacoes legais e contratuais.
- Descarte deve remover ou anonimizar anexos, exportacoes e dados operacionais.
- Backups devem ter criptografia e ciclo de vida definido.

## Resposta a incidente

1. Detectar e classificar incidente.
2. Conter acesso indevido.
3. Preservar logs.
4. Avaliar risco aos titulares.
5. Notificar responsaveis internos e, quando aplicavel, autoridade/titulares.
6. Corrigir causa raiz.
7. Registrar licoes aprendidas.
