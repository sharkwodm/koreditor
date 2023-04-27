"""Handler for editing tower stages"""
from typing import Any

from . import event_stages
from ... import user_input_handler

def edit_tower(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing tower stages"""

    stage_data = save_stats["tower"]["progress"]
    stage_data = {
        "Value": stage_data,
        "Lengths": {"stars": stage_data["stars"], "stages": stage_data["stages"]},
    }

    ids = []
    ids = user_input_handler.get_range(
        user_input_handler.colored_input(
            "타워 ID 입력 (&이벤트 출시 순서 전투 고양이&를 찾아 스크롤하여 &이벤트& and &건틀릿& &탑& ID 찾기) (&all&을 입력하여 &1&-&49&와 같은 범위 또는 &5 4 7&와 같이 공백으로 구분된 ID를 모두 가져올 수 있습니다.):"
        ),
        stage_data["Value"]["total"],
    )
    save_stats["tower"]["progress"] = event_stages.stage_handler(
        stage_data, ids, 0, False
    )["Value"]
    save_stats["tower"]["progress"]["total"] = stage_data["Value"]["total"]
    save_stats["tower"]["progress"]["stars"] = stage_data["Lengths"]["stars"]
    save_stats["tower"]["progress"]["stages"] = stage_data["Lengths"]["stages"]

    return save_stats
