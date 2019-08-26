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
        self["data"][0]["marker"] = {"color": "rgb(153,50,50)"}
        self["layout"]["yaxis"]["title"] = "CAMCOG total (Puntuación máx.: 107)"


class ORIGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(ORIGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(218,213,72)"}
        self["layout"]["yaxis"]["title"] = "Orientación (Puntuación máx.: 10)"


class LTGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(LTGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(28,79,3)"}
        self["layout"]["yaxis"]["title"] = "Lenguaje total (Puntuación máx.: 30)"


class LCGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(LCGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(140,186,115)"}
        self["layout"]["yaxis"]["title"] = "Lenguaje comprensivo (Puntuación máx.: 9)"


class LPGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(LPGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(48,121,8)"}
        self["layout"]["yaxis"]["title"] = "Lenguaje expresivo (Puntuación máx.: 21)"


class MTGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(MTGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(0,72,79)"}
        self["layout"]["yaxis"]["title"] = "Memoria total (Puntuación máx.: 27)"


class MRECGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(MRECGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(32,139,149)"}
        self["layout"]["yaxis"]["title"] = "Memoria reciente (Puntuación máx.: 4)"


class MREMGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(MREMGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(102,173,180)"}
        self["layout"]["yaxis"]["title"] = "Memoria remota (Puntuación máx.: 6)"


class MAGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(MAGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(102,146,180)"}
        self["layout"]["yaxis"]["title"] = "Memoria aprendizaje (Puntuación máx.: 17)"


class ACGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(ACGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(117,102,180)"}
        self["layout"]["yaxis"]["title"] = "Atención-concentración (Puntuación máx.: 7)"


class PRGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(PRGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(100,56,159)"}
        self["layout"]["yaxis"]["title"] = "Praxis (Puntuación máx.: 12)"


class CALGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(CALGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(159,56,136)"}
        self["layout"]["yaxis"]["title"] = "Cálculo (Puntuación máx.: 2)"


class PABSGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(PABSGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(215,84,42)"}
        self["layout"]["yaxis"]["title"] = "Pensamiento abstracto (Puntuación máx.: 8)"


class PTVGraph(XYGraph):
    def __init__(self, x, y, *args, **kwargs):
        super(PTVGraph, self).__init__(x, y, *args, **kwargs)
        self["data"][0]["marker"] = {"color": "rgb(141,227,183)"}
        self["layout"]["yaxis"]["title"] = "Percepción táctil-visual (Puntuación máx.: 11)"


data_graphs = {
    CamdexData.mmse: MMSEGraph,
    CamdexData.mec: MECGraph,
    CamdexData.ryh: RYHGraph,
    CamdexData.ct: CTGraph,
    CamdexData.ori: ORIGraph,
    CamdexData.lt: LTGraph,
    CamdexData.lc: LCGraph,
    CamdexData.lp: LPGraph,
    CamdexData.mt: MTGraph,
    CamdexData.mrec: MRECGraph,
    CamdexData.mrem: MREMGraph,
    CamdexData.ma: MAGraph,
    CamdexData.ac: ACGraph,
    CamdexData.pr: PRGraph,
    CamdexData.cal: CALGraph,
    CamdexData.pabs: PABSGraph,
    CamdexData.ptv: PTVGraph,
}