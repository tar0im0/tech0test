import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('stremlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')

# text =st.text_input('あなたの趣味を教えてください',)
# condition = st.slider('あなたの今の調子は？',0, 1000, 200)

# 'あなたの趣味；', text
# 'コンディション:',condition

# if st.checkbox('画像を表示しますか？') :
#  img = Image.open('sample.png')
#  st.image(img, caption='logo', use_column_width=True)

