"""Handler for unlocking the enemy guide"""
from typing import Any

from ... import user_input_handler


def enemy_guide(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for unlocking the enemy guide"""

    enemy_guide_stats = save_stats["enemy_guide"]
    total = len(enemy_guide_stats)
    unlock = (
        user_input_handler.colored_input(
            "적 가이드 항목 &(1)&을(를) 제거하거나 &(2)&를 잠금 해제하시겠습니까?:"
        )
        == "2"
    )
    set_val = 1
    if not unlock:
        set_val = 0
    ids = user_input_handler.get_range(
        user_input_handler.colored_input(
            "적 ID를 입력하십시오(ID를 찾으려면 적군 해제 명령 전투 고양이를 조회하십시오)(모든 범위를 얻으려면 &all&을 입력할 수 있습니다. 예: &1&-&50& 또는 공백으로 구분된 ID(예: &5 4 7&):"
        ),
        total,
    )

    for enemy_id in ids:
        if enemy_id >= 2:
            enemy_id -= 2
        if enemy_id >= len(enemy_guide_stats):
            print(f"Invalid enemy id: {enemy_id+2}")
            continue
        enemy_guide_stats[enemy_id] = set_val
    save_stats["enemy_guide"] = enemy_guide_stats
    if not unlock:
        print("적 가이드 항목을 성공적으로 제거했습니다.")
    else:
        print("적 가이드 항목을 성공적으로 잠금 해제했습니다.")
    return save_stats
