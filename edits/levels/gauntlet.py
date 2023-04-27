"""Handler for clearing gauntlets"""
from typing import Any

from . import event_stages
from ... import user_input_handler, helper
from ..other import meow_medals


def edit_gauntlet(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for clearing gauntlets"""

    stage_data = save_stats["gauntlets"]
    lengths = stage_data["Lengths"]

    ids = []
    ids = user_input_handler.get_range(
        user_input_handler.colored_input(
            "건틀릿 ID 입력 (찾아보기 및 이벤트 릴리스 전투 고양이를 주문하고 이벤트를 스크롤하여 건틀릿 ​​ID를 찾으십시오.) (&all&을 입력하여 모두 가져오거나 범위(예: 1-49) 또는 공백으로 구분된 ID(예: &5 4 7&)를 가져올 수 있습니다.):"
        ),
        lengths["total"],
    )
    save_stats["gauntlets"] = event_stages.stage_handler(stage_data, ids, 0)
    base_addr = meow_medals.BaseMapIds.GAUNTLETS.value
    save_stats["gauntlets"], save_stats["medals"] = event_stages.set_medals(
        save_stats["gauntlets"],
        save_stats["medals"],
        (base_addr, base_addr + len(save_stats["gauntlets"]["Value"]["unlock_next"])),
        -base_addr,
        helper.check_data_is_jp(save_stats),
    )
    return save_stats


def edit_collab_gauntlet(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for clearing collab gauntlets"""

    stage_data = save_stats["collab_gauntlets"]
    lengths = stage_data["Lengths"]

    ids = []
    ids = user_input_handler.get_range(
        user_input_handler.colored_input(
            "콜라보 건틀릿 ID 입력 (&이벤트& 및 &건틀릿& 과거를 지나 &콜라보 건틀렛& ID를 찾으려면 &이벤트 출시 순서 전투 고양이&를 찾아 스크롤하십시오.) (&all&을 입력하여 모두 가져오거나 범위(예: 1-49) 또는 공백으로 구분된 ID(예: &5 4 7&)를 가져올 수 있습니다.):"
        ),
        lengths["total"],
    )
    save_stats["collab_gauntlets"] = event_stages.stage_handler(stage_data, ids, 0)
    return save_stats
