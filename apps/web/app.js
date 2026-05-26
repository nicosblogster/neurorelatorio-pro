const TABS = window.FILLABLE_TABS || [];
const STORAGE_KEY = "neurorelatorio-pro-draft-v1";
const SOURCES = [
  "",
  "Observacao direta",
  "Relato familiar",
  "Relato escolar",
  "Documento apresentado",
  "Instrumento/protocolo"
];

const elements = {
  tabList: document.querySelector("#tabList"),
  currentTabTitle: document.querySelector("#currentTabTitle"),
  optionsTitle: document.querySelector("#optionsTitle"),
  completionBadge: document.querySelector("#completionBadge"),
  optionsList: document.querySelector("#optionsList"),
  toggleCampo44Button: document.querySelector("#toggleCampo44Button"),
  campo44Form: document.querySelector("#campo44Form"),
  campo44Label: document.querySelector("#campo44Label"),
  campo44Type: document.querySelector("#campo44Type"),
  campo44Value: document.querySelector("#campo44Value"),
  campo44Source: document.querySelector("#campo44Source"),
  campo44Reason: document.querySelector("#campo44Reason"),
  customFieldsList: document.querySelector("#customFieldsList"),
  reportPreview: document.querySelector("#reportPreview"),
  copyButton: document.querySelector("#copyButton"),
  exportButton: document.querySelector("#exportButton"),
  resetButton: document.querySelector("#resetButton"),
  saveStatus: document.querySelector("#saveStatus")
};

const state = loadState();

