"use client";

import { useMemo, useState } from "react";
import type { FillableTab } from "@/lib/mock-data";

type Metric = {
  label: string;
  value: string;
  detail: string;
};

type CaseSummary = {
  code: string;
  initials: string;
  status: string;
  nextStep: string;
  risk: string;
};

type ProtocolHighlight = {
  name: string;
  access: string;
  context: string;
};

type OptionDraft = {
  selected: boolean;
  value: string;
  source: string;
};

type Campo44Draft = {
  id: string;
  label: string;
  type: string;
  value: string;
  source: string;
  reason: string;
};

type TabDraft = {
  options: Record<string, OptionDraft>;
  campo44: Campo44Draft[];
};

type Campo44Form = {
  label: string;
  type: string;
  value: string;
  source: string;
  reason: string;
};

type DashboardShellProps = {
  alerts: string[];
  cases: CaseSummary[];
  fillableTabs: FillableTab[];
  metrics: Metric[];
  protocolHighlights: ProtocolHighlight[];
  reportSections: string[];
  skillDomains: string[];
};

const reportModes = ["Clinico completo", "Triagem", "Devolutiva familiar", "Plano de intervencao"];
const sourceOptions = [
  "Observacao direta",
  "Relato familiar",
  "Relato escolar",
  "Documento apresentado",
  "Instrumento/protocolo"
];
const emptyCampo44Form: Campo44Form = {
  label: "",
  type: "texto",
  value: "",
  source: "",
  reason: ""
};

function createDraft(tabs: FillableTab[]): Record<string, TabDraft> {
  return tabs.reduce<Record<string, TabDraft>>((acc, tab) => {
    acc[tab.key] = {
      options: tab.options.reduce<Record<string, OptionDraft>>((optionAcc, option) => {
        optionAcc[option] = {
          selected: false,
          value: "",
          source: ""
        };
        return optionAcc;
      }, {}),
      campo44: []
    };
    return acc;
  }, {});
}

function countTabFields(tabDraft: TabDraft) {
  const selectedOptions = Object.values(tabDraft.options).filter((option) => option.selected).length;
  return selectedOptions + tabDraft.campo44.length;
}

