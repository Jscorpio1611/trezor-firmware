# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class StellarManageDataOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 220

    def __init__(
        self,
        source_account: str = None,
        key: str = None,
        value: bytes = None,
    ) -> None:
        self.source_account = source_account
        self.key = key
        self.value = value

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('source_account', p.UnicodeType, 0),
            2: ('key', p.UnicodeType, 0),
            3: ('value', p.BytesType, 0),
        }
