# Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'variables': {
    'includes_common': [
      'include/base/cef_atomic_ref_count.h',
      'include/base/cef_atomicops.h',
      'include/base/cef_basictypes.h',
      'include/base/cef_bind.h',
      'include/base/cef_bind_helpers.h',
      'include/base/cef_build.h',
      'include/base/cef_callback.h',
      'include/base/cef_callback_forward.h',
      'include/base/cef_callback_helpers.h',
      'include/base/cef_callback_list.h',
      'include/base/cef_cancelable_callback.h',
      'include/base/cef_lock.h',
      'include/base/cef_logging.h',
      'include/base/cef_macros.h',
      'include/base/cef_move.h',
      'include/base/cef_platform_thread.h',
      'include/base/cef_ref_counted.h',
      'include/base/cef_scoped_ptr.h',
      'include/base/cef_string16.h',
      'include/base/cef_template_util.h',
      'include/base/cef_thread_checker.h',
      'include/base/cef_trace_event.h',
      'include/base/cef_tuple.h',
      'include/base/cef_weak_ptr.h',
      'include/base/internal/cef_bind_internal.h',
      'include/base/internal/cef_callback_internal.h',
      'include/base/internal/cef_lock_impl.h',
      'include/base/internal/cef_raw_scoped_refptr_mismatch_checker.h',
      'include/base/internal/cef_thread_checker_impl.h',
      'include/cef_base.h',
      'include/cef_version.h',
      'include/internal/cef_export.h',
      'include/internal/cef_logging_internal.h',
      'include/internal/cef_ptr.h',
      'include/internal/cef_string.h',
      'include/internal/cef_string_list.h',
      'include/internal/cef_string_map.h',
      'include/internal/cef_string_multimap.h',
      'include/internal/cef_string_types.h',
      'include/internal/cef_string_wrappers.h',
      'include/internal/cef_thread_internal.h',
      'include/internal/cef_time.h',
      'include/internal/cef_trace_event_internal.h',
      'include/internal/cef_types.h',
      'include/internal/cef_types_wrappers.h',
    ],
    'includes_capi': [
      'include/capi/cef_base_capi.h',
    ],
    'includes_wrapper': [
      'include/wrapper/cef_byte_read_handler.h',
      'include/wrapper/cef_closure_task.h',
      'include/wrapper/cef_helpers.h',
      'include/wrapper/cef_message_router.h',
      'include/wrapper/cef_resource_manager.h',
      'include/wrapper/cef_scoped_temp_dir.h',
      'include/wrapper/cef_stream_resource_handler.h',
      'include/wrapper/cef_xml_object.h',
      'include/wrapper/cef_zip_archive.h',
    ],
    'includes_wrapper_mac': [
      'include/wrapper/cef_library_loader.h',
    ],
    'includes_win': [
      'include/base/internal/cef_atomicops_x86_msvc.h',
      'include/base/internal/cef_bind_internal_win.h',
      'include/cef_sandbox_win.h',
      'include/internal/cef_types_win.h',
      'include/internal/cef_win.h',
    ],
    'includes_mac': [
      'include/base/internal/cef_atomicops_atomicword_compat.h',
      'include/base/internal/cef_atomicops_mac.h',
      'include/cef_application_mac.h',
      'include/cef_sandbox_mac.h',
      'include/internal/cef_mac.h',
      'include/internal/cef_types_mac.h',
    ],
    'includes_linux': [
      'include/base/internal/cef_atomicops_atomicword_compat.h',
      'include/base/internal/cef_atomicops_arm_gcc.h',
      'include/base/internal/cef_atomicops_x86_gcc.h',
      'include/internal/cef_linux.h',
      'include/internal/cef_types_linux.h',
    ],
    'libcef_sources_common': [
      'libcef_dll/cpptoc/cpptoc_ref_counted.h',
      'libcef_dll/cpptoc/cpptoc_scoped.h',
      'libcef_dll/ctocpp/base_ref_counted_ctocpp.cc',
      'libcef_dll/ctocpp/base_ref_counted_ctocpp.h',
      'libcef_dll/ctocpp/base_scoped_ctocpp.cc',
      'libcef_dll/ctocpp/base_scoped_ctocpp.h',
      'libcef_dll/ctocpp/ctocpp_ref_counted.h',
      'libcef_dll/ctocpp/ctocpp_scoped.h',
      'libcef_dll/libcef_dll.cc',
      'libcef_dll/libcef_dll2.cc',
      'libcef_dll/ptr_util.h',
      'libcef_dll/resource.h',
      'libcef_dll/transfer_util.cc',
      'libcef_dll/transfer_util.h',
      'libcef_dll/wrapper_types.h',
    ],
    'libcef_dll_wrapper_sources_base': [
      'libcef_dll/base/cef_atomicops_x86_gcc.cc',
      'libcef_dll/base/cef_bind_helpers.cc',
      'libcef_dll/base/cef_callback_helpers.cc',
      'libcef_dll/base/cef_callback_internal.cc',
      'libcef_dll/base/cef_lock.cc',
      'libcef_dll/base/cef_lock_impl.cc',
      'libcef_dll/base/cef_logging.cc',
      'libcef_dll/base/cef_ref_counted.cc',
      'libcef_dll/base/cef_string16.cc',
      'libcef_dll/base/cef_thread_checker_impl.cc',
      'libcef_dll/base/cef_weak_ptr.cc',
    ],
    'libcef_dll_wrapper_sources_common': [
      'libcef_dll/cpptoc/base_ref_counted_cpptoc.cc',
      'libcef_dll/cpptoc/base_ref_counted_cpptoc.h',
      'libcef_dll/cpptoc/base_scoped_cpptoc.cc',
      'libcef_dll/cpptoc/base_scoped_cpptoc.h',
      'libcef_dll/cpptoc/cpptoc_ref_counted.h',
      'libcef_dll/cpptoc/cpptoc_scoped.h',
      'libcef_dll/ctocpp/ctocpp_ref_counted.h',
      'libcef_dll/ctocpp/ctocpp_scoped.h',
      'libcef_dll/ptr_util.h',
      'libcef_dll/transfer_util.cc',
      'libcef_dll/transfer_util.h',
      'libcef_dll/wrapper_types.h',
      'libcef_dll/wrapper/cef_browser_info_map.h',
      'libcef_dll/wrapper/cef_byte_read_handler.cc',
      'libcef_dll/wrapper/cef_closure_task.cc',
      'libcef_dll/wrapper/cef_message_router.cc',
      'libcef_dll/wrapper/cef_resource_manager.cc',
      'libcef_dll/wrapper/cef_scoped_temp_dir.cc',
      'libcef_dll/wrapper/cef_stream_resource_handler.cc',
      'libcef_dll/wrapper/cef_xml_object.cc',
      'libcef_dll/wrapper/cef_zip_archive.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper2.cc',
    ],
    'libcef_dll_wrapper_sources_mac': [
      'libcef_dll/wrapper/cef_library_loader_mac.mm',
      'libcef_dll/wrapper/libcef_dll_dylib.cc',
    ],
    'shared_sources_browser': [
      'tests/shared/browser/client_app_browser.cc',
      'tests/shared/browser/client_app_browser.h',
      'tests/shared/browser/extension_util.cc',
      'tests/shared/browser/extension_util.h',
      'tests/shared/browser/file_util.cc',
      'tests/shared/browser/file_util.h',
      'tests/shared/browser/geometry_util.cc',
      'tests/shared/browser/geometry_util.h',
      'tests/shared/browser/main_message_loop.cc',
      'tests/shared/browser/main_message_loop.h',
      'tests/shared/browser/main_message_loop_external_pump.cc',
      'tests/shared/browser/main_message_loop_external_pump.h',
      'tests/shared/browser/main_message_loop_std.cc',
      'tests/shared/browser/main_message_loop_std.h',
      'tests/shared/browser/resource_util.h',
    ],
    'shared_sources_common': [
      'tests/shared/common/client_app.cc',
      'tests/shared/common/client_app.h',
      'tests/shared/common/client_app_other.cc',
      'tests/shared/common/client_app_other.h',
      'tests/shared/common/client_switches.cc',
      'tests/shared/common/client_switches.h',
    ],
    'shared_sources_renderer': [
      'tests/shared/renderer/client_app_renderer.cc',
      'tests/shared/renderer/client_app_renderer.h',
    ],
    'shared_sources_resources': [
      'tests/shared/resources/osr_test.html',
      'tests/shared/resources/pdf.html',
      'tests/shared/resources/pdf.pdf',
      'tests/shared/resources/window_icon.1x.png',
      'tests/shared/resources/window_icon.2x.png',
    ],
    'shared_sources_linux': [
      'tests/shared/browser/main_message_loop_external_pump_linux.cc',
      'tests/shared/browser/resource_util_posix.cc',
    ],
    'shared_sources_mac': [
      'tests/shared/browser/main_message_loop_external_pump_mac.mm',
      'tests/shared/browser/resource_util_mac.mm',
      'tests/shared/browser/resource_util_posix.cc',
    ],
    'shared_sources_mac_helper': [
      'tests/shared/process_helper_mac.cc',
    ],
    'shared_sources_win': [
      'tests/shared/browser/main_message_loop_external_pump_win.cc',
      'tests/shared/browser/resource_util_win.cc',
      'tests/shared/browser/util_win.cc',
      'tests/shared/browser/util_win.h',
    ],
    'cefclient_sources_browser': [
      'tests/cefclient/browser/binding_test.cc',
      'tests/cefclient/browser/binding_test.h',
      'tests/cefclient/browser/browser_window.cc',
      'tests/cefclient/browser/browser_window.h',
      'tests/cefclient/browser/bytes_write_handler.cc',
      'tests/cefclient/browser/bytes_write_handler.h',
      'tests/cefclient/browser/client_app_delegates_browser.cc',
      'tests/cefclient/browser/client_browser.cc',
      'tests/cefclient/browser/client_browser.h',
      'tests/cefclient/browser/client_handler.cc',
      'tests/cefclient/browser/client_handler.h',
      'tests/cefclient/browser/client_handler_osr.cc',
      'tests/cefclient/browser/client_handler_osr.h',
      'tests/cefclient/browser/client_handler_std.cc',
      'tests/cefclient/browser/client_handler_std.h',
      'tests/cefclient/browser/client_types.h',
      'tests/cefclient/browser/dialog_test.cc',
      'tests/cefclient/browser/dialog_test.h',
      'tests/cefclient/browser/drm_test.cc',
      'tests/cefclient/browser/drm_test.h',
      'tests/cefclient/browser/image_cache.cc',
      'tests/cefclient/browser/image_cache.h',
      'tests/cefclient/browser/main_context.cc',
      'tests/cefclient/browser/main_context.h',
      'tests/cefclient/browser/main_context_impl.cc',
      'tests/cefclient/browser/main_context_impl.h',
      'tests/cefclient/browser/osr_dragdrop_events.h',
      'tests/cefclient/browser/osr_renderer.h',
      'tests/cefclient/browser/osr_renderer.cc',
      'tests/cefclient/browser/preferences_test.cc',
      'tests/cefclient/browser/preferences_test.h',
      'tests/cefclient/browser/resource.h',
      'tests/cefclient/browser/response_filter_test.cc',
      'tests/cefclient/browser/response_filter_test.h',
      'tests/cefclient/browser/root_window.cc',
      'tests/cefclient/browser/root_window.h',
      'tests/cefclient/browser/root_window_create.cc',
      'tests/cefclient/browser/root_window_manager.cc',
      'tests/cefclient/browser/root_window_manager.h',
      'tests/cefclient/browser/scheme_test.cc',
      'tests/cefclient/browser/scheme_test.h',
      'tests/cefclient/browser/server_test.cc',
      'tests/cefclient/browser/server_test.h',
      'tests/cefclient/browser/temp_window.h',
      'tests/cefclient/browser/test_runner.cc',
      'tests/cefclient/browser/test_runner.h',
      'tests/cefclient/browser/urlrequest_test.cc',
      'tests/cefclient/browser/urlrequest_test.h',
      'tests/cefclient/browser/window_test.cc',
      'tests/cefclient/browser/window_test.h',
      'tests/cefclient/browser/window_test_runner.cc',
      'tests/cefclient/browser/window_test_runner.h',
    ],
    'cefclient_sources_common': [
      'tests/cefclient/common/client_app_delegates_common.cc',
      'tests/cefclient/common/scheme_test_common.cc',
      'tests/cefclient/common/scheme_test_common.h',
    ],
    'cefclient_sources_renderer': [
      'tests/cefclient/renderer/client_app_delegates_renderer.cc',
      'tests/cefclient/renderer/client_renderer.cc',
      'tests/cefclient/renderer/client_renderer.h',
      'tests/cefclient/renderer/performance_test.cc',
      'tests/cefclient/renderer/performance_test.h',
      'tests/cefclient/renderer/performance_test_setup.h',
      'tests/cefclient/renderer/performance_test_tests.cc',
    ],
    'cefclient_sources_resources': [
      'tests/cefclient/resources/binding.html',
      'tests/cefclient/resources/dialogs.html',
      'tests/cefclient/resources/draggable.html',
      'tests/cefclient/resources/drm.html',
      'tests/cefclient/resources/localstorage.html',
      'tests/cefclient/resources/logo.png',
      'tests/cefclient/resources/menu_icon.1x.png',
      'tests/cefclient/resources/menu_icon.2x.png',
      'tests/cefclient/resources/other_tests.html',
      'tests/cefclient/resources/performance.html',
      'tests/cefclient/resources/performance2.html',
      'tests/cefclient/resources/preferences.html',
      'tests/cefclient/resources/response_filter.html',
      'tests/cefclient/resources/server.html',
      'tests/cefclient/resources/transparency.html',
      'tests/cefclient/resources/urlrequest.html',
      'tests/cefclient/resources/websocket.html',
      'tests/cefclient/resources/window.html',
      'tests/cefclient/resources/xmlhttprequest.html',
    ],
    'cefclient_sources_resources_extensions_set_page_color': [
      'tests/cefclient/resources/extensions/set_page_color/icon.png',
      'tests/cefclient/resources/extensions/set_page_color/manifest.json',
      'tests/cefclient/resources/extensions/set_page_color/popup.html',
      'tests/cefclient/resources/extensions/set_page_color/popup.js',
      'tests/cefclient/resources/extensions/set_page_color/README.md',
    ],
    'cefclient_sources_win': [
      'tests/cefclient/browser/browser_window_osr_win.cc',
      'tests/cefclient/browser/browser_window_osr_win.h',
      'tests/cefclient/browser/browser_window_std_win.cc',
      'tests/cefclient/browser/browser_window_std_win.h',
      'tests/cefclient/browser/main_context_impl_win.cc',
      'tests/cefclient/browser/main_message_loop_multithreaded_win.cc',
      'tests/cefclient/browser/main_message_loop_multithreaded_win.h',
      'tests/cefclient/browser/osr_accessibility_helper.cc',
      'tests/cefclient/browser/osr_accessibility_helper.h',
      'tests/cefclient/browser/osr_accessibility_node.cc',
      'tests/cefclient/browser/osr_accessibility_node.h',
      'tests/cefclient/browser/osr_accessibility_node_win.cc',
      'tests/cefclient/browser/osr_dragdrop_win.cc',
      'tests/cefclient/browser/osr_dragdrop_win.h',
      'tests/cefclient/browser/osr_ime_handler_win.cc',
      'tests/cefclient/browser/osr_ime_handler_win.h',
      'tests/cefclient/browser/osr_window_win.cc',
      'tests/cefclient/browser/osr_window_win.h',
      'tests/cefclient/browser/resource_util_win_idmap.cc',
      'tests/cefclient/browser/root_window_views.cc',
      'tests/cefclient/browser/root_window_views.h',
      'tests/cefclient/browser/root_window_win.cc',
      'tests/cefclient/browser/root_window_win.h',
      'tests/cefclient/browser/temp_window_win.cc',
      'tests/cefclient/browser/temp_window_win.h',
      'tests/cefclient/browser/views_menu_bar.cc',
      'tests/cefclient/browser/views_menu_bar.h',
      'tests/cefclient/browser/views_style.cc',
      'tests/cefclient/browser/views_style.h',
      'tests/cefclient/browser/views_window.cc',
      'tests/cefclient/browser/views_window.h',
      'tests/cefclient/browser/window_test_runner_views.cc',
      'tests/cefclient/browser/window_test_runner_views.h',
      'tests/cefclient/browser/window_test_runner_win.cc',
      'tests/cefclient/browser/window_test_runner_win.h',
      'tests/cefclient/cefclient_win.cc',
      'tests/cefclient/resources/win/cefclient.exe.manifest',
      'tests/cefclient/resources/win/cefclient.ico',
      'tests/cefclient/resources/win/cefclient.rc',
      'tests/cefclient/resources/win/small.ico',
    ],
    'cefclient_sources_mac': [
      'tests/cefclient/browser/browser_window_osr_mac.h',
      'tests/cefclient/browser/browser_window_osr_mac.mm',
      'tests/cefclient/browser/browser_window_std_mac.h',
      'tests/cefclient/browser/browser_window_std_mac.mm',
      'tests/cefclient/browser/main_context_impl_posix.cc',
      'tests/cefclient/browser/osr_accessibility_helper.cc',
      'tests/cefclient/browser/osr_accessibility_helper.h',
      'tests/cefclient/browser/osr_accessibility_node.cc',
      'tests/cefclient/browser/osr_accessibility_node.h',
      'tests/cefclient/browser/osr_accessibility_node_mac.mm',
      'tests/cefclient/browser/root_window_mac.h',
      'tests/cefclient/browser/root_window_mac.mm',
      'tests/cefclient/browser/temp_window_mac.h',
      'tests/cefclient/browser/temp_window_mac.mm',
      'tests/cefclient/browser/text_input_client_osr_mac.h',
      'tests/cefclient/browser/text_input_client_osr_mac.mm',
      'tests/cefclient/browser/window_test_runner_mac.h',
      'tests/cefclient/browser/window_test_runner_mac.mm',
      'tests/cefclient/cefclient_mac.mm',
   ],
    'cefclient_bundle_resources_mac': [
      'tests/cefclient/resources/mac/cefclient.icns',
      'tests/cefclient/resources/mac/English.lproj/InfoPlist.strings',
      'tests/cefclient/resources/mac/English.lproj/MainMenu.xib',
      'tests/cefclient/resources/mac/Info.plist',
    ],
    'cefclient_sources_linux': [
      'tests/cefclient/browser/browser_window_osr_gtk.cc',
      'tests/cefclient/browser/browser_window_osr_gtk.h',
      'tests/cefclient/browser/browser_window_std_gtk.cc',
      'tests/cefclient/browser/browser_window_std_gtk.h',
      'tests/cefclient/browser/dialog_handler_gtk.cc',
      'tests/cefclient/browser/dialog_handler_gtk.h',
      'tests/cefclient/browser/main_context_impl_posix.cc',
      'tests/cefclient/browser/print_handler_gtk.cc',
      'tests/cefclient/browser/print_handler_gtk.h',
      'tests/cefclient/browser/resource_util_linux.cc',
      'tests/cefclient/browser/root_window_gtk.cc',
      'tests/cefclient/browser/root_window_gtk.h',
      'tests/cefclient/browser/root_window_views.cc',
      'tests/cefclient/browser/root_window_views.h',
      'tests/cefclient/browser/temp_window_x11.cc',
      'tests/cefclient/browser/temp_window_x11.h',
      'tests/cefclient/browser/views_menu_bar.cc',
      'tests/cefclient/browser/views_menu_bar.h',
      'tests/cefclient/browser/views_style.cc',
      'tests/cefclient/browser/views_style.h',
      'tests/cefclient/browser/views_window.cc',
      'tests/cefclient/browser/views_window.h',
      'tests/cefclient/browser/window_test_runner_gtk.cc',
      'tests/cefclient/browser/window_test_runner_gtk.h',
      'tests/cefclient/browser/window_test_runner_views.cc',
      'tests/cefclient/browser/window_test_runner_views.h',
      'tests/cefclient/cefclient_gtk.cc',
    ],
    'cefsimple_sources_common': [
      'tests/cefsimple/simple_app.cc',
      'tests/cefsimple/simple_app.h',
      'tests/cefsimple/simple_handler.cc',
      'tests/cefsimple/simple_handler.h',
    ],
    'cefsimple_sources_win': [
      'tests/cefsimple/cefsimple.exe.manifest',
      'tests/cefsimple/cefsimple.rc',
      'tests/cefsimple/cefsimple_win.cc',
      'tests/cefsimple/simple_handler_win.cc',
      'tests/cefsimple/resource.h',
      'tests/cefsimple/res/cefsimple.ico',
      'tests/cefsimple/res/small.ico',
    ],
    'cefsimple_sources_mac': [
      'tests/cefsimple/cefsimple_mac.mm',
      'tests/cefsimple/simple_handler_mac.mm',
    ],
    'cefsimple_sources_mac_helper': [
      'tests/cefsimple/process_helper_mac.cc',
    ],
    'cefsimple_bundle_resources_mac': [
      'tests/cefsimple/mac/cefsimple.icns',
      'tests/cefsimple/mac/English.lproj/InfoPlist.strings',
      'tests/cefsimple/mac/English.lproj/MainMenu.xib',
      'tests/cefsimple/mac/Info.plist',
    ],
    'cefsimple_sources_linux': [
      'tests/cefsimple/cefsimple_linux.cc',
      'tests/cefsimple/simple_handler_linux.cc',
    ],
    'ceftests_sources_common': [
      'tests/ceftests/browser_info_map_unittest.cc',
      'tests/ceftests/command_line_unittest.cc',
      'tests/ceftests/cookie_unittest.cc',
      'tests/ceftests/dialog_unittest.cc',
      'tests/ceftests/display_unittest.cc',
      'tests/ceftests/dom_unittest.cc',
      'tests/ceftests/download_unittest.cc',
      'tests/ceftests/draggable_regions_unittest.cc',
      'tests/ceftests/extensions/background_unittest.cc',
      'tests/ceftests/extensions/chrome_alarms_unittest.cc',
      'tests/ceftests/extensions/chrome_storage_unittest.cc',
      'tests/ceftests/extensions/chrome_tabs_unittest.cc',
      'tests/ceftests/extensions/extension_test_handler.cc',
      'tests/ceftests/extensions/extension_test_handler.h',
      'tests/ceftests/extensions/view_unittest.cc',
      'tests/ceftests/file_util_unittest.cc',
      'tests/ceftests/frame_unittest.cc',
      'tests/ceftests/image_unittest.cc',
      'tests/ceftests/image_util.cc',
      'tests/ceftests/image_util.h',
      'tests/ceftests/jsdialog_unittest.cc',
      'tests/ceftests/life_span_unittest.cc',
      'tests/ceftests/message_router_unittest.cc',
      'tests/ceftests/navigation_unittest.cc',
      'tests/ceftests/os_rendering_unittest.cc',
      'tests/ceftests/osr_accessibility_unittest.cc',
      'tests/ceftests/osr_display_unittest.cc',
      'tests/ceftests/parser_unittest.cc',
      'tests/ceftests/plugin_unittest.cc',
      'tests/ceftests/preference_unittest.cc',
      'tests/ceftests/print_unittest.cc',
      'tests/ceftests/process_message_unittest.cc',
      'tests/ceftests/request_context_unittest.cc',
      'tests/ceftests/request_handler_unittest.cc',
      'tests/ceftests/request_unittest.cc',
      'tests/ceftests/resource.h',
      'tests/ceftests/resource_manager_unittest.cc',
      'tests/ceftests/routing_test_handler.cc',
      'tests/ceftests/routing_test_handler.h',
      'tests/ceftests/run_all_unittests.cc',
      'tests/ceftests/scheme_handler_unittest.cc',
      'tests/ceftests/scoped_temp_dir_unittest.cc',
      'tests/ceftests/server_unittest.cc',
      'tests/ceftests/stream_unittest.cc',
      'tests/ceftests/stream_resource_handler_unittest.cc',
      'tests/ceftests/string_unittest.cc',
      'tests/ceftests/client_app_delegates.cc',
      'tests/ceftests/task_unittest.cc',
      'tests/ceftests/test_handler.cc',
      'tests/ceftests/test_handler.h',
      'tests/ceftests/test_suite.cc',
      'tests/ceftests/test_suite.h',
      'tests/ceftests/test_util.cc',
      'tests/ceftests/test_util.h',
      'tests/ceftests/thread_helper.cc',
      'tests/ceftests/thread_helper.h',
      'tests/ceftests/thread_unittest.cc',
      'tests/ceftests/tracing_unittest.cc',
      'tests/ceftests/translator_unittest.cc',
      'tests/ceftests/urlrequest_unittest.cc',
      'tests/ceftests/v8_unittest.cc',
      'tests/ceftests/values_unittest.cc',
      'tests/ceftests/version_unittest.cc',
      'tests/ceftests/waitable_event_unittest.cc',
      'tests/ceftests/webui_unittest.cc',
      'tests/ceftests/xml_reader_unittest.cc',
      'tests/ceftests/zip_reader_unittest.cc',
    ],
    'ceftests_sources_views': [
      'tests/ceftests/views/button_unittest.cc',
      'tests/ceftests/views/panel_unittest.cc',
      'tests/ceftests/views/scroll_view_unittest.cc',
      'tests/ceftests/views/test_window_delegate.cc',
      'tests/ceftests/views/test_window_delegate.h',
      'tests/ceftests/views/textfield_unittest.cc',
      'tests/ceftests/views/window_unittest.cc',
    ],
    'ceftests_sources_win': [
      'tests/ceftests/resource_util_win_idmap.cc',
      'tests/ceftests/resources/win/ceftests.exe.manifest',
      'tests/ceftests/resources/win/ceftests.ico',
      'tests/ceftests/resources/win/ceftests.rc',
      'tests/ceftests/resources/win/small.ico',
    ],
    'ceftests_sources_mac': [
      'tests/ceftests/os_rendering_unittest_mac.h',
      'tests/ceftests/os_rendering_unittest_mac.mm',
      'tests/ceftests/run_all_unittests_mac.mm',
    ],
    'ceftests_sources_mac_helper': [
      'tests/shared/browser/file_util.cc',
      'tests/shared/browser/file_util.h',
      'tests/shared/browser/resource_util.h',
      'tests/shared/browser/resource_util_mac.mm',
      'tests/shared/browser/resource_util_posix.cc',
      'tests/ceftests/client_app_delegates.cc',
      'tests/ceftests/cookie_unittest.cc',
      'tests/ceftests/dom_unittest.cc',
      'tests/ceftests/frame_unittest.cc',
      'tests/ceftests/message_router_unittest.cc',
      'tests/ceftests/navigation_unittest.cc',
      'tests/ceftests/plugin_unittest.cc',
      'tests/ceftests/preference_unittest.cc',
      'tests/ceftests/process_message_unittest.cc',
      'tests/ceftests/request_handler_unittest.cc',
      'tests/ceftests/request_unittest.cc',
      'tests/ceftests/routing_test_handler.cc',
      'tests/ceftests/routing_test_handler.h',
      'tests/ceftests/scheme_handler_unittest.cc',
      'tests/ceftests/urlrequest_unittest.cc',
      'tests/ceftests/test_handler.cc',
      'tests/ceftests/test_handler.h',
      'tests/ceftests/test_suite.cc',
      'tests/ceftests/test_suite.h',
      'tests/ceftests/test_util.cc',
      'tests/ceftests/test_util.h',
      'tests/ceftests/thread_helper.cc',
      'tests/ceftests/thread_helper.h',
      'tests/ceftests/thread_unittest.cc',
      'tests/ceftests/tracing_unittest.cc',
      'tests/ceftests/v8_unittest.cc',
    ],
    'ceftests_bundle_resources_mac': [
      'tests/ceftests/resources/mac/ceftests.icns',
      'tests/ceftests/resources/mac/English.lproj/InfoPlist.strings',
      'tests/ceftests/resources/mac/English.lproj/MainMenu.xib',
      'tests/ceftests/resources/mac/Info.plist',
    ],
    'ceftests_sources_linux': [
      'tests/ceftests/resource_util_linux.cc',
    ],
  },
}
