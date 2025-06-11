import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carrega a chave da API do arquivo .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Inicializa o modelo
model = genai.GenerativeModel("gemini-pro")

# Lista de matérias disponíveis
subjects = [
    "Matemática", "Física", "Química", "História",
    "Geografia", "Biologia", "Português", "Inglês"
]

st.set_page_config(page_title="Tutor Inteligente", page_icon="📚")
st.title("Tutor Inteligente com IA")
st.write("Seu assistente de estudos com explicações, resumos e quizzes!")

# Seleção de matéria
subject = st.selectbox("Escolha uma matéria:", subjects)

# Tipo de atividade
task = st.radio("O que você deseja?", ["Explicação", "Resumo", "Gerar Quiz"])

# Entrada de conteúdo
prompt = st.text_area("Digite sua dúvida, tópico ou conteúdo:", height=150)

# Botão para gerar
if st.button("🔍 Obter Resposta"):
    with st.spinner("Consultando a IA..."):
        try:
            if task == "Explicação":
                user_input = f"Explique detalhadamente sobre {prompt}, na matéria de {subject}."
            elif task == "Resumo":
                user_input = f"Resuma o seguinte conteúdo de {subject}: {prompt}"
            elif task == "Gerar Quiz":
                user_input = f"Crie 5 questões de múltipla escolha com respostas corretas sobre: {prompt} (matéria: {subject})."

            response = model.generate_content(user_input)
            st.markdown("###  Resposta da IA:")
            st.write(response.text)

        except Exception as e:
            st.error(" Erro ao gerar resposta. Verifique sua conexão ou chave da API.")
            st.exception(e)

st.markdown("---")
st.caption("Desenvolvido com Streamlit + Gemini")
