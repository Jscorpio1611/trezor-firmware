# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class StellarCreateAccountOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 210

    def __init__(
        self,
        source_account: str = None,
        new_account: str = None,
        starting_balance: int = None,
    ) -> None:
        self.source_account = source_account
        self.new_account = new_account
        self.starting_balance = starting_balance

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('source_account', p.UnicodeType, 0),
            2: ('new_account', p.UnicodeType, 0),
            3: ('starting_balance', p.SVarintType, 0),
        }
