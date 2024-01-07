import streamlit as st
from streamlit_option_menu import option_menu
import DigitalTwin as digitaltwin
import Monitoring as monitoring

def constructoemain():

    selected = option_menu(None, ["Digital Twin", "Monitoring", "Recommendation"],
        menu_icon="cast", default_index=0, orientation="horizontal")
    if selected == "Digital Twin":
        digitaltwin.digitaltwinconstructor()


    if selected == "Monitoring":
        monitoring.MonitoringConstructor()

