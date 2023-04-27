from typing import Any

from ... import helper, user_input_handler


def convert_to_jp(save_stats: dict[str, Any]) -> dict[str, Any]:
    save_stats["version"] = "jp"
    save_stats["dst"] = False

    helper.colored_text("jp로 변환된 데이터 저장", helper.GREEN)
    return save_stats


def convert_to_non_jp(save_stats: dict[str, Any], cc: str) -> dict[str, Any]:
    save_stats["version"] = cc
    save_stats["dst"] = True

    helper.colored_text(f"변환된 데이터 저장 {cc}", helper.GREEN)
    return save_stats


def convert(save_stats: dict[str, Any], version: str) -> dict[str, Any]:
    if version == "jp":
        return convert_to_jp(save_stats)
    else:
        return convert_to_non_jp(save_stats, version)


def convert_save(save_stats: dict[str, Any]) -> dict[str, Any]:
    gvs = ["en", "jp", "kr", "tw"]

    helper.colored_text(
        "경고: 이로 인해 문제가 발생할 수 있으며 두 앱의 버전이 동일해야 합니다(예: 둘 다 12.1.0)!",
        helper.RED,
    )

    if save_stats["version"] in gvs:
        gvs.remove(save_stats["version"])

    gv_index = (
        user_input_handler.select_single(
            gvs, title="저장을 변환할 버전 선택:"
        )
        - 1
    )
    gv = gvs[gv_index]

    return convert(save_stats, gv)
