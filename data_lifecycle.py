# logic/data_lifecycle.py
class SafetyGateManager:
    """
    Implements safety mechanisms for drive deletion and seat reclamation.
    Slack Context: 'Literal undo button' and '30-day soft-delete state.'
    """
    RETENTION_PERIOD = 30  # Days

    async def initiate_safe_deletion(self, employee_id: str, drive_id: str):
        """
        Instead of permanent purge, move to 'Soft Delete' state.
        Allows DataSafe leads to have a safety net.
        """
        # Step 1: Verification of 'Transfer Ownership'
        if not await self._check_ownership_transfer(drive_id):
            return {"status": "BLOCKED", "reason": "Ownership not transferred to Manager."}

        # Step 2: Timestamp the deletion for the 30-day grace period
        purge_date = datetime.now() + timedelta(days=self.RETENTION_PERIOD)
        
        await db.update("drives", {"id": drive_id}, {
            "state": "SOFT_DELETE",
            "purge_date": purge_date,
            "is_recoverable": True
        })

        return {"status": "SUCCESS", "purge_deadline": purge_deadline}

    async def _check_ownership_transfer(self, drive_id: str):
        # Slack Context: 'Did you explain the Transfer Ownership safety gate?'
        metadata = await db.fetch("drive_metadata", drive_id)
        return metadata.get("has_delegate_access") is True