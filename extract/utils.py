import copy


class MergeableDict(dict):
    template = {}

    def __init__(self, *args, **kwargs):
        """Prefill with template and merge arguments."""
        super(MergeableDict, self).__init__(self.template)
        for arg in args:
            self.merge(arg)
        self.merge(kwargs)

    def merge(self, other):
        """Merge recursively two dict's."""
        if isinstance(other, dict):
            for k, v in other.items():
                if k in self and (
                    isinstance(self[k], dict) and isinstance(v, dict)
                ):
                    if not isinstance(self[k], MergeableDict):
                        self[k] = MergeableDict(self[k])
                    self[k].merge(v)
                else:
                    self[k] = copy.deepcopy(v)