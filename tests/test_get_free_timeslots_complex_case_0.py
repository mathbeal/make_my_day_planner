import pytest

from app_scripts.get_free_timeslots import get_free_timeslots

"""
Pytest file for testing.
Run with `pytest` in root of project
"""

"""
If any test fails, drop to the python shell and use the following to execute
tests for a specific time_min

```
from app_scripts.get_free_timeslots import get_free_timeslots
time_min = '2019-12-14T13:00:00+01:00'
time_max = '2019-12-14T23:59:00+01:00'
scheduled_time_blocks = [['2019-12-14T09:00:00+01:00', '2019-12-14T10:00:00+01:00'],
 ['2019-12-14T11:00:00+01:00', '2019-12-14T12:30:00+01:00'],
 ['2019-12-14T11:30:00+01:00', '2019-12-14T12:00:00+01:00'],
 ['2019-12-14T14:00:00+01:00', '2019-12-14T15:00:00+01:00'],
 ['2019-12-14T14:30:00+01:00', '2019-12-14T16:00:00+01:00'],
 ['2019-12-14T17:00:00+01:00', '2019-12-14T18:00:00+01:00'],
 ['2019-12-14T18:00:00+01:00', '2019-12-14T19:00:00+01:00']]
get_free_timeslots(time_min, time_max, scheduled_time_blocks)

```

"""

time_s_p = ["2019-12-14T", ":00+01:00"]

scheduled_time_blocks_raw = [
    ["09:00", "10:00"],
    ["11:00", "12:30"],
    ["11:30", "12:00"],
    ["14:00", "15:00"],
    ["14:30", "16:00"],
    ["17:00", "18:00"],
    ["18:00", "19:00"],
]

time_max_raw = "23:59"

time_mins_raw = {
    "08:00": [
        ["08:00", "09:00"],
        ["10:00", "11:00"],
        ["12:30", "14:00"],
        ["16:00", "17:00"],
        ["19:00", "23:59"],
    ],
    "09:00": [
        ["10:00", "11:00"],
        ["12:30", "14:00"],
        ["16:00", "17:00"],
        ["19:00", "23:59"],
    ],
    "09:30": [
        ["10:00", "11:00"],
        ["12:30", "14:00"],
        ["16:00", "17:00"],
        ["19:00", "23:59"],
    ],
    "10:00": [
        ["10:00", "11:00"],
        ["12:30", "14:00"],
        ["16:00", "17:00"],
        ["19:00", "23:59"],
    ],
    "10:30": [
        ["10:30", "11:00"],
        ["12:30", "14:00"],
        ["16:00", "17:00"],
        ["19:00", "23:59"],
    ],
    "11:00": [["12:30", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "11:15": [["12:30", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "11:30": [["12:30", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "11:45": [["12:30", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "12:00": [["12:30", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "12:15": [["12:30", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "12:30": [["12:30", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "13:00": [["13:00", "14:00"], ["16:00", "17:00"], ["19:00", "23:59"]],
    "14:00": [["16:00", "17:00"], ["19:00", "23:59"]],
    "14:15": [["16:00", "17:00"], ["19:00", "23:59"]],
    "14:30": [["16:00", "17:00"], ["19:00", "23:59"]],
    "14:45": [["16:00", "17:00"], ["19:00", "23:59"]],
    "15:00": [["16:00", "17:00"], ["19:00", "23:59"]],
    "15:30": [["16:00", "17:00"], ["19:00", "23:59"]],
    "16:00": [["16:00", "17:00"], ["19:00", "23:59"]],
    "16:30": [["16:30", "17:00"], ["19:00", "23:59"]],
    "17:00": [["19:00", "23:59"]],
    "17:30": [["19:00", "23:59"]],
    "18:00": [["19:00", "23:59"]],
    "18:30": [["19:00", "23:59"]],
    "19:00": [["19:00", "23:59"]],
    "19:30": [["19:30", "23:59"]],
}

scheduled_time_blocks = [
    [f"{time_s_p[0]}{i[0]}{time_s_p[1]}", f"{time_s_p[0]}{i[1]}{time_s_p[1]}"]
    for i in scheduled_time_blocks_raw
]
time_min_free_time_dict = {}

for a_time_min, a_free_result_list in time_mins_raw.items():

    temp_free_timeblocks = []
    for i in a_free_result_list:
        temp_free_timeblocks.append(
            [f"{time_s_p[0]}{i[0]}{time_s_p[1]}", f"{time_s_p[0]}{i[1]}{time_s_p[1]}"]
        )

    time_min_free_time_dict[
        f"{time_s_p[0]}{a_time_min}{time_s_p[1]}"
    ] = temp_free_timeblocks

time_max = f"{time_s_p[0]}{time_max_raw}{time_s_p[1]}"

free_timeblock_expected_and_received_results = []

for time_min, expected_free_timeblocks in time_min_free_time_dict.items():
    received_free_timeblocks = get_free_timeslots(
        time_min, time_max, scheduled_time_blocks
    )
    free_timeblock_expected_and_received_results.append(
        [expected_free_timeblocks, received_free_timeblocks]
    )


@pytest.mark.parametrize(
    "expected_free_timeblocks, received_free_timeblocks",
    free_timeblock_expected_and_received_results,
)
def test_complex_case_0(expected_free_timeblocks, received_free_timeblocks):
    assert received_free_timeblocks == expected_free_timeblocks
