library pub_tests;
import '../../descriptor.dart' as d;
import '../../test_pub.dart';
main() {
  initConfig();
  integration(
      'upgrades a locked Git package with a new incompatible ' 'constraint',
      () {
    ensureGit();
    d.git('foo.git', [d.libDir('foo'), d.libPubspec('foo', '0.5.0')]).create();
    d.appDir({
      "foo": {
        "git": "../foo.git"
      }
    }).create();
    pubGet();
    d.dir(
        packagesPath,
        [d.dir('foo', [d.file('foo.dart', 'main() => "foo";')])]).validate();
    d.git(
        'foo.git',
        [d.libDir('foo', 'foo 1.0.0'), d.libPubspec("foo", "1.0.0")]).commit();
    d.appDir({
      "foo": {
        "git": "../foo.git",
        "version": ">=1.0.0"
      }
    }).create();
    pubGet();
    d.dir(
        packagesPath,
        [d.dir('foo', [d.file('foo.dart', 'main() => "foo 1.0.0";')])]).validate();
  });
}
