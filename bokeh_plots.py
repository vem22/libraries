from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource,HoverTool, Select, CustomJS, Legend
from bokeh.transform import dodge
from bokeh.layouts import column


def make_plot(decomp):
  
  """
  Creation of bokeh chart
  ROI: line chart
  Spend Share & Effect Share: bar chart

  Parameters
  -----
  decomp : dict

  Returns
  -----
  script : str
      JS script
  div : str
      HTML div
  """
  
  # defining input chart data
  variables = [k for k in decomp.keys()]
  percentageSpend = [decomp[k]['spend_share'] for k in decomp.keys()]
  var1 = [decomp[k]['var1'] for k in decomp.keys()]
  var2 = [decomp[k]['var2'] for k in decomp.keys()]
  sorted_variables = sorted(variables, key=lambda x: rois[variables.index(x)])
  var3 = sorted([decomp[k]['var3'] for k in decomp.keys()])

  mydata = {"variables": variables,
          "var1": var1,
          "var2": var2,
          "var3": var3}
  
  # defining source data
  source = ColumnDataSource(data=mydata)

  # bokeh figure definition
  p = figure(y_range=sorted_variables, x_range=(0, 50),
         toolbar_location=None, tools="", sizing_mode='scale_width', height=150)

  current_app.logger.info(f"Figure created!")

  # var1 horizontal barplot & hover tooltips definition
  var1_plot = p.hbar(y=dodge('variables', -0.25, range=p.y_range), right='var1', height=0.2, source=source,
      color="#c9d9d3")

  dictValues = [{'header':'Var1 Value',
                  'values': {'Variable': '@variables', '% var1':'@var1{0.2f}%'}}]

  ht = getHoverTool(dictValues, var1_plot)  
  p.add_tools(ht)
  current_app.logger.info(f"var1 plot created!")

  # var2 share horizontal barplot & effect share plot hover tooltips definition
  var2_plot = p.hbar(y=dodge('variables',  0.0,  range=p.y_range), right='var2', height=0.2, source=source,
      color="#718dbf")

  dictValues = [{'header':'Var2 Value',
                  'values': {'Variable': '@variables', '% var2':'@var2{0.2f}%'}}]

  ht = getHoverTool(dictValues, var2_plot)  
  p.add_tools(ht)
  current_app.logger.info(f"var2 plot created!")

  # var3 line plot & var3 hover tooltips definition
  line_plot = p.line(y=sorted_variables, x=var3,
      color="#e84d60", line_width=3)
  var3_plot = p.circle(x=var3, y=sorted_variables, fill_color="#e84d60", 
                  line_color="#e84d60", size=6)

  dictValues = [{'header':'var3',
                  'values': {'Variable': '@y', 'var3':'@x{0.2f}'}}]

  ht = getHoverTool(dictValues, roi_plot)  
  p.add_tools(ht)
  current_app.logger.info(f"var3 plot created!")

  # legend labels definition 
  legend_lab = [("var1", [var1]), ("var2", [var2]), ("var3", [line_plot, var3])]
  legend = Legend(items=legend_lab)
  legend.click_policy="mute"

  # figure options definition
  p.add_layout(legend, "right")
  p.xaxis.visible = False
  p.y_range.range_padding = 0.1
  p.ygrid.grid_line_color = None
  p.legend.location="top_right"
  p.legend.orientation="vertical"

  # get script and div code
  script, div = components(p)
  current_app.logger.info("script div components created!")

  return script, div
