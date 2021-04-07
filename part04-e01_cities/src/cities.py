#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cities():
    city = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    pop_per_city = pd.Series(
        [643272, 279044, 231853, 223027, 201810], index=city, name="pop_per_cityulation"
    )
    area_per_city = pd.Series(
        [715.48, 528.03, 689.59, 240.35, 3817.52],
        index=city,
        name="Total area_per_city",
    )
    
    # Generate data frame containing population per city and total area per city
    return pd.DataFrame({"Population": pop_per_city, "Total area": area_per_city})


def main():
    print(cities())


if __name__ == "__main__":
    main()
