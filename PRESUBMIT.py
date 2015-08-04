# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Top-level presubmit script for catapult.

See https://www.chromium.org/developers/how-tos/depottools/presubmit-scripts
for more details about the presubmit API built into depot_tools.
"""
import sys


def GetPreferredTryMasters(project, change):  # pylint: disable=unused-argument
  return {
      'tryserver.client.catapult': {
          'Catapult Linux Tryserver': {'defaulttests'},
          'Catapult Mac Tryserver': {'defaulttests'},
          'Catapult Windows Tryserver': {'defaulttests'},
      }
  }


def RunChecks(input_api, output_api):
  from build import presubmit_checks
  return map(output_api.PresubmitError, presubmit_checks.RunChecks(input_api))


def CheckChange(input_api, output_api):
  results = []
  results.extend(
      input_api.canned_checks.PanProjectChecks(input_api, output_api))
  original_sys_path = sys.path
  try:
    sys.path += [input_api.PresubmitLocalPath()]
    results.extend(RunChecks(input_api, output_api))
  finally:
    sys.path = original_sys_path
  return results


def CheckChangeOnUpload(input_api, output_api):
  return CheckChange(input_api, output_api)


def CheckChangeOnCommit(input_api, output_api):
  return CheckChange(input_api, output_api)