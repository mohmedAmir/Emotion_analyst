

def print_results(results):
    print("\nResults:\n" + "-"*40)
    for r in results:
        print(f"text: {r.text[:50]}...")
        print(f"polarity: {r.polarity:.2f}")
        print(f"label: {r.label}")
        print("-"*40)
