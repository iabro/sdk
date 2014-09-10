import 'package:scheduled_test/scheduled_test.dart';
import '../../lib/src/exit_codes.dart' as exit_codes;
import '../descriptor.dart' as d;
import '../test_pub.dart';
main() {
  initConfig();
  integration('an explicit --server argument does not override privacy', () {
    var pkg = packageMap("test_pkg", "1.0.0");
    pkg["publish_to"] = "none";
    d.dir(appPath, [d.pubspec(pkg)]).create();
    schedulePub(
        args: ["lish", "--server", "http://arg.com"],
        error: startsWith("A private package cannot be published."),
        exitCode: exit_codes.DATA);
  });
}
