import yaml
from core.llm_client import call_llm
from core.sampler import sample_responses

with open("config/prompts.yaml") as f:
    prompt = yaml.safe_load(f)[0]["prompt"]

responses = sample_responses(call_llm, prompt, k=10)

with open("baseline_outputs.txt", "w") as f:
    for r in responses:
        f.write(r.replace("\n", " ") + "\n")
