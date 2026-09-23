class AssessmentAgent:

    def assess(self, document_result, policy_result):
        return (
            "Claim Assessment\n"
            "----------------\n\n"
            "📄 Document Findings\n"
            f"{document_result}\n\n"
            "📋 Policy Findings\n"
            f"{policy_result}\n\n"
            "🔎 Assessment Summary\n"
            "The claim information has been reviewed against "
            "the retrieved policy information.\n\n"
            "Assessment status: Further evidence and human review "
            "are required before any claim decision is made."
        )