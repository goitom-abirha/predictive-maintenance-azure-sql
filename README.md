# predictive-maintenance-azure-sql
Predictive Maintenance ML project (Completed Jan–Mar 2023) using simulated IoT data, Python, and Azure SQL.

---

## Documentation (Completed 2023)

### **Project Proposal**
- [PDF](docs/Predictive_Maintenance_Project_Proposal.pdf)
- [DOCX](docs/Predictive_Maintenance_Project_Proposal.docx)

### **Project Plan – 8 Week Timeline**
- [PDF](docs/Predictive_Maintenance_Project_Plan.pdf)
- [DOCX](docs/Predictive_Maintenance_Project_Plan.docx)

---

## Repository Structure (Planned)

docs/ → Project proposal, project plan, diagrams
data/ → Simulated IoT sensor data (later)
notebooks/ → Jupyter notebooks (simulation, features, modeling)
src/ → Python scripts (data simulation, features, training)
sql/ → SQL schema + queries
figures/ → EDA plots + evaluation charts
models/ → Saved ML model (.pkl)

## 4. Model Performance

The goal of the model is to predict whether a machine will experience a failure
within the next 72 hours (`failure_within_72h = 1`) using engineered sensor
features.

### 4.1 Model Comparison

The following models were trained and evaluated on a held-out test set:

| Model           | Accuracy | Precision | Recall | F1-score | ROC–AUC |
|-----------------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.991 | 0.932 | 0.987 | 0.959 | **0.999** |
| Gradient Boosting   | 0.996 | 0.993 | 0.967 | 0.980 | 0.999 |
| Random Forest       | 0.996 | 1.000 | 0.959 | 0.979 | 0.998 |

> **Note:** All models perform extremely well on this synthetic IoT dataset.  
> Logistic Regression was selected as the **primary model** because it achieves
> the highest ROC–AUC while remaining simple, fast, and easy to interpret.

- **Accuracy** ≈ 99% → the model correctly classifies almost all hourly readings.  
- **Precision** (LogReg ≈ 0.93) → when the model predicts an upcoming failure, it is correct ~93% of the time.  
- **Recall** (LogReg ≈ 0.99) → the model detects almost all true upcoming failures.  
- **ROC–AUC** (LogReg ≈ 0.999) → the model has excellent ranking ability in distinguishing risky vs. healthy machine states.

### 4.2 Selected Model

- **Chosen model:** Logistic Regression (with StandardScaler and class_weight="balanced")  
- **Saved artifact:** `models/best_model.pkl`  
- **Metrics log:** `models/model_metrics.json` (contains all model scores)

These artifacts will be used in Week 4 for integration with Azure SQL
and optional deployment steps (API or dashboard).

## 5. Azure SQL Integration (Week 4)

Week 4 focused on deploying the engineered dataset to **Azure SQL Database** and establishing
a cloud-based data pipeline.

### Key actions:
- Configured Azure SQL server (`goitom-pm-sqlserver`) on East US 2
- Created database `predictive_maintenance_db`
- Enabled public endpoint & firewall to allow secure access
- Created SQL table `SensorFeatures`
- Wrote ingestion script using `pyodbc` and secure password handling
- Inserted all engineered features into Azure SQL
- Verified rows using Azure Query Editor

Notebook:  
`notebooks/04_azure_sql_ingestion.ipynb`

## 6. Power BI Dashboard (Week 5)

In Week 5, the project connects live Azure SQL data to Power BI to build an
interactive predictive maintenance dashboard.

### Key visuals:
- KPI Cards:
  - Machines monitored
  - Predicted failures (next 72 hours)
  - Failure rate (%)
- Bar chart: failures by machine
- Line chart: sensor trends over time
- Slicers: machine, day of week, hour of day

Power BI File:
`powerbi/predictive_maintenance_dashboard.pbix`

This dashboard allows maintenance teams to monitor risk levels, view real-time
sensor behavior, and prioritize repairs.
