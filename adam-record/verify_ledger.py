#!/usr/bin/env python3
"""Offline check of a Genesis Seed ledger, mirroring verifyLedger() in genesis-seed-v0.1.html.
Written for this repository (not part of the original seed). Usage: python3 verify_ledger.py [file]"""
import base64, hashlib, json, sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature

def js(x):
    if isinstance(x, bool): return "true" if x else "false"
    if x is None: return "null"
    if isinstance(x, float) and x.is_integer(): return str(int(x))
    if isinstance(x, (int, float)): return repr(x)
    return json.dumps(x, ensure_ascii=False)

def canon(x):
    if isinstance(x, list): return "[" + ",".join(map(canon, x)) + "]"
    if isinstance(x, dict): return "{" + ",".join(json.dumps(k, ensure_ascii=False) + ":" + canon(x[k]) for k in sorted(x)) + "}"
    return js(x)

def main(path):
    d = json.load(open(path, encoding="utf-8"))
    L = (d.get("state") or d)["ledger"]
    assert L and L[0]["kind"] == "genesis", "no genesis entry"
    k = L[0]["body"]["owner_public_key"]
    n = lambda s: int.from_bytes(base64.urlsafe_b64decode(s + "=="), "big")
    pub = ec.EllipticCurvePublicNumbers(n(k["x"]), n(k["y"]), ec.SECP256R1()).public_key()
    prev, signed = "0" * 64, 0
    for e in L:
        core = {key: e[key] for key in ("i", "t", "kind", "body", "prev")}
        if e["prev"] != prev: sys.exit(f"FAIL: entry {e['i']} does not follow entry {e['i']-1}")
        if hashlib.sha256(canon(core).encode()).hexdigest() != e["hash"]: sys.exit(f"FAIL: entry {e['i']} altered")
        if e["kind"] in ("genesis", "tier_opened"):
            s = base64.b64decode(e["sig"])
            pub.verify(encode_dss_signature(int.from_bytes(s[:32], "big"), int.from_bytes(s[32:], "big")),
                       e["hash"].encode(), ec.ECDSA(hashes.SHA256()))
            signed += 1
        prev = e["hash"]
    print(f"OK: {len(L)} entries chained, {signed} owner signatures valid. head {prev}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "adam-ledger-public.json")
