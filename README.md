# OAR-Dashboard
Simple dashboard script to visualise dose to organs at risk (OARs). Values from the treatment plans as generated in [Box-Plots](../../../Box-Plots). The purpose of this code is to see how dose to OARs is affected by factors such as tumour size, target conformity or leaf width.

## Requirements
For this code to work, you will need to provide a .csv file matching the format of the template provided. All volumes are in centimetres cubed [cc].
Python packages used are dash, plotly and pandas.

## How It Works
In the file app.py, enter the metrics to compare. The dashboard presents data in 4 dimensions: {x, y, size and colour}. Hovering over each data point will return all the values associated with that point. The metrics you can plot against are listed in the table below.

| Variable Name | Description                                            | Allowed Dimensions  |
| ------------- | ------------------------------------------------------ | ------------------- |
| `PlanID`      | MLC Leaf Width {2.5mm, 5mm, 10mm}                      | All, except size    |
| `Site`        | Anatomical Site {Prostate, Lung, Liver}                | All, except size    |
| `OAR`         | Organ at Risk {Total: 8}                               | All, except size    |
| `Volume`      | Volume of the Tumour (PTV) [cc]                        | All                 |
| `CI_RTOG100`  | Conformity Index of PTV, treated volume/planned volume | All                 |
| `ALPO`        | Average Leaf Pair Opening [mm]                         | All                 |
| `MUperGy`     | Monitor Units per Gy                                   | All                 |
| `V60Gy`       | Percentage of OAR Volume receiving 60Gy                | All                 |
| `V50Gy`       | Percentage of OAR Volume receiving 50Gy                | All                 |
| `V45Gy`       | Percentage of OAR Volume receiving 45Gy                | All                 |
| `V40Gy`       | Percentage of OAR Volume receiving 40Gy                | All                 |
| `V35Gy`       | Percentage of OAR Volume receiving 35Gy                | All                 |
| `V30Gy`       | Percentage of OAR Volume receiving 30Gy                | All                 |
| `V25Gy`       | Percentage of OAR Volume receiving 25Gy                | All                 |
| `V20Gy`       | Percentage of OAR Volume receiving 20Gy                | All                 |
| `V5Gy`        | Percentage of OAR Volume receiving 5Gy                 | All                 |
| `D5cc`        | Absolute dose received by 5cc of the OAR               | All                 |
| `D0cc`        | Absolute dose received by 0cc of the OAR               | All                 |

If the plot does not immediately open, the development server address will print in the terminal. Copy-paste the address into a web browser and the plot should open.
