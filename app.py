import streamlit as st
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap, factor_mark

import numpy as np
import datetime as dt
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
from bokeh.io import push_notebook, show, output_notebook
from math import pi


tmin = pd.read_csv('hist_Tmin.csv')
tmax = pd.read_csv('hist_Tmax.csv')
hpre = pd.read_csv('hist_precipitaciones.csv')

tmin['ENTIDAD'] = tmin['ENTIDAD'].str.upper()
tmax['ENTIDAD'] = tmax['ENTIDAD'].str.upper()
hpre['ENTIDAD'] = hpre['ENTIDAD'].str.upper()

entidades = sorted(list(set(tmin['ENTIDAD'])))

entidad = st.selectbox("Seleccione la entidad" , entidades)
#st.write('Entidad Seleccionada:', entidad)

meses  = {'ABR' : 4,
 'AGO' : 8,
 'DIC' : 12,
 'ENE' : 1,
 'FEB' : 2,
 'JUL' : 7,
 'JUN' : 6,
 'MAR' : 3,
 'MAY' : 5,
 'NOV' : 11,
 'OCT' : 10,
 'SEP' : 9}


df_tmin = tmin[tmin['ENTIDAD'] == entidad]
df_tmx = tmax[tmax['ENTIDAD'] == entidad]
df_hpre = hpre[hpre['ENTIDAD'] == entidad]

df_tmin['MES'] = df_tmin['MESES'].replace(meses)
df_tmin['FECHA'] = pd.to_datetime(dict(year=df_tmin['AÑO'],month=df_tmin['MES'],day=1))
df = df_tmin.copy()
df['Tmax'] = df_tmx['Tmax']
df['ANUAL'] = df_hpre['ANUAL']
df['Prec'] = df_hpre['Prec']

entidad_title = entidad.lower().title()
#### Graficas de temperatura
a = figure(plot_width=600, plot_height=400, title= f'Historial de temperturas: {entidad_title}',
           toolbar_location="above",  tools="pan,wheel_zoom,box_zoom,reset,hover")

#p.vbar(x=df['FECHA'], top=df['Tmin'], width=0.9,color="blue")
#p.vbar(x=df['FECHA'], top=df['Tmax'], width=0.9,color="red")

a.line(df['FECHA'], df['Tmin'], legend_label="Temp Minima", line_width=2,color="blue")
a.line(df['FECHA'], df['Tmax'], legend_label="Temp Maxima", line_width=2,color="red")


a.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],)
#show(p)

st.bokeh_chart (a, use_container_width=True)



####### Graficas de precipitaciones
b = figure(plot_width=600, plot_height=400, title= f'Historial de precipitaciones {entidad_title}',
           toolbar_location="above",  tools="pan,wheel_zoom,box_zoom,reset,hover")
b.line(df['FECHA'], df['Prec'], legend_label="Precipitaciones", line_width=2,color="gray")

b.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],)
#show(p)
st.bokeh_chart (b, use_container_width=True)


c = figure(plot_width=600, plot_height=400, title= f'Precipataciones anual: {entidad_title}',
           toolbar_location="above",  tools="pan,wheel_zoom,box_zoom,reset,hover")
c.line(df['FECHA'], df['ANUAL'], legend_label="Precipitaciones anual", line_width=2,color="gray")

c.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],)

#st.bokeh_chart (c, use_container_width=True)

#show(p)