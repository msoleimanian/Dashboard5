import streamlit as st
from streamlit_option_menu import option_menu
import Insights as insights
import Explore as explore
import HistoricalAnalyzeMenu as historical
import DigitalTwinMenu as digitialtwin
import Summary as summary
import Recommendation as recom



st.set_page_config(layout="wide")


def menuconstructor():
    # 1. as sidebar menu
    with st.sidebar:
        select = option_menu("AgroPulse TwinHub", ["Home","Historical Analyze", 'Digital Twin'],
            icons=['bank','easel-fill', 'info-square-fill'], menu_icon="database-up")

    if select == "Historical Analyze":
        historical.constructoemain()

    if select == "Digital Twin":
        digitialtwin.constructoemain()



if __name__ == '__main__':
    menuconstructor()
