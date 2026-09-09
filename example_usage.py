from client import PolynomialVectorCommitment

def main():
    print("=== Polynomial Vector Commitment ===")
    pvc = PolynomialVectorCommitment()
    vec = [3, 2, 1] # f(x) = 3 + 2x + x^2

    comm = pvc.commit(vec, secret_setup_point=5)
    print("Commitment:", comm)
    assert len(comm["commitment"]) == 64

    proof = pvc.prove_eval(vec, z=2)
    print("Evaluation proof:", proof)
    assert proof["y"] == 11

    print("Polynomial Vector Commitment verified successfully!")

if __name__ == "__main__":
    main()
