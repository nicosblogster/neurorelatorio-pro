import json
from datetime import datetime
from pathlib import Path
from typing import Any

import streamlit as st


APP_ROOT = Path(__file__).resolve().parent
FILLABLE_TABS_PATH = APP_ROOT / "apps" / "api" / "app" / "seed" / "fillable_tabs.json"
SOURCE_OPTIONS = [
    "Observacao direta",
    "Relato familiar",
    "Relato escolar",
    "Documento apresentado",
    "Instrumento/protocolo",
]
OPTION_HELP = {
    "Nome": "Identificacao usada no documento. Prefira iniciais quando estiver testando o sistema.",
    "Data de nascimento": "Informe a data completa ou deixe claro quando for apenas relato/documento.",
    "Idade": "Pode ser preenchida manualmente quando ainda nao houver calculo automatico.",
    "Escola": "Nome da escola ou contexto escolar informado.",
    "Serie": "Ano/serie escolar atual.",
    "Turno": "Turno escolar ou periodo de atendimento.",
    "Responsaveis legais": "Nome ou vinculo dos responsaveis, conforme documento ou relato.",
    "Fonte": "Origem da informacao: observacao, relato, documento ou instrumento.",
    "Justificativa": "Explique por que o dado foi incluido e como ele ajuda a compreender o caso.",
}


def option_prompt(option_label: str) -> str:
    return f"Registro de {option_label.lower()}"


def option_placeholder(option_label: str) -> str:
    examples = {
        "Nome": "Ex.: A.M.S. ou nome completo conforme autorizacao",
        "Data de nascimento": "Ex.: 12/03/2016, conforme documento apresentado",
        "Idade": "Ex.: 9 anos e 2 meses na data da avaliacao",
        "Escola": "Ex.: Escola Municipal ..., informado pela familia",
        "Serie": "Ex.: 3o ano do Ensino Fundamental",
        "Turno": "Ex.: matutino",
        "Responsaveis legais": "Ex.: mae e pai presentes na entrevista inicial",
    }
    return examples.get(option_label, f"Descreva aqui o dado referente a {option_label.lower()}.")


def load_fillable_tabs() -> list[dict[str, Any]]:
    return json.loads(FILLABLE_TABS_PATH.read_text(encoding="utf-8"))


def ensure_state(fillable_tabs: list[dict[str, Any]]) -> None:
    if "draft" not in st.session_state:
        st.session_state.draft = {}

    for tab in fillable_tabs:
        tab_key = tab["tab_key"]
        st.session_state.draft.setdefault(
            tab_key,
            {
                "tab_label": tab["tab_label"],
                "selected_options": {},
                "additional_fields": [],
            },
        )
        entry = st.session_state.draft[tab_key]
        if "campo44" in entry and "additional_fields" not in entry:
            entry["additional_fields"] = entry.pop("campo44")


def selected_entry(tab_key: str) -> dict[str, Any]:
    return st.session_state.draft[tab_key]


def build_payload(fillable_tabs: list[dict[str, Any]]) -> dict[str, Any]:
    entries = []
    for tab in fillable_tabs:
        tab_key = tab["tab_key"]
        entry = selected_entry(tab_key)
        selected_options = [
            {
                "label": label,
                "value": values.get("value", ""),
                "source": values.get("source", ""),
            }
            for label, values in entry["selected_options"].items()
        ]
        entries.append(
            {
                "tab_key": tab_key,
                "tab_label": tab["tab_label"],
                "selected_options": selected_options,
                "additional_fields": entry["additional_fields"],
            }
        )
    return {"entries": entries}


def validate_payload(payload: dict[str, Any]) -> list[dict[str, str]]:
    issues = []
    for entry in payload["entries"]:
        tab_label = entry["tab_label"]
        for option in entry["selected_options"]:
            if not option["value"].strip():
                issues.append(
                    {
                        "severity": "warning",
                        "message": f"{tab_label}: a opcao '{option['label']}' esta sem valor.",
                    }
                )
            if not option["source"].strip():
                issues.append(
                    {
                        "severity": "warning",
                        "message": f"{tab_label}: a opcao '{option['label']}' esta sem fonte.",
                    }
                )

        for index, additional_field in enumerate(entry["additional_fields"], start=1):
            missing = [
                label
                for label, value in {
                    "rotulo": additional_field.get("label", ""),
                    "tipo": additional_field.get("type", ""),
                    "valor": additional_field.get("value", ""),
                    "fonte": additional_field.get("source", ""),
                    "justificativa": additional_field.get("reason", ""),
                }.items()
                if not str(value).strip()
            ]
            if missing:
                issues.append(
                    {
                        "severity": "blocker",
                        "message": f"{tab_label}: campo adicional #{index} sem {', '.join(missing)}.",
                    }
                )
    return issues


