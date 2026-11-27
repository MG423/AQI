from tinydb import TinyDB, Query
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../../analytics_database.json")
db = TinyDB(DB_PATH)

analytics_collection = db.table("city_analytics")
enforcement_logs = db.table("enforcement_logs")

db_available = True

# Automatically seed the database with real structural data if it's empty
if len(analytics_collection) == 0:
    analytics_collection.insert_multiple([
        {"city": "New Delhi", "current_avg_aqi": 280, "primary_pollutant_source": "Industrial", "enforcement_compliance_rate": "65%", "trend": "increasing"},
        {"city": "Mumbai", "current_avg_aqi": 150, "primary_pollutant_source": "Traffic", "enforcement_compliance_rate": "82%", "trend": "stable"},
        {"city": "Bangalore", "current_avg_aqi": 85, "primary_pollutant_source": "Traffic", "enforcement_compliance_rate": "90%", "trend": "decreasing"}
    ])

if len(enforcement_logs) == 0:
    enforcement_logs.insert_multiple([
        {"id": "INV-101", "target": "Flatted Factories", "aqi_before": 250, "aqi_after": 210, "status": "Success"},
        {"id": "INV-102", "target": "Open Waste Fire", "aqi_before": 310, "aqi_after": 305, "status": "Failed"}
    ])
