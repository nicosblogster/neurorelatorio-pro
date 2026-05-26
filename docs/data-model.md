# Modelo de Banco de Dados

## Entidades principais

### organizations

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| name | text | Clinica, escola ou consultorio |
| document | text | CNPJ/CPF quando aplicavel |
| lgpd_controller_name | text | Controlador ou representante |
| dpo_contact | text | Encarregado/canal LGPD |
| created_at | timestamptz | Auditoria |

### users

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| organization_id | uuid | FK |
| full_name | text | Nome do usuario |
| email | citext | Login |
| password_hash | text | Nunca armazenar senha em claro |
| role | enum | admin, clinical_npp, institutional_npp, assistant, supervisor, external_reader |
| status | enum | active, suspended, invited |
| mfa_enabled | boolean | Obrigatorio em producao para perfis sensiveis |

### professional_profiles

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| user_id | uuid | FK |
| professional_context | enum | clinical, institutional, both |
| qualification | text | Formacao declarada/comprovada |
| association_number | text | Numero de associacao/registro quando aplicavel |
| authorized_restricted_instruments | jsonb | Evidencias de autorizacao/licenca |
| supervisor_id | uuid | FK opcional |

### assessees

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| organization_id | uuid | FK |
| full_name_encrypted | bytea | Dado sensivel/pessoal |
| birth_date_encrypted | bytea | Usado para idade automatica |
| sex | text | Apenas quando necessario ao documento |
| school_id | uuid | FK opcional |
| grade_year | text | Serie/ano |
| shift | text | Turno |
| main_complaint | text | Queixa principal |
| referral_source | text | Encaminhamento |
| case_status | enum | intake, assessment, intervention, followup, closed |

### guardians

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| assessee_id | uuid | FK |
| full_name_encrypted | bytea | Responsavel legal |
| relationship | text | Mae, pai, tutor etc. |
| contact_encrypted | bytea | Telefone/email |
| legal_responsibility_confirmed | boolean | Obrigatorio para menores |

### consents

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| assessee_id | uuid | FK |
| guardian_id | uuid | FK quando menor |
| purpose | text | Finalidade do tratamento |
| legal_basis | text | Consentimento, contrato, obrigacao legal etc. |
| signed_at | timestamptz | Data da assinatura |
| expires_at | timestamptz | Validade |
| revoked_at | timestamptz | Revogacao |
| document_id | uuid | Termo anexado |

### anamneses

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| assessee_id | uuid | FK |
| responsible_professional_id | uuid | FK |
| sections | jsonb | Historico gestacional, desenvolvimento, escola, rotina etc.; cada aba deve guardar opcoes pre-definidas selecionadas e campos adicionados |
| source_map | jsonb | Relato familiar/escolar/documental/observacao |
| custom_fields | jsonb | Inclui `campo44` por aba, com rotulo, tipo, valor, fonte e justificativa |
| completed_at | timestamptz | Conclusao |

### sessions

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| assessee_id | uuid | FK |
| professional_id | uuid | FK |
| occurred_at | timestamptz | Data |
| duration_minutes | int | Duracao |
| objective | text | Objetivo |
| protocol_id | uuid | FK opcional |
| activity_description | text | Descricao |
| observed_behavior | text | Comportamento |
| mediation_level | text | Nivel de mediacao |
| qualitative_results | text | Resultados qualitativos |
| quantitative_results | jsonb | Escores informados pelo profissional |
| custom_fields | jsonb | Inclui `campo44` por aba, com rotulo, tipo, valor, fonte e justificativa |
| next_steps | text | Proximos passos |

### protocols

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| name | text | Nome |
| assessed_area | text | Area |
| objective | text | Objetivo |
| age_or_grade | text | Faixa etaria/serie |
| type | enum | triagem, sondagem, avaliacao, intervencao, observacao, entrevista, escala, questionario |
| context | enum | clinical, institutional, both |
| authorized_professional | text | Perfil permitido |
| usage_restriction | text | Restricao |
| access_level | enum | open, non_private, private, verify_satepsi |
| reference | text | Referencia |
| active | boolean | Ativo |

