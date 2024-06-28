import numpy as np


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    try:
        h, w = np.array(h), np.array(w)
        assert h.size == w.size, "Your lists don't have the same size"
        assert h.size and w.size, "Your lists are empty"
        assert h.dtype.kind in 'fi' and w.dtype.kind, "bad type arguments"
        t = [float(w[i] / h[i] / h[i])for i in range(w.size)]
        return t
    except AssertionError as err:
        print(f"ExceptionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        bmi = np.array(bmi)
        assert bmi.size, "Your lists are empty"
        assert bmi.dtype.kind in 'fi', "bad type arguments"
        t = [bool(i > limit) for i in bmi]
        return t
    except AssertionError as err:
        print(f"ExceptionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")
