class FraudAgent:

    def review(self, claim):
        return (
            "Fraud Indicator Review\n"
            "----------------------\n"
            f"Claim submitted: {claim}\n\n"
            "Potential indicators such as inconsistent information, "
            "unusual timing, duplicate documentation, or suspicious "
            "patterns should be reviewed.\n\n"
            "Important: An indicator does not establish fraud. "
            "Further investigation and human review are required."
        )