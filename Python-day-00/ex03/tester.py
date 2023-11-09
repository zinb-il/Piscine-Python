from NULL_not_found import NULL_not_found
import math


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False


NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
NULL_not_found(0.0)
NULL_not_found([])
NULL_not_found({})
NULL_not_found(())
NULL_not_found(set())
NULL_not_found(math.nan)
print(NULL_not_found("Brian"))
