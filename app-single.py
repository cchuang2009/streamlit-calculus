import streamlit as st
import sympy as sp
from sympy import *
from sympy.printing.latex import latex
from io import StringIO
from MultipleCalculus import *
import sys
import requests

# Import the MultipleCalculus module from GitHub
#url = 'https://raw.githubusercontent.com/cchuang2009/2022-1/main/Calculus/MultipleCalculus.py'
#exec(requests.get(url).text)

# Redirect print statements to capture LaTeX output
#output = StringIO()
#sys.stdout = output


# Streamlit app
def main():
    st.title("Multiple Integral Calculator")

    # Input variables and ranges
    col1, col2 = st.columns(2)
    with col1:
        f = st.text_input("Enter the function:",value="x*y")
    with col2:
        X = st.text_input("Enter the variables (comma-separated):","[x,y]")

    XR = st.text_input("Enter the ranges (comma-separated):","[[0,1],[0,2]]")

    if st.button("Calculate"):
        try:
            # Call the MultipleIntegral function
            X_Sp = sp.sympify(X)
            XR_Sp = sp.sympify(XR)
            f_Sp = sp.sympify(f)
            result = MultipleIntegral_st(f_Sp, X_Sp, XR_Sp)

            # Display the result in LaTeX format
            st.latex(rf"{result}")

        except (sp.SympifyError, ValueError, TypeError) as e:
            st.error("Can't be evaluated!")
            print(e)
        except NameError as e:
            st.error("Can't solve; ask your mentor to help.")
            print(e)    

if __name__ == '__main__':
    main()
