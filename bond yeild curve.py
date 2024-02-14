import numpy as np
import plotly.graph_objects as go


def bootstrap_yield_curve(bonds):
    spot_rates = np.zeros(len(bonds))


    for i, (price, coupon_rate, maturity) in enumerate(
            sorted(bonds, key=lambda x: x[2])):
        cash_flows = np.array(
            [coupon_rate] * int(maturity - 1) + [100 + coupon_rate])
        time_periods = np.arange(1, maturity + 1)
        # Use previously calculated spot rates for discounted cash flows

        if i == 0:
            discounted_cash_flows = cash_flows / (1 + spot_rates[i])**time_periods
        else:
            discounted_cash_flows = [cf / (1 + spot_rates[j]) ** time_periods[j]
                                     for j, cf in enumerate(cash_flows)]
            discounted_cash_flows = np.sum(discounted_cash_flows)

        residual = price - discounted_cash_flows
        if residual <= 0:
            # Handle cases where residual is too low
            print(
                f"Warning: Residual for bond with maturity {maturity} is too low. Adjusting spot rate calculation.")
            spot_rate = spot_rates[
                i - 1]  # Use previous spot rate as an approximation
        else:
            if i == 0:
                spot_rate = -0.029
            else:
                spot_rate = ((100 / residual) ** (1 / maturity)) - 1
        spot_rates[i] = spot_rate

    return spot_rates

import csv
file = open("apm466 data 2.csv", newline='')
files = csv.reader(file)
file.__next__()

bonds4 = []
bonds5 = []
bonds6 = []
bonds7 = []
bonds8 = []
bonds9 = []
bonds10 = []
bonds11 = []
bonds12 = []
bonds13 = []
bonds14 = []
for row in files:
    bonds4.append((float(row[4]), float(row[3][:-1]), float(row[2])))
    bonds5.append((float(row[5]), float(row[3][:-1]), float(row[2])))
    bonds6.append((float(row[6]), float(row[3][:-1]), float(row[2])))
    bonds7.append((float(row[7]), float(row[3][:-1]), float(row[2])))
    bonds8.append((float(row[8]), float(row[3][:-1]), float(row[2])))
    bonds9.append((float(row[9]), float(row[3][:-1]), float(row[2])))
    bonds10.append((float(row[10]), float(row[3][:-1]), float(row[2])))
    bonds11.append((float(row[11]), float(row[3][:-1]), float(row[2])))
    bonds12.append((float(row[12]), float(row[3][:-1]), float(row[2])))
    bonds13.append((float(row[13]), float(row[3][:-1]), float(row[2])))
    bonds14.append((float(row[14]), float(row[3][:-1]), float(row[2])))



spot_rates4 = bootstrap_yield_curve(bonds4)
spot_rates5 = bootstrap_yield_curve(bonds5)
spot_rates6 = bootstrap_yield_curve(bonds6)
spot_rates7 = bootstrap_yield_curve(bonds7)
spot_rates8 = bootstrap_yield_curve(bonds8)
spot_rates9 = bootstrap_yield_curve(bonds9)
spot_rates10 = bootstrap_yield_curve(bonds10)
spot_rates11 = bootstrap_yield_curve(bonds11)
spot_rates12 = bootstrap_yield_curve(bonds12)
spot_rates13 = bootstrap_yield_curve(bonds13)
spot_rates14 = bootstrap_yield_curve(bonds14)


maturities4 = [bond[2] for bond in bonds4]
maturities5 = [bond[2] for bond in bonds5]
maturities6 = [bond[2] for bond in bonds6]
maturities7 = [bond[2] for bond in bonds7]
maturities8 = [bond[2] for bond in bonds8]
maturities9 = [bond[2] for bond in bonds9]
maturities10 = [bond[2] for bond in bonds10]
maturities11 = [bond[2] for bond in bonds11]
maturities12 = [bond[2] for bond in bonds12]
maturities13 = [bond[2] for bond in bonds13]
maturities14 = [bond[2] for bond in bonds14]


fig = go.Figure(
    go.Scatter(x=maturities4, y=spot_rates4 * 100, mode='lines+markers'))
fig.add_scatter(x=maturities5, y=spot_rates5 * 100, mode='lines+markers', name="day 2")
fig.add_scatter(x=maturities6, y=spot_rates6 * 100, mode='lines+markers', name="day 3")
fig.add_scatter(x=maturities7, y=spot_rates7 * 100, mode='lines+markers', name="day 4")
fig.add_scatter(x=maturities8, y=spot_rates8 * 100, mode='lines+markers', name="day 5")
fig.add_scatter(x=maturities9, y=spot_rates9 * 100, mode='lines+markers', name="day 6")
fig.add_scatter(x=maturities10, y=spot_rates10 * 100, mode='lines+markers', name="day 7")
fig.add_scatter(x=maturities11, y=spot_rates11 * 100, mode='lines+markers', name="day 8")
fig.add_scatter(x=maturities12, y=spot_rates12 * 100, mode='lines+markers', name="day 9")
fig.add_scatter(x=maturities13, y=spot_rates13 * 100, mode='lines+markers', name="day 10")
fig.add_scatter(x=maturities14, y=spot_rates14 * 100, mode='lines+markers', name="day 11")

fig.update_layout(title='Bootstrapped Yield Curve',
                  xaxis_title='Maturity (Years)', yaxis_title='Spot Rate (%)')
fig.show()
