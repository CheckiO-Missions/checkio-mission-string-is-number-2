"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["34"],
            "answer": True,
        },
        {
            "input": ["df"],
            "answer": False,
        },
        {
            "input": [""],
            "answer": False,
        },
        {
            "input": ["+10.0"],
            "answer": True,
        },
        {
            "input": ["1OOO"],
            "answer": False,
        },
        {
            "input": ["1."],
            "answer": True,
        },
        {
            "input": ["+.l"],
            "answer": False,
        },
       
    ],
    "Extra": [
        {
            "input": ["ITS A NUMBER"],
            "answer": False,
        },
        {
            "input": ["1033"],
            "answer": True,
        },
        {
            "input": ["-1000.25"],
            "answer": True,
        },
        {
            "input": ["1l0O"],
            "answer": False,
        },
        {
            "input": ["+1"],
            "answer": True,
        },
        {
            "input": ["+25.25"],
            "answer": True,
        },
        {
            "input": ["+.123"],
            "answer": True,
        },
        {
            "input": ["-40."],
            "answer": True,
        },
        {
            "input": [".1"],
            "answer": True,
        },

    ]
}
