import streamlit as st
import math
st.header("2305A21L55 PS2")
st.title("Electrical Power Calculator")
st.subheader("Estimate Active, Reactive, and Apparent Power")



def Elec_Power(V, I, PF):
    S = V * I
    phi = math.acos(PF) 
    P = S * PF 
    Q = S * math.sqrt(1 - PF**2)  
    return P, Q, S

col, col1 = st.columns(2)

with col:
    
        
        V = st.number_input("Voltage (V) in Volts:", min_value=0.0, step=50.0, format="%.2f")
        I = st.number_input("Current (I) in Amperes:", min_value=0.0, step=0.5, format="%.2f")
        PF = st.number_input("Power Factor (PF):", min_value=0.0, max_value=1.0, step=0.02, format="%.2f")
        a = st.button("Calculate Power")
        
with col1:
    if a:
        P, Q, S = Elec_Power(V, I, PF)
        st.write(f"*Active Power (P):* {P:.2f} W")
        st.write(f"*Reactive Power (Q):* {Q:.2f} VAR")
        st.write(f"*Apparent Power (S):* {S:.2f} VA")



