from datetime import datetime
name = input("Your name: ").strip()
print(f"Hello, {name or 'student'}!")
print("Run time:", datetime.now().isoformat(timespec="seconds"))
