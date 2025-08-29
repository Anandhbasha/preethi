# %%

import ipywidgets as wid
from IPython.display import display

slider = wid.IntSlider(value = 5, min=0, max=20)
display(slider)

Fslider = wid.FloatSlider(value = 2.5, min=0, max=10)
display(Fslider)

Itext= wid.IntText(value = 40, description = "intText")
display(Itext)


ani = wid.Play(value =0,min=0,max=10,step=1,interval=500 ,description="Press Play")
display(ani)


text = wid.Text(value="", placeholder = "Please enter your name", description = "Name")

textarea = wid.Text(value="", placeholder = "Please enter your comments", description = "Comments")

acc = wid.Accordion(children=[text,textarea])
acc.set_title(0,'Name')
acc.set_title(1,'Comments')
display(acc)
# %%
