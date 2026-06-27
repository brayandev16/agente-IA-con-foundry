# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://agentbrayanrodriguez-resource.services.ai.azure.com/api/projects/agentbrayanrodriguez"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "history-agent"
my_version = "1"

openai_client = project_client.get_openai_client()

print("Agent is ready. Type 'quit' to exit.")
while True:
    user_input = input("\nYou: ")
    if user_input.strip().lower() == 'quit':
        print("Goodbye!")
        break

    try:
        # Reference the agent to get a response
        response = openai_client.responses.create(
            input=[{"role": "user", "content": user_input}],
            extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
        )
        print(f"Agent: {response.output_text}")
    except Exception as e:
        print(f"An error occurred: {e}")
