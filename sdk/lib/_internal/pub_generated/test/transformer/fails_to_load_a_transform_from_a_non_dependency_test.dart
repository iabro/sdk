library pub_tests;
import 'package:scheduled_test/scheduled_test.dart';
import '../../lib/src/exit_codes.dart' as exit_codes;
import '../descriptor.dart' as d;
import '../test_pub.dart';
import '../serve/utils.dart';
main() {
  initConfig();
  withBarbackVersions("any", () {
    integration("fails to load a transform from a non-dependency", () {
      d.dir(appPath, [d.pubspec({
          "name": "myapp",
          "transformers": ["foo"]
        })]).create();
      var pub = startPubServe();
      pub.stderr.expect(contains('"foo" is not a dependency.'));
      pub.shouldExit(exit_codes.DATA);
    });
  });
}
