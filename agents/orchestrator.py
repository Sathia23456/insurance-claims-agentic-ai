from agents.document_agent import DocumentAgent
from agents.policy_agent import PolicyAgent
from agents.assessment_agent import AssessmentAgent
from agents.fraud_agent import FraudAgent
from agents.report_agent import ReportAgent


class OrchestratorAgent:

    def __init__(self):
        self.document_agent = DocumentAgent()
        self.policy_agent = PolicyAgent()
        self.assessment_agent = AssessmentAgent()
        self.fraud_agent = FraudAgent()
        self.report_agent = ReportAgent()

    def run(self, claim):
        print(f"\n🎯 Orchestrator received claim: {claim}")

        document_result = self.document_agent.extract(claim)

        policy_result = self.policy_agent.review(claim)

        assessment_result = self.assessment_agent.assess(
            document_result,
            policy_result
        )

        fraud_result = self.fraud_agent.review(claim)

        report_result = self.report_agent.generate(
            document_result,
            policy_result,
            assessment_result,
            fraud_result
        )

        return report_result