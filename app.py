import streamlit as st
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


def MultipleInt(f, X, XR):
    # Convert the input strings to SymPy expressions
    f_expr = sympify(f)
    X_expr = [sympify(var) for var in X]

    # Create a dictionary to hold the symbols and their corresponding ranges
    variables = {var: range_ for var, range_ in zip(X_expr, XR)}

    # Call the MultipleIntegral function from the imported module
    result = MultipleIntegral(f_expr, X_expr, variables)

    # Print the LaTeX output
    print(latex(result))


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
       # Call the MultipleIntegral function
        X_Sp= sympify(X)
        XR_Sp= sympify(XR)
        f_Sp= sympify(f)
        result=MultipleIntegral_st(f_Sp, X_Sp, XR_Sp)        
        # only result was read (f) in raw format (r)
        st.latex(rf'''{result}''')

if __name__ == '__main__':
    main()