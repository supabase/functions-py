# Functions-py


## Installation

`pip3 install supafunc`

## Usage

Deploy your function as per documentation.


```python3

from supafunc import FunctionsClient
async def run_func():
    fc = FunctionsClient("https://<project_ref>.functions.supabase.co", {})
    res = await fc.invoke("payment-sheet", {"responseType": "json"})

if __name__ == "__main__":
    asyncio.run(run_func())
```