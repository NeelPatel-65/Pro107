import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("dataofpro.csv")

print(df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
         x=df.groupby("level")["attempt"].mean(),
         y=["Level 1", "Level 2", "Level 3", "Level 4"], orientation ='h'
))
fig.show()