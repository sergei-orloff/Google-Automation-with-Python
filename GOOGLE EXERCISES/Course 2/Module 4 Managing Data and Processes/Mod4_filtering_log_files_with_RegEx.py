import re


def show_time_of_pid(line):
    # Regex pattern to match the date, time, and PID inside square brackets
    pattern = r'^(\w+ \d+ \d+:\d+:\d+).*?\[(\d+)\]'

    # Search for the pattern in the line
    result = re.search(pattern, line)

    # If a match is found, return the formatted string
    if result:
        return f"{result.group(1)} pid:{result.group(2)}"

    # If no match is found, return None or an appropriate message
    return None


# Test cases
print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Output: Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Output: Jul 6 14:02:08
# pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

"""
 Explanation:
1. The regular expression should capture:
   - The date and time (e.g., `Jul 6 14:01:23`).
   - The process ID, which appears inside square brackets (e.g., `[29440]`).
2. We can use groups in the regular expression to extract these parts separately and then format them as needed.


### Breakdown of the Regex Pattern:
- `^`: Anchors the pattern to the start of the string.
- `(\w+ \d+ \d+:\d+:\d+)`: Captures the date and time (e.g., `Jul 6 14:01:23`).
- `.*?`: Matches any characters (non-greedy) between the time and the process ID.
- `\[(\d+)\]`: Captures the process ID inside square brackets (e.g., `[29440]`).

"""