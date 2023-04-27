"""Handler for clearing behemoth culling stages"""
from typing import Any

from . import event_stages
from ... import user_input_handler


def edit_behemoth_culling(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for clearing behemoth culling stages"""

    stage_data = save_stats["behemoth_culling"]
    lengths = stage_data["Lengths"]

    ids = []
    ids = user_input_handler.get_range(
        user_input_handler.colored_input(
            "베헤모스 컬링 ID를 입력하세요. (예) &0& = &가프라의 숨겨진 숲&, &1& = &아쉬비니 사막&) (&all&을 입력하여 모두 가져오거나 범위(예: 1-49) 또는 공백으로 구분된 ID(예: &5 4 7&)를 가져올 수 있습니다.):"
        ),
        lengths["total"],
    )
    save_stats["behemoth_culling"] = event_stages.stage_handler(stage_data, ids, 0)
    return save_stats
