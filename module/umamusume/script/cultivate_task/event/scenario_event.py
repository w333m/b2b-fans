from module.umamusume.context import UmamusumeContext
from module.umamusume.define import TurnOperationType
from bot.recog.image_matcher import image_match
from bot.conn.fetch import read_energy
import time

import bot.base.log as logger
log = logger.get_logger(__name__)

# First year New Year event
def scenario_event_1(ctx: UmamusumeContext) -> int:
    energy = read_energy()
    if ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_REST or \
            (ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_MEDIC and energy >= 50) or \
            (ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_TRIP and energy >= 50):
        return 3
    else:
        return 2


# Second year New Year event
def scenario_event_2(ctx: UmamusumeContext) -> int:
    energy = read_energy()
    if ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_REST or \
            (ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_MEDIC and energy >= 40) or \
            (ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_TRIP and energy >= 50):
        return 3
    else:
        return 1
