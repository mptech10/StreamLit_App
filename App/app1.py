

import streamlit as st
st.title("Hiearchical Data Viewer")

import pandas as pd
filename = "data/employee-manager.csv"
df = pd.read_csv(filename).convert_dtypes()
st.dataframe(df)

import graphs
graph = graphs.getEdges(df)
st.graphviz_chart(graph)
