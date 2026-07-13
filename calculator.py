import streamlit as st

st.set_page_config(page_title="Pocket Calculator", layout="centered")

st.title("🧮 Pocket Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# ---------- Functions ----------
def press(value):
    st.session_state.expression += value
    st.rerun()

def clear():
    st.session_state.expression = ""
    st.rerun()

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]
    st.rerun()

def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"
    st.rerun()

# ---------- Display ----------
st.text_input(
    "Display",
    value=st.session_state.expression,
    disabled=True,
)

# ---------- Row 1 ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", use_container_width=True):
        press("7")

with col2:
    if st.button("8", use_container_width=True):
        press("8")

with col3:
    if st.button("9", use_container_width=True):
        press("9")

with col4:
    if st.button("/", use_container_width=True):
        press("/")

# ---------- Row 2 ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", use_container_width=True):
        press("4")

with col2:
    if st.button("5", use_container_width=True):
        press("5")

with col3:
    if st.button("6", use_container_width=True):
        press("6")

with col4:
    if st.button("*", use_container_width=True):
        press("*")

# ---------- Row 3 ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", use_container_width=True):
        press("1")

with col2:
    if st.button("2", use_container_width=True):
        press("2")

with col3:
    if st.button("3", use_container_width=True):
        press("3")

with col4:
    if st.button("-", use_container_width=True):
        press("-")


# ---------- Row 4 ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("0", use_container_width=True):
        press("0")

with col2:
    if st.button("00", use_container_width=True):
        press("00")

with col3:
    if st.button("000", use_container_width=True):
        press("000")

with col4:
    if st.button("+", use_container_width=True):
        press("+")
# ---------- Row 5 ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("xⁿ", use_container_width=True):
        press("**")

with col2:
    if st.button(".", use_container_width=True):
        press(".")

with col3:
    if st.button("=", type="primary", use_container_width=True):
        calculate()

with col4:
    if st.button("%", use_container_width=True):
        press("%")


# ---------- Last Row ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("C", type="secondary", use_container_width=True):
        clear()

with col2:
    if st.button("⌫", use_container_width=True):
        backspace()