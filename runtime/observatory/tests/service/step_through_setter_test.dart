// Copyright (c) 2017, the Dart project authors.  Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

import 'test_helper.dart';
import 'service_test_common.dart';

const int LINE = 11;
const String file = "step_through_setter_test.dart";

code() {
  Bar bar = new Bar();
  bar.barXYZ = 42;
  fooXYZ = 42;
}

int _xyz = -1;

set fooXYZ(int i) {
  _xyz = i - 1;
}

class Bar {
  int _xyz = -1;

  set barXYZ(int i) {
    _xyz = i - 1;
  }

  get barXYZ => _xyz + 1;
}

List<String> stops = [];
List<String> expected = [
  "$file:${LINE+0}:5", // after 'code'
  "$file:${LINE+1}:17", // on 'Bar'

  "$file:${LINE+2}:7", // on 'barXYZ'
  "$file:${LINE+15}:18", // on 'i'
  "$file:${LINE+16}:14", // on '-'
  "$file:${LINE+16}:5", // on '_xyz'
  "$file:${LINE+17}:3", // on '}'

  "$file:${LINE+3}:3", // on 'fooXYZ'
  "$file:${LINE+8}:16", // on 'i'
  "$file:${LINE+9}:12", // on '-'
  "$file:${LINE+10}:1", // on '}'

  "$file:${LINE+4}:1" // on ending '}'
];

var tests = [
  hasPausedAtStart,
  setBreakpointAtLine(LINE),
  runStepIntoThroughProgramRecordingStops(stops),
  checkRecordedStops(stops, expected,
      debugPrint: true, debugPrintFile: file, debugPrintLine: LINE)
];

main(args) {
  runIsolateTestsSynchronous(args, tests,
      testeeConcurrent: code, pause_on_start: true, pause_on_exit: true);
}
