import datetime
import streamlit as st
import pandas as pd
from zoneinfo import ZoneInfo



# Create form to search last name
st.title('Sign In Form')

st.write(
    'Select student names to be checked in'
)

names = pd.read_csv('names.csv').sort_values(by='LastName')

# options = ['Not Checked-In', 'Checked-In']
last_name_letters = sorted(names['LastName'].str[0].unique())
options = last_name_letters
filter_selection = st.pills(
    'Display',
    options,
    default=options,
    selection_mode='multi',
)
st.markdown(f'Your selected options: {filter_selection}.')

# Override time option they were checked in. Defaults to current time
is_override = st.checkbox('Override Time')
override_checkin_time = None

with st.form(key='my_form'):
    submitted = st.form_submit_button('Check In')

    
    if is_override:
        now = datetime.datetime.now()
        print(f'Datetime: {now=}')
        time_inc_minute = 10
        override_checkin_time = st.time_input(
            label='Check-in Time',
            value=datetime.time(
                hour=now.hour,
                minute=(now.minute // time_inc_minute)*time_inc_minute,
                tzinfo=ZoneInfo('America/Los_Angeles')
            ),
            step=datetime.timedelta(minutes=time_inc_minute),
        )
        print(f'Override: {override_checkin_time=}')



    # selected_names = st.multiselect('Names', names['FullName'])
    all_names = {}

    # Display each name grouped by last name so a section appears for each last name letter
    for letter in last_name_letters:
        if letter not in filter_selection:
            continue
        st.subheader(letter)
        filtered_names = names[names['LastName'].str.startswith(letter)]
        filtered_names = filtered_names.sort_values(by='FullName')
        # Split names into three columns to be displayed
        cols = st.columns(3)
        for index, name in enumerate(filtered_names['FullName']):
            col_index = index % 3
            col = cols[col_index]
            all_names[name] = col.checkbox(
                label=name,
                key=name,
            )
        st.divider()

            

    
    if submitted:
        # Track time of actual submission
        submit_time = datetime.datetime.now().time()
        st.write(f'Submitted on {submit_time} ')
        st.write(f'{override_checkin_time}')
        for name, checkedin in all_names.items():
            if checkedin:
                info = names[names['FullName'] == name]
                st.write(f'{name} checked in (grade {info["Grade"].values[0]})')



