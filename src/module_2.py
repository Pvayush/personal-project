"""
Module for data processing - Version 2
"""

def process_data(data):
    """Process input data and return formatted result"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    return {
        'processed': True,
        'count': len(data),
        'items': data
    }

if __name__ == "__main__":
    print("Processing module loaded")
