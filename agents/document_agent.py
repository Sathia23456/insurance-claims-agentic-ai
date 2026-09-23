class DocumentAgent:

    def extract(self, claim):
        return (
            "Document Review\n"
            "---------------\n"
            f"Claim details received: {claim}\n\n"
            "Required documents should be reviewed against the "
            "claim information and applicable policy requirements."
        )