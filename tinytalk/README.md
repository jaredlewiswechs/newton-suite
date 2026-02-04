# TinyTalk

**The Verified General-Purpose Programming Language**

> Every loop bounded. Every operation traced. Every output proven.

TinyTalk is a Turing-complete programming language built on Newton's verified computation architecture. It combines the power of a modern general-purpose language with the safety guarantees of bounded, verifiable execution.

```
┌─────────────────────────────────────────────────────────────────┐
│                        TinyTalk Architecture                     │
├─────────────────────────────────────────────────────────────────┤
│  Source → Lexer → Parser → Type Check → Verify → Execute        │
│                                              ↓                   │
│                                         Bounded                  │
│                                              ↓                   │
│                              Trace ← Ledger ← Result             │
└─────────────────────────────────────────────────────────────────┘
```

## Features

| Feature | Description |
|---------|-------------|
| **Verified Execution** | Every operation is bounded and traced |
| **Turing Complete** | Full loops, recursion, conditionals |
| **Type System** | Static typing with inference |
| **FFI** | Call Python, JavaScript, Go, Rust, C |
| **Functional** | First-class functions, lambdas, pipes |
| **Safe by Default** | No infinite loops, no stack overflow |

## Quick Start

### Installation

```bash
pip install tinytalk
# or from source
git clone https://github.com/your-repo/tinytalk
cd tinytalk
pip install -e .
```

### Hello World

```tinytalk
println("Hello, World!")
```

### Run Code

```python
from tinytalk import run

result = run('println("Hello!")')
```

### REPL

```python
from tinytalk import repl
repl()
```

```
TinyTalk v1.0.0 - Verified Computation
Type 'exit' to quit, 'help' for help

>>> let x = 42
>>> println(x * 2)
84
>>> exit
Goodbye!
```

## Language Reference

### Variables

```tinytalk
// Mutable variable
let x = 10
x = 20

// Immutable constant
const PI = 3.14159
// PI = 3  // Error: Cannot reassign constant
```

### Types

```tinytalk
// Primitives
let n: int = 42
let f: float = 3.14
let s: str = "hello"
let b: bool = true
let nothing = null

// Collections
let list: list[int] = [1, 2, 3]
let map: map[str, int] = {"a": 1, "b": 2}

// Optional
let maybe: ?int = null
```

### Functions

```tinytalk
// Function declaration
fn add(a: int, b: int) -> int {
    return a + b
}

// Lambda expressions
let double = (x) => x * 2

// Higher-order functions
let numbers = [1, 2, 3, 4, 5]
let evens = filter((x) => x % 2 == 0, numbers)
let doubled = map_((x) => x * 2, numbers)
```

### Control Flow

```tinytalk
// If-else
if x > 0 {
    println("positive")
} elif x < 0 {
    println("negative")
} else {
    println("zero")
}

// Ternary
let sign = x > 0 ? "+" : "-"

// For loop
for i in range(10) {
    println(i)
}

// For with collection
for item in [1, 2, 3] {
    println(item)
}

// While loop
let i = 0
while i < 10 {
    println(i)
    i += 1
}

// Match expression
match value {
    1 => println("one"),
    2 => println("two"),
    _ => println("other")
}
```

### Operators

```tinytalk
// Arithmetic
+ - * / // % **

// Comparison
== != < > <= >=

// Logical
and or not

// Bitwise
& | ^ ~ << >>

// Assignment
= += -= *= /= //= %=

// Pipe (functional)
x |> f |> g   // Same as g(f(x))
```

### Structs

```tinytalk
struct Point {
    x: float,
    y: float
}

let p = Point(3.0, 4.0)
println(p.x)  // 3.0

// Methods via functions
fn distance(p: Point) -> float {
    return sqrt(p.x ** 2 + p.y ** 2)
}
```

### Enums

```tinytalk
enum Color {
    Red,
    Green,
    Blue,
    RGB(int, int, int)
}

let c = Color.Red
let custom = Color.RGB(255, 128, 0)
```

### Error Handling

```tinytalk
try {
    let result = risky_operation()
} catch e {
    println("Error: " + e)
} finally {
    cleanup()
}

// Throw errors
throw "Something went wrong"
```

## Standard Library

### Output
```tinytalk
print("no newline")
println("with newline")
```

### Type Functions
```tinytalk
len([1, 2, 3])      // 3
type(42)            // "int"
str(123)            // "123"
int("42")           // 42
float("3.14")       // 3.14
bool(1)             // true
```

### Collections
```tinytalk
range(5)            // [0, 1, 2, 3, 4]
range(1, 5)         // [1, 2, 3, 4]
range(0, 10, 2)     // [0, 2, 4, 6, 8]

append(list, item)
push(list, item)
pop(list)
keys(map)
values(map)
contains(list, item)
slice(list, start, end)
reverse(list)
sort(list)
```

### Higher-Order Functions
```tinytalk
filter(fn, list)
map_(fn, list)
reduce(fn, list, initial)
zip(list1, list2)
enumerate(list)
```

### Strings
```tinytalk
split("a,b,c", ",")     // ["a", "b", "c"]
join(["a", "b"], "-")   // "a-b"
```

