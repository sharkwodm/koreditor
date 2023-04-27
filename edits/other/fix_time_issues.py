"""Handler for fixing time issues"""
from typing import Any
from ... import helper


def fix_time_issues(save_stats: dict[str, Any]) -> dict[str, Any]:
    """
    Fix time issues

    Args:
        save_stats (dict[str, Any]): Save stats

    Returns:
        dict[str, Any]: Save stats
    """
    save_stats["third_time"] = helper.get_iso_time()

    save_stats["time_stamp"] = helper.get_time()
    save_stats["time_stamp_4"] = helper.get_time()

    helper.colored_text(
        "시간 문제를 성공적으로 수정했습니다 &(이 작업을 수행하려면 두 장치의 장치 시간이 정확해야 합니다!)&",
        helper.GREEN,
        helper.RED,
    )
    return save_stats
