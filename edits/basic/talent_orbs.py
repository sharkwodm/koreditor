"""Handler for editing talent orbs"""

from typing import Any

from ... import helper, user_input_handler


def edit_all_orbs(save_stats: dict[str, Any], orb_list: list[str]) -> dict[str, Any]:
    """Handler for editing all talent orbs"""

    val = user_input_handler.colored_input(
        "모든 재능 구슬의 값을 무엇으로 설정하시겠습니까?:"
    )
    val = helper.check_int_max(val)
    if val is None:
        print("오류 숫자를 입력하십시오")
        return save_stats

    for orb in orb_list:
        try:
            orb_id = orb_list.index(orb)
        except ValueError:
            continue
        save_stats["talent_orbs"][orb_id] = val

    helper.colored_text(f"모든 재능 오브를 다음으로 설정 &{val}&")
    return save_stats


def edit_talent_orbs(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing talent orbs"""

    orb_list = get_talent_orbs_types()

    talent_orbs = save_stats["talent_orbs"]
    print("You have:")
    for orb in talent_orbs:
        amount = talent_orbs[orb]
        text = "orbs" if amount != 1 else "orb"
        try:
            helper.colored_text(f"&{amount}& {orb_list[orb]} {text}")
        except IndexError:
            helper.colored_text(f"&{amount}& Unknown {orb} {text}")

    orbs_str = user_input_handler.colored_input(
        "원하는 구의 이름을 입력합니다. &공백&로 구분된 여러 오브 이름을 입력하여 한 번에 여러 개를 편집하거나 &all&을 입력하여 편집할 모든 재능 오브를 선택할 수 있습니다.):"
    ).split(" ")
    if orbs_str[0] == "all":
        return edit_all_orbs(save_stats, orb_list)
    length = len(orbs_str) // 3
    orbs_to_set: list[int] = []

    for i in range(length):
        orb_name = " ".join(orbs_str[i * 3 : i * 3 + 3]).lower()
        orb_name = orb_name.replace("angle", "angel").title()
        try:
            orbs_to_set.append(orb_list.index(orb_name))
        except ValueError:
            helper.colored_text(
                f"Error orb &{orb_name}& does not exist or is not recognized"
            )

    for orb_id in orbs_to_set:
        name = orb_list[orb_id]
        val = helper.check_int_max(
            user_input_handler.colored_input(
                f"What do you want to set the value of &{name}& to?:"
            )
        )
        if val is None:
            print("Error please enter a number")
            continue
        talent_orbs[orb_id] = val
    save_stats["talent_orbs"] = talent_orbs

    return save_stats


ATTRIBUTES = [
    "빨간색",
    "떠있는 적",
    "검정",
    "메탈",
    "천사",
    "에이리언",
    "좀비",
]
EFFECTS = [
    "공격",
    "방어",
    "강한",
    "엄청난",
    "내성",
]
GRADES = [
    "D",
    "C",
    "B",
    "A",
    "S",
]


def create_orb_list(
    attributes: list[str], effects: list[str], grades: list[str], incl_metal: bool
) -> list[str]:
    """Create a list of all possible talent orbs"""

    orb_list: list[str] = []
    for attribute in attributes:
        effects_trim = effects

        if attribute == "Metal" and incl_metal:
            effects_trim = [effects[1]]
        if attribute == "Metal" and not incl_metal:
            effects_trim = []

        for effect in effects_trim:
            for grade in grades:
                orb_list.append(f"{attribute} {grade} {effect}")

    return orb_list


def create_aku_orbs(effects: list[str], grades: list[str]) -> list[str]:
    """Create a list of all possible aku orbs"""

    orb_list: list[str] = []
    for effect in effects:
        for grade in grades:
            orb_list.append(f"Aku {grade} {effect}")

    return orb_list


def get_talent_orbs_types() -> list[str]:
    """Get a list of all possible talent orbs"""

    orb_list = create_orb_list(ATTRIBUTES, EFFECTS[0:2], GRADES, True)
    orb_list += create_orb_list(ATTRIBUTES, EFFECTS[2:], GRADES, False)
    orb_list += create_aku_orbs(EFFECTS, GRADES)
    print(orb_list)
    return orb_list
