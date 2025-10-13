import streamlit as st


st.write('# Corrections to Attendance')

st.write(
    'Submit corrections/adjustments to attendance via form below.\n'
    '- Submission will record email account used to submit.\n'
    '- One correction per submission. (Enter multiple for: checkin *and* '
    'checkout times; multiple students; etc.)\n'
    '- Submissions **cannot be undone**. However, the ***most recent*** '
    'correction/adjustment will be considered correct for a given date, time '
    'period, and student.'
)

st.write(
    f'[Correction Google Form]({st.secrets.corrections.form_url})'
)
st.write(
    f'[Spreadsheet]({st.secrets.corrections.spreadsheet_url}) of '
    'corrections/adjustments already submitted.'
)