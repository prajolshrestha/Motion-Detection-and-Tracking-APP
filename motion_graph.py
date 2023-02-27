from folium import Tooltip
from numpy import source
from motion_detector import df 
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

#date time format to hr  and min , (used in hover feature)
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

#convert dataframe to column 
cds = ColumnDataSource(df)


#a)create figure object
f=figure(x_axis_type = 'datetime',height =100,width=500,sizing_mode='scale_width',title='Motion Detection Graph')
f.yaxis.minor_tick_line_color=None           #removes yaxis tick
f.yaxis[0].ticker.desired_num_ticks = 1      #removes grid

#b)create hover object tools and add to figure object
hover =  HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")]) 
f.add_tools(hover)

#c)create quad diagram
#f.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green")   #without hover feature
f.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)


#d)save and display figure
output_file('Time_data.html')
show(f)