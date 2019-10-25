# ℕ𝕖𝕤𝕥𝕖𝕕𝔽𝕖𝕥𝕔𝕙
[![Build Status](https://travis-ci.org/saintlyzero/NestedFetch.svg?branch=master)](https://travis-ci.org/saintlyzero/NestedFetch)  ![GitHub](https://img.shields.io/github/license/saintlyzero/NestedFetch?color=light%20green)

## Overview
**NestedFetch** provides syntactic sugar 🍬 to deal with nested python dictionaries 🐍.
You can `get` `set` `update`, `flatten`  values from deeply nested dictionaries with a more concise, easier and a more *KeyError*, *IndexError* free way 😌.  

## Concept

```python
data = {
        "league": "Champions League",
        "matches": [
            {
                "match_id": "match_1",
                "goals": [
                {
                    "time": 13,
                    "scorrer": "Lionel Messi",
                    "assist": "Luis Suarez"
                },
                {
                    "time": 78,
                    "scorrer": "Luis Suarez",
                    "assist": "Ivan Rakitic"
                }]
            },
            {
                "match_id": "match_2",
                "goals": [
                {
                    "time": 36,
                    "scorrer": "C. Ronaldo",
                    "assist": "Luka Modric"
                }]
            }]
        }
```

![Nested Fetch Illustration](asset/NestedFetchConcept.jpg)

