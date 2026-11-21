import psycopg2
import pandas as pd
import matplotlib .pyplot as plt
from scipy .interpolate import make_interp_spline
import numpy as np
activity_id =124863703316
conn =psycopg2 .connect (host ="localhost",database ="garmin_data",user ="postgres",password ="*****")
df =pd .read_sql_query ("""select timestamp, heart_rate, cadence, power from record
where activity_id ={} order by timestamp asc""".format (activity_id ),conn )
df ['sec']=(df ['timestamp']-min (df ['timestamp'])).dt .total_seconds ()/60
fig ,ax =plt .subplots ()
fig .subplots_adjust (right =0.75 )
plt .title (str (min (df ['timestamp']).date ())+" / Активность - "+str (activity_id ))
twin1 =ax .twinx ()
twin2 =ax .twinx ()
twin2 .spines .right .set_position (("axes",1.1 ))
def spline (x ,y ,n ):
    do_spline =make_interp_spline (x ,y )
    x_ =np .linspace (x .min (),x .max (),n )
    y_ =do_spline (x_ )
    return x_ ,y_
p1 ,=ax .plot (spline (df .sec ,df .heart_rate ,150 )[0 ],spline (df .sec ,df .heart_rate ,150 )[1 ],"r-",label ="HR")
p2 ,=twin1 .plot (spline (df .sec ,df .power ,150 )[0 ],spline (df .sec ,df .power ,150 )[1 ],"b-",label ="Power")
p3 ,=twin2 .plot (spline (df .sec ,df .cadence ,150 )[0 ],spline (df .sec ,df .cadence ,150 )[1 ],"g-",label ="Cadence")
ax .set_xlim (0 ,90 )
ax .set_ylim (0 ,200 )
twin1 .set_ylim (0 ,400 )
twin2 .set_ylim (0 ,120 )
ax .set_xlabel ("Час, мин")
ax .set_ylabel ("ЧСС, ударов в минуту")
twin1 .set_ylabel ("Мощность, Вт")
twin2 .set_ylabel ("Каденс, ударов в минуту")
ax .yaxis .label .set_color (p1 .get_color ())
twin1 .yaxis .label .set_color (p2 .get_color ())
twin2 .yaxis .label .set_color (p3 .get_color ())
tkw =dict (size =4 ,width =1.5 )
ax .tick_params (axis ='y',colors =p1 .get_color (),**tkw )
twin1 .tick_params (axis ='y',colors =p2 .get_color (),**tkw )
twin2 .tick_params (axis ='y',colors =p3 .get_color (),**tkw )
ax .tick_params (axis ='x',**tkw )
ax .legend (handles =[p1 ,p2 ,p3 ])
plt .rcParams ['figure.figsize']=[10 ,5 ]
plt .show ()