#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

population = ["47.2 White",
          "25.8 Hispanic",
          "13.7 Black",
          "8.3 Asian",
          "5 Multiracial"]

data = [float(x.split()[0]) for x in population]
race = [x.split()[-1] for x in population]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, race,
          title="Race",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
 
plt.setp(autotexts, size=8, weight="bold")

ax.set_title("US CENSUS: Projected 2024 US Population")
plt.savefig("/home/student/mycode/2024uspopulation.png")
        # save a copy to "~/static" (the "files" view)
plt.savefig("/home/student/static/2024uspopulation.png")

if __name__ == "__main__":
    main()
