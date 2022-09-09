# OAR-Dashboard
Simple dashboard script to visualise dose to organs at risk (OARs). Values from the treatment plans as generated in [Box-Plots](../../../Box-Plots). The purpose of this code is to see how dose to OARs is affected by factors such as tumour size, target conformity or leaf width.

The code is built and modified from a tutorial code provided by [Statworx](https://github.com/STATWORX/blog/blob/master/DashApp/app.py). 

## Requirements
For this code to work, you will need to provide a .csv file matching the format of the template provided. All volumes are in centimetres cubed [cc].
Python packages used are dash, plotly and pandas, listed in requirements.txt .

The folder assests contains a style sheet provided by statworx. Dash will automatically load .css files placed in a folder named "assets".

## How It Works
Run the file app.py and open the development server address printed in the terminal. The left-hand side will have three dropdown menus. Select one or more leaf widths to display on the graphs on the right-hand side. You can also isolate via specific Organ At Risk.

The right-hand side displays the resulting graphs. On top is the PTV Volume against dose metric and on the bottom is Conformity Index against dose metric. Hovering over the data point will return the specific x,y values.

If you wish to change what is being plotted against, as opposed to Volume and Conformity Index, edit lines 14 and 15 with one of the variables listed in the table below.

| Variable Name | Description                                            | <!---Allowed Dimensions  |--->
| ------------- | ------------------------------------------------------ | <!---------------------- |--->
| `PlanID`      | MLC Leaf Width {2.5mm, 5mm, 10mm}                      | <!---All, except size    |--->
| `Site`        | Anatomical Site {Prostate, Lung, Liver}                | <!---All, except size    |--->
| `OAR`         | Organ at Risk {Total: 8}                               | <!---All, except size    |--->
| `Volume`      | Volume of the Tumour (PTV) [cc]                        | <!---All                 |--->
| `CI_RTOG100`  | Conformity Index of PTV, treated volume/planned volume | <!---All                 |--->
| `ALPO`        | Average Leaf Pair Opening [mm]                         | <!---All                 |--->
| `MUperGy`     | Monitor Units per Gy                                   | <!---All                 |--->
| `V60Gy`       | Percentage of OAR Volume receiving 60Gy                | <!---All                 |--->
| `V50Gy`       | Percentage of OAR Volume receiving 50Gy                | <!---All                 |--->
| `V45Gy`       | Percentage of OAR Volume receiving 45Gy                | <!---All                 |--->
| `V40Gy`       | Percentage of OAR Volume receiving 40Gy                | <!---All                 |--->
| `V35Gy`       | Percentage of OAR Volume receiving 35Gy                | <!---All                 |--->
| `V30Gy`       | Percentage of OAR Volume receiving 30Gy                | <!---All                 |--->
| `V25Gy`       | Percentage of OAR Volume receiving 25Gy                | <!---All                 |--->
| `V20Gy`       | Percentage of OAR Volume receiving 20Gy                | <!---All                 |--->
| `V5Gy`        | Percentage of OAR Volume receiving 5Gy                 | <!---All                 |--->
| `D5cc`        | Absolute dose received by 5cc of the OAR               | <!---All                 |--->
| `D0cc`        | Absolute dose received by 0cc of the OAR               | <!---All                 |--->
