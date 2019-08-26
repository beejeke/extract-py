from extract.model import CamdexData
from extract.utils import MergeableDict


class XAxis(MergeableDict):
    template = dict(rangeslider={})


class YAxis(MergeableDict):
    template = dict(fixedrange=True)


class XYLayout(MergeableDict):
    template = dict(xaxis=XAxis(title="Consulta (Numérica ordenada: 1ª, 2ª, 3ª..."), yaxis=YAxis())


class Trace(MergeableDict):
    template = dict(fill="tozeroy", type="bar")


class Config(MergeableDict):
    template = dict(responsive=True, displayModeBar=True, locale="es")


class XYGraph(MergeableDict):
    trace = Trace()
    data = [trace]
    layout = XYLayout()
    template = dict(data=data, layout=layout, config=Config())

    def __init__(self, x, y, *args, **kwargs):
        super(XYGraph, self).__init__(*args, **kwargs)
        self["data"][0]["x"] = x
        self["data"][0]["y"] = y


class MMSEGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(MMSEGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(230,138,0)"}
        self["layout"]["yaxis"]["title"] = "Mini Mental State de Folstein (Puntuación máx.: 30)"


class MECGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(MECGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(102,0,204)"}
        self["layout"]["yaxis"]["title"] = "Mini Ex. Cogn. de Lobo y colbs. (Puntuación máx.: 35)"


class RYHGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(RYHGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(56,131,128)"}
        self["layout"]["yaxis"]["title"] = "Test de Roth y Hopkins (Puntuación máx.: 10)"


class CTGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(CTGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(230,138,0)"}
        self["layout"]["yaxis"]["title"] = "Mini Mental State de Folstein (Puntuación máx.: 30)"


class ORIGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(ORIGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(230,138,0)"}
        self["layout"]["yaxis"]["title"] = "Mini Mental State de Folstein (Puntuación máx.: 30)"


class LTGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(LTGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(230,138,0)"}
        self["layout"]["yaxis"]["title"] = "Mini Mental State de Folstein (Puntuación máx.: 30)"


class LCGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(LCGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(230,138,0)"}
        self["layout"]["yaxis"]["title"] = "Mini Mental State de Folstein (Puntuación máx.: 30)"


data_graphs = {
    CamdexData.mmse: MMSEGraph,
    CamdexData.mec: MECGraph,
    CamdexData.ryh: RYHGraph
}