# Copyright (c) 2016, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

# This file contains all dart, css, and html sources for Observatory.
{
  'sources': [
    'lib/allocation_profile.dart',
    'lib/app.dart',
    'lib/cli.dart',
    'lib/cpu_profile.dart',
    'lib/debugger.dart',
    'lib/elements.dart',
    'lib/elements.html',
    'lib/heap_snapshot.dart',
    'lib/models.dart',
    'lib/object_graph.dart',
    'lib/repositories.dart',
    'lib/service.dart',
    'lib/service_common.dart',
    'lib/service_html.dart',
    'lib/service_io.dart',
    'lib/src/allocation_profile/allocation_profile.dart',
    'lib/src/app/analytics.dart',
    'lib/src/app/application.dart',
    'lib/src/app/event.dart',
    'lib/src/app/location_manager.dart',
    'lib/src/app/notification.dart',
    'lib/src/app/page.dart',
    'lib/src/app/settings.dart',
    'lib/src/app/view_model.dart',
    'lib/src/cli/command.dart',
    'lib/src/cpu_profile/cpu_profile.dart',
    'lib/src/debugger/debugger.dart',
    'lib/src/debugger/debugger_location.dart',
    'lib/src/elements/action_link.dart',
    'lib/src/elements/action_link.html',
    'lib/src/elements/allocation_profile.dart',
    'lib/src/elements/class_ref.dart',
    'lib/src/elements/class_ref_as_value.dart',
    'lib/src/elements/class_ref_as_value.html',
    'lib/src/elements/class_ref_wrapper.dart',
    'lib/src/elements/class_tree.dart',
    'lib/src/elements/class_view.dart',
    'lib/src/elements/class_view.html',
    'lib/src/elements/code_ref.dart',
    'lib/src/elements/code_ref_wrapper.dart',
    'lib/src/elements/code_view.dart',
    'lib/src/elements/code_view.html',
    'lib/src/elements/containers/virtual_collection.dart',
    'lib/src/elements/containers/virtual_tree.dart',
    'lib/src/elements/context_ref.dart',
    'lib/src/elements/context_ref_wrapper.dart',
    'lib/src/elements/context_view.dart',
    'lib/src/elements/context_view.html',
    'lib/src/elements/cpu_profile.dart',
    'lib/src/elements/cpu_profile/virtual_tree.dart',
    'lib/src/elements/cpu_profile_table.dart',
    'lib/src/elements/cpu_profile_table.html',
    'lib/src/elements/css/shared.css',
    'lib/src/elements/curly_block.dart',
    'lib/src/elements/curly_block_wrapper.dart',
    'lib/src/elements/debugger.dart',
    'lib/src/elements/debugger.html',
    'lib/src/elements/error_ref.dart',
    'lib/src/elements/error_ref_wrapper.dart',
    'lib/src/elements/error_view.dart',
    'lib/src/elements/error_view.html',
    'lib/src/elements/eval_box.dart',
    'lib/src/elements/eval_box.html',
    'lib/src/elements/eval_link.dart',
    'lib/src/elements/eval_link.html',
    'lib/src/elements/field_ref.dart',
    'lib/src/elements/field_ref_wrapper.dart',
    'lib/src/elements/field_view.dart',
    'lib/src/elements/field_view.html',
    'lib/src/elements/flag_list.dart',
    'lib/src/elements/function_ref.dart',
    'lib/src/elements/function_ref_wrapper.dart',
    'lib/src/elements/function_view.dart',
    'lib/src/elements/function_view.html',
    'lib/src/elements/general_error.dart',
    'lib/src/elements/heap_map.dart',
    'lib/src/elements/heap_map.html',
    'lib/src/elements/heap_snapshot.dart',
    'lib/src/elements/helpers/any_ref.dart',
    'lib/src/elements/helpers/rendering_queue.dart',
    'lib/src/elements/helpers/rendering_scheduler.dart',
    'lib/src/elements/helpers/tag.dart',
    'lib/src/elements/helpers/uris.dart',
    'lib/src/elements/icdata_ref.dart',
    'lib/src/elements/icdata_view.dart',
    'lib/src/elements/icdata_view.html',
    'lib/src/elements/img/chromium_icon.png',
    'lib/src/elements/img/dart_icon.png',
    'lib/src/elements/img/isolate_icon.png',
    'lib/src/elements/inbound_references.dart',
    'lib/src/elements/instance_ref.dart',
    'lib/src/elements/instance_ref_wrapper.dart',
    'lib/src/elements/instance_view.dart',
    'lib/src/elements/instance_view.html',
    'lib/src/elements/isolate/counter_chart.dart',
    'lib/src/elements/isolate/shared_summary.dart',
    'lib/src/elements/isolate/shared_summary_wrapper.dart',
    'lib/src/elements/isolate_reconnect.dart',
    'lib/src/elements/isolate_ref.dart',
    'lib/src/elements/isolate_ref_wrapper.dart',
    'lib/src/elements/isolate_summary.dart',
    'lib/src/elements/isolate_summary.html',
    'lib/src/elements/isolate_view.dart',
    'lib/src/elements/isolate_view.html',
    'lib/src/elements/json_view.dart',
    'lib/src/elements/json_view.html',
    'lib/src/elements/library_ref.dart',
    'lib/src/elements/library_ref_as_value.dart',
    'lib/src/elements/library_ref_as_value.html',
    'lib/src/elements/library_ref_wrapper.dart',
    'lib/src/elements/library_view.dart',
    'lib/src/elements/library_view.html',
    'lib/src/elements/local_var_descriptors_ref.dart',
    'lib/src/elements/logging.dart',
    'lib/src/elements/logging.html',
    'lib/src/elements/megamorphiccache_ref.dart',
    'lib/src/elements/megamorphiccache_view.dart',
    'lib/src/elements/megamorphiccache_view.html',
    'lib/src/elements/metrics.dart',
    'lib/src/elements/metrics.html',
    'lib/src/elements/nav/bar.dart',
    'lib/src/elements/nav/class_menu.dart',
    'lib/src/elements/nav/class_menu_wrapper.dart',
    'lib/src/elements/nav/isolate_menu.dart',
    'lib/src/elements/nav/isolate_menu_wrapper.dart',
    'lib/src/elements/nav/library_menu.dart',
    'lib/src/elements/nav/library_menu_wrapper.dart',
    'lib/src/elements/nav/menu.dart',
    'lib/src/elements/nav/menu_item.dart',
    'lib/src/elements/nav/menu_item_wrapper.dart',
    'lib/src/elements/nav/menu_wrapper.dart',
    'lib/src/elements/nav/notify.dart',
    'lib/src/elements/nav/notify_event.dart',
    'lib/src/elements/nav/notify_exception.dart',
    'lib/src/elements/nav/notify_wrapper.dart',
    'lib/src/elements/nav/refresh.dart',
    'lib/src/elements/nav/refresh_wrapper.dart',
    'lib/src/elements/nav/top_menu.dart',
    'lib/src/elements/nav/top_menu_wrapper.dart',
    'lib/src/elements/nav/vm_menu.dart',
    'lib/src/elements/nav/vm_menu_wrapper.dart',
    'lib/src/elements/object_common.dart',
    'lib/src/elements/object_common_wrapper.dart',
    'lib/src/elements/object_view.dart',
    'lib/src/elements/object_view.html',
    'lib/src/elements/objectpool_ref.dart',
    'lib/src/elements/objectpool_view.dart',
    'lib/src/elements/objectpool_view.html',
    'lib/src/elements/objectstore_view.dart',
    'lib/src/elements/objectstore_view.html',
    'lib/src/elements/observatory_application.dart',
    'lib/src/elements/observatory_element.dart',
    'lib/src/elements/pc_descriptors_ref.dart',
    'lib/src/elements/persistent_handles.dart',
    'lib/src/elements/persistent_handles.html',
    'lib/src/elements/ports.dart',
    'lib/src/elements/retaining_path.dart',
    'lib/src/elements/sample_buffer_control.dart',
    'lib/src/elements/script_inset.dart',
    'lib/src/elements/script_inset.html',
    'lib/src/elements/script_ref.dart',
    'lib/src/elements/script_ref_wrapper.dart',
    'lib/src/elements/script_view.dart',
    'lib/src/elements/script_view.html',
    'lib/src/elements/sentinel_value.dart',
    'lib/src/elements/service_ref.dart',
    'lib/src/elements/service_ref.html',
    'lib/src/elements/service_view.dart',
    'lib/src/elements/service_view.html',
    'lib/src/elements/shims/binding.dart',
    'lib/src/elements/source_link.dart',
    'lib/src/elements/source_link_wrapper.dart',
    'lib/src/elements/stack_trace_tree_config.dart',
    'lib/src/elements/timeline_page.dart',
    'lib/src/elements/timeline_page.html',
    'lib/src/elements/token_stream_ref.dart',
    'lib/src/elements/unknown_ref.dart',
    'lib/src/elements/view_footer.dart',
    'lib/src/elements/vm_connect.dart',
    'lib/src/elements/vm_connect_target.dart',
    'lib/src/elements/vm_view.dart',
    'lib/src/elements/vm_view.html',
    'lib/src/heap_snapshot/heap_snapshot.dart',
    'lib/src/models/exceptions.dart',
    'lib/src/models/objects/allocation_profile.dart',
    'lib/src/models/objects/bound_field.dart',
    'lib/src/models/objects/breakpoint.dart',
    'lib/src/models/objects/class.dart',
    'lib/src/models/objects/code.dart',
    'lib/src/models/objects/context.dart',
    'lib/src/models/objects/error.dart',
    'lib/src/models/objects/event.dart',
    'lib/src/models/objects/extension_data.dart',
    'lib/src/models/objects/field.dart',
    'lib/src/models/objects/flag.dart',
    'lib/src/models/objects/frame.dart',
    'lib/src/models/objects/function.dart',
    'lib/src/models/objects/guarded.dart',
    'lib/src/models/objects/heap_snapshot.dart',
    'lib/src/models/objects/heap_space.dart',
    'lib/src/models/objects/icdata.dart',
    'lib/src/models/objects/inbound_references.dart',
    'lib/src/models/objects/instance.dart',
    'lib/src/models/objects/isolate.dart',
    'lib/src/models/objects/library.dart',
    'lib/src/models/objects/local_var_descriptors.dart',
    'lib/src/models/objects/map_association.dart',
    'lib/src/models/objects/megamorphiccache.dart',
    'lib/src/models/objects/notification.dart',
    'lib/src/models/objects/object.dart',
    'lib/src/models/objects/objectpool.dart',
    'lib/src/models/objects/pc_descriptors.dart',
    'lib/src/models/objects/ports.dart',
    'lib/src/models/objects/retaining_path.dart',
    'lib/src/models/objects/sample_profile.dart',
    'lib/src/models/objects/script.dart',
    'lib/src/models/objects/sentinel.dart',
    'lib/src/models/objects/source_location.dart',
    'lib/src/models/objects/target.dart',
    'lib/src/models/objects/timeline_event.dart',
    'lib/src/models/objects/token_stream.dart',
    'lib/src/models/objects/unknown.dart',
    'lib/src/models/objects/vm.dart',
    'lib/src/models/repositories/allocation_profile.dart',
    'lib/src/models/repositories/class.dart',
    'lib/src/models/repositories/event.dart',
    'lib/src/models/repositories/flag.dart',
    'lib/src/models/repositories/heap_snapshot.dart',
    'lib/src/models/repositories/inbound_references.dart',
    'lib/src/models/repositories/instance.dart',
    'lib/src/models/repositories/notification.dart',
    'lib/src/models/repositories/ports.dart',
    'lib/src/models/repositories/reachable_size.dart',
    'lib/src/models/repositories/retained_size.dart',
    'lib/src/models/repositories/retaining_path.dart',
    'lib/src/models/repositories/sample_profile.dart',
    'lib/src/models/repositories/script.dart',
    'lib/src/models/repositories/target.dart',
    'lib/src/repositories/allocation_profile.dart',
    'lib/src/repositories/class.dart',
    'lib/src/repositories/event.dart',
    'lib/src/repositories/flag.dart',
    'lib/src/repositories/heap_snapshot.dart',
    'lib/src/repositories/inbound_references.dart',
    'lib/src/repositories/instance.dart',
    'lib/src/repositories/notification.dart',
    'lib/src/repositories/ports.dart',
    'lib/src/repositories/reachable_size.dart',
    'lib/src/repositories/retained_size.dart',
    'lib/src/repositories/retaining_path.dart',
    'lib/src/repositories/sample_profile.dart',
    'lib/src/repositories/script.dart',
    'lib/src/repositories/settings.dart',
    'lib/src/repositories/target.dart',
    'lib/src/service/object.dart',
    'lib/tracer.dart',
    'lib/utils.dart',
    'web/favicon.ico',
    'web/index.html',
    'web/main.dart',
    'web/third_party/trace_viewer_full.html',
    'web/timeline.html',
    'web/timeline.js',
    'web/timeline_message_handler.js',
  ]
}