def build_draft_text(payload: dict[str, Any]) -> str:
    lines = [
        "RELATORIO NEUROPSICOPEDAGOGICO - RASCUNHO",
        "Documento preliminar para revisao profissional.",
        f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "",
    ]

    for entry in payload["entries"]:
        lines.append(f"## {entry['tab_label']}")
        if not entry["selected_options"] and not entry["additional_fields"]:
            lines.append("- [sem campos preenchidos]")
            lines.append("")
            continue

        for option in entry["selected_options"]:
            value = option["value"] or "[preencher]"
            source = option["source"] or "[informar fonte]"
            lines.append(f"- {option['label']}: {value}")
            lines.append(f"  Fonte: {source}")

        for additional_field in entry["additional_fields"]:
            lines.append(f"- Campo adicional justificado / {additional_field['label']}: {additional_field['value']}")
            lines.append(f"  Tipo: {additional_field['type']}")
            lines.append(f"  Fonte: {additional_field['source']}")
            lines.append(f"  Justificativa: {additional_field['reason']}")
        lines.append("")

    return "\n".join(lines)


def add_additional_field(tab_key: str, form_values: dict[str, str]) -> bool:
    required = ["label", "type", "value", "source", "reason"]
    if any(not form_values[field].strip() for field in required):
        return False

    selected_entry(tab_key)["additional_fields"].append(
        {
            "label": form_values["label"].strip(),
            "type": form_values["type"],
            "value": form_values["value"].strip(),
            "source": form_values["source"],
            "reason": form_values["reason"].strip(),
            "evidence_id": form_values.get("evidence_id", "").strip(),
        }
    )
    return True


st.set_page_config(page_title="NeuroRelatorio Pro", layout="wide")

fillable_tabs = load_fillable_tabs()
ensure_state(fillable_tabs)

