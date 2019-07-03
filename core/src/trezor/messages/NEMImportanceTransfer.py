# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class NEMImportanceTransfer(p.MessageType):

    def __init__(
        self,
        mode: int = None,
        public_key: bytes = None,
    ) -> None:
        self.mode = mode
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mode', p.UVarintType, 0),
            2: ('public_key', p.BytesType, 0),
        }
