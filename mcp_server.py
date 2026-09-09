import sys
import json
from client import PolynomialVectorCommitment

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    pvc = PolynomialVectorCommitment()
    if method == "commit":
        return pvc.commit(params.get("vector", []))
    elif method == "prove":
        return pvc.prove_eval(params.get("vector", []), params.get("z", 0))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
