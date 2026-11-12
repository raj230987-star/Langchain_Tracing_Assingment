
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 1. INITIALIZE CHAT MODEL
# ==========================================

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# ==========================================
# 2. CREATE THREE DIFFERENT PROMPTS
# ==========================================

prompts = [
    {
        "name": "Prompt 1 - Basic",
        "text": "What is the Internet of Things? Explain in 3 sentences."
    },
    {
        "name": "Prompt 2 - Technical",
        "text": """
        Explain how an industrial temperature sensor
        communicates with a PLC and SCADA system.

        Include:
        1. Sensor output
        2. Signal transmission
        3. PLC processing
        4. SCADA monitoring

        Give a practical example.
        """
    },
    {
        "name": "Prompt 3 - Detailed",
        "text": """
        I am an Electrical and Instrumentation Engineer.

        Prepare a detailed technical implementation plan
        for an IoT-based marine weather monitoring system.

        The system should include:

        1. Wind speed and direction sensors
        2. Temperature and humidity sensors
        3. Data acquisition system
        4. RS485 and Modbus communication
        5. Edge computer and data logger
        6. GSM/4G communication
        7. Cloud server and database
        8. Real-time web dashboard

        Explain the system architecture, hardware,
        communication flow, data storage, challenges
        and practical implementation steps.

        Organize the answer using clear headings.
        """
    }
]

# ==========================================
# 3. SEND PROMPTS TO OPENAI
# ==========================================

for prompt in prompts:

    print("\n" + "=" * 60)
    print(prompt["name"])
    print("=" * 60)

    response = model.invoke(prompt["text"])

    print("\nAI RESPONSE:")
    print(response.content)

print("\nAll three prompts completed successfully!")
