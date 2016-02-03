from .abstract import _AbstractMicrostructureBasis
import numpy as np


class _RealFFTBasis(_AbstractMicrostructureBasis):
    def __init__(self, *args, **kwargs):
        super(_RealFFTBasis, self).__init__(*args, **kwargs)

    def _fftn(self, X, threads=1, avoid_copy=True):
        if self._pyfftw:
            return self._fftmodule.rfftn(np.ascontiguousarray(X),
                                         axes=self._axes,
                                         threads=threads,
                                         planner_effort='FFTW_ESTIMATE',
                                         overwrite_input=True,
                                         avoid_copy=avoid_copy)()
        else:
            return self._fftmodule.rfftn(X, axes=self._axes)

    def _ifftn(self, X, s=None, threads=1, avoid_copy=True):
        if self._pyfftw:
            return self._fftmodule.irfftn(np.ascontiguousarray(X), s=s,
                                          axes=self._axes,
                                          threads=threads,
                                          planner_effort='FFTW_ESTIMATE',
                                          avoid_copy=avoid_copy)().real
        else:
            return self._fftmodule.irfftn(X, axes=self._axes, s=s).real

    def discretize(self, X):
        raise NotImplementedError