import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations.")

st.divider()

# User Inputs
num1 = st.text_input("Enter First Number")
num2 = st.text_input("Enter Second Number")

operation = st.selectbox(
    "Choose Operation",
    (
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division"
    )
)

if st.button("Calculate"):

    try:
        # Convert inputs to float
        number1 = float(num1)
        number2 = float(num2)

        # Perform calculation
        if operation == "Addition":
            result = number1 + number2

        elif operation == "Subtraction":
            result = number1 - number2

        elif operation == "Multiplication":
            result = number1 * number2

        elif operation == "Division":
            if number2 == 0:
                raise ZeroDivisionError
            result = number1 / number2

        st.success(f"Result = {result}")

    except ValueError:
        st.error("Please enter valid numeric values.")

    except ZeroDivisionError:
        st.error("Cannot divide by zero.")

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")