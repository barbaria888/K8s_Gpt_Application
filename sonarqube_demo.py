#!/usr/bin/env python3
"""
Demo file to show SonarQube MCP detection of local changes
This file intentionally contains some issues for analysis
"""

def unused_variable_demo():
    """This function has an unused variable"""
    x = 10  # This variable is never used
    y = 20
    return y


def duplicate_code_demo():
    """This function has duplicated logic"""
    result = []
    for i in range(10):
        result.append(i * 2)
    return result


def sql_injection_risk():
    """Security hotspot: potential SQL injection"""
    user_input = input("Enter username: ")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # Unsafe!
    return query


def complex_function(a, b, c, d, e):
    """This function has high cyclomatic complexity"""
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        return a + b + c + d + e
                    else:
                        return a + b + c + d
                else:
                    return a + b + c
            else:
                return a + b
        else:
            return a
    else:
        return 0


class EmptyClassDemo:
    """Empty class with no implementation"""
    pass


def hardcoded_credentials():
    """Code smell: hardcoded credentials"""
    api_key = "sk-1234567890abcdefghij"  # Hardcoded!
    return api_key