export function DashboardShell({
  alerts,
  cases,
  fillableTabs,
  metrics,
  protocolHighlights,
  reportSections,
  skillDomains
}: DashboardShellProps) {
  const [selectedMode, setSelectedMode] = useState(reportModes[0]);
  const [activeTabKey, setActiveTabKey] = useState(fillableTabs[0]?.key ?? "");
  const [draft, setDraft] = useState(() => createDraft(fillableTabs));
  const [campo44Form, setCampo44Form] = useState<Campo44Form>(emptyCampo44Form);
  const [formError, setFormError] = useState("");

  const blockers = useMemo(
    () => [
      "Profissional responsavel identificado",
      "Responsavel legal cadastrado quando menor",
      "Consentimento/base legal valido",
      "Evidencias vinculadas a conclusao",
      "Blocos de IA revisados"
    ],
    []
  );

  const activeTab = useMemo(
    () => fillableTabs.find((tab) => tab.key === activeTabKey) ?? fillableTabs[0],
    [activeTabKey, fillableTabs]
  ) as FillableTab;
  const activeDraft = draft[activeTab.key];
  const selectedCount = Object.values(activeDraft.options).filter((option) => option.selected).length;
  const reportPreview = useMemo(() => buildPreview(fillableTabs, draft), [draft, fillableTabs]);

  function updateOption(tabKey: string, optionLabel: string, patch: Partial<OptionDraft>) {
    setDraft((current) => ({
      ...current,
      [tabKey]: {
        ...current[tabKey],
        options: {
          ...current[tabKey].options,
          [optionLabel]: {
            ...current[tabKey].options[optionLabel],
            ...patch
          }
        }
      }
    }));
  }

  function addCampo44() {
    const field = {
      ...campo44Form,
      label: campo44Form.label.trim(),
      value: campo44Form.value.trim(),
      reason: campo44Form.reason.trim()
    };

    if (!field.label || !field.value || !field.source || !field.reason) {
      setFormError("Preencha rotulo, valor, fonte e justificativa.");
      return;
    }

    setDraft((current) => ({
      ...current,
      [activeTab.key]: {
        ...current[activeTab.key],
        campo44: [
          ...current[activeTab.key].campo44,
          {
            ...field,
            id: `${Date.now()}-${field.label}`
          }
        ]
      }
    }));
    setCampo44Form(emptyCampo44Form);
    setFormError("");
  }

  function removeCampo44(fieldId: string) {
    setDraft((current) => ({
      ...current,
      [activeTab.key]: {
        ...current[activeTab.key],
        campo44: current[activeTab.key].campo44.filter((field) => field.id !== fieldId)
      }
    }));
  }

  return (
    <main className="appShell">
      <aside className="sidebar" aria-label="Navegacao principal">
        <div className="brand">
          <span className="brandMark">NR</span>
          <div>
            <strong>NeuroRelatorio Pro</strong>
            <small>Ambiente profissional</small>
          </div>
        </div>

        <nav className="navList">
          {["Dashboard", "Avaliados", "Anamnese", "Sessoes", "Protocolos", "Relatorios", "LGPD"].map((item) => (
            <a className={item === "Relatorios" ? "active" : ""} href="#" key={item}>
              {item}
            </a>
          ))}
        </nav>
      </aside>

      <section className="workspace">
        <header className="topbar">
          <div>
            <p className="sectionLabel">Relatorios</p>
            <h1>Editor com abas preenchiveis e revisao humana</h1>
          </div>
          <button className="primaryButton" type="button">
            Novo avaliado
          </button>
        </header>

        <section className="metricsGrid" aria-label="Indicadores gerais">
          {metrics.map((metric) => (
            <article className="metricCard" key={metric.label}>
              <span>{metric.label}</span>
              <strong>{metric.value}</strong>
              <small>{metric.detail}</small>
            </article>
          ))}
        </section>

        <section className="contentGrid">
          <div className="panel widePanel">
            <div className="panelHeader">
              <div>
                <p className="sectionLabel">Fila de casos</p>
                <h2>Avaliacoes e acompanhamentos</h2>
              </div>
              <button className="secondaryButton" type="button">
                Filtrar
              </button>
            </div>

            <div className="caseList">
              {cases.map((item) => (
                <article className="caseRow" key={item.code}>
                  <div>
                    <strong>{item.initials}</strong>
                    <small>{item.code}</small>
                  </div>
                  <div>
                    <span>{item.status}</span>
                    <small>{item.nextStep}</small>
                  </div>
                  <span className={item.risk.includes("Sem") ? "statusOk" : "statusWarn"}>{item.risk}</span>
                </article>
              ))}
            </div>
          </div>

          <div className="panel">
            <p className="sectionLabel">Alertas</p>
            <h2>Revisao necessaria</h2>
            <ul className="alertList">
              {alerts.map((alert) => (
                <li key={alert}>{alert}</li>
              ))}
            </ul>
          </div>

          <div className="panel">
            <p className="sectionLabel">Protocolos</p>
            <h2>Base inicial</h2>
            <div className="protocolList">
              {protocolHighlights.map((protocol) => (
                <article key={protocol.name}>
                  <strong>{protocol.name}</strong>
                  <small>
                    {protocol.access} - {protocol.context}
                  </small>
                </article>
              ))}
            </div>
          </div>

          <div className="panel widePanel reportPanel">
            <div className="panelHeader">
              <div>
                <p className="sectionLabel">Gerador</p>
                <h2>Relatorio com opcoes pre-definidas</h2>
              </div>
              <div className="segmented" role="tablist" aria-label="Tipo de documento">
                {reportModes.map((mode) => (
                  <button
                    aria-selected={mode === selectedMode}
                    className={mode === selectedMode ? "selected" : ""}
                    key={mode}
                    onClick={() => setSelectedMode(mode)}
                    role="tab"
                    type="button"
                  >
                    {mode}
                  </button>
                ))}
              </div>
            </div>

            <div className="fillableBuilder">
              <aside className="fillableTabs" aria-label="Abas preenchiveis">
                {fillableTabs.map((tab) => (
                  <button
                    className={tab.key === activeTab.key ? "active" : ""}
                    key={tab.key}
                    onClick={() => {
                      setActiveTabKey(tab.key);
                      setFormError("");
                    }}
                    type="button"
                  >
                    <span>{tab.label}</span>
                    <strong>{countTabFields(draft[tab.key])}</strong>
                  </button>
                ))}
              </aside>

              <section className="fillableEditor">
                <div className="fillableHeader">
                  <div>
                    <p className="sectionLabel">{selectedMode}</p>
                    <h3>{activeTab.label}</h3>
                  </div>
                  <span>{selectedCount} selecionados</span>
                </div>

                <div className="optionStack">
                  {activeTab.options.map((optionLabel) => {
                    const optionDraft = activeDraft.options[optionLabel];
                    return (
                      <article className="optionItem" key={optionLabel}>
                        <label className="optionCheck">
                          <input
                            checked={optionDraft.selected}
                            onChange={(event) =>
                              updateOption(activeTab.key, optionLabel, { selected: event.target.checked })
                            }
                            type="checkbox"
                          />
                          <span>{optionLabel}</span>
                        </label>
                        {optionDraft.selected ? (
                          <div className="optionInputs">
                            <label>
                              Valor registrado
                              <textarea
                                onChange={(event) =>
                                  updateOption(activeTab.key, optionLabel, { value: event.target.value })
                                }
                                placeholder="Dado informado pelo profissional"
                                rows={3}
                                value={optionDraft.value}
                              />
                            </label>
                            <label>
                              Fonte
                              <select
                                onChange={(event) =>
                                  updateOption(activeTab.key, optionLabel, { source: event.target.value })
                                }
                                value={optionDraft.source}
                              >
                                <option value="">Selecionar fonte</option>
                                {sourceOptions.map((source) => (
                                  <option key={source}>{source}</option>
                                ))}
                              </select>
                            </label>
                          </div>
                        ) : null}
                      </article>
                    );
                  })}
                </div>
              </section>

              <aside className="campo44Panel">
                <div className="fillableHeader">
                  <div>
                    <p className="sectionLabel">Campo adicional</p>
                    <h3>Adicionar campo44</h3>
                  </div>
                </div>

                <div className="campo44Form">
                  <label>
                    Rotulo
                    <input
                      onChange={(event) => setCampo44Form({ ...campo44Form, label: event.target.value })}
                      placeholder="Ex.: rotina de estudos"
                      value={campo44Form.label}
                    />
                  </label>
                  <label>
                    Tipo
                    <select
                      onChange={(event) => setCampo44Form({ ...campo44Form, type: event.target.value })}
                      value={campo44Form.type}
                    >
                      <option value="texto">Texto</option>
                      <option value="numero">Numero</option>
                      <option value="data">Data</option>
                      <option value="lista">Lista</option>
                      <option value="sim_nao">Sim/Nao</option>
                    </select>
                  </label>
                  <label>
                    Valor
                    <textarea
                      onChange={(event) => setCampo44Form({ ...campo44Form, value: event.target.value })}
                      placeholder="Registro complementar"
                      rows={3}
                      value={campo44Form.value}
                    />
                  </label>
                  <label>
                    Fonte
                    <select
                      onChange={(event) => setCampo44Form({ ...campo44Form, source: event.target.value })}
                      value={campo44Form.source}
                    >
                      <option value="">Selecionar fonte</option>
                      {sourceOptions.map((source) => (
                        <option key={source}>{source}</option>
                      ))}
                    </select>
                  </label>
                  <label>
                    Justificativa
                    <textarea
                      onChange={(event) => setCampo44Form({ ...campo44Form, reason: event.target.value })}
                      placeholder="Motivo da inclusao"
                      rows={3}
                      value={campo44Form.reason}
                    />
                  </label>
                  {formError ? <p className="formError">{formError}</p> : null}
                  <button className="primaryButton" onClick={addCampo44} type="button">
                    Salvar campo44
                  </button>
                </div>

                <div className="campo44List">
                  {activeDraft.campo44.length ? (
                    activeDraft.campo44.map((field) => (
                      <article className="campo44Item" key={field.id}>
                        <div>
                          <strong>{field.label}</strong>
                          <small>
                            {field.type} - {field.source}
                          </small>
                        </div>
                        <p>{field.value}</p>
                        <small>{field.reason}</small>
                        <button onClick={() => removeCampo44(field.id)} type="button">
                          Remover
                        </button>
                      </article>
                    ))
                  ) : (
                    <p className="emptyNote">Nenhum campo44 nesta aba.</p>
                  )}
                </div>
              </aside>
            </div>

            <div className="reportPreviewGrid">
              <section>
                <h3>Estrutura do documento</h3>
                <ol>
                  {reportSections.map((section) => (
                    <li key={section}>{section}</li>
                  ))}
                </ol>
              </section>
              <section>
                <h3>Bloqueios antes da finalizacao</h3>
                <div className="checklist">
                  {blockers.map((blocker) => (
                    <label key={blocker}>
                      <input readOnly checked={blocker !== "Blocos de IA revisados"} type="checkbox" />
                      <span>{blocker}</span>
                    </label>
                  ))}
                </div>
              </section>
              <section className="previewText">
                <h3>Previa do rascunho</h3>
                <pre>{reportPreview}</pre>
              </section>
            </div>
          </div>

          <div className="panel widePanel">
            <p className="sectionLabel">Matriz de habilidades</p>
            <h2>Dominios avaliados</h2>
            <div className="skillGrid">
              {skillDomains.map((skill) => (
                <span key={skill}>{skill}</span>
              ))}
            </div>
          </div>
        </section>
      </section>
    </main>
  );
}

function buildPreview(tabs: FillableTab[], draft: Record<string, TabDraft>) {
  return tabs
    .map((tab) => {
      const tabDraft = draft[tab.key];
      const selected = Object.entries(tabDraft.options).filter(([, optionDraft]) => optionDraft.selected);
      const lines = [`## ${tab.label}`];

      if (!selected.length && !tabDraft.campo44.length) {
        lines.push("- [sem campos preenchidos]");
        return lines.join("\n");
      }

      selected.forEach(([label, optionDraft]) => {
        lines.push(`- ${label}: ${optionDraft.value || "[preencher]"}`);
        lines.push(`  Fonte: ${optionDraft.source || "[informar fonte]"}`);
      });

      tabDraft.campo44.forEach((field) => {
        lines.push(`- campo44 / ${field.label}: ${field.value}`);
        lines.push(`  Fonte: ${field.source}`);
        lines.push(`  Justificativa: ${field.reason}`);
      });

      return lines.join("\n");
    })
    .join("\n\n");
}
