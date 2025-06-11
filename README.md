#  Tutor Inteligente com IA

Um assistente de estudos alimentado por IA (Google Gemini) feito com **Streamlit**!  
Faça perguntas, peça explicações, resumos ou exercícios simulados. Ideal para estudantes do ensino médio, vestibular e universitários.


---

##  Funcionalidades

-  **Explicações por matéria** (Matemática, Física, História, etc.)
-  **Respostas passo a passo**
-  **Resumos rápidos de tópicos**
-  **Geração de quizzes personalizados**
-  **Interface simples e direta feita com Streamlit**

---

##  Como usar localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/ThalesCavalcanti/Tutor-inteligente.git
cd tutor
```
2. **(Opcional) Crie um ambiente virtual**
```bash
# Criar ambiente virtual
python -m venv streamlit_env

# Ativar ambiente virtual
streamlit_env\Scripts\activate

# Desativar (quando necessário)
deactivate
```
**No linux/mac**
```bash
# Criar ambiente virtual
python3 -m venv streamlit_env

# Ativar ambiente virtual
source streamlit_env/bin/activate

# Desativar (quando necessário)
deactivate
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
4. **Adicione sua chave API do Gemini**
```ini
GEMINI_API_KEY=your_api_key_here
```
5. **Execute a aplicação**
```bash
streamlit run app.py
```
