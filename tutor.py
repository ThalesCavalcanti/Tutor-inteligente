import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carregar chave da API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("gemini-1.5-flash")


st.set_page_config(page_title="Tutor IA")
st.title("Tutor Inteligente com Gemini")
st.write("Use a IA para explicar, resumir ou testar seu conhecimento!")

subjects = ["Matemática", "Física", "História", "Geografia", "Português"]
subject = st.selectbox("Escolha a matéria:", subjects)
task = st.radio("Tipo de ajuda:", ["Explicação", "Resumo", "Quiz"])
user_input = st.text_area("Descreva o que você quer saber:")


if "quiz_gerado" not in st.session_state:
    st.session_state.quiz_gerado = False
if "quiz_texto" not in st.session_state:
    st.session_state.quiz_texto = ""
if "gabarito" not in st.session_state:
    st.session_state.gabarito = {}


if st.button("Gerar resposta"):
    with st.spinner("A IA está gerando o conteúdo..."):
        try:
            if task == "Explicação":
                prompt = f"Explique o seguinte conteúdo de {subject}: {user_input}"
                response = model.generate_content(prompt)
                st.subheader("Explicação:")
                st.write(response.text)
                st.session_state.quiz_gerado = False

            elif task == "Resumo":
                prompt = f"Resuma o seguinte conteúdo de {subject}: {user_input}"
                response = model.generate_content(prompt)
                st.subheader("Resumo:")
                st.write(response.text)
                st.session_state.quiz_gerado = False

            elif task == "Quiz":
                prompt = (
                    f"Crie 3 perguntas de múltipla escolha com 4 alternativas cada "
                    f"(a, b, c, d) sobre {user_input} na matéria {subject}. "
                    "Inclua o gabarito no final no formato 'Respostas: 1:b 2:a 3:d'"
                )
                response = model.generate_content(prompt)
                quiz_text = response.text

                
                parts = quiz_text.strip().split("Respostas:")
                perguntas = parts[0].strip()
                respostas = parts[1].strip() if len(parts) > 1 else ""

                
                gabarito = {}
                for item in respostas.split():
                    if ':' in item:
                        num, letra = item.split(':')
                        gabarito[num] = letra.lower()

                
                st.session_state.quiz_texto = perguntas
                st.session_state.gabarito = gabarito
                st.session_state.quiz_gerado = True

        except Exception as e:
            st.error("Erro ao gerar resposta.")
            st.exception(e)


if st.session_state.quiz_gerado:
    st.subheader("Quiz gerado:")
    st.markdown(st.session_state.quiz_texto)

    respostas_usuario = {}
    for i in range(1, 4):
        respostas_usuario[str(i)] = st.radio(
            f"Pergunta {i}:", ["a", "b", "c", "d"], key=f"resposta_{i}"
        )

    if st.button("Ver resultado"):
        acertos = 0
        for i in range(1, 4):
            correta = st.session_state.gabarito.get(str(i), "")
            if respostas_usuario[str(i)] == correta:
                acertos += 1
        st.success(f"Você acertou {acertos} de 3 perguntas.")
