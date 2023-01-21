import pandas as pd
#import geopandas as gpd
import pandas_bokeh
import bokeh
import panel as pn
import numpy as np
import json
import jinja2
bokeh.plotting.curdoc().theme='dark_minimal'
import param

df=pd.read_csv('/Users/carolinebowen/VisualStudio/Aqua/HWM_trimmed_labelled_data_09Jan2023.csv', parse_dates=True)
print('reading csv file')

#df=df.sort_values(by=['Sensor_ID','TimeStamp'])
df.TimeStamp=pd.to_datetime(df.TimeStamp)
Sensor=df.Sensor_ID.unique().tolist()
Blocked_Sensor=df.loc[df.Blocked==1].Sensor_ID.unique().tolist()
s={}

print('resampling')
for i in Blocked_Sensor:
    s[i]=df.loc[df.Sensor_ID==i] 
    s[i].resample('60Min',on='TimeStamp').max()

TOOLS = "pan,wheel_zoom,box_zoom,reset,save, hover"

print('creating dashboard')

class BlockedDashboard(param.Parameterized):
    
    # drop down selector widget containing the list of animals, with the default being 'Goat'
    plot = param.ObjectSelector(default=Blocked_Sensor[0], objects=Blocked_Sensor)
    
    # create data set containing only the data applicable to the animal in the drop down selector
    def get_data(self):
        class_df = s[self.plot][['TimeStamp','Sensor_value']].copy()
        return class_df
    

    def line_view(self):
        data=self.get_data()
        data.set_index=data.TimeStamp
        #p=data['Sensor_value'].plot_bokeh(title="Historic level data plot for {} Sensor".format(i), show_figure=False)
        p = bokeh.plotting.figure(x_axis_type="datetime",tools=TOOLS,
            title="Historic level data plot for {} Sensor".format(i),
            x_axis_label='DateTime',
            y_axis_label='Sensor Level',
            active_scroll='wheel_zoom')

        hover=p.select(dict(type=bokeh.models.HoverTool))
        hover.tooltips=[('Period','$x{%Y-%m-%d,%H:%M}'),('Sensor Level','$y')]
        hover.formatters={'$x':'datetime'}

        p.line(data.TimeStamp,data.Sensor_value, line_width=2)
        
        return pn.WidgetBox(p)

bd = BlockedDashboard(name='')

dashboard=pn.Row(bd.param,bd.line_view, sizing_mode='stretch_both')

temp=pn.template.BootstrapTemplate(theme=pn.template.DarkTheme,
         site='Aqua DNA',header_background ='#4099da',header_color='black',
         logo='https://media.licdn.com/dms/image/C4E22AQF-mbaih5LBBQ/feedshare-shrink_2048_1536/0/1642175339327?e=2147483647&v=beta&t=K_CaphKHMMoD2B8H96aneSM6D6kgzyStn7Unaanxojk' 
         ,title="HWM - Historic level data plot for Blocked Sensors")
temp.main.append(dashboard)
temp.servable()



