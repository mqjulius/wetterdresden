#import streamlit, pandas
import streamlit as st
import pandas as pd     


#Header
st.title("Wetter Dresden")
st.markdown("""
Diese App zeigt das Wetter in Dresden von 1827 bis 2022 (monatlich) und ermöglicht es nach Jahr und Wetterstation zu filtern
* **Python libraries:** pandas, streamlit
* **Data source:** [www.opendata.dresden.de/informationsportal/](http://opendata.dresden.de/duva2ckan/files/de-sn-dresden-wetterdaten_-_monatlich_md1_1828ff_dresden_temepratur_niederschlag_windgeschwindkeit_bedeckungsgrad_sonnenscheindauer/content)
""")


#Dataframe Load
@st.cache
def load_data():
    path = "http://opendata.dresden.de/duva2ckan/files/de-sn-dresden-wetterdaten_-_monatlich_md1_1828ff_dresden_temepratur_niederschlag_windgeschwindkeit_bedeckungsgrad_sonnenscheindauer/content"
    return pd.read_csv("http://opendata.dresden.de/duva2ckan/files/de-sn-dresden-wetterdaten_-_monatlich_md1_1828ff_dresden_temepratur_niederschlag_windgeschwindkeit_bedeckungsgrad_sonnenscheindauer/content", encoding='latin-1', sep=';')
df = load_data()


#df = pd.read_csv("http://opendata.dresden.de/duva2ckan/files/de-sn-dresden-wetterdaten_-_monatlich_md1_1828ff_dresden_temepratur_niederschlag_windgeschwindkeit_bedeckungsgrad_sonnenscheindauer/content", encoding='latin-1', sep=';')
df = df[["Jahr", "Monat", "Stations ID", "Monatsmittel des Tagesmin. der Lufttemperatur", "Monatsmittel des Tagesmax. der Lufttemperatur", "Monatsmittel der tägl. Windstärke", "Monatssumme der Niederschlagshöhe" ]]
    

#Sidebar
st.sidebar.header('Filter')
selected_year = st.sidebar.selectbox('Jahr', list(reversed(range(1828,2023))))
maskstation = df.drop_duplicates(subset=['Stations ID'])
#selected_station = st.sidebar.selectbox('Station', list(maskstation['Stations ID']))
selected_station = st.sidebar.multiselect('Station', list(maskstation['Stations ID']), default=['Dresden-Klotzsche','Dresden (Mitte)','Dresden-Hosterwitz','Dresden-Strehlen'])


#Filtered Dataframe
filtered_df = df[df["Stations ID"].isin(selected_station)]


#Output
#st.write(df.loc[(df['Jahr'] == selected_year)])
st.write(filtered_df.loc[(filtered_df['Jahr'] == selected_year)])
#st.write(filtered_df)






