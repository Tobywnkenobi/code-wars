def time_to_milliseconds(h, m, s):
    # Convert hours to milliseconds
    h_to_ms = h * 3600000
    # Convert minutes to milliseconds
    m_to_ms = m * 60000
    # Convert seconds to milliseconds
    s_to_ms = s * 1000
    # Return the total time in milliseconds since midnight
    return h_to_ms + m_to_ms + s_to_ms
