import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
"""

"""


st.title("LaPorte Charging Instructions")
current_datetime = datetime.now(ZoneInfo("US/Central"))
current_time = current_datetime.time()

with st.container(border=True):
    cols = st.columns(4)
    with cols[0]:
        st.write("Current Time:")
    with cols[1]:
        hr_ = st.number_input("Hour:",min_value = 0,max_value=23,value=current_time.hour)
    with cols[2]:
        min_ = st.number_input("Minute:",min_value = 0,max_value=59,value = current_time.minute)

with st.container(border=True):
    cols = st.columns(3)
    with cols[0]:
        cp = st.number_input("Current Percentage:",min_value = 0, max_value=100,value=50)
    with cols[1]:
        huf = st.number_input("Hours Until Full:",min_value = 0,max_value = 10,value = 5)
    with cols[2]:
        muf = st.number_input("Minutes Until Full:",min_value = 0, max_value = 59,)
with st.container(border = True):
    goal = st.select_slider("Charge Percentage Goal",
                            options=[50,60,70,80,90,100],
                            value = 80)

submit = st.button("OK")
if submit:
    minutes_until_goal = (goal-cp)/(100-cp) * (huf*60+muf)
    hrs_until_goal = minutes_until_goal//60
    mins_until_goal = np.floor(minutes_until_goal-(hrs_until_goal*60))
    dt = timedelta(hours=hrs_until_goal,minutes=mins_until_goal)
    charge_complete_time = current_datetime+dt
    res_time = charge_complete_time.strftime("%H:%M:%S")
    res = f"Total time to charge to {int(goal)}% = {int(hrs_until_goal)} "
    res += f"hours : {int(mins_until_goal)} minutes. \n\n "
    res += f"Time to check: {res_time}."
    st.write(res)
