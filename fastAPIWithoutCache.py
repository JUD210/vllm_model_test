from typing import Union
from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.responses import JSONResponse, Response, StreamingResponse
from fastapi import FastAPI
import langchain
from vllm import LLM, SamplingParams
import time
import uvicorn

app = FastAPI()

# How To Use
# https://unfinishedgod.netlify.app/2024/07/26/llm-llama3-1-vllm-api-feat-fastapi/
# 
# 1. Edit model_path
# 2. python3 fastAPIWithoutCache.py # nohup python3 fastAPIWithoutCache.py >> fastAPIWithoutCache.log &
model_path = "/home/jud_ch/_ALL_CODES/Meta-Llama-3.2-3B-Instruct"
llm = LLM(model=model_path,
           max_model_len=512,  # 최대 길이 조정
           gpu_memory_utilization=0.9,  # GPU 메모리 사용량 조절
           tensor_parallel_size=1,  # 텐서 병렬화 크기 조정
           dtype="half"
          )

sampling_params = SamplingParams(temperature=0.7, 
                                 top_p=0.8, 
                                 repetition_penalty=1.05, 
                                 max_tokens=256)


    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/v1/generateText")
async def generateText(request: Request) -> Response:
    request_dict = await request.json()
    prompt = request_dict.pop("prompt")
    print(prompt)
    outputs = llm.generate(prompt, sampling_params)
    generated_text  = outputs[0].outputs[0].text
    print("Generated text:", generated_text)
    ret = {"text": generated_text}
    return JSONResponse(ret)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
