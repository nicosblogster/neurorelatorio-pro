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
                "campo44": [],
            },
        )


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
                "campo44": entry["campo44"],
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

        for index, campo44 in enumerate(entry["campo44"], start=1):
            missing = [
                label
                for label, value in {
                    "rotulo": campo44.get("label", ""),
                    "tipo": campo44.get("type", ""),
                    "valor": campo44.get("value", ""),
                    "fonte": campo44.get("source", ""),
                    "justificativa": campo44.get("reason", ""),
                }.items()
                if not str(value).strip()
            ]
            if missing:
                issues.append(
                    {
                        "severity": "blocker",
                        "message": f"{tab_label}: campo44 #{index} sem {', '.join(missing)}.",
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
        if not entry["selected_options"] and not entry["campo44"]:
            lines.append("- [sem campos preenchidos]")
            lines.append("")
            continue

        for option in entry["selected_options"]:
            value = option["value"] or "[preencher]"
            source = option["source"] or "[informar fonte]"
            lines.append(f"- {option['label']}: {value}")
            lines.append(f"  Fonte: {source}")

        for campo44 in entry["campo44"]:
            lines.append(f"- campo44 / {campo44['label']}: {campo44['value']}")
            lines.append(f"  Tipo: {campo44['type']}")
            lines.append(f"  Fonte: {campo44['source']}")
            lines.append(f"  Justificativa: {campo44['reason']}")
        lines.append("")

    return "\n".join(lines)


def add_campo44(tab_key: str, form_values: dict[str, str]) -> bool:
    required = ["label", "type", "value", "source", "reason"]
    if any(not form_values[field].strip() for field in required):
        return False

    selected_entry(tab_key)["campo44"].append(
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

st.title("NeuroRelatorio Pro")
st.caption("Editor Streamlit com abas preenchiveis, opcoes pre-definidas e campo44.")

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
    selected_options = st.multiselect(
        "Opcoes pre-definidas",
        active_tab["predefined_options"],
        default=list(active_entry["selected_options"].keys()),
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
            "Valor registrado",
            value=option_state.get("value", ""),
            key=f"{active_tab_key}_{option_label}_value",
        )
        option_state["source"] = source_col.selectbox(
            "Fonte",
            [""] + SOURCE_OPTIONS,
            index=([""] + SOURCE_OPTIONS).index(option_state.get("source", ""))
            if option_state.get("source", "") in [""] + SOURCE_OPTIONS
            else 0,
            key=f"{active_tab_key}_{option_label}_source",
        )

    st.divider()
    st.subheader("Adicionar campo44")

    with st.form(f"{active_tab_key}_campo44_form", clear_on_submit=True):
        campo_left, campo_right = st.columns(2)
        form_values = {
            "label": campo_left.text_input("Rotulo"),
            "type": campo_right.selectbox("Tipo", ["texto", "numero", "data", "lista", "sim_nao"]),
            "value": st.text_area("Valor"),
            "source": campo_left.selectbox("Fonte", [""] + SOURCE_OPTIONS),
            "evidence_id": campo_right.text_input("ID da evidencia (opcional)"),
            "reason": st.text_area("Justificativa"),
        }
        submitted = st.form_submit_button("Salvar campo44")
        if submitted:
            if add_campo44(active_tab_key, form_values):
                st.success("campo44 salvo nesta aba.")
            else:
                st.error("Preencha rotulo, tipo, valor, fonte e justificativa.")

    if active_entry["campo44"]:
        st.markdown("**Campos campo44 desta aba**")
        for index, field in enumerate(active_entry["campo44"]):
            with st.expander(f"{field['label']} - {field['source']}"):
                st.write(field["value"])
                st.caption(f"Tipo: {field['type']} | Justificativa: {field['reason']}")
                if st.button("Remover campo44", key=f"remove_{active_tab_key}_{index}"):
                    active_entry["campo44"].pop(index)
                    st.rerun()

with right:
    payload = build_payload(fillable_tabs)
    draft_text = build_draft_text(payload)
    issues = validate_payload(payload)

    st.subheader("Validacao")
    if not issues:
        st.success("Nenhuma pendencia encontrada no rascunho.")
    else:
        for issue in issues:
            if issue["severity"] == "blocker":
                st.error(issue["message"])
            else:
                st.warning(issue["message"])

    st.subheader("Previa do rascunho")
    st.text_area("Texto gerado", value=draft_text, height=360)

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
