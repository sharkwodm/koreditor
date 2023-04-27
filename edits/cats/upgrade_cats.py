"""Handler for cat upgrades"""
from typing import Any, Union

from ... import helper, user_input_handler
from . import cat_id_selector, cat_helper


def set_level_caps(save_stats: dict[str, Any]) -> dict[str, Any]:
    """
    Set the level caps for the cats

    Args:
        save_stats (dict[str, Any]): The save stats

    Returns:
        dict[str, Any]: The save stats
    """

    unit_max_data = cat_helper.get_unit_max_levels(helper.is_jp(save_stats))
    rarities = cat_helper.get_rarities(helper.is_jp(save_stats))
    for cat_id in range(len(save_stats["cats"])):
        base_level = save_stats["cat_upgrades"]["Base"][cat_id]
        if unit_max_data is not None:
            max_base_level = cat_helper.get_unit_max_level(unit_max_data, cat_id)[0]
        else:
            max_base_level = 50000
        try:
            rarity = rarities[cat_id]
        except IndexError:
            rarity = 0
        max_base_level_ur = cat_helper.get_max_level(save_stats, rarity, cat_id)
        level_cap = cat_helper.get_level_cap_increase_amount(
            min(base_level, max_base_level, max_base_level_ur)
        )
        save_stats["catseye_cat_data"][cat_id] = level_cap
        save_stats["catseye_related_data"]["Base"][cat_id] = level_cap + 10
    return save_stats


def set_user_popups(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Set user popups, stops the user rank popups from spamming up the screen"""

    save_stats["user_rank_popups"]["Value"] = 0xFFFFFF
    return save_stats


def get_plus_base(usr_input: str) -> tuple[Union[int, None], Union[int, None]]:
    """Get the base and plus level of an input"""

    split = usr_input.split("+")
    base = None
    plus = None
    if split[0]:
        base = helper.check_int_max(split[0])
    if len(split) == 2 and split[1]:
        plus = helper.check_int_max(split[1])
    if len(split) == 1:
        plus = 0
    return base, plus


def upgrade_cats(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Upgrade specific cats"""

    ids = cat_id_selector.select_cats(save_stats)

    return upgrade_cats_ids(save_stats, ids)


def upgrade_handler(
    data: dict[str, Any], ids: list[int], item_name: str, save_stats: dict[str, Any]
) -> dict[str, Any]:
    """Handler for cat upgrades"""

    ids = helper.check_cat_ids(ids, save_stats)

    base = data["Base"]
    plus = data["Plus"]
    individual = True
    if len(ids) > 1:
        individual = user_input_handler.ask_if_individual(
            f"냥코의 업그레이드{item_name}"
        )
    first = True
    base_lvl = None
    plus_lvl = None
    for cat_id in ids:
        if not individual and first:
            levels = get_plus_base(
                user_input_handler.colored_input(
                    '냥코 캐릭터 기본 수준 다음에 "&+&" 다음에 플러스 수준을 입력합니다(예: 5&+&12). 기본 레벨을 무시하려면 &+&12 를 입력 하시구 플러스 레벨을 무시하려면 &+5&를 입력하십시오.:\n'
                )
            )
            base_lvl = levels[0]
            plus_lvl = levels[1]
            first = False
        elif individual:
            helper.colored_text(
                f"냥코캐릭터 id의 현재 업그레이드 레벨&{cat_id}& is &{base[cat_id]+1}&+&{plus[cat_id]}&"
            )
            levels = get_plus_base(
                user_input_handler.colored_input(
                    f'냥코캐릭터 대한 기준 레벨을 입력합니다.{item_name}: &{cat_id}&"&+&"그런 다음 플러스 수준뒤에 , 예: 5&+&12. 기본 레벨을 무시하려면 &+&12를 수행하고 플러스 레벨을 무시하려면 &+&5를 수행하십시오.\n'
                )
            )
            base_lvl = levels[0]
            plus_lvl = levels[1]
        if base_lvl is not None:
            if base_lvl > 0:
                base_lvl = helper.clamp(base_lvl, 0, 50000)
                base[cat_id] = base_lvl - 1
        if plus_lvl is not None:
            plus_lvl = helper.clamp(plus_lvl, 0, 50000)
            plus[cat_id] = plus_lvl
    data["Base"] = base
    data["Plus"] = plus

    return data


def upgrade_cats_ids(save_stats: dict[str, Any], ids: list[int]) -> dict[str, Any]:
    """Upgrade cats by ids"""

    save_stats["cat_upgrades"] = upgrade_handler(
        data=save_stats["cat_upgrades"],
        ids=ids,
        item_name="cat",
        save_stats=save_stats,
    )
    save_stats = set_user_popups(save_stats)
    # save_stats = set_level_caps(save_stats)
    print("고양이 레벨을 성공적으로 설정했습니다.")
    return save_stats
