import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Avaliação Tátil", layout="centered")

st.title("📋 QUESTIONÁRIO DE AVALIAÇÃO TÁTIL")
st.markdown("Este formulário destina-se à coleta de dados de perfil, estado atual e percepção após um teste de sensibilidade tátil.")

# Conexão com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Listas de opções comuns
escala_concordancia = ["Discordo Totalmente", "Discordo", "Neutro", "Concordo", "Concordo Totalmente"]
escala_1_5 = [1, 2, 3, 4, 5]
estados_br = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]
regioes_br = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

with st.form(key="tactile_form"):
    
    # --- SEÇÃO 1 ---
    st.header("SEÇÃO 1: PERFIL E ESTADO ATUAL")
    col1, col2 = st.columns(2)
    with col1:
        sexo = st.radio("1. Qual seu sexo?", ["Masculino", "Feminino", "Outro / Prefiro não dizer"])
        idade = st.number_input("2. Qual sua idade?", min_value=0, max_value=120, step=1)
    with col2:
        escolaridade = st.text_input("3. Qual seu nível de escolaridade?")
    
    proteses = st.text_area("4. Você usa próteses ou dispositivos eletrônicos (ex: marca-passos)?")
    exp_vibro = st.text_area("5. Experiência prévia com dispositivos vibrotáteis?")
    atividades_laborais = st.text_area("6. Exerce atividades que diminuem a sensibilidade tátil?")
    exposicao_fisica = st.text_area("7. Exposição a elementos físicos/químicos nas mãos?")

    st.subheader("8. Nível de concordância")
    afirmacoes = [
        "Eu estou descansado", "Eu estou concentrado", "Eu estou calmo", 
        "Eu estou com produtividade normal", "Eu estou com a visão descansada", 
        "Ausência de dor de cabeça", "Ausência de dor no braço/punho/mão (D)", 
        "Ausência de dor no braço/punho/mão (E)", "Ausência de dor em outra parte do corpo"
    ]
    respostas_concordancia = {}
    for af in afirmacoes:
        respostas_concordancia[af] = st.select_slider(af, options=escala_concordancia, value="Neutro")

    st.divider()

    # --- SEÇÃO 2 ---
    st.header("SEÇÃO 2: CENÁRIO DE AVALIAÇÃO 1")
    
    st.subheader("Questão 01")
    q2_1_relacao = st.radio("Relação expectativa de vida x atenção primária:", [
        "A) Existe uma relação positiva", 
        "B) Existe uma relação negativa", 
        "C) Não há uma relação clara"
    ])
    q2_1_ajuda = st.select_slider("Medida que a estimulação ajudou a identificar a relação:", options=escala_1_5)
    q2_1_facilidade = st.select_slider("Facilidade em identificar a relação:", options=escala_1_5)
    q2_1_facilidade_comp = st.select_slider("Facilidade em comparar cuidados primários:", options=escala_1_5)
    q2_1_eficaz = st.select_slider("Ajudou a comparar de forma mais eficaz?", options=escala_1_5)
    q2_1_modalidade = st.radio("Modalidade mais importante (Q1):", ["Visual", "Vibrotátil", "Ambas igualmente"])
    q2_1_confianca = st.select_slider("Nível de confiança (Q1):", options=escala_1_5)

    st.subheader("Questão 02")
    q2_2_menor_san = st.selectbox("Estado com menor cobertura de saneamento:", estados_br)
    q2_2_maior_san = st.selectbox("Estado com maior cobertura de saneamento:", estados_br)
    q2_2_comparacao = st.radio("Qual apresenta maior cobertura de atenção primária (vibrotátil)?", ["A) Estado com menor saneamento", "B) Estado com maior saneamento", "C) Semelhante"])
    q2_2_facilidade_id = st.select_slider("Facilidade em identificar estados (Q2):", options=escala_1_5)
    q2_2_facilidade_comp = st.select_slider("Facilidade em comparar (vibrotátil) (Q2):", options=escala_1_5)
    q2_2_eficaz = st.select_slider("Ajudou a comparar de forma mais eficaz? (Q2):", options=escala_1_5)
    q2_2_modalidade = st.radio("Modalidade mais importante (Q2):", ["Visual", "Vibrotátil", "Ambas igualmente"])
    q2_2_confianca = st.select_slider("Confiança (Q2):", options=escala_1_5)

    st.subheader("Questão 03")
    q2_3_maior_int = st.selectbox("Estado com maior taxa de internação:", estados_br)
    q2_3_menor_int = st.selectbox("Estado com menor taxa de internação:", estados_br)
    q2_3_comparacao = st.radio("Maior cobertura de atenção primária (vibrotátil)?", ["A) Estado com maior internação", "B) Estado com menor internação", "C) Semelhante"])
    q2_3_facilidade_id = st.select_slider("Facilidade em identificar estados (Q3):", options=escala_1_5)
    q2_3_facilidade_comp = st.select_slider("Facilidade em comparar (vibrotátil) (Q3):", options=escala_1_5)
    q2_3_eficaz = st.select_slider("Ajudou a comparar de forma mais eficaz? (Q3):", options=escala_1_5)
    q2_3_modalidade = st.radio("Modalidade mais importante (Q3):", ["Visual", "Vibrotátil", "Ambas igualmente"])
    q2_3_confianca = st.select_slider("Confiança (Q3):", options=escala_1_5)

    st.divider()

    # --- SEÇÃO 3 ---
    st.header("SEÇÃO 3: CENÁRIO DE AVALIAÇÃO 2")
    st.subheader("Questão 01")
    q3_1_visual = st.radio("Região com maior número de focos (Visual):", regioes_br)
    q3_1_facilidade = st.select_slider("Facilidade visual (Q1):", options=escala_1_5)
    q3_1_modalidade = st.radio("Modalidade mais importante (Q3-Q1):", ["Visual", "Vibrotátil", "Ambas igualmente"])
    q3_1_confianca = st.select_slider("Confiança (Q3-Q1):", options=escala_1_5)

    st.subheader("Questão 02")
    q3_2_maior = st.selectbox("Região com MAIOR focos:", regioes_br)
    q3_2_menor = st.selectbox("Região com MENOR focos:", regioes_br)
    q3_2_vibro = st.radio("Qual região (vibrotátil)?", ["A) Maior focos", "B) Menor focos", "C) Semelhante"])
    q3_2_facilidade_id = st.select_slider("Facilidade id regiões (Q2):", options=escala_1_5)
    q3_2_facilidade_comp = st.select_slider("Facilidade comparar regiões (vibrotátil):", options=escala_1_5)
    q3_2_eficaz = st.select_slider("Ajudou a comparar eficazmente? (Q2):", options=escala_1_5)
    q3_2_modalidade = st.radio("Modalidade mais importante (Q3-Q2):", ["Visual", "Vibrotátil", "Ambas igualmente"])
    q3_2_confianca = st.select_slider("Confiança (Q3-Q2):", options=escala_1_5)

    st.subheader("Questão 03")
    q3_3_relacao = st.radio("Relação focos x cobertura:", ["A) Positiva", "B) Negativa", "C) Sem relação clara"])
    q3_3_facilidade = st.select_slider("Facilidade identificar relação (Q3):", options=escala_1_5)
    q3_3_ajuda = st.select_slider("Medida que vibrotátil ajudou:", options=escala_1_5)
    q3_3_modalidade = st.radio("Modalidade importante (Q3-Q3):", ["Visual", "Vibrotátil", "Ambas igualmente"])
    q3_3_confianca = st.select_slider("Confiança (Q3-Q3):", options=escala_1_5)

    st.divider()

    # --- SEÇÃO 4 ---
    st.header("SEÇÃO 4: AVALIAÇÃO PERCEPTIVA")
    percebeu_mudanca = st.radio("1. Percebeu mudança na sensibilidade tátil?", ["Sim", "Não"])
    natureza_mudanca = st.text_input("2. Qual a natureza da mudança?")
    dificuldade_equip = st.radio("3. Equipamento dificultou?", ["Sim", "Não"])
    desc_dificuldade = st.text_area("4. Descreva a dificuldade:")
    distancia_elementos = st.select_slider("5. Distância entre elementos (1-Inadequada, 5-Adequada):", options=escala_1_5)
    textuais_faceis = st.text_input("6. Elementos textuais fáceis de identificar?")
    dificuldade_operar = st.text_input("7. Dificuldade em operar equipamento?")

    submit_button = st.form_submit_button(label="Enviar Respostas")

    if submit_button:
        # Criar dicionário de dados
        data = {
            "Sexo": sexo, "Idade": idade, "Escolaridade": escolaridade, "Proteses": proteses,
            "Exp_Vibrotatil": exp_vibro, "Trab_Sensibilidade": atividades_laborais, "Exp_Fisica": exposicao_fisica,
            **respostas_concordancia,
            "S2_Q1_Relacao": q2_1_relacao, "S2_Q1_Ajuda": q2_1_ajuda, "S2_Q1_Facil": q2_1_facilidade,
            "S2_Q1_Comp": q2_1_facilidade_comp, "S2_Q1_Eficaz": q2_1_eficaz, "S2_Q1_Mod": q2_1_modalidade, "S2_Q1_Conf": q2_1_confianca,
            "S2_Q2_MenorSan": q2_2_menor_san, "S2_Q2_MaiorSan": q2_2_maior_san, "S2_Q2_Comp": q2_2_comparacao,
            "S2_Q2_Id": q2_2_facilidade_id, "S2_Q2_FacilComp": q2_2_facilidade_comp, "S2_Q2_Eficaz": q2_2_eficaz, "S2_Q2_Mod": q2_2_modalidade, "S2_Q2_Conf": q2_2_confianca,
            "S2_Q3_MaiorInt": q2_3_maior_int, "S2_Q3_MenorInt": q2_3_menor_int, "S2_Q3_Comp": q2_3_comparacao,
            "S2_Q3_Id": q2_3_facilidade_id, "S2_Q3_FacilComp": q2_3_facilidade_comp, "S2_Q3_Eficaz": q2_3_eficaz, "S2_Q3_Mod": q2_3_modalidade, "S2_Q3_Conf": q2_3_confianca,
            "S3_Q1_Visual": q3_1_visual, "S3_Q1_Facil": q3_1_facilidade, "S3_Q1_Mod": q3_1_modalidade, "S3_Q1_Conf": q3_1_confianca,
            "S3_Q2_Maior": q3_2_maior, "S3_Q2_Menor": q3_2_menor, "S3_Q2_Vibro": q3_2_vibro, "S3_Q2_Id": q3_2_facilidade_id,
            "S3_Q2_Comp": q3_2_facilidade_comp, "S3_Q2_Eficaz": q3_2_eficaz, "S3_Q2_Mod": q3_2_modalidade, "S3_Q2_Conf": q3_2_confianca,
            "S3_Q3_Relacao": q3_3_relacao, "S3_Q3_Facil": q3_3_facilidade, "S3_Q3_Ajuda": q3_3_ajuda, "S3_Q3_Mod": q3_3_modalidade, "S3_Q3_Conf": q3_3_confianca,
            "S4_Percepcao": percebeu_mudanca, "S4_Nat_Mudanca": natureza_mudanca, "S4_Dificuldade_Eq": dificuldade_equip,
            "S4_Desc_Dificuldade": desc_dificuldade, "S4_Distancia": distancia_elementos, "S4_Textuais": textuais_faceis, "S4_Operar": dificuldade_operar
        }
        
        # Lógica para salvar
        try:
            df_atual = conn.read(worksheet="Sheet1", usecols=list(range(len(data))))
            df_novo = pd.DataFrame([data])
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            conn.update(worksheet="Sheet1", data=df_final)
            st.success("✅ Dados enviados com sucesso!")
            st.balloons()
        except Exception as e:
            st.error(f"Erro ao enviar: {e}")