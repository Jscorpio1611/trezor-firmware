# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroKeyImageSyncFinalAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 535

    def __init__(
        self,
        enc_key: bytes = None,
    ) -> None:
        self.enc_key = enc_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('enc_key', p.BytesType, 0),
        }
