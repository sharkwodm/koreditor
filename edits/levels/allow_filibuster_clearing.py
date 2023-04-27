"""Handler for allowing the filibuster stage to reappear in the game."""
import random
from typing import Any
from ... import helper


def allow_filibuster_clearing(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Allow filibuster clearing in the game."""

    save_stats["filibuster_stage_enabled"]["Value"] = 1
    save_stats["filibuster_stage_id"]["Value"] = random.randint(0, 47)

    helper.colored_text("필리버스터 단계가 성공적으로 다시 활성화되었습니다..")

    return save_stats
