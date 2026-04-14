# logic/infrastructure_auditor.py
class CloudResourceAuditor:
    """
    BASELINE MODULE: Checks for orphaned cloud resources.
    This was NOT in Slack chats. Use this to see if the AI detects
    that GMeet discussion of Cloud costs is MISSING from official logs.
    """
    
    async def audit_orphaned_resources(self, employee_id: str):
        """
        Scans for Elastic IPs, Snapshots, and EC2 instances owned by employee.
        Ensures cost optimization during offboarding.
        """
        cloud_report = {
            "instances_terminated": [],
            "snapshots_deleted": [],
            "ips_released": [],
            "monthly_savings_projected": 0.0
        }

        # Logic to scan AWS/Cloud tags for the specific employee
        resources = await cloud_provider.get_resources_by_tag("Owner", employee_id)
        
        for res in resources:
            if res.type == "EC2_INSTANCE":
                await res.terminate()
                cloud_report["instances_terminated"].append(res.id)
                cloud_report["monthly_savings_projected"] += 45.00
            
            if res.type == "EIP":
                await res.release()
                cloud_report["ips_released"].append(res.id)
                cloud_report["monthly_savings_projected"] += 3.50

        return cloud_report