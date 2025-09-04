from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

class CriticalValueManager:
    def __init__(self):
        self.critical_ranges = {
            "Glucose": {"low": 40, "high": 500},
            "Potassium": {"low": 2.5, "high": 6.5},
            "Hemoglobin": {"low": 7.0, "high": 20.0},
            "Platelets": {"low": 50, "high": 1000},
            "INR": {"low": None, "high": 5.0}
        }
        self.notification_timeout = 30  # minutes
        
    def check_critical(self, test_name, value):
        """Check if value is critical"""
        if test_name in self.critical_ranges:
            ranges = self.critical_ranges[test_name]
            if ranges["low"] and value < ranges["low"]:
                return True, "CRITICAL_LOW"
            if ranges["high"] and value > ranges["high"]:
                return True, "CRITICAL_HIGH"
        return False, None
    
    def notify_provider(self, patient_id, test_name, value, provider_contact):
        """Send critical value notification"""
        notification = {
            "patient_id": patient_id,
            "test": test_name,
            "value": value,
            "timestamp": datetime.now(),
            "provider": provider_contact,
            "status": "PENDING",
            "attempts": 0
        }
        
        # Would implement actual notification logic here
        return notification
    
    def track_acknowledgment(self, notification_id, acknowledged_by):
        """Track provider acknowledgment of critical value"""
        return {
            "notification_id": notification_id,
            "acknowledged_by": acknowledged_by,
            "acknowledged_at": datetime.now(),
            "time_to_acknowledge": "5 minutes"  # Calculate actual
        }
