import pandas as pd
import urllib.parse


#digraph with edges only
def getEdges(df):

    edges = ""

    for _, row in df.iterrows():
        if not pd.isna(row.iloc[1]):
            edges += f'\t{row.iloc[0]} -> {row.iloc[1]}\n'
            
    return f'digraph {{\n{edges}}}'


def getURL(dot):
    return f'http://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(dot)}'

