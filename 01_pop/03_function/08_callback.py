def callback(message):
    print(f"Callback function called with message: {message}")

def main(cb):
    print("Main function is doing some work...")
    cb("Processing completed!")

main(callback)