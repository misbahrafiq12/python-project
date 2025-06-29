import streamlit as st
import re
st.write('Password Strength Meter')

passwordReq = {
   'characters':         r'[A-Za-z]',        
   'digits' :            r'[0-9]',            
   'special_characters': r'[!@#$%^&*]'       
}


input_value = st.text_input("Enter Your Password") 

 

def passwordchecker(password) -> str:
  
    
    # strong
    if len(password) >= 8: 
        
        
        results = {
    'characters': bool(re.search(passwordReq['characters'], password)), 
    'digits': bool(re.search(passwordReq['digits'], password)),
    'special_characters': bool(re.search(passwordReq['special_characters'], password))
        }
        match_count = sum(results.values())
        
        if match_count == 3:
             st.success("strong")
        elif match_count == 2:
              st.info("medium")
        else:
             st.warning("weak") 
             missing = [key for key ,value in results.items() if not value]
             for m in missing:
                   st.warning(f"{m.replace('_', ' ').capitalize()} is missing.")
                 
                 
    else:
        st.error("Password must be at least 8 characters long")           
                 
passwordchecker(input_value)        
        
        
   