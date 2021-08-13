import streamlit as st
import time
st.title("streamlit 入門")

st.write("プログレスバーの表示")
"start!!"

latest_iteration= st.empty()
bar= st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"done!!"



left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです。")

expander = st.beta_expander("問い合わせ")
expander.write("問い合わせ")

text=st.text_input("あなたの趣味を教えてください")
"あなたの趣味は",text,"です"

condition=st.slider("あなたの調子は？",0, 100, 50)
"コンディション",condition 
if st.checkbox("Show Image"):
    img=Image.open("就活用写真.jpg")
    st.image(img, caption="Endo Akira", use_column_width=True)
