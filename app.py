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


# Streamlit app
# Streamlit app
# Streamlit app
# Streamlit app
# Streamlit app
# Streamlit app
def main():
    st.title("Multiple Integral Calculator")

    # Add option selection
    integral_type = st.selectbox("Select Integral Type", ["Multiple Integral (In Cartesian Coordinated)", "Triple Integral (Spherical)", "Triple Integral (Cylindrical)"])

    # Input variables and ranges based on the selected integral type
    if integral_type == "Multiple Integral (In Cartesian Coordinated)":
        col1, col2 = st.columns(2)
        with col1:
            f = st.text_input("Enter the function:", value="x*y")
        with col2:
            X = st.text_input("Enter the variables (comma-separated):", "[x,y]")
        XR = st.text_input("Enter the ranges (comma-separated):", "[[0,1],[0,2]]")
    elif integral_type == "Triple Integral (Spherical)":
        col1, col2, col3 = st.columns(3)
        with col1:
            f = st.text_input("Enter the function:", value="y**2")
        with col2:
            X = st.text_input("Enter the variables (comma-separated):", "[x,y,z]")
        with col3:
            U = st.text_input("Enter the variables for ranges (comma-separated):", "[ρ,φ,θ]")
        col4, col5, col6 = st.columns(3) 
        with col4:
            XR = st.text_input("Range of ρ:", "[0,1]")
        with col5:
            XT = st.text_input("Range of φ:", "[0,pi]")  
        with col6:
            XP = st.text_input("Range of θ:", "[0,pi/2]")    
        
    elif integral_type == "Triple Integral (Cylindrical)":
        col1, col2, col3 = st.columns(3)
        with col1:
            f = st.text_input("Enter the function:", value="x*y*z")
        with col2:
            X = st.text_input("Enter the variables (comma-separated):", "[x,y,z]")
        with col3:
            U = st.text_input("Enter the variables for ranges (comma-separated):", "[r,θ,z]")
        col4, col5, col6 = st.columns(3) 
        with col4:
            XR = st.text_input("Range of r:", "[0,1]")
        with col5:
            XT = st.text_input("Range of θ:", "[0,2*pi]")  
        with col6:
            XP = st.text_input("Range of z:", "[0,3]")
            #XR = st.text_input("Enter the ranges (comma-separated):", "[[0,1],[0,2*pi],[0,3]]")

    if st.button("Calculate"):
        X_Sp = sympify(X)
        f_Sp = sympify(f)
        

        if integral_type == "Multiple Integral (In Cartesian Coordinated)":
            XR_Sp = sympify(XR)
            result = MultipleIntegral(f_Sp, X_Sp, XR_Sp)
            
        elif integral_type == "Triple Integral (Spherical)":
            # Default coordinate transformation
            XU = "[rho*cos(theta)*sin(phi),rho*sin(theta)*sin(phi),rho*cos(phi)]"
            
            U_Sp = sympify(U)
            XU_Sp = sympify(XU)
            XR_Sp= sympify(XR)
            XT_Sp= sympify(XT)
            XP_Sp= sympify(XP)
            
            result = TripleInt_Spherical_st(f_Sp, X_Sp, XU_Sp, U_Sp, XR_Sp, XT_Sp, XP_Sp)
            #st.write(r"$ρ θ φ\frac{\pi^{2} ρ^{2} \sin{\left(φ \right)}}{24}$")
        elif integral_type == "Triple Integral (Cylindrical)":
            XU = "[r*cos(theta),r*sin(theta),z]"
            
            U_Sp = sympify(U)
            XU_Sp = sympify(XU)
            XR_Sp= sympify(XR)
            XT_Sp= sympify(XT)
            XP_Sp= sympify(XP)
            result = TripleInt_Cylind_st(f_Sp, X_Sp, XU_Sp, U_Sp, XR_Sp, XT_Sp, XP_Sp)

        # Display the result
        st.latex(rf'''{result}''')
if __name__ == '__main__':
    main()
