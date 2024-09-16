import frappe

def test():
    frappe.log_error(message="This is a scheduled message printed every minute", title="Minute Scheduler Test")