"""
TinyTalk Web IDE Server
Monaco-powered editor with live execution
"""

import sys
import os
import json
import time
import traceback
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from flask import Flask, request, jsonify, send_from_directory
from tinytalk import run, ExecutionBounds
from tinytalk.runtime import TinyTalkError

app = Flask(__name__, static_folder='static')

# ═══════════════════════════════════════════════════════════════════════════════
# ROUTES
# ═══════════════════════════════════════════════════════════════════════════════

@app.route('/')
def index():
    """Serve the main IDE page."""
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files."""
    return send_from_directory('static', path)

@app.route('/api/run', methods=['POST'])
def run_code():
    """Execute TinyTalk code and return results."""
    data = request.get_json()
    code = data.get('code', '')
    
    # Capture print output
    import io
    from contextlib import redirect_stdout
    
    stdout_capture = io.StringIO()
    
    start_time = time.time()
    
    try:
        bounds = ExecutionBounds(
            max_ops=1_000_000,
            max_iterations=100_000,
            max_recursion=500,
            timeout_seconds=10.0
        )
        
        with redirect_stdout(stdout_capture):
            result = run(code, bounds)
        
        elapsed = (time.time() - start_time) * 1000
        output = stdout_capture.getvalue()
        
        # Format result
        result_str = str(result) if result.type.value != 'null' else ''
        
        return jsonify({
            'success': True,
            'output': output,
            'result': result_str,
            'elapsed_ms': round(elapsed, 2)
        })
        
    except TinyTalkError as e:
        elapsed = (time.time() - start_time) * 1000
        return jsonify({
            'success': False,
            'error': str(e),
            'output': stdout_capture.getvalue(),
            'elapsed_ms': round(elapsed, 2)
        })
    except SyntaxError as e:
        elapsed = (time.time() - start_time) * 1000
        return jsonify({
            'success': False,
            'error': f"Syntax Error: {e}",
            'output': stdout_capture.getvalue(),
            'elapsed_ms': round(elapsed, 2)
        })
    except Exception as e:
        elapsed = (time.time() - start_time) * 1000
        return jsonify({
            'success': False,
            'error': f"{type(e).__name__}: {e}",
            'output': stdout_capture.getvalue(),
            'elapsed_ms': round(elapsed, 2)
        })

@app.route('/api/examples')
def get_examples():
    """Get example programs - using ultra-clean tinyTalk syntax."""
    examples = [
        {
            'name': 'Hello World',
            'code': '''// The cleanest Hello World
show("Hello World!")
show("Welcome to tinyTalk!")'''
        },
        {
            'name': '📜 when (Facts)',
            'code': '''// WHEN - Declares immutable facts

when answer = 42
when name = "Newton"
when pi = 3.14159

// show() auto-converts everything!
show("The answer is", answer)
show("Name:", name)
show("Pi:", pi)

// Or use + with .str for concat
show("Combined: " + name + " says " + answer.str)'''
        },
        {
            'name': '🔧 Property Magic',
            'code': '''// Property conversions - no function calls!
// x.str  -> to string
// x.num  -> to number  
// x.int  -> to integer
// x.bool -> to boolean
// x.type -> type name
// x.len  -> length

let num = 42
let text = "3.14"
let flag = true

show("=== Type Conversions ===")
show("num.str:", num.str)
show("text.num:", text.num)
show("text.int:", text.int)
show("flag.int:", flag.int)
show("num.type:", num.type)

show("")
show("=== String Properties ===")
let msg = "  hello world  "
show("original:", msg)
show("trimmed:", msg.trim)
show("upper:", msg.upper)
show("len:", msg.len)

show("")
show("=== List Properties ===")
let items = [1, 2, 3, 4, 5]
show("items:", items)
show("first:", items.first)
show("last:", items.last)
show("len:", items.len)
show("empty:", items.empty)

show("")
show("=== String Concat ===")
show("The number is " + num.str + "!")'''
        },
        {
            'name': '🔨 forge (Actions)',
            'code': '''// FORGE - Actions that can change state

forge greet(name)
    show("Hello", name)
    reply "greeted"
end

forge countdown(n)
    while n > 0 {
        show(n)
        n = n - 1
    }
    show("Liftoff!")
    reply "done"
end

greet("World")
show("")
countdown(5)'''
        },
        {
            'name': '⚖️ law (Pure Functions)',
            'code': '''// LAW - Pure functions, no side effects

law square(x)
    reply x * x
end

law factorial(n)
    if n <= 1 { reply 1 }
    reply n * factorial(n - 1)
end

law is_even(n)
    reply n % 2 == 0
end

show("square(5):", square(5))
show("factorial(6):", factorial(6))
show("is_even(4):", is_even(4))
show("is_even(7):", is_even(7))'''
        },
        {
            'name': 'Fibonacci',
            'code': '''// Fibonacci - clean and simple

law fib(n)
    if n <= 1 { reply n }
    reply fib(n - 1) + fib(n - 2)
end

show("Fibonacci sequence:")
for i in range(12) {
    show("fib(" + i.str + ") =", fib(i))
}'''
        },
        {
            'name': 'FizzBuzz',
            'code': '''// FizzBuzz

law fizzbuzz(n)
    if n % 15 == 0 { reply "FizzBuzz" }
    if n % 3 == 0 { reply "Fizz" }
    if n % 5 == 0 { reply "Buzz" }
    reply n
end

show("FizzBuzz 1 to 20:")
for i in range(1, 21) {
    show(fizzbuzz(i))
}'''
        },
        {
            'name': 'Primes',
            'code': '''// Prime numbers

law is_prime(n)
    if n < 2 { reply false }
    for i in range(2, n) {
        if n % i == 0 { reply false }
    }
    reply true
end

show("Primes up to 30:")
for n in range(2, 31) {
    if is_prime(n) {
        show(n)
    }
}'''
        },
        {
            'name': 'Collections',
            'code': '''// Working with collections

let numbers = [1, 2, 3, 4, 5]
let fruits = ["apple", "banana", "cherry"]

show("Numbers:", numbers)
show("Length:", numbers.len)
show("First:", numbers.first)
show("Last:", numbers.last)

show("")
show("Fruits:")
for fruit in fruits {
    show("  -", fruit)
}

// Maps
let person = {"name": "Newton", "age": 384}
show("")
show("Person:", person)'''
        },
        {
            'name': 'Calculator',
            'code': '''// Simple calculator

law add(a, b)
    reply a + b
end

law subtract(a, b)
    reply a - b
end

law multiply(a, b)
    reply a * b
end

law divide(a, b)
    if b == 0 { reply "error: division by zero" }
    reply a / b
end

show("Calculator:")
show("10 + 5 =", add(10, 5))
show("10 - 5 =", subtract(10, 5))
show("10 * 5 =", multiply(10, 5))
show("10 / 5 =", divide(10, 5))'''
        },
    ]
    return jsonify(examples)


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                    TinyTalk Web IDE                           ║
║                                                               ║
║  The Verified General-Purpose Programming Language            ║
║  Every loop bounded. Every operation traced.                  ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    print("Starting server at http://localhost:5555")
    print("Press Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=5555, debug=True)
