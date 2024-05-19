INTRO_PAPER = "https://www.researchgate.net/publication/235641830_On_field_calibration_of_an_electronic_nose_for_benzene_estimation_in_an_urban_pollution_monitoring_scenario"
DATA_SOURCE = "https://archive.ics.uci.edu/dataset/360/air+quality"

FEATURES_ORDERED = ["co_gt", "c6h6_gt", "nox_gt", "no2_gt", "s1_co", "s2_nhmc",  "s3_nox",  "s4_no2", "s5_o3", "temp", "rh", "ah"]
FEATURES_UNORDERED = ["co_gt", "s1_co", "c6h6_gt", "s2_nhmc", "nox_gt", "s3_nox", "no2_gt", "s4_no2", "s5_o3", "temp", "rh", "ah"]
FEATURES = {"co_gt": "True hourly averaged CO (mg/m³)", 
            "c6h6_gt": "True hourly averaged Benzene (µg/m³)", 
            "nox_gt": "True hourly averaged NOₓ concentration (ppb)",
            "no2_gt": "True hourly averaged NO₂ concentration (µg/m³)",
            "s1_co": "Hourly averaged sensor 1 response (CO targeted)", 
            "s2_nhmc": "Hourly averaged sensor 2 response (NMHC targeted)", 
            "s3_nox": "Hourly averaged sensor 3 response (NOₓ targeted)", 
            "s4_no2": "Hourly averaged sensor 4 response (NO₂ targeted)", 
            "s5_o3": "Hourly averaged sensor 5 response (O₃ targeted)", 
            "temp": "Temperature (°C)", 
            "rh": "Relative Humidity (%)", 
            "ah": "Absolute Humidity"}
FEATURES_MEAN = {"co_gt": "2.00", 
            "c6h6_gt": "9.63", 
            "nox_gt": "223.40",
            "no2_gt": "107.09",
            "s1_co": "1090.08", 
            "s2_nhmc": "927.65", 
            "s3_nox": "832.23", 
            "s4_no2": "1443.34", 
            "s5_o3": "1007.72", 
            "temp": "18.55", 
            "rh": "48.54", 
            "ah": "1.02"}