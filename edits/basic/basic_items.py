"""Handler for basic, items that work in a common way"""
from typing import Any
from ... import item, managed_item


def edit_cat_food(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing cat food"""

    cat_food = item.IntItem(
        name="통조림",
        value=item.Int(save_stats["cat_food"]["Value"]),
        max_value=45000,
        bannable=item.Bannable(
            managed_item.ManagedItemType.CATFOOD,
        ),
    )
    cat_food.edit()
    save_stats["cat_food"]["Value"] = cat_food.get_value()
    return save_stats


def edit_xp(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing xp"""

    experience = item.IntItem(
        name="경험치",
        value=item.Int(save_stats["xp"]["Value"]),
        max_value=99999999,
    )
    experience.edit()
    save_stats["xp"]["Value"] = experience.get_value()
    return save_stats


def edit_normal_tickets(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing normal tickets"""

    normal_tickets = item.IntItem(
        name="노말 티켓",
        value=item.Int(save_stats["normal_tickets"]["Value"]),
        max_value=2999,
    )
    normal_tickets.edit()
    save_stats["normal_tickets"]["Value"] = normal_tickets.get_value()
    return save_stats


def edit_rare_tickets(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing rare tickets"""

    rare_tickets = item.IntItem(
        name="레어 티켓",
        value=item.Int(save_stats["rare_tickets"]["Value"]),
        max_value=299,
        bannable=item.Bannable(
            work_around='&희귀 티켓을 직접 편집하는 대신 "일반 티켓 최대 거래 진행" 전환 기능을 대신 사용하십시오! 훨씬 더 안전합니다.',
            type=managed_item.ManagedItemType.RARE_TICKET,
        ),
    )
    rare_tickets.edit()
    save_stats["rare_tickets"]["Value"] = rare_tickets.get_value()
    return save_stats


def edit_platinum_tickets(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing platinum tickets"""

    platinum_tickets = item.IntItem(
        name="플래티넘 티켓",
        value=item.Int(save_stats["platinum_tickets"]["Value"]),
        max_value=9,
        bannable=item.Bannable(
            work_around="&플래티넘 티켓을 편집하는 대신 플래티넘 샤드를 편집하세요! 그들은 훨씬 더 안전합니다. 10 플래티넘 조각 = 1 플래티넘 티켓",
            type=managed_item.ManagedItemType.PLATINUM_TICKET,
        ),
    )
    platinum_tickets.edit()
    save_stats["platinum_tickets"]["Value"] = platinum_tickets.get_value()
    return save_stats


def edit_platinum_shards(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing platinum shards"""

    ticket_amount = save_stats["platinum_tickets"]["Value"]
    max_value = 99 - (ticket_amount * 10)
    platinum_shards = item.IntItem(
        name="플래티넘 조각",
        value=item.Int(save_stats["platinum_shards"]["Value"]),
        max_value=max_value,
    )
    platinum_shards.edit()
    save_stats["platinum_shards"]["Value"] = platinum_shards.get_value()
    return save_stats


def edit_np(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing np"""

    nyanko_points = item.IntItem(
        name="NP",
        value=item.Int(save_stats["np"]["Value"]),
        max_value=9999,
    )
    nyanko_points.edit()
    save_stats["np"]["Value"] = nyanko_points.get_value()
    return save_stats


def edit_leadership(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing leadership"""

    leadership = item.IntItem(
        name="리더쉽",
        value=item.Int(save_stats["leadership"]["Value"]),
        max_value=9999,
    )
    leadership.edit()
    save_stats["leadership"]["Value"] = leadership.get_value()
    return save_stats


def edit_battle_items(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing battle items"""

    battle_items = item.IntItemGroup.from_lists(
        names=[
            "스피드 업",
            "보물 레이더",
            "부자 냥코고양이",
            "고양이 cpu",
            "고양이 직업",
            "고양이 스나이퍼",
        ],
        values=save_stats["battle_items"],
        maxes=9999,
        group_name="배틀 아이템",
    )
    battle_items.edit()
    save_stats["battle_items"] = battle_items.get_values()

    return save_stats


def edit_engineers(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing ototo engineers"""

    engineers = item.IntItem(
        name="오토토",
        value=item.Int(save_stats["engineers"]["Value"]),
        max_value=5,
    )
    engineers.edit()
    save_stats["engineers"]["Value"] = engineers.get_value()
    return save_stats


def edit_catamins(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing catamins"""

    catamins = item.IntItemGroup.from_lists(
        names=[
            "고양이 드링크 A",
            "고양이 드링크 B",
            "고양이 드링크 C",
        ],
        values=save_stats["catamins"],
        maxes=9999,
        group_name="Catamins",
    )
    catamins.edit()
    save_stats["catamins"] = catamins.get_values()
    return save_stats


def edit_inquiry_code(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing the inquiry code"""

    print(
        "경고: 문의 코드 편집은 자신이 무엇을 하고 있는지 알고 있는 경우에만 수행해야 합니다! 올바르게 수행하지 않으면 게임 내에서 다른 오류가 발생하기 때문입니다!"
    )
    inquiry_code = item.StrItem(
        name="문의 코드",
        value=save_stats["inquiry_code"],
    )
    inquiry_code.edit()
    save_stats["inquiry_code"] = inquiry_code.get_value()
    return save_stats


def edit_rare_gacha_seed(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing the rare gacha seed"""

    rare_gacha_seed = item.IntItem(
        name="레어 가챠 씨앗",
        value=item.Int(save_stats["rare_gacha_seed"]["Value"], signed=False),
        max_value=None,
    )
    rare_gacha_seed.edit()
    save_stats["rare_gacha_seed"]["Value"] = rare_gacha_seed.get_value()
    return save_stats


def edit_unlocked_slots(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing the amount of unlocked slots"""

    unlocked_slots = item.IntItem(
        name="잠금 해제된 슬롯",
        value=item.Int(save_stats["unlocked_slots"]["Value"]),
        max_value=len(save_stats["slots"]),
    )
    unlocked_slots.edit()
    save_stats["unlocked_slots"]["Value"] = unlocked_slots.get_value()
    return save_stats


def edit_token(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing the password-refresh-token"""

    print(
        "경고: 토큰 편집은 수행 중인 작업을 알고 있는 경우에만 수행해야 합니다! 올바르게 수행하지 않으면 게임 내에서 다른 오류가 발생하기 때문입니다!"
    )
    token = item.StrItem(
        name="Token",
        value=save_stats["token"],
    )
    token.edit()
    save_stats["token"] = token.get_value()
    return save_stats


def edit_restart_pack(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for giving the restart pack"""

    save_stats["restart_pack"]["Value"] = 1
    print("재시작 팩을 성공적으로 제공했습니다.")
    return save_stats


def edit_challenge_battle(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing the score of the challenge battle"""

    challenge_battle = item.IntItem(
        name="도전 전투",
        value=item.Int(save_stats["challenge"]["Score"]["Value"]),
        max_value=None,
    )
    challenge_battle.edit()
    save_stats["challenge"]["Score"]["Value"] = challenge_battle.get_value()
    save_stats["challenge"]["Cleared"]["Value"] = 1
    return save_stats


def edit_legend_tickets(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing legend tickets"""

    legend_tickets = item.IntItem(
        name="레전드 티켓",
        value=item.Int(save_stats["legend_tickets"]["Value"]),
        max_value=4,
        bannable=item.Bannable(
            type=managed_item.ManagedItemType.LEGEND_TICKET,
        ),
    )
    legend_tickets.edit()
    save_stats["legend_tickets"]["Value"] = legend_tickets.get_value()
    return save_stats


def edit_dojo_score(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editing the dojo score"""

    if not save_stats["dojo_data"]:
        save_stats["dojo_data"] = {0: {0: 0}}

    dojo_score = item.IntItem(
        name="랭킹 점수",
        value=item.Int(save_stats["dojo_data"][0][0]),
        max_value=None,
    )
    dojo_score.edit()
    save_stats["dojo_data"][0][0] = dojo_score.get_value()
    return save_stats