st.markdown(
    """
    <style>
    .npro-intro {
        border: 1px solid rgba(49, 91, 101, 0.22);
        border-radius: 12px;
        padding: 1rem 1.1rem;
        background: linear-gradient(135deg, rgba(37, 111, 122, 0.12), rgba(255, 255, 255, 0.02));
        margin-bottom: 1.2rem;
    }
    .npro-intro strong {
        color: #9bdad5;
    }
    .npro-note {
        border-left: 4px solid #2f8f83;
        padding: 0.85rem 1rem;
        background: rgba(47, 143, 131, 0.10);
        border-radius: 0.35rem;
        margin: 0.8rem 0 1rem;
    }
    .npro-additional-field {
        border: 1px solid rgba(255, 193, 7, 0.35);
        border-radius: 12px;
        padding: 1rem;
        background: rgba(255, 193, 7, 0.08);
        margin-top: 1rem;
    }
    .npro-additional-field ul {
        margin-bottom: 0;
    }
    .npro-mini-title {
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("NeuroRelatorio Pro")
st.markdown(
    """
    <div class="npro-intro">
      <strong>Fluxo de preenchimento:</strong> escolha uma aba no menu lateral, selecione apenas os campos que deseja registrar,
      informe o dado e a fonte. Use <strong>Campo adicional justificado</strong> somente quando a informacao importante nao existir nas opcoes pre-definidas.
    </div>
    """,
    unsafe_allow_html=True,
)

tab_labels = [tab["tab_label"] for tab in fillable_tabs]
selected_label = st.sidebar.radio("Abas preenchiveis", tab_labels)
active_tab = next(tab for tab in fillable_tabs if tab["tab_label"] == selected_label)
active_tab_key = active_tab["tab_key"]
active_entry = selected_entry(active_tab_key)

st.sidebar.divider()
st.sidebar.write("Publicacao")
st.sidebar.caption("Este app pode ser publicado no Streamlit Community Cloud a partir do GitHub.")

left, right = st.columns([0.62, 0.38], gap="large")

with left:
    st.subheader(active_tab["tab_label"])
    st.markdown(
        """
        <div class="npro-note">
        Selecione abaixo os campos que deseja preencher nesta aba. Cada campo selecionado deve ter
        uma informacao objetiva e a fonte de onde ela veio.
        </div>
        """,
        unsafe_allow_html=True,
    )
    selected_options = st.multiselect(
        "Campos disponiveis nesta aba",
        active_tab["predefined_options"],
        default=list(active_entry["selected_options"].keys()),
        help="Estas sao as opcoes padronizadas para manter o relatorio organizado e consistente.",
        key=f"{active_tab_key}_selected_options",
    )

    active_entry["selected_options"] = {
        label: active_entry["selected_options"].get(label, {"value": "", "source": ""})
        for label in selected_options
    }

    for option_label in selected_options:
        st.markdown(f"**{option_label}**")
        value_col, source_col = st.columns([0.68, 0.32])
        option_state = active_entry["selected_options"][option_label]
        option_state["value"] = value_col.text_area(
            option_prompt(option_label),
            value=option_state.get("value", ""),
            placeholder=option_placeholder(option_label),
            help=OPTION_HELP.get(option_label, "Registre somente informacoes fornecidas, observadas ou documentadas."),
            key=f"{active_tab_key}_{option_label}_value",
        )
        option_state["source"] = source_col.selectbox(
            f"Fonte de {option_label.lower()}",
            [""] + SOURCE_OPTIONS,
            index=([""] + SOURCE_OPTIONS).index(option_state.get("source", ""))
            if option_state.get("source", "") in [""] + SOURCE_OPTIONS
            else 0,
            help="Informe a origem do dado para manter rastreabilidade clinica.",
            key=f"{active_tab_key}_{option_label}_source",
        )

    st.divider()
    st.subheader("Campo adicional justificado")
    st.markdown(
        """
        <div class="npro-additional-field">
        <div class="npro-mini-title">Quando usar?</div>
        Use este recurso para registrar uma informacao relevante que nao aparece nas opcoes desta aba.
        <br><br>
        <div class="npro-mini-title">Como preencher?</div>
        <ul>
          <li><strong>Rotulo:</strong> nome curto do novo campo, por exemplo "rotina de estudos".</li>
          <li><strong>Tipo:</strong> formato da resposta: texto, numero, data, lista ou sim/nao.</li>
          <li><strong>Valor:</strong> dado informado ou observado, sem interpretacao automatica.</li>
          <li><strong>Fonte:</strong> origem da informacao.</li>
          <li><strong>Justificativa:</strong> por que esse campo extra precisa entrar no relatorio.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form(f"{active_tab_key}_additional_field_form", clear_on_submit=True):
        campo_left, campo_right = st.columns(2)
        form_values = {
            "label": campo_left.text_input(
                "Rotulo do campo extra",
                placeholder="Ex.: rotina de estudos",
                help="Use um nome curto e claro para identificar a informacao.",
            ),
            "type": campo_right.selectbox(
                "Tipo de resposta",
                ["texto", "numero", "data", "lista", "sim_nao"],
                help="Escolha o formato que melhor representa o dado.",
            ),
            "value": st.text_area(
                "Conteudo do campo adicional",
                placeholder="Ex.: realiza tarefas com supervisao familiar tres vezes por semana.",
                help="Escreva o dado concreto. Evite conclusoes que nao estejam sustentadas por evidencia.",
            ),
            "source": campo_left.selectbox(
                "Fonte do campo adicional",
                [""] + SOURCE_OPTIONS,
                help="Campo obrigatorio para permitir rastreabilidade.",
            ),
            "evidence_id": campo_right.text_input(
                "ID da evidencia (opcional)",
                placeholder="Ex.: entrevista-01",
                help="Use se houver um codigo interno para documento, sessao ou evidencia.",
            ),
            "reason": st.text_area(
                "Justificativa para adicionar este campo",
                placeholder="Ex.: informacao necessaria para orientar recomendacoes escolares.",
                help="Explique por que as opcoes pre-definidas nao foram suficientes.",
            ),
        }
        submitted = st.form_submit_button("Salvar campo adicional")
        if submitted:
            if add_additional_field(active_tab_key, form_values):
                st.success("Campo adicional salvo nesta aba.")
            else:
                st.error("Preencha rotulo, tipo, valor, fonte e justificativa.")

    if active_entry["additional_fields"]:
        st.markdown("**Campos adicionais desta aba**")
        for index, field in enumerate(active_entry["additional_fields"]):
            with st.expander(f"{field['label']} - {field['source']}"):
                st.write(field["value"])
                st.caption(f"Tipo: {field['type']} | Justificativa: {field['reason']}")
                if st.button("Remover campo adicional", key=f"remove_{active_tab_key}_{index}"):
                    active_entry["additional_fields"].pop(index)
                    st.rerun()

with right:
    payload = build_payload(fillable_tabs)
    draft_text = build_draft_text(payload)
    issues = validate_payload(payload)

    st.subheader("Pendencias do preenchimento")
    if not issues:
        st.success("Nenhuma pendencia encontrada no rascunho.")
    else:
        st.caption("Revise estes pontos antes de exportar ou usar o texto em documento profissional.")
        for issue in issues:
            if issue["severity"] == "blocker":
                st.error(issue["message"])
            else:
                st.warning(issue["message"])

    st.subheader("Previa do rascunho")
    st.caption("Texto organizado a partir dos campos preenchidos. Revise antes de usar.")
    st.text_area("Rascunho estruturado", value=draft_text, height=360)

    st.download_button(
        "Baixar rascunho TXT",
        data=draft_text,
        file_name="neurorelatorio-rascunho.txt",
        mime="text/plain",
    )
    st.download_button(
        "Baixar dados JSON",
        data=json.dumps(payload, ensure_ascii=False, indent=2),
        file_name="neurorelatorio-rascunho.json",
        mime="application/json",
    )

    with st.expander("Ver JSON estruturado"):
        st.json(payload)