### protocol_results

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| session_id | uuid | FK |
| protocol_id | uuid | FK |
| entered_by | uuid | FK |
| scores | jsonb | Apenas resultados lancados pelo profissional |
| qualitative_indicators | jsonb | Indicadores |
| evidence_source | enum | direct_observation, family_report, school_report, instrument_result, document |
| manual_reproduced | boolean | Deve permanecer falso |

### skill_findings

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| assessee_id | uuid | FK |
| skill_key | text | Ex.: sustained_attention |
| finding_type | enum | strength, difficulty, neutral, not_observed |
| evidence_ids | uuid[] | Evidencias que sustentam o achado |
| interpretation | text | Interpretacao cautelosa |

### reports

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| assessee_id | uuid | FK |
| kind | enum | full_clinical, screening, school_probe, institutional, followup, evolution, family_feedback, school_feedback, individual_plan, institutional_plan |
| status | enum | draft, in_review, approved, final, revoked |
| responsible_professional_id | uuid | Obrigatorio para finalizar |
| reviewed_by | uuid | Supervisor opcional |
| conclusion | text | Deve referenciar evidencias |
| limitations | text | Obrigatorio em relatorios finais |
| finalized_at | timestamptz | Data final |

### report_versions

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| report_id | uuid | FK |
| version_number | int | Sequencial |
| content | jsonb | Blocos do documento, opcoes selecionadas e `campo44` preenchido por aba |
| change_summary | text | Motivo |
| author_id | uuid | FK |
| created_at | timestamptz | Auditoria |

### fillable_tab_templates

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| organization_id | uuid | FK |
| scope | enum | assessee, anamnesis, session, report, intervention_plan, feedback |
| tab_key | text | Chave tecnica da aba preenchivel |
| tab_label | text | Nome exibido ao profissional |
| predefined_options | jsonb | Opcoes pre-definidas exibidas na aba |
| allow_campo44 | boolean | Deve ser verdadeiro para abas preenchiveis |
| required_source_for_campo44 | boolean | Deve ser verdadeiro |
| active | boolean | Controla uso em novos registros |
| created_at | timestamptz | Auditoria |

### fillable_tab_entries

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| organization_id | uuid | FK |
| template_id | uuid | FK para `fillable_tab_templates` |
| entity_type | text | anamnesis, session, report_version etc. |
| entity_id | uuid | Registro preenchido |
| selected_options | jsonb | Opcoes pre-definidas escolhidas |
| free_text | text | Texto complementar digitado pelo profissional |
| campo44 | jsonb | Campo adicional por aba: rotulo, tipo, valor, fonte, evidencia_id e justificativa |
| created_by | uuid | FK para usuario |
| updated_at | timestamptz | Auditoria |

### audit_logs

| Campo | Tipo | Observacao |
| --- | --- | --- |
| id | uuid | PK |
| organization_id | uuid | FK |
| actor_id | uuid | FK |
| action | text | create, update, read, export, share, ai_request |
| entity_type | text | Tabela/objeto |
| entity_id | uuid | ID |
| ip_address | inet | Origem |
| user_agent | text | Cliente |
| metadata | jsonb | Sem dados sensiveis desnecessarios |
| created_at | timestamptz | Append-only |

## Indices recomendados

- `assessees(organization_id, case_status)`.
- `sessions(assessee_id, occurred_at desc)`.
- `reports(assessee_id, status, kind)`.
- `consents(assessee_id, expires_at, revoked_at)`.
- `audit_logs(organization_id, created_at desc)`.
- `protocols(active, access_level, context)`.

## Regras de integridade

- Relatorio final exige profissional responsavel.
- Relatorio de menor exige responsavel legal e consentimento valido.
- Resultado de protocolo nao pode conter itens/manual/crivo protegido.
- Conclusao exige evidencias vinculadas.
- Toda exportacao cria evento em `audit_logs`.
