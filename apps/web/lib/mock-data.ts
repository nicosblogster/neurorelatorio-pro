export const metrics = [
  { label: "Avaliados ativos", value: "128", detail: "22 em avaliacao" },
  { label: "Relatorios pendentes", value: "14", detail: "9 aguardam revisao" },
  { label: "Sessoes da semana", value: "36", detail: "5 devolutivas" },
  { label: "Consentimentos", value: "7", detail: "alertas de vencimento" }
];

export const alerts = [
  "Consentimento vence em 10 dias: caso NRP-0241",
  "Relatorio com bloco de IA pendente de revisao humana",
  "Instrumento exige verificacao de manual/licenca/SATEPSI antes da aplicacao"
];

export const cases = [
  {
    code: "NRP-0241",
    initials: "L.M.",
    status: "Avaliacao em andamento",
    nextStep: "Sessao de sondagem de leitura",
    risk: "Consentimento proximo do vencimento"
  },
  {
    code: "NRP-0238",
    initials: "A.R.",
    status: "Relatorio em revisao",
    nextStep: "Validar limitacoes e evidencias",
    risk: "Conclusao sem evidencia vinculada"
  },
  {
    code: "NRP-0234",
    initials: "T.S.",
    status: "Intervencao",
    nextStep: "Atualizar plano quinzenal",
    risk: "Sem alerta critico"
  }
];

export const protocolHighlights = [
  { name: "Sondagem de leitura", access: "Aberto", context: "Ambos" },
  { name: "TDE / TDE II", access: "Verificar SATEPSI", context: "Ambos" },
  { name: "Observacao institucional", access: "Aberto", context: "Institucional" },
  { name: "Funcoes executivas", access: "Verificar instrumento", context: "Ambos" }
];

export const skillDomains = [
  "Atencao sustentada",
  "Memoria operacional",
  "Consciencia fonologica",
  "Compreensao leitora",
  "Producao textual",
  "Raciocinio logico",
  "Controle inibitorio",
  "Autorregulacao",
  "Motricidade fina",
  "Autonomia academica"
];

export const reportSections = [
  "Identificacao",
  "Procedimentos e instrumentos",
  "Achados observados",
  "Indicadores compativeis com",
  "Hipoteses neuropsicopedagogicas",
  "Limitacoes da avaliacao",
  "Conclusao tecnica revisada"
];

export type FillableTab = {
  key: string;
  label: string;
  options: string[];
};

export const fillableTabs: FillableTab[] = [
  {
    key: "identificacao_avaliado",
    label: "Identificacao do avaliado",
    options: ["Nome", "Data de nascimento", "Idade", "Escola", "Serie", "Turno", "Responsaveis legais"]
  },
  {
    key: "dados_profissional",
    label: "Dados do profissional",
    options: ["Nome", "Formacao", "Qualificacao", "Contexto clinico", "Contexto institucional", "Registro ou associacao"]
  },
  {
    key: "solicitante_objetivo",
    label: "Solicitante e objetivo",
    options: [
      "Familia",
      "Escola",
      "Profissional de saude",
      "Equipe pedagogica",
      "Demanda espontanea",
      "Objetivo avaliativo",
      "Objetivo interventivo"
    ]
  },
  {
    key: "procedimentos_instrumentos",
    label: "Procedimentos e instrumentos",
    options: [
      "Entrevista",
      "Anamnese",
      "Observacao clinica",
      "Observacao escolar",
      "Analise documental",
      "Sessao avaliativa",
      "Protocolo",
      "Escala",
      "Questionario"
    ]
  },
  {
    key: "historico_relevante",
    label: "Historico relevante",
    options: [
      "Gestacao",
      "Desenvolvimento",
      "Linguagem",
      "Saude",
      "Familia",
      "Escola",
      "Alfabetizacao",
      "Rotina",
      "Sono",
      "Alimentacao",
      "Telas",
      "Socializacao",
      "Comportamento",
      "Autonomia",
      "Intervencoes anteriores"
    ]
  },
  {
    key: "observacoes_comportamentais",
    label: "Observacoes comportamentais",
    options: [
      "Observacao direta",
      "Relato familiar",
      "Relato escolar",
      "Documento apresentado",
      "Comportamento em tarefa",
      "Engajamento",
      "Mediacao",
      "Autorregulacao"
    ]
  },
  {
    key: "analise_dominio",
    label: "Analise por dominio",
    options: [
      "Atencao",
      "Memoria",
      "Linguagem",
      "Leitura",
      "Escrita",
      "Matematica",
      "Funcoes executivas",
      "Motricidade",
      "Comportamento em tarefa",
      "Autorregulacao",
      "Interacao social",
      "Autonomia academica"
    ]
  },
  {
    key: "potencialidades",
    label: "Potencialidades",
    options: ["Recursos preservados", "Estrategias efetivas", "Interesses", "Condicoes facilitadoras", "Apoio familiar", "Apoio escolar"]
  },
  {
    key: "dificuldades_impactos",
    label: "Dificuldades e impactos",
    options: [
      "Dificuldade observada",
      "Contexto",
      "Impacto funcional",
      "Impacto academico",
      "Evidencia vinculada",
      "Frequencia",
      "Intensidade"
    ]
  },
  {
    key: "interpretacao",
    label: "Interpretacao",
    options: [
      "Dado observado",
      "Evidencia",
      "Hipotese cautelosa",
      "Necessidade de investigacao complementar",
      "Limitacao interpretativa"
    ]
  },
  {
    key: "recomendacoes",
    label: "Recomendacoes",
    options: [
      "Familia",
      "Escola",
      "Professor",
      "Intervencao neuropsicopedagogica",
      "Equipe multiprofissional",
      "Rotina",
      "Adaptacoes",
      "Acompanhamento"
    ]
  },
  {
    key: "encaminhamentos",
    label: "Encaminhamentos",
    options: [
      "Psicologia",
      "Fonoaudiologia",
      "Neurologia",
      "Psiquiatria",
      "Terapia ocupacional",
      "Psicopedagogia",
      "Pediatria",
      "Oftalmologia",
      "Audiologia"
    ]
  },
  {
    key: "limitacoes",
    label: "Limitacoes",
    options: [
      "Dados ausentes",
      "Tempo reduzido",
      "Instrumento nao aplicado",
      "Necessidade de avaliacao complementar",
      "Interferencia emocional",
      "Fadiga",
      "Contexto de aplicacao"
    ]
  },
  {
    key: "conclusao",
    label: "Conclusao",
    options: ["Sintese dos achados", "Evidencias principais", "Limites de inferencia", "Conduta sugerida", "Revisao profissional"]
  }
];