function createEmptyEntries() {
  return TABS.reduce((acc, tab) => {
    acc[tab.key] = {
      options: tab.options.reduce((optionAcc, option) => {
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

function loadState() {
  const baseState = {
    activeTab: TABS[0]?.key || "",
    entries: createEmptyEntries()
  };

  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
    if (!saved?.entries) return baseState;

    TABS.forEach((tab) => {
      const savedTab = saved.entries[tab.key];
      if (!savedTab) return;

      tab.options.forEach((option) => {
        const savedOption = savedTab.options?.[option];
        if (savedOption) {
          baseState.entries[tab.key].options[option] = {
            selected: Boolean(savedOption.selected),
            value: savedOption.value || "",
            source: savedOption.source || ""
          };
        }
      });

      baseState.entries[tab.key].campo44 = Array.isArray(savedTab.campo44)
        ? savedTab.campo44
        : [];
    });

    if (TABS.some((tab) => tab.key === saved.activeTab)) {
      baseState.activeTab = saved.activeTab;
    }
  } catch {
    return baseState;
  }

  return baseState;
}

function persist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  elements.saveStatus.textContent = "Salvo localmente";
  window.clearTimeout(persist.timer);
  persist.timer = window.setTimeout(() => {
    elements.saveStatus.textContent = "Pronto";
  }, 1400);
}

function getActiveTab() {
  return TABS.find((tab) => tab.key === state.activeTab) || TABS[0];
}

function getTabEntry(tabKey) {
  return state.entries[tabKey];
}

function getSelectedCount(tabKey) {
  const entry = getTabEntry(tabKey);
  const selectedOptions = Object.values(entry.options).filter((option) => option.selected).length;
  return selectedOptions + entry.campo44.length;
}

function render() {
  renderTabs();
  renderCurrentTab();
  renderPreview();
}

function renderTabs() {
  elements.tabList.replaceChildren();

  TABS.forEach((tab) => {
    const button = document.createElement("button");
    button.className = `tab-button${tab.key === state.activeTab ? " is-active" : ""}`;
    button.type = "button";
    button.setAttribute("aria-current", tab.key === state.activeTab ? "page" : "false");
    button.addEventListener("click", () => {
      state.activeTab = tab.key;
      elements.campo44Form.classList.add("is-hidden");
      persist();
      render();
    });

    const label = document.createElement("span");
    label.textContent = tab.label;

    const count = document.createElement("span");
    count.className = "tab-count";
    count.textContent = getSelectedCount(tab.key);

    button.append(label, count);
    elements.tabList.append(button);
  });
}

function renderCurrentTab() {
  const tab = getActiveTab();
  const entry = getTabEntry(tab.key);
  const selectedOptions = Object.values(entry.options).filter((option) => option.selected).length;

  elements.currentTabTitle.textContent = tab.label;
  elements.optionsTitle.textContent = tab.label;
  elements.completionBadge.textContent = `${selectedOptions} selecionados`;
  elements.optionsList.replaceChildren();

  tab.options.forEach((optionLabel) => {
    const optionState = entry.options[optionLabel];
    const row = createOptionRow(tab.key, optionLabel, optionState);
    elements.optionsList.append(row);
  });

  renderCustomFields(tab.key);
}

function createOptionRow(tabKey, optionLabel, optionState) {
  const row = document.createElement("article");
  row.className = "option-row";

  const summary = document.createElement("div");
  summary.className = "option-summary";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = optionState.selected;
  checkbox.setAttribute("aria-label", optionLabel);
  checkbox.addEventListener("change", () => {
    optionState.selected = checkbox.checked;
    persist();
    renderTabs();
    renderCurrentTab();
    renderPreview();
  });

  const title = document.createElement("span");
  title.className = "option-title";
  title.textContent = optionLabel;

  const source = document.createElement("span");
  source.className = "option-source";
  source.textContent = optionState.source || "Fonte pendente";

  summary.append(checkbox, title, source);

  const details = document.createElement("div");
  details.className = `option-details${optionState.selected ? "" : " is-hidden"}`;

  const valueLabel = document.createElement("label");
  valueLabel.textContent = "Valor registrado";
  const valueInput = document.createElement("textarea");
  valueInput.rows = 3;
  valueInput.value = optionState.value;
  valueInput.placeholder = "Dado informado pelo profissional";
  valueInput.addEventListener("input", () => {
    optionState.value = valueInput.value;
    persist();
    renderPreview();
  });
  valueLabel.append(valueInput);

  const sourceLabel = document.createElement("label");
  sourceLabel.textContent = "Fonte";
  const sourceSelect = document.createElement("select");
  SOURCES.forEach((sourceName) => {
    const option = document.createElement("option");
    option.value = sourceName;
    option.textContent = sourceName || "Selecionar fonte";
    sourceSelect.append(option);
  });
  sourceSelect.value = optionState.source;
  sourceSelect.addEventListener("change", () => {
    optionState.source = sourceSelect.value;
    source.textContent = optionState.source || "Fonte pendente";
    persist();
    renderPreview();
  });
  sourceLabel.append(sourceSelect);

  details.append(valueLabel, sourceLabel);
  row.append(summary, details);

  return row;
}

function renderCustomFields(tabKey) {
  const entry = getTabEntry(tabKey);
  elements.customFieldsList.replaceChildren();

  if (!entry.campo44.length) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = "Nenhum campo44 adicionado nesta aba.";
    elements.customFieldsList.append(empty);
    return;
  }

  entry.campo44.forEach((field) => {
    const item = document.createElement("article");
    item.className = "custom-field";

    const header = document.createElement("div");
    header.className = "custom-field-header";

    const title = document.createElement("h4");
    title.textContent = field.label;

    const remove = document.createElement("button");
    remove.className = "remove-field";
    remove.type = "button";
    remove.setAttribute("aria-label", `Remover ${field.label}`);
    remove.textContent = "x";
    remove.addEventListener("click", () => {
      entry.campo44 = entry.campo44.filter((currentField) => currentField.id !== field.id);
      persist();
      render();
    });

    header.append(title, remove);

    const value = document.createElement("p");
    value.textContent = field.value;

    const meta = document.createElement("div");
    meta.className = "field-meta";
    [field.type, field.source, field.reason].forEach((text) => {
      const pill = document.createElement("span");
      pill.textContent = text;
      meta.append(pill);
    });

    item.append(header, value, meta);
    elements.customFieldsList.append(item);
  });
}

function handleCampo44Submit(event) {
  event.preventDefault();

  const field = {
    id: `${Date.now()}-${Math.random().toString(16).slice(2)}`,
    label: elements.campo44Label.value.trim(),
    type: elements.campo44Type.value,
    value: elements.campo44Value.value.trim(),
    source: elements.campo44Source.value,
    reason: elements.campo44Reason.value.trim()
  };

  if (!field.label || !field.value || !field.source || !field.reason) {
    showToast("Preencha rotulo, valor, fonte e justificativa do campo44.", true);
    return;
  }

  getTabEntry(state.activeTab).campo44.push(field);
  elements.campo44Form.reset();
  elements.campo44Form.classList.add("is-hidden");
  persist();
  render();
  showToast("campo44 salvo nesta aba.");
}

function buildReportData() {
  return TABS.map((tab) => {
    const entry = getTabEntry(tab.key);
    const selectedOptions = Object.entries(entry.options)
      .filter(([, value]) => value.selected)
      .map(([label, value]) => ({
        label,
        value: value.value || "[preencher]",
        source: value.source || "[informar fonte]"
      }));

    return {
      tab_key: tab.key,
      tab_label: tab.label,
      selected_options: selectedOptions,
      campo44: entry.campo44
    };
  });
}

function buildDraftText() {
  const sections = buildReportData().map((section) => {
    const lines = [`## ${section.tab_label}`];

    if (!section.selected_options.length && !section.campo44.length) {
      lines.push("- [sem campos preenchidos]");
      return lines.join("\n");
    }

    section.selected_options.forEach((option) => {
      lines.push(`- ${option.label}: ${option.value}`);
      lines.push(`  Fonte: ${option.source}`);
    });

    section.campo44.forEach((field) => {
      lines.push(`- campo44 / ${field.label}: ${field.value}`);
      lines.push(`  Tipo: ${field.type}`);
      lines.push(`  Fonte: ${field.source}`);
      lines.push(`  Justificativa: ${field.reason}`);
    });

    return lines.join("\n");
  });

  return [
    "RELATORIO NEUROPSICOPEDAGOGICO - RASCUNHO",
    "Documento preliminar para revisao profissional.",
    "",
    sections.join("\n\n")
  ].join("\n");
}

function renderPreview() {
  elements.reportPreview.textContent = buildDraftText();
}

async function copyDraft() {
  const text = buildDraftText();
  try {
    await navigator.clipboard.writeText(text);
    showToast("Rascunho copiado.");
  } catch {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.append(textarea);
    textarea.select();
    document.execCommand("copy");
    textarea.remove();
    showToast("Rascunho copiado.");
  }
}

function exportJson() {
  const blob = new Blob([JSON.stringify(buildReportData(), null, 2)], {
    type: "application/json"
  });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "neurorelatorio-rascunho.json";
  link.click();
  URL.revokeObjectURL(url);
}

function resetDraft() {
  if (!window.confirm("Limpar todo o preenchimento local?")) return;
  localStorage.removeItem(STORAGE_KEY);
  const cleanState = loadState();
  state.activeTab = cleanState.activeTab;
  state.entries = cleanState.entries;
  elements.campo44Form.reset();
  elements.campo44Form.classList.add("is-hidden");
  persist();
  render();
}

function showToast(message, isError = false) {
  const toast = document.createElement("div");
  toast.className = `toast${isError ? " is-error" : ""}`;
  toast.textContent = message;
  document.body.append(toast);
  window.setTimeout(() => toast.remove(), 2600);
}

elements.toggleCampo44Button.addEventListener("click", () => {
  elements.campo44Form.classList.toggle("is-hidden");
  if (!elements.campo44Form.classList.contains("is-hidden")) {
    elements.campo44Label.focus();
  }
});

elements.campo44Form.addEventListener("submit", handleCampo44Submit);
elements.copyButton.addEventListener("click", copyDraft);
elements.exportButton.addEventListener("click", exportJson);
elements.resetButton.addEventListener("click", resetDraft);

render();
