from typing import Annotated
from shared import slap
from fastapi import Header, HTTPException, Query


async def get_verify_signature(date: Annotated[str, Query()], signature: Annotated[str, Header()], 
                           publicKey: Annotated[str, Header()]):   
    try:
        if not slap.verifySignature(signature, date, publicKey):
                raise HTTPException(status_code=403, detail="Signature could not be verified.")
                
        return {
                "publicKey": publicKey,
                "signature": signature,
                "date": date
                }
    except ValueError:
        raise HTTPException(status_code=401, detail="Public key and/or signature are not in correct format.")


async def post_verify_signature(signature: Annotated[str, Header()], 
                           publicKey: Annotated[str, Header()]):
    return {
        "publicKey": publicKey,
        "signature": signature
    }
    