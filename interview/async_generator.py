import asyncio
import time

start = time.time()


async def async_generator():
    for i in range(5):
        # await asyncio.sleep(1)
        yield i


async def main():
    async for value in async_generator():
        print(value)


# asyncio.run(main())
# print(time.time() - start)

async def async_gen():
    for i in range(4):
        # await asyncio.sleep(1)
        yield i


async def manual_iteration():
    gen = aiter(async_gen())
    try:
        while True:
            value = await anext(gen)
            print(value)
    except StopAsyncIteration:
        pass


asyncio.run(manual_iteration())
print(time.time() - start)
