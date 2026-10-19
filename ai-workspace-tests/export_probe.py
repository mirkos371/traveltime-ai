#!/usr/bin/env python3
"""Synthetic export pipeline smoke test. NOT part of private TravelTime code."""
EXPORT_TEST_VERSION = "v1"
def export_probe():
    return "TRAVELTIME_WORKSPACE_TEST_" + EXPORT_TEST_VERSION
if __name__ == "__main__":
    print(export_probe())
