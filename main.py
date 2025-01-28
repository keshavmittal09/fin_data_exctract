import streamlit as st
import extracter
import pandas as pd
import json

st.title("💬📃📄EXCTRACTER")

col1,col2 = st.columns([3,2])


with col1:
    data = st.text_area("enter",height=400)

uploaded_file = st.file_uploader("Choose a file",type=["csv", "txt", "pdf", "png", "jpg"])
if uploaded_file is not None:
  data = uploaded_file


if st.button("submit"):
    with col2 :
        a = extracter.def_prompt(data)
        try:
            result = json.loads(a)
            df = pd.DataFrame(result.items(),columns=["Measures","Values"])  # This will print the parsed dictionary if the response is valid JSON
            # st.dataframe(df,width=400,hide_index=True)
            st.markdown("""
                <style>
                    .right-align {
                        display: flex;
                        justify-content: flex-end;
                    }
                </style>
            """, unsafe_allow_html=True)

            # Wrap the table in a div with the right-align class
            st.markdown('<div class="right-align">' + df.to_html(index=False) + '</div>', unsafe_allow_html=True)

        except json.JSONDecodeError as e:
            er = "some error, TRY AGAIN" 
            pass
