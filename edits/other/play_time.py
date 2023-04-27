"""Handler for editting play time"""
from typing import Any

from ... import helper, user_input_handler


def edit_play_time(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editting play time"""
    play_time = save_stats["play_time"]

    hours = play_time["hh"]
    minutes = play_time["mm"]

    helper.colored_text(
        f"현재 플레이 시간은 다음과 같습니다.: &{hours}& 시간과 &{minutes}& 분"
    )
    hours = helper.check_int_max(
        user_input_handler.colored_input("몇 시로 설정하시겠습니까?:")
    )
    minutes = helper.check_int_max(
        user_input_handler.colored_input("몇 분으로 설정하시겠습니까?:")
    )
    if hours is None or minutes is None or hours < 0 or minutes < 0:
        print("유효한 숫자를 입력하세요.")
        return save_stats
    play_time["hh"] = hours
    play_time["mm"] = minutes

    save_stats["play_time"] = play_time

    print("플레이 시간을 설정했습니다.")
    return save_stats
