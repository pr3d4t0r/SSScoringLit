# See: https://github.com/pr3d4t0r/SSSCoringLit/blob/master/LICENSE.txt


from ssscoring import __VERSION__
from ssscoring.ssscoremultiple import main as score_multilple_jumps
from ssscoring.ssscoresingle import main as score_single_jump

import streamlit as st


if '__main__' == __name__:
    st.set_page_config(layout = 'wide', page_title='SSScore %s α' % __VERSION__)

    multiScoresPage = st.Page(score_multilple_jumps, title='Multiple Jumps Set', url_path='jumps_set', icon='🔢')
    singleScorePage = st.Page(score_single_jump, title='Single Jump', url_path='single_jump', icon='1️⃣')
    pageApp = st.navigation([ multiScoresPage, singleScorePage, ])
    pageApp.run()