### Math
```tinytalk
sum([1, 2, 3])      // 6
min(1, 2, 3)        // 1
max([1, 2, 3])      // 3
abs(-5)             // 5
round(3.7)          // 4
floor(3.7)          // 3
ceil(3.2)           // 4
sqrt(16)            // 4.0
pow(2, 10)          // 1024.0
sin(PI / 2)         // 1.0
cos(0)              // 1.0
tan(PI / 4)         // 1.0
log(E)              // 1.0
exp(1)              // 2.718...
```

### Constants
```tinytalk
PI      // 3.14159...
E       // 2.71828...
TAU     // 6.28318...
INF     // Infinity
NAN     // Not a Number
```

## Foreign Function Interface (FFI)

TinyTalk can call code from other languages.

### Python Interop

```tinytalk
// Import Python module
import @math

let x = math.sqrt(16)
println(x)  // 4.0

// Import specific functions
import @statistics { mean, median }

let data = [1, 2, 3, 4, 5]
println(mean(data))  // 3.0

// Execute Python code directly
let result = eval_python("sum([1, 2, 3, 4, 5])")
println(result)  // 15
```

### JavaScript Interop

```tinytalk
// Execute JavaScript (requires Node.js)
let result = javascript("return args[0] * 2", 21)
println(result)  // 42

// Import Node.js module
import "lodash" as _
```

### HTTP Requests

```tinytalk
// GET request
let response = http_get("https://api.example.com/data")
println(response.status)  // 200
println(response.body)

// POST request
let data = {"name": "TinyTalk"}
let response = http_post("https://api.example.com/create", data)
```

### Shell Commands

```tinytalk
// Run shell command (requires system access)
let result = shell("ls -la")
println(result.stdout)
```

## Verified Execution

TinyTalk guarantees bounded execution through:

### Execution Bounds

```python
from tinytalk import run, ExecutionBounds

bounds = ExecutionBounds(
    max_ops=1_000_000,        # Maximum operations
    max_iterations=100_000,   # Maximum loop iterations
    max_recursion=1000,       # Maximum recursion depth
    timeout_seconds=30.0      # Maximum execution time
)

result = run(source, bounds)
```

### Trace & Ledger

Every execution produces a trace:

```python
from tinytalk import TinyTalkKernel

kernel = TinyTalkKernel()
result = kernel.execute("let x = 1 + 2")

# Check trace
print(result.trace.steps)

# Check ledger
for entry in kernel.ledger.entries:
    print(entry.hash, entry.operation)
```

### Fin/Finfr Results

All operations return verified results:

```python
from tinytalk import fin, finfr

# Success
result = fin(42, trace)

# Failure  
error = finfr("Division by zero", trace)

# Check result
if result.success:
    print(result.value)
else:
    print(result.error)
```

## FFI Security

Control what external code can do:

```python
from tinytalk import FFIConfig, configure_ffi

config = FFIConfig(
    allow_python=True,
    allow_javascript=True,
    allow_system=False,      # No shell commands
    allow_network=False,     # No HTTP requests
    allow_filesystem=False,  # No file access
    trusted_modules=[
        'math', 'json', 'datetime', 
        'collections', 'itertools'
    ]
)

configure_ffi(config)
```

## Examples

### Fibonacci

```tinytalk
fn fib(n: int) -> int {
    if n <= 1 {
        return n
    }
    return fib(n - 1) + fib(n - 2)
}

println(fib(10))  // 55
```

### FizzBuzz

```tinytalk
for i in range(1, 101) {
    if i % 15 == 0 {
        println("FizzBuzz")
    } elif i % 3 == 0 {
        println("Fizz")
    } elif i % 5 == 0 {
        println("Buzz")
    } else {
        println(i)
    }
}
```

### Quick Sort

```tinytalk
fn quicksort(arr: list[int]) -> list[int] {
    if len(arr) <= 1 {
        return arr
    }
    
    let pivot = arr[0]
    let less = filter((x) => x < pivot, slice(arr, 1, null))
    let greater = filter((x) => x >= pivot, slice(arr, 1, null))
    
    return quicksort(less) + [pivot] + quicksort(greater)
}

let sorted = quicksort([3, 1, 4, 1, 5, 9, 2, 6])
println(sorted)  // [1, 1, 2, 3, 4, 5, 6, 9]
```

### Data Processing

```tinytalk
import @json

let data = json.loads('{"users": [{"name": "Alice", "age": 30}]}')
let users = data["users"]

for user in users {
    println(user["name"] + " is " + str(user["age"]))
}
```

### Pipe Operations

```tinytalk
let result = [1, 2, 3, 4, 5]
    |> filter((x) => x % 2 == 0)
    |> map_((x) => x * 2)
    |> sum

println(result)  // 12
```

## Architecture

```
tinytalk/
├── __init__.py      # Package exports
├── kernel.py        # Newton verified execution kernel
├── lexer.py         # Tokenizer (~100 token types)
├── parser.py        # Recursive descent parser (20+ AST nodes)
├── types.py         # Type system with inference
├── runtime.py       # Interpreter with bounded execution
├── ffi.py           # Foreign function interface
└── stdlib.py        # Standard library functions
```

## Philosophy

TinyTalk is built on three principles:

1. **The constraint IS the instruction** - Execution bounds aren't limits, they're guarantees
2. **The verification IS the computation** - Every operation is automatically verified
3. **The trace IS the proof** - Full audit trail for every execution

## License

MIT License - See [LICENSE](LICENSE) for details.

---

*Built with Newton Supercomputer - Where 1 == 1*
