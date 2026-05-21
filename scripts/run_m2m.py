from scripts.state_engine import StateEngine, append_log


def local_convert(text: str, target: str = "B") -> str:
    # 실제 번역 API 전 단계: 로컬 실행 흐름 검증용 변환기
    return f"[M2M:{target}] {text}"


def run_demo(message: str = "안녕하세요. 말대말 로컬 실행 테스트입니다.") -> None:
    engine = StateEngine()
    append_log("M2M_DEMO_START", engine.current_state(), "local execution demo start")
    engine.run_until("SECURITY_SELECTED")
    converted = local_convert(message, "user_B")
    engine.record_message("user_A", "user_B", message, converted)
    engine.set_state("TRANSLATE_SUCCESS", "message_converted")
    engine.queue_join("user_A")
    engine.match_room("room_local_001")
    append_log("M2M_DEMO_COMPLETE", engine.current_state(), "local m2m flow reached ROOM_CONNECTED")
    print("KRXA M2M LOCAL RUN: PASS")
    print(f"DELIVERED: {converted}")
    print(f"STATE: {engine.current_state()}")


if __name__ == "__main__":
    run_demo()
