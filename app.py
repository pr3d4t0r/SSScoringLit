# See: https://github.com/pr3d4t0r/SSSCoring/blob/master/LICENSE.txt


from ssscoring.app import main

import os

import streamlit as st


if '__main__' == __name__:
    st.set_page_config(layout = 'wide')
    st.write('wide!')
    main()

