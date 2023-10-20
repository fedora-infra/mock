try:
    from contextlib import nullcontext
except ImportError:
    # Python < 3.7
    from contextlib import contextmanager

    @contextmanager
    def nullcontext(enter_result=None):
        """Trimmed down version of contextlib.nullcontext()"""
        yield enter_result
