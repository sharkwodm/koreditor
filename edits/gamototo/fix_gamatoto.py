"""Fix gamatoto from crashing the game"""
from typing import Any


def fix_gamatoto(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Fix gamatoto from crashing the game"""

    save_stats["gamatoto_skin"]["Value"] = 2
    print("게임 충돌로부터 가마토토를 성공적으로 수정했습니다.")
    return save_stats
