"""
A small example showing a Tree client and optinal scatter client. The
scatter client displays the values of 2 different images based on the
pixel masks described by the tree subsets.

Note that the scatter client is SLOOOOOOW
"""
import cloudviz as cv
import cloudviz.data_dendro_cpp as cpp
import matplotlib.pyplot as plt
from cloudviz.io import extract_data_fits
from cloudviz.tree_layout import DendrogramLayout
from cloudviz import RasterAxes


#Primary component is extinction data for Ophiuchus
#ha component is h-alpha
data = cpp('dendro_oph.fits')
d2 = extract_data_fits('ha_regrid.fits')
comp = cv.data.Component(d2['PRIMARY'])
data.components['ha'] = comp

# a tree layout manager that mimics the
# original dendrogram code
layout = DendrogramLayout(data.tree,
                          data.components['PRIMARY'].data)


h = cv.Hub()
c = cv.MplTreeClient(data, layout=layout)
data.register_to_hub(h)
c.register_to_hub(h)
# initial plot is blank
c.refresh()

fig = plt.figure()
ax = RasterAxes(fig, [0.1, 0.1, 0.8, 0.8])
fig.add_axes(ax)

# scatter client
# set data plot to invisible initially.
c3 = cv.MplScatterClient(data, axes=ax)
c2 = cv.MplImageClient(data)
c3.set_xdata('PRIMARY')
c3.set_ydata('ha')
#c3._plots[data].set_visible(False)
c2.register_to_hub(h)
c2.set_component('PRIMARY')

c3.register_to_hub(h)

# create some subsets
data.tree.index()
id1 = data.tree._index[12].get_subtree_indices()
id2 = data.tree._index[40].get_subtree_indices()

s = cv.subset.TreeSubset(data, node_list=id1)
s2 = cv.subset.TreeSubset(data)
s2.node_list = id2

s.register()
s2.register()


# attach some event handlers
def pick_branch(x, y, client=c):
    branch = client.layout.pick(x, y)
    if not branch:
        s2.node_list = []
    else:
        id = branch.get_subtree_indices()
        s2.node_list = id


def motion_notify_event(event, **kwargs):
    if not event.inaxes:
        return
    pick_branch(event.xdata, event.ydata)


c._figure.canvas.mpl_connect('motion_notify_event',
                             motion_notify_event)
