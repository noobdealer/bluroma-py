from logging import debug

from atproto import DidDocument
from atproto_identity.resolver import HandleResolver, DidResolver
from dotenv import load_dotenv
import os

load_dotenv()

# These are here in case these ever need to be resolved specifically. For finding a user's PDS, use the
# resolve_handle_pds function.
def resolve_did(username: str) -> str:
    return HandleResolver().resolve(username)

def resolve_did_doc(did: str) -> DidDocument:
    return DidResolver(os.getenv("PLC_DIRECTORY")).resolve(did)

def resolve_pds(did_doc: DidDocument) -> str:
    return DidDocument.get_pds_endpoint(did_doc)

def resolve_pds_from_handle(username: str) -> str:
    did = resolve_did(username)
    did_doc = resolve_did_doc(did)
    debug("Resolving PDS from DID: ", did)
    return resolve_pds(did_doc)

