import streamlit as st
import google.generativeai as genai

# Заголовок сайта
st.title("Моё первое AI приложение")
st.write("Привет! Я только учусь, но уже могу помочь тебе.")

# Получаем API ключ из "секретов" (об этом ниже)
api_key = st.secrets["GOOGLE_API_KEY"]

# Настройка модели
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro') # Или 'gemini-1.5-flash', если используете его

# Чат с пользователем
if "messages" not in st.session_state:
    st.session_state.messages = []

# Показываем историю сообщений
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Поле для ввода вопроса
if prompt := st.chat_input("Напишите что-нибудь..."):
    # Показываем сообщение пользователя
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Получаем ответ от AI
    response = model.generate_content(prompt)
    
    # Показываем ответ AI
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
