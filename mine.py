import hashlib
import time
import sys

def run_apple_compute():
    print("Initializing Apple System Compute Nodes...")
    difficulty = 5 # Higher number = more CPU work
    target = "0" * difficulty
    nonce = 0
    start_time = time.time()

    try:
        while True:
            text = f"apple_block_{nonce}".encode()
            h = hashlib.sha256(text).hexdigest()
            
            if h.startswith(target):
                print(f"\n[SUCCESS] Proof found: {h}")
                print(f"Time: {time.time() - start_time:.2f}s")
                break
            
            nonce += 1
            if nonce % 10000 == 0:
                sys.stdout.write(f"\rCalculated {nonce} hashes...")
                sys.stdout.flush()
    except KeyboardInterrupt:
        print("\nProcess Terminated.")

if __name__ == "__main__":
    run_apple_compute()
