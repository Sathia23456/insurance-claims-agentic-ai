from agents.orchestrator import OrchestratorAgent


def main():
    print("🏦 Insurance Claims Agentic AI")
    print("=" * 45)

    claim = input("Enter insurance claim details: ")

    orchestrator = OrchestratorAgent()

    result = orchestrator.run(claim)

    print("\n📋 Final Claims Assessment Report")
    print("-" * 45)
    print(result)


if __name__ == "__main__":
    main()