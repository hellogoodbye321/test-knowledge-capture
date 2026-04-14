# logic/sales_pricing.py
class DealOrchestrator:
    """
    Handles complex pricing tiers and legal workflows for Enterprise accounts.
    Slack Context: 15% discount on 3-year deals and Hooli RFP discovery.
    """
    DISCOUNT_RATE = 0.15
    MIN_COMMITMENT_YEARS = 3

    def calculate_enterprise_bid(self, user_count: int, years: int, is_soc2_required: bool):
        base_price = 12.00  # Per user/month
        if user_count > 1000:
            base_price = 8.50  # Bulk discount tier
        
        total_contract_value = (user_count * base_price) * (years * 12)
        
        # Applying the 'Nitin' 15% Multi-year rule
        if years >= self.MIN_COMMITMENT_YEARS:
            total_contract_value *= (1 - self.DISCOUNT_RATE)
            applied_discount = True
        else:
            applied_discount = False

        return {
            "total_arr": total_contract_value / years,
            "tcv": total_contract_value,
            "compliance_add_on": "SOC2_PREMIUM" if is_soc2_required else "STANDARD",
            "multi_year_discount_applied": applied_discount
        }

    async def track_legal_review(self, document_id: str):
        """
        Tracks Legal review status. 
        Slack Context: 'Legal is backed up, follow up Monday morning.'
        """
        submission_date = datetime.now()
        # Simulated legal queue delay
        if submission_date.weekday() >= 4:  # Friday or weekend
            eta = submission_date + timedelta(days=3)
        else:
            eta = submission_date + timedelta(days=1)
            
        return {"doc_id": document_id, "status": "PENDING_LEGAL", "estimated_completion": eta}