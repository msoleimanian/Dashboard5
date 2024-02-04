import streamlit as st
from streamlit_option_menu import option_menu
import HistoricalAnalyzeMenu as historical
import DigitalTwinMenu as digitialtwin
import Home as home
import Monitoring_Combine as MonitCombine
import Simulation as sim
import ExploreMenue as expmenu
def menuconstructor():

    # 1. as sidebar menu
    st.set_page_config(layout="wide")
    with st.sidebar:
        select = option_menu("AgroPulse TwinHub", [ 'Monitoring' , 'Explore' , 'Simulation' , 'Configuration', 'About'],
             menu_icon="database-up")


    if select == "Explore":
        expmenu.constructoemain()

    if select == 'Monitoring':
        MonitCombine.MonitConstructor()

    if select == 'Simulation':
        sim.SimulationConstructor()


    if select == 'About':
        home.homepageconstructor()


if __name__ == '__main__':
    menuconstructor()
