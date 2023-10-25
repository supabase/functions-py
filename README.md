# Functions-py


## Installation

`pip3 install supafunc`

## Usage

Deploy your function as per documentation.


```python3
import asyncio
from supafunc import AsyncFunctionsClient
async def run_func():
    fc = AsyncFunctionsClient("https://<project_ref>.functions.supabase.co", {})
    res = await fc.invoke("payment-sheet", {"responseType": "json"})

if __name__ == "__main__":
    asyncio.run(run_func())
```
