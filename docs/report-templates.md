# Modelos de Relatorio e Plano de Intervencao

## Padrao das abas preenchiveis

Todas as abas preenchiveis devem conter opcoes pre-definidas e a opcao `Adicionar campo adicional justificado`.

Regras gerais:

- As opcoes pre-definidas devem ser exibidas antes do campo livre.
- `Adicionar campo adicional justificado` deve criar um campo adicional na propria aba, com rotulo definido pelo profissional.
- Todo `additional_fields` deve registrar tipo de resposta, valor, fonte da informacao e justificativa de inclusao.
- O sistema nao deve gerar interpretacoes a partir de `additional_fields` vazio.
- O assistente de escrita so pode usar `additional_fields` quando ele estiver preenchido e vinculado a uma fonte/evidencia.

Abas e opcoes iniciais:

| Aba preenchivel | Opcoes pre-definidas minimas | Campo adicional |
| --- | --- | --- |
| Identificacao do avaliado | nome, data de nascimento, idade, escola, serie, turno, responsaveis legais | `Adicionar campo adicional justificado` |
| Dados do profissional | nome, formacao, qualificacao, contexto de atuacao, registro/associacao quando aplicavel | `Adicionar campo adicional justificado` |
| Solicitante e objetivo | familia, escola, profissional de saude, equipe pedagogica, demanda espontanea, objetivo avaliativo, objetivo interventivo | `Adicionar campo adicional justificado` |
| Procedimentos e instrumentos | entrevista, anamnese, observacao clinica, observacao escolar, analise documental, sessao avaliativa, protocolo, escala, questionario | `Adicionar campo adicional justificado` |
| Historico relevante | gestacao, desenvolvimento, linguagem, saude, familia, escola, alfabetizacao, rotina, sono, alimentacao, telas, socializacao, comportamento, autonomia, intervencoes anteriores | `Adicionar campo adicional justificado` |
| Observacoes comportamentais | observacao direta, relato familiar, relato escolar, documento apresentado, comportamento em tarefa, engajamento, mediacao, autorregulacao | `Adicionar campo adicional justificado` |
| Analise por dominio | atencao, memoria, linguagem, leitura, escrita, matematica, funcoes executivas, motricidade, comportamento em tarefa, autorregulacao, interacao social, autonomia academica | `Adicionar campo adicional justificado` |
| Potencialidades | recursos preservados, estrategias efetivas, interesses, condicoes facilitadoras, apoio familiar, apoio escolar | `Adicionar campo adicional justificado` |
| Dificuldades e impactos | dificuldade observada, contexto, impacto funcional, impacto academico, evidencia vinculada, frequencia, intensidade | `Adicionar campo adicional justificado` |
| Interpretacao | dado observado, evidencia, hipotese cautelosa, necessidade de investigacao complementar, limitacao interpretativa | `Adicionar campo adicional justificado` |
| Recomendacoes | familia, escola, professor, intervencao neuropsicopedagogica, equipe multiprofissional, rotina, adaptacoes, acompanhamento | `Adicionar campo adicional justificado` |
| Encaminhamentos | psicologia, fonoaudiologia, neurologia, psiquiatria, terapia ocupacional, psicopedagogia, pediatria, oftalmologia, audiologia | `Adicionar campo adicional justificado` |
| Limitacoes | dados ausentes, tempo reduzido, instrumento nao aplicado, necessidade de avaliacao complementar, interferencia emocional, fadiga, contexto de aplicacao | `Adicionar campo adicional justificado` |
| Conclusao | sintese dos achados, evidencias principais, limites de inferencia, conduta sugerida, revisao profissional | `Adicionar campo adicional justificado` |

## Relatorio neuropsicopedagogico completo

> Documento preliminar. Deve ser revisado e aprovado por profissional habilitado antes de emissao.

### 1. Identificacao do avaliado

- Nome: `[informar]`
- Data de nascimento: `[informar]`
- Idade: `[calcular]`
- Escola/serie/turno: `[informar]`
- Responsaveis legais: `[informar]`

### 2. Dados do profissional

- Nome: `[informar]`
- Formacao/qualificacao: `[informar]`
- Contexto de atuacao: `[clinico/institucional]`
- Registro/associacao quando aplicavel: `[informar]`

### 3. Solicitante e objetivo

Descrever quem solicitou a avaliacao, a queixa principal e o objetivo tecnico do processo.

### 4. Procedimentos e instrumentos

Listar entrevistas, observacoes, sessoes, protocolos e documentos analisados. Para cada instrumento, registrar apenas resultados/escores inseridos pelo profissional e indicar que manual, licenca, faixa etaria e restricoes foram verificados.

### 5. Historico relevante

Organizar dados de anamnese: gestacao, desenvolvimento, linguagem, saude, familia, escola, alfabetizacao, rotina, sono, alimentacao, telas, socializacao, comportamento, autonomia e intervencoes anteriores.

### 6. Observacoes comportamentais

Separar observacao direta, relato familiar, relato escolar e documentos apresentados.

### 7. Analise por dominio

Para cada dominio:

- Achados observados.
- Evidencias vinculadas.
- Indicadores compativeis com.
- Hipoteses neuropsicopedagogicas.
- Limitacoes.

Dominios sugeridos: atencao, memoria, linguagem, leitura, escrita, matematica, funcoes executivas, motricidade, comportamento em tarefa, autorregulacao, interacao social e autonomia academica.

### 8. Potencialidades

Descrever recursos preservados, estrategias efetivas, interesses e condicoes facilitadoras.

### 9. Dificuldades observadas e impactos na aprendizagem

Apresentar dificuldade observada, contexto, impacto funcional e evidencias.

### 10. Interpretacao neuropsicopedagogica

Usar linguagem cautelosa: "os dados sugerem", "observou-se", "ha indicadores compativeis com", "recomenda-se investigacao complementar".

### 11. Hipoteses levantadas

Registrar hipoteses neuropsicopedagogicas, sem fechar diagnostico clinico ou emitir CID.

### 12. Recomendações

- Familia.
- Escola.
- Professor.
- Intervencao neuropsicopedagogica.
- Equipe multiprofissional.

### 13. Encaminhamentos sugeridos

Sugerir encaminhamento quando os achados extrapolarem a area neuropsicopedagogica.

### 14. Limitacoes da avaliacao

Informar dados ausentes, restricoes de tempo, instrumentos nao aplicados, necessidade de avaliacao complementar e limites de inferencia.

### 15. Conclusao tecnica revisada pelo profissional

Conclusao baseada apenas nas evidencias registradas, com data, local, assinatura e identificacao profissional.

## Plano de intervencao neuropsicopedagogica

### Identificacao

- Avaliado: `[informar]`
- Periodo do plano: `[informar]`
- Responsavel tecnico: `[informar]`

### Objetivos gerais

Descrever metas amplas relacionadas a aprendizagem, autonomia, estrategias cognitivas e contexto.

### Objetivos especificos

Cada objetivo deve conter:

- habilidade-alvo;
- evidencia que justifica;
- estrategia;
- frequencia;
- recursos;
- responsaveis;
- criterio de acompanhamento;
- prazo de reavaliacao.

### Estrategias

Incluir atividades de mediacao, treino de estrategias, organizacao de rotina, adaptacoes pedagogicas, orientacao familiar/escolar e monitoramento.

### Acompanhamento

Registrar indicadores qualitativos e quantitativos, evolucao por sessao e revisao periodica.

### Devolutiva

Preparar versoes em linguagem tecnica, familiar e escolar, mantendo sigilo e finalidade.

