from importlib import metadata

from langchain_qwen.chat_models import ChatQWen

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    "ChatQWen",
    "__version__",
]
