library lish.utils;
import 'dart:convert';
import 'package:scheduled_test/scheduled_test.dart';
import 'package:scheduled_test/scheduled_server.dart';
import 'package:shelf/shelf.dart' as shelf;
import '../../lib/src/io.dart';
void handleUploadForm(ScheduledServer server, [Map body]) {
  server.handle('GET', '/api/packages/versions/new', (request) {
    return server.url.then((url) {
      expect(
          request.headers,
          containsPair('authorization', 'Bearer access token'));
      if (body == null) {
        body = {
          'url': url.resolve('/upload').toString(),
          'fields': {
            'field1': 'value1',
            'field2': 'value2'
          }
        };
      }
      return new shelf.Response.ok(JSON.encode(body), headers: {
        'content-type': 'application/json'
      });
    });
  });
}
void handleUpload(ScheduledServer server) {
  server.handle('POST', '/upload', (request) {
    return drainStream(
        request.read()).then(
            (_) =>
                server.url).then((url) => new shelf.Response.found(url.resolve('/create')));
  });
}
