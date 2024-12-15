# Import libraries
import streamlit as st
import math

# Set the app title
st.title('Finance Calculator')

# Add a logo in the corner
st.logo("calculator.jpg")

# Display the app introduction
st.markdown("""
###### By Isabelle Rajendiran
Welcome to my finance calculator! 
         
Here, you can access two different financial calculators: **an investment calculator** and a **mortgage repayment calculator**.
""")

# Display the app menu 
st.subheader('Menu')
st.markdown("""
    - **Investment** - to calculate the amount of interest you'll earn on your investment  
    - **Mortgage** - to calculate the monthly repayment amount for a home loan
""")

# Request user input
choice = st.selectbox("Choose from the options: ", options=['Investment', 'Mortgage'], index=None)

with st.container(border = True):
    # Mortgage calculator
    if choice == 'Mortgage':
        st.subheader("Mortgage Calculator")

        # Display the repayment equation if toggle is on
        if st.toggle("Display formula"):
            st.latex(r"""
                    \text{Monthly Repayment} = \frac{i \cdot P}{1 - (1 + i)^{-n}}
            """)
            st.markdown("""
                    Where:
                    - _P_ = Loan amount (house price minus any deposit)
                    - _i_ = Monthly interest rate (annual interest rate divided by 12)
                    - _n_ = Number of months for repayment (years divded by 12)
            """)

        # Input fields for the mortgage calculator
        # P = Present value of the house
        P = st.number_input("Enter the present value of the house (£):", min_value = 0.00, format = "%0.2f", step = 100.00)
        
        # i = Monthly interest rate
        i = st.number_input("Enter your yearly interest rate (%):", min_value= 0.0, format = "%0.1f", , step = 1.0)/100
        i = i/12 # Convert from yearly to monthly rate
        
        # n = The number of months over which the bond will be repaid
        n = st.number_input("Enter the amount of years you plan to repay the mortgage:", min_value= 0.0, max_value = 100.0, format = "%0.1f", , step = 1.00)
        n = n*12

        # Calculate monthly repayment
        if st.button("Calculate", type="primary"):
            try:
                repayment = round((i * P) / (1 - (1 + i) ** -n), 2)
                st.markdown(f"Your monthly repayment is:")
                st.subheader(f":white_check_mark: :green-background[£{repayment:.2f}]")
            except ZeroDivisionError:
                st.markdown(":exclamation: :red[**Error**: Please ensure the interest rate and the number of months is greater than 0.]")

    # Investment calculator
    elif choice == 'Investment':
        st.subheader("Investment Calculator")

        # Display the repayment equation if toggle is on
        if st.toggle("Display formulas"):
                st.markdown("##### Simple Interest Formula:")
                st.latex(r"""
                        \text{Amount} = P \cdot (1 + r \cdot t)
                """)

                st.markdown("##### Compound Interest Formula:")
                st.latex(r"""
                        \text{Amount} = P \cdot (1 + r)^t
                """)
                
                st.markdown("""
                        Where: 
                        - _P_ = Initial deposit (principal amount)  
                        - _r_ = Annual interest rate (in decimal form)  
                        - _t_ = Number of years the money is invested  
                """)

        # Input fields for the mortgage calculator
        # P = The amount deposited
        P = st.number_input("Enter the amount of money you are depositing (£):", min_value = 0.00, format = "%0.2f", , step = 1.00)
        
        # r = yearly interest rate
        r = st.number_input("Enter your yearly interest rate (%):", min_value= 0.0, format = "%0.1f", , step = 1.0)/100
        
        # t = The amount of years planned to invest
        t = st.number_input("Enter the amount of years you plan to invest:", min_value= 0.0, format = "%0.1f", , step = 1.0)

        # Request user input for the type of interest
        option = st.selectbox("Choose from the interest type: ", options=['Simple', 'Compound'], index=0)

        # Calculate and display simple interest
        if option == 'Simple':
            if st.button("Calculate", type="primary"):
                # A = Total amount with added simple interest
                A = round(P * (1 + r*t),2)
                st.markdown(f"Your total amount with applied simple interest is:")
                st.subheader(f":white_check_mark: :green-background[£{A:.2f}]")
        
             # Calculate and display compound interest
        else:
            if st.button("Calculate", type="primary"):
                # A = Total amount with added compound interest
                A = round(P * math.pow((1+r), t),2) 
                st.markdown(f"Your total amount with applied compound interest is:")
                st.subheader(f":white_check_mark: :green-background[£{A:.2f}]")
