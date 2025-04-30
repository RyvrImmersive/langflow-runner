from fastapi import FastAPI, Request
import langflow

app = FastAPI()

@app.post("/run-my-flow")
async def run_my_flow(request: Request):
    body = await request.json()
    input_data = body.get("input", {})
    # Replace below with your actual Langflow load logic
    flow = langflow.load_flow("your_flow.json")
    output = await flow.run_async(inputs=input_data)
    return {"output": output}
