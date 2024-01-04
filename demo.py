# import streamlit as st
#
# import streamlit as st
# a = st.sidebar.radio('Choose:',[1,2])
# '_This_ is some __Markdown__'
# a=3
# 'dataframe:', data
#
#
#
# # Insert a chat message container.
# >>> with st.chat_message("user"):
# >>>    st.write("Hello ??")
# >>>    st.line_chart(np.random.randn(30, 3))
#
# # Display a chat input widget.
# >>> st.chat_input("Say something")


# My first app

# Here's our first attempt at using data to create a table:
#
# """

# import streamlit as st
# import pandas as pd
# df = pd.DataFrame({
# 'first column': [1, 2, 3, 4],
# 'second column': [10, 20, 30, 40]
# })
# df


# import streamlit as st
# import pandas as pd
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
# 'first column': [1, 2, 3, 4],
# 'second column': [10, 20, 30, 40]
# }))


# import streamlit as st
# import numpy as np
# import pandas as pd
# dataframe = pd.DataFrame(
# np.random.randn(10, 20),
#
# columns=('col %d' % i for i in range(20)))
# st.dataframe(dataframe.style.highlight_max(axis=0))
#
#
# x = st.slider('x') # this is a widget
#
# st.write(x, 'squared is', x * x)
#
# st.text_input("Your name", key="name")
#
# # You can access the value at any point with:
#
# st.session_state.name
#
#
# st.header('st.button')
# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 样例 1

st.write('Hello, *World!* :sunglasses:')

# 样例 2

st.write(1234)

# 样例 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)