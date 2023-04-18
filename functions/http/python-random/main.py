import random

import functions_framework


@functions_framework.http
def handler(request):
    times = request.args.get("times")
    if not times:
        # return a random number
        return {"number": random.randint(1, 100)}
    else:
        # return a list of random numbers of length times
        return {"numbers": [random.randint(1, 100) for _ in range(int(times))]}

    return {"number": 0}
