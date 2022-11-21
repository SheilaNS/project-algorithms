def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not isinstance(target_time, int):
        return None

    count = 0
    for get_in, get_out in permanence_period:
        if not isinstance(get_in, int) or not isinstance(get_out, int):
            return None
        if get_in <= target_time <= get_out:
            count += 1
    return count
