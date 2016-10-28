# from .. import altair
import altair
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


def interact_with(df):

    def plot(x=None, y=None, color=None, text=None,
         mark='mark_point', shape=None, size=None, row=None, column=None):
        if df is None:
            raise ValueError('pandas.DataFrame needs to be passed in')
        kwargs = {'x': x, 'y': y, 'color': color, 'text': text,
                'shape': shape, 'size': size, 'row': row, 'column': column}
        for key, value in list(kwargs.items()):
            if value in {None, False, 'None'}:
                del kwargs[key]

        c = getattr(altair.Chart(df), mark)().encode(**kwargs)
        return c

    cols = [None] + list(df.columns)
    marks = ['mark_' + f for f in ['line', 'point', 'bar', 'tick', 'text',
                                   'square', 'rule', 'circle', 'area']]

    return interact(plot, x=cols, y=cols, color=cols, shape=cols, size=cols,
                    text=cols, mark=marks, row=cols, column=cols)