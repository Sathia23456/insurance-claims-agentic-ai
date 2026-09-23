class ReportAgent:

    def generate(self, document_result, policy_result, assessment_result, fraud_result):
        return (
            "\n"
            "🏦 INSURANCE CLAIMS ASSESSMENT REPORT\n"
            "=====================================\n\n"
            "📄 Document Review\n"
            "------------------\n"
            f"{document_result}\n\n"
            "📋 Policy Review\n"
            "----------------\n"
            f"{policy_result}\n\n"
            "🔎 Claim Assessment\n"
            "-------------------\n"
            f"{assessment_result}\n\n"
            "🚨 Fraud Indicator Review\n"
            "-------------------------\n"
            f"{fraud_result}\n\n"
            "👨‍💼 Human Review\n"
            "----------------\n"
            "This system is a decision-support prototype. "
            "Final claim decisions require review by an "
            "authorized insurance professional."
        )