"""Handler for selecting and running editor features"""

from typing import Any, Union

from . import (
    helper,
    user_input_handler,
    config_manager,
)
from .edits import basic, cats, gamototo, levels, other, save_management

def fix_elsewhere_old(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Fix the elsewhere error using 2 save files"""

    main_token = save_stats["token"]
    main_iq = save_stats["inquiry_code"]
    input(
        "다른 곳 오류가 없고 금지되지 않은 현재 게임 내 로드된 저장 파일을 선택하세요.\n 계속하려면 엔터 키를 누르세요.:"
    )
    new_path = helper.select_file(
        "클리어 세이브 파일 선택",
        helper.get_save_file_filetype(),
        helper.get_save_path(),
    )
    if not new_path:
        print("세이브 파일을 선택해주세요")
        return save_stats

    data = helper.load_save_file(new_path)
    new_stats = data["save_stats"]
    new_token = new_stats["token"]
    new_iq = new_stats["inquiry_code"]
    save_stats["token"] = new_token
    save_stats["inquiry_code"] = new_iq

    helper.colored_text(f"대체된 문의 코드: &{main_iq}& with &{new_iq}&")
    helper.colored_text(f"교체된 토큰: &{main_token}& with &{new_token}&")
    return save_stats


FEATURES: dict[str, Any] = {
    "저장 관리": {
        "저장 저장": save_management.save.save_save,
        "변경 사항 저장 및 게임 서버에 업로드(전송 및 확인 코드 받기)": save_management.server_upload.save_and_upload,
        "변경 사항을 파일에 저장": save_management.save.save,
        "adb를 사용하여 변경 사항을 저장하고 저장 데이터를 게임에 푸시합니다(게임을 다시 열지 않음).": save_management.save.save_and_push,
        "adb를 사용하여 변경 사항을 저장하고 저장 데이터를 게임에 푸시(게임 다시 열기)": save_management.save.save_and_push_rerun,
        "저장 데이터를 json으로 내보내기": save_management.other.export,
        "adb로 저장 데이터 지우기(게임을 재설치하지 않고 새 계정을 생성하는 데 사용)": save_management.other.clear_data,
        "추적 금지 항목 업로드(저장 또는 종료 시 자동으로 수행됨)": save_management.server_upload.upload_metadata,
        "세이브 데이터 불러오기": save_management.load.select,
        "저장 데이터를 다른 버전으로 변환": save_management.convert.convert_save,
        # "Manage Presets": preset_handler.preset_manager,
    },
    "아이템": {
        "통조림": basic.basic_items.edit_cat_food,
        "경험치": basic.basic_items.edit_xp,
        "티켓": {
            "일반 티켓": basic.basic_items.edit_normal_tickets,
            "희귀 티켓": basic.basic_items.edit_rare_tickets,
            "플래티넘 티켓": basic.basic_items.edit_platinum_tickets,
            "플래티넘 조각": basic.basic_items.edit_platinum_shards,
            "레전드 티켓": basic.basic_items.edit_legend_tickets,
        },
        "NP": basic.basic_items.edit_np,
        "리더쉽": basic.basic_items.edit_leadership,
        "전투 아이템": basic.basic_items.edit_battle_items,
        "캣츠아이": basic.catseyes.edit_catseyes,
        "개다래 / 베히모스 스톤": basic.catfruit.edit_catfruit,
        "본능구슬": basic.talent_orbs_new.edit_talent_orbs,
        "가마토토 드링크": basic.basic_items.edit_catamins,
        "아이템구성 (금지할 수 없는 아이템을 얻을 수 있음)": other.scheme_item.edit_scheme_data,
    },
    "가마토토 / 오토토": {
        "오토토 조수": basic.basic_items.edit_engineers,
        "오토토 기본 재료": basic.ototo_base_mats.edit_base_mats,
        "가마토토 드링크": basic.basic_items.edit_catamins,
        "가마토토 경험치/ 레벨": gamototo.gamatoto_xp.edit_gamatoto_xp,
        "오토토 대포": gamototo.ototo_cat_cannon.edit_cat_cannon,
        "가마토토 조수": gamototo.helpers.edit_helpers,
        "가마토토 때려서 오류 고치기": gamototo.fix_gamatoto.fix_gamatoto,
    },
    "냥코 / 특수 기술 ": {
        "냥코 얻다 / 삭제 ": {
            "냥코 캐릭터를 얻다": cats.get_remove_cats.get_cat,
            "냥코 캐릭터를 삭제": cats.get_remove_cats.remove_cats,
        },
        "업글레이드 냥코캐릭터": cats.upgrade_cats.upgrade_cats,
        "진정한 형태의 캐틱터얻기": {
            "진정한 냥코캐릭터 얻기": cats.evolve_cats.get_evolve,
            "진정한 냥코캐릭터 삭제": cats.evolve_cats.remove_evolve,
            "강제로 진정한 형태의 고양이 (진정한 형태가 없는 캐릭터를 위한 빈 캐릭터로 이어질 것입니다.)": cats.evolve_cats.get_evolve_forced,
        },
        "본능": {
            "선택한 각 고양이의 재능을 개별적으로 설정": cats.talents.edit_talents_individual,
            "최대 / 선택된 모든 고양이 재능 제거": cats.talents.max_all_talents,
        },
        "고양이 가이드 수집/제거": {
            "고양이 가이드 항목 설정(참조하지 않음)": cats.clear_cat_guide.collect_cat_guide,
            "고양이 가이드 항목 설정 취소": cats.clear_cat_guide.remove_cat_guide,
        },
        '스테이지 단위 드랍을 가져오면 이 스테이지를 클리어하여 특별한 고양이 대화 상자를 제거합니다[안씀].': cats.chara_drop.get_character_drops,
        "특수 기술/능력 업그레이드[안씀]": cats.upgrade_blue.upgrade_blue,
    },
    "레벨 / 보물": {
        "메인 스토리 챕터 클리어/노클리어": {
            "선택한 모든 챕터의 모든 챕터에서 각 스테이지 클리어": levels.main_story.clear_all,
            "선택한 각 챕터의 모든 챕터에서 각 스테이지 클리어": levels.main_story.clear_each,
        },
        "보물": {
            "보물 그룹 (예: 에너지 드링크, 아쿠아 크리스탈 등)": levels.treasures.treasure_groups,
            "개별적으로 특정 단계 및 특정 챕터": levels.treasures.specific_stages,
            "특정 스테이지와 챕터를 한 번에": levels.treasures.specific_stages_all_chapters,
        },
        "좀비 스테이지 / 바이러스": levels.outbreaks.edit_outbreaks,
        "이벤트 스테이지": levels.event_stages.event_stages,
        "전설의 이야기": levels.event_stages.stories_of_legend,
        "섬뜩한 레전드리": levels.uncanny.edit_uncanny,
        "아쿠 렐름/게이트 클리어링": levels.aku.edit_aku,
        "악마 영역/게이트 잠금 해제": levels.unlock_aku_realm.unlock_aku_realm,
        "건틀릿": levels.gauntlet.edit_gauntlet,
        "콜라보 건틀릿": levels.gauntlet.edit_collab_gauntlet,
        "타워": levels.towers.edit_tower,
        "베히모스 컬링": levels.behemoth_culling.edit_behemoth_culling,
        "미래편 시간 초과 점수": levels.itf_timed_scores.timed_scores,
        "도전 전투 점수": basic.basic_items.edit_challenge_battle,
        "튜토리얼 클리어": levels.clear_tutorial.clear_tutorial,
        "랭킹 점수(입문자의 전당)": basic.basic_items.edit_dojo_score,
        "수수께끼 단계 추가": levels.enigma_stages.edit_enigma_stages,
        "필리버스터 단계 재청산 허용": levels.allow_filibuster_clearing.allow_filibuster_clearing,
        "레전드 퀘스트": levels.legend_quest.edit_legend_quest,
    },
    "계정 / 문의 코드 / 토큰 ": {
        "문의 코드": basic.basic_items.edit_inquiry_code,
        "토큰": basic.basic_items.edit_token,
        "다른 곳 오류 수정 / 계정 차단 해제": other.fix_elsewhere.fix_elsewhere,
        "이전 수정 다른 곳 오류 / 계정 금지 해제(2개의 저장 파일 필요)": fix_elsewhere_old,
        "새로운 조회 코드 및 토큰 생성": other.create_new_account.create_new_account,
    },
    "다른": {
        "레어 가챠 씨앗": basic.basic_items.edit_rare_gacha_seed,
        "잠금 해제된 장비 슬롯": basic.basic_items.edit_unlocked_slots,
        "재시작 팩 받기/ 귀환자 모드": basic.basic_items.edit_restart_pack,
        "냥코 메달": other.meow_medals.medals,
        "플레이 타임": other.play_time.edit_play_time,
        "적 가이드 항목 잠금 해제/제거": other.unlock_enemy_guide.enemy_guide,
        "개다래 챌린지 / 임무": other.missions.edit_missions,
        "일반 티켓 최대 거래 진행률(금지할 수 없는 희귀 티켓 허용)": other.trade_progress.set_trade_progress,
        "골드 패스 받기/제거": other.get_gold_pass.get_gold_pass,
        "클레임 / 모든 사용자 등급 보상 제거(아무 아이템도 주지 않음)": other.claim_user_rank_rewards.edit_rewards,
        "냥코 신전 레벨 / 경험치": other.cat_shrine.edit_shrine_xp,
    },
    "수정": {
        "시간 오류 수정": other.fix_time_issues.fix_time_issues,
        "장비 메뉴 잠금 해제": other.unlock_equip_menu.unlock_equip,
        "튜토리얼 클리어": levels.clear_tutorial.clear_tutorial,
        "다른 곳 오류 수정 / 계정 차단 해제": other.fix_elsewhere.fix_elsewhere,
        "오래된 다른 곳 수정 오류 / 계정 금지 해제(2개의 저장 파일 필요)": fix_elsewhere_old,
        "게임 충돌에서 가마모토 수정": gamototo.fix_gamatoto.fix_gamatoto,
    },
    "구성 편집": {
        "현지화 편집": config_manager.edit_locale,
        "기본 국가 코드 편집": config_manager.edit_default_gv,
        "기본 저장 경로 편집": config_manager.edit_default_save_file_path,
        "고정 저장 경로 편집": config_manager.edit_fixed_save_path,
       "에디터 설정 편집": config_manager.edit_editor_settings,
        "시작 설정 편집": config_manager.edit_start_up_settings,
        "변경 사항 저장 설정 편집": config_manager.edit_save_changes_settings,
        "서버 설정 편집": config_manager.edit_server_settings,
        "구성 경로 편집": config_manager.edit_config_path,
    },
    "종료": helper.exit_check_changes,
}


def get_feature(
    selected_features: Any, search_string: str, results: dict[str, Any]
) -> dict[str, Any]:
    """Search for a feature if the feature name contains the search string"""

    for feature in selected_features:
        feature_data = selected_features[feature]
        if isinstance(feature_data, dict):
            feature_data = get_feature(feature_data, search_string, results)
        if search_string.lower().replace(" ", "") in feature.lower().replace(" ", ""):
            results[feature] = selected_features[feature]
    return results


def show_options(
    save_stats: dict[str, Any], features_to_use: dict[str, Any]
) -> dict[str, Any]:
    """Allow the user to either enter a feature number or a feature name, and get the features that match"""

    if (
       not config_manager.get_config_value_category("EDITOR", "SHOW_CATEGORIES")
        and FEATURES == features_to_use
    ):
        user_input = ""
    else:
        prompt = (
            "무엇을 편집하시겠습니까(일부 옵션에는 다른 기능이 포함되어 있음)"
        )
        if config_manager.get_config_value_category(
           "EDITOR", "SHOW_FEATURE_SELECT_EXPLANATION"
        ):
            prompt += "\n숫자를 입력하여 기능을 실행하거나 단어를 입력하여 해당 기능을 검색할 수 있습니다(예: catfood를 입력하면 통조림 기능이 실행되고 티켓을 입력하면 티켓을 편집하는 모든 기능이 표시됨)\nEnter를 눌러 목록을 볼 수 있습니다. 모든 기능의"
        user_input = user_input_handler.colored_input(f"{prompt}:\n")
    user_int = helper.check_int(user_input)
    results = []
    if user_int is None:
        results = get_feature(features_to_use, user_input, {})
    else:
        if user_int < 1 or user_int > len(features_to_use) + 1:
            helper.colored_text("범위를 벗어난 값", helper.RED)
            return show_options(save_stats, features_to_use)
        if FEATURES != features_to_use:
            if user_int - 2 < 0:
                return menu(save_stats)
            results = features_to_use[list(features_to_use)[user_int - 2]]
        else:
            results = features_to_use[list(features_to_use)[user_int - 1]]
    if not isinstance(results, dict):
        save_stats_return = results(save_stats)
        if save_stats_return is None:
            return save_stats
        return save_stats_return
    if len(results) == 0:
        helper.colored_text("해당 이름의 기능을 찾을 수 없습니다..", helper.RED)
        return menu(save_stats)
    if len(results) == 1 and isinstance(list(results.values())[0], dict):
        results = results[list(results)[0]]
    if len(results) == 1:
        save_stats_return = results[list(results)[0]](save_stats)
        if save_stats_return is None:
            return save_stats
        return save_stats_return

    helper.colored_list(["뒤로가기"] + list(results))
    return show_options(save_stats, results)


def menu(
    save_stats: dict[str, Any], path_save: Union[str, None] = None
) -> dict[str, Any]:
    """메뉴를 표시하고 사용자가 편집할 기능을 선택할 수 있도록 합니다."""

    if path_save:
        helper.set_save_path(path_save)
    if config_manager.get_config_value_category("EDITOR", "SHOW_CATEGORIES"):
        helper.colored_list(list(FEATURES))
    save_stats = show_options(save_stats, FEATURES)

    return save_stats
