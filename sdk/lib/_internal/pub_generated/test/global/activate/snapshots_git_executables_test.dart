import 'package:scheduled_test/scheduled_test.dart';
import '../../descriptor.dart' as d;
import '../../test_pub.dart';
main() {
  initConfig();
  integration('snapshots the executables for a Git repo', () {
    ensureGit();
    d.git(
        'foo.git',
        [
            d.libPubspec("foo", "1.0.0"),
            d.dir(
                "bin",
                [
                    d.file("hello.dart", "void main() => print('hello!');"),
                    d.file("goodbye.dart", "void main() => print('goodbye!');"),
                    d.file("shell.sh", "echo shell"),
                    d.dir(
                        "subdir",
                        [d.file("sub.dart", "void main() => print('sub!');")])])]).create();
    schedulePub(
        args: ["global", "activate", "-sgit", "../foo.git"],
        output: allOf(
            [contains('Precompiled foo:hello.'), contains("Precompiled foo:goodbye.")]));
    d.dir(
        cachePath,
        [
            d.dir(
                'global_packages',
                [
                    d.dir(
                        'foo',
                        [
                            d.matcherFile('pubspec.lock', contains('1.0.0')),
                            d.dir(
                                'bin',
                                [
                                    d.matcherFile('hello.dart.snapshot', contains('hello!')),
                                    d.matcherFile('goodbye.dart.snapshot', contains('goodbye!')),
                                    d.nothing('shell.sh.snapshot'),
                                    d.nothing('subdir')])])])]).validate();
  });
}
