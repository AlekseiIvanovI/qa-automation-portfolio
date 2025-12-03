# qa_utils/generator.py
from typing import List


class TestIdGenerator:
    """Generate sequential, zero-padded test IDs (e.g., LOGIN_0001)."""

    def generate(self, prefix: str, count: int) -> List[str]:
        if count <= 0:
            return []
        return [f"{prefix}_{i:04d}" for i in range(1, count + 1)]
