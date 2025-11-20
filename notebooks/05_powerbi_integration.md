# Week 5 – Power BI Integration (Azure SQL → Live Dashboard)

This file documents how the engineered sensor_features dataset from Azure SQL
was connected to Power BI using **DirectQuery** to build real-time dashboards.

---

## 1. Connect to Azure SQL Database

1. Open **Power BI Desktop**
2. Select **Get Data**
3. Choose **Azure SQL Database**
4. Enter:
   - **Server:** goitom-pm-sqlserver.database.windows.net
   - **Database:** predictive_maintenance_db
5. Sign in using SQL authentication:
   - Username: `sqladmin`
   - Password: your environment variable password
6. Select **DirectQuery** for live connection

---

## 2. Load the SensorFeatures Table

- Select table: **sensor_features**
- Click **Load**

This allows Power BI to query Azure SQL in real time without importing data.

---

## 3. Build KPI Dashboard 

Visuals created:
- Card: Total Sensor Readings  
- Card: Failures Detected  
- Card: Model Accuracy  
- Card: Precision  
- Card: Recall  
- Slicer: Machine ID  
- Line Chart: Failures Over Time  

---

## 4. Build Analytics Dashboard 

Visuals created:
- Slicer: Machine ID  
- Slicer: Reading Time  
- Line Chart: Failure Trend  
- Line Chart: Temperature Trend  
- Line Chart: Vibration Trend  
- Bar Chart: Failures by Machine  
- Line/Bar Chart: Pressure Trend  

---

## 5. Dashboard Output

dashboards/predictive_maintenance_dashboard.pbix

Screenshots saved in:

figures/kpi_dashboard.png
figures/analytics_dashboard.png


---

## 6. Notes

- DirectQuery ensures the dashboard updates automatically when Azure SQL updates.
- This completes the Week 5 step of the Predictive Maintenance project pipeline.


