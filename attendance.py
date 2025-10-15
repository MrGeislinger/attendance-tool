import streamlit as st
import helpers



st.write('# Attendance Record')

st.write(
    'Look up current attendance record for students (grouped by name).\n'
    '- [REQUIRED] Choose a date range → can be just a single date\n'
    '- Select students (blank for all students)\n'
    '- Option to display only final value for corrections (will only show most '
    'recent correction or record). Recommended to leave off if wanting to see '
    'all records & corrections.'
)

names = helpers.get_student_roster(
    name='studentinfo',
    cache_ttl_secs=helpers.SECS_IN_DAY,
)

# Form to select student(s), date range, session time
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


    only_final_values = st.checkbox(
        'Only display final value for corrections'
        ' (will only show most recent correction or record)'
    )


    submitted = st.form_submit_button('Search')

    if submitted:
        if date_range:
            # Pull the data from the data source (ideally only students & time)
            df= helpers.get_attendance(
                students=students,
                date_start=date_range[0],
                date_end=date_range[1],
                drop_duplicates=only_final_values,
            )
            
            st.dataframe(df)
        else:
            st.warning('Please select a date range')


