import streamlit as st
from sympy import *
from sympy.printing.latex import latex
from MultipleCalculus import *

def main():
    st.title("Multiple Integral Calculator")

    integral_type = st.selectbox("Select Integral Type", [
        "Multiple Integral (In Cartesian Coordinated)", 
        "Double Integral (Polar)",
        "Triple Integral (Cylindrical)", 
        "Triple Integral (Spherical)",
        "Triple Integral (General Coordinate [U,V,W])"
    ])

    if integral_type == "Multiple Integral (In Cartesian Coordinated)":
        f = st.text_input("Enter the function:", value="x*y")
        X = st.text_input("Enter the variables (comma-separated):", "[x,y]")
        XR = st.text_input("Enter the ranges (e.g. [[0,1],[0,2]]):", "[[0,1],[0,2]]")

    elif integral_type == "Double Integral (Polar)":
        f = st.text_input("Enter the function:", value="x**2 + y**2")
        U = st.text_input("Polar variables integration order (e.g. [r,theta] or [theta,r]):", "[r,theta]")
        U_range = st.text_input("Range of [r,theta] (e.g. [[0,1],[0,pi/2]]:", "[[0,1],[0,pi/2]]")
        #theta_range = st.text_input("Range of θ (e.g. [0,2*pi]):", "[0,2*pi]")

    elif integral_type == "Triple Integral (Cylindrical)":
        f = st.text_input("Enter the function:", value="x*y*z")
        X = st.text_input("Cartesian variables (e.g. [x,y,z]):", "[x,y,z]")
        U = st.text_input("Cylindrical variables (e.g. [r,theta,z]):", "[r,theta,z]")
        rR = st.text_input("Range of r:", "[0,1]")
        tR = st.text_input("Range of θ:", "[0,2*pi]")
        zR = st.text_input("Range of z:", "[0,3]")

    elif integral_type == "Triple Integral (Spherical)":
        f = st.text_input("Enter the function:", value="y**2")
        X = st.text_input("Cartesian variables (e.g. [x,y,z]):", "[x,y,z]")
        U = st.text_input("Spherical variables (e.g. [rho,theta,phi]):", "[rho,theta,phi]")
        rhoR = st.text_input("Range of ρ:", "[0,1]")
        phiR = st.text_input("Range of φ:", "[0,pi]")
        thetaR = st.text_input("Range of θ:", "[0,pi/2]")

    elif integral_type == "Triple Integral (General Coordinate [U,V,W])":
        f = st.text_input("Enter the function:", value="x*y*z")
        X = st.text_input("Cartesian variables (e.g. [x,y,z]):", "[x,y,z]")
        U = st.text_input("General coordinates (e.g. [u,v,w]):", "[u,v,w]")
        XU = st.text_input("Transform to Cartesian (e.g. [u+v, v+w, u-v]):", "[u+v, v+w, u-v]")
        xR = st.text_input("Range of u:", "[0,1]")
        yR = st.text_input("Range of v:", "[0,1]")
        zR = st.text_input("Range of w:", "[0,1]")

    if st.button("Calculate"):
        f_Sp = sympify(f)

        if integral_type == "Multiple Integral (In Cartesian Coordinated)":
            X_Sp = sympify(X)
            XR_Sp = sympify(XR)
            result = MultipleIntegral(f_Sp, X_Sp, XR_Sp)

        elif integral_type == "Double Integral (Polar)":
            f_Sp = sympify(f)
            U_Sp = sympify(U)
            Ur_Sp = sympify(U_range)
            
            f_Sp = f_Sp.replace(
                      lambda expr: expr.is_Add and set(expr.args) == {x**2, y**2},
                      lambda _: r**2
    )
            result = PolarDoubleIntegration(f_Sp, U_Sp, Ur_Sp)

        elif integral_type == "Triple Integral (Cylindrical)":
            X_Sp = sympify(X)
            U_Sp = sympify(U)
            XU = "[r*cos(theta),r*sin(theta),z]"
            XU_Sp = sympify(XU)
            rR_Sp = sympify(rR)
            tR_Sp = sympify(tR)
            zR_Sp = sympify(zR)
            #f_Sp = f_Sp.replace(
            #            lambda expr: expr.is_Add and set(expr.args) == {x**2, y**2},
            #            lambda _: r**2
            #          )
            result = TripleInt_Cylind_st(f_Sp, X_Sp, XU_Sp, U_Sp, rR_Sp, tR_Sp, zR_Sp)

        elif integral_type == "Triple Integral (Spherical)":
            X_Sp = sympify(X)
            U_Sp = sympify(U)
            XU = "[rho*cos(theta)*sin(phi), rho*sin(theta)*sin(phi), rho*cos(phi)]"
            XU_Sp = sympify(XU)
            rhoR_Sp = sympify(rhoR)
            phiR_Sp = sympify(phiR)
            thetaR_Sp = sympify(thetaR)
            result = TripleInt_Spherical_st(f_Sp, X_Sp, XU_Sp, U_Sp, rhoR_Sp, thetaR_Sp, phiR_Sp)

        elif integral_type == "Triple Integral (General Coordinate [U,V,W])":
            X_Sp = sympify(X)
            U_Sp = sympify(U)
            XU_Sp = sympify(XU)
            xR_Sp = sympify(xR)
            yR_Sp = sympify(yR)
            zR_Sp = sympify(zR)
            result = TripleInt_Cylind_st(f_Sp, X_Sp, XU_Sp, U_Sp, xR_Sp, yR_Sp, zR_Sp)

        st.latex(rf"{result}")

if __name__ == '__main__':
    main()

