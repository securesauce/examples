# This example demostrates an insecure way of comparing a digest
# that exposes the code to a timing attack. This is because using
# equals operator on digest does not compare in constant time.
import hmac


received_digest = (
    b"\xe2\x93\x08\x19T8\xdc\x80\xef\x87\x90m\x1f\x9d\xf7\xf2"
    b"\xf5\x10>\xdbf\xa2\xaf\xf7x\xcdX\xdf"
)

key = b"my-super-duper-secret-key"
password = b"pass"
digest = hmac.digest(key, password, digest="sha224")

if digest == received_digest:
    print("Authentication okay")
