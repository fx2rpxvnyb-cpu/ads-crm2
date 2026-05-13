import streamlit as st
import pandas as pd
from datetime import datetime

# ===================== НАСТРОЙКИ =====================
st.set_page_config(
    page_title="АДС CRM",
    page_icon="🏗️",
    layout="wide"
)

# ===================== ПОЛЬЗОВАТЕЛИ =====================
USERS = {
    "admin": {"password": "admin123", "role": "Администратор"},
    "director": {"password": "director123", "role": "Директор"},
}

# ===================== SESSION STATE =====================
def init_state():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""

    if "role" not in st.session_state:
        st.session_state.role = ""

    if "employees" not in st.session_state:
        st.session_state.employees = [
            {"Имя": "Иван Петров", "Должность": "Прораб", "Статус": "На объекте"},
            {"Имя": "Сергей Кузнецов", "Должность": "Электрик", "Статус": "На складе"},
        ]

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    if "messages" not in st.session_state:
        st.session_state.messages = []

init_state()

# ===================== АВТОРИЗАЦИЯ =====================
if not st.session_state.logged_in:
    st.title("🔐 Вход в АДС CRM")

    username = st.text_input("Логин")
    password = st.text_input("Пароль", type="password")

    if st.button("Войти"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = USERS[username]["role"]
            st.success("Вход выполнен")
            st.rerun()
        else:
            st.warning("Введите сообщение")
