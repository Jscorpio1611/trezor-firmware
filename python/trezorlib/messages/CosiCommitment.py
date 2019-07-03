# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class CosiCommitment(p.MessageType):
    MESSAGE_WIRE_TYPE = 72

    def __init__(
        self,
        commitment: bytes = None,
        pubkey: bytes = None,
    ) -> None:
        self.commitment = commitment
        self.pubkey = pubkey

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('commitment', p.BytesType, 0),
            2: ('pubkey', p.BytesType, 0),
        }
