import streamlit as st

st.title('لا توجد فرص وظيفية بعد التخرج !')

st.image("img.gif", use_column_width=True)

st.markdown("""
دائمًا نسمع أنه ما فيه وظائف لحديثي التخرج، وأنه ما فيه وظائف إلا بالواسطة، فلا تتعب نفسك في الدراسة. خلينا نشوف إذا كان كلامهم صحيحًا أو لا.
أخذت بيانات من منصة "جدارات" وحللت بيانات آخر سنتين للتعرف على سوق العمل.
""")

st.image("C:\Users\Dani_\Desktop\Jupyter\strim\strimlit\img.gif", use_column_width=True)


st.write("<p style='text-align: right;'> دائمًا نسمع أنه ما فيه وظائف لحديثي التخرج، وأنه ما فيه وظائف إلا بالواسطة، فلا تتعب نفسك في الدراسة. خلينا نشوف إذا كان كلامهم صحيحًا أو لا. </p>", unsafe_allow_html=True)
st.write("<p style='text-align: right;'> أخذت بيانات من منصة جدارات وحللت بيانات آخر سنتين للتعرف على سوق العمل. </p>", unsafe_allow_html=True)

import os
print(os.path.exists("img.gif"))
print(os.path.exists("img1.gif"))
