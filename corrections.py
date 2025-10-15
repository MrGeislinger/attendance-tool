import streamlit as st
import helpers




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

st.write('---')

st.write('## Corrections Look-Up')
st.write(
    'Use this form to search by specific date range and students '
    '(blank for all students)'
)

names = helpers.get_student_roster(
    name='studentinfo',
    cache_ttl_secs=helpers.SECS_IN_DAY,
)

with st.form(key='my_form'):
    date_range = st.date_input(
        'Date Range (required)',
        value=(
            "today",
            "today",
        ),
        format="MM/DD/YYYY",
    )

    students = st.multiselect(
        'Select students (blank for all students)',
        names['FullName'],
        format_func=(
            lambda x: helpers.format_student_name(x, names)
        ),
    )

    submitted = st.form_submit_button('Search')

    if submitted:
        if date_range:
            # Pull the data from the data source (ideally only students & time)
            df= helpers.get_corrections(
                students=students,
                date_start=date_range[0],
                date_end=date_range[1],
            )
            
            st.dataframe(df)
        else:
            st.warning('Please select a date range')
