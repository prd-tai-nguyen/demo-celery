from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from celery_tasks import create_task, test_task, create_error_task
from celery import signature, chain

app = FastAPI()


@app.post("/test")
async def run_task(data=Body(...)):
    x = data["x"]
    y = data["y"]

    # task = create_task.delay(x, y)

    # task = signature('create_task', args=(2, 2))
    # result = task.delay()
    # result = result.get()

    # result = create_task.apply_async((2, 3), link=test_task.s(4))
    # a = result.get()
    # b = result.children[0].get()

    # chain_task = chain(create_task.s(4, 4), test_task.s(8), create_task.s(10))
    # result = chain_task.delay()

    result = create_error_task.apply_async(
        (2, 2)
    )
    return JSONResponse({"Result": result.get()})
