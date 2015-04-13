// Copyright (c) 2015 The Chromium Embedded Framework Authors. All rights
// reserved. Use of this source code is governed by a BSD-style license that
// can be found in the LICENSE file.
//
// ---------------------------------------------------------------------------
//
// This file was generated by the CEF translator tool. If making changes by
// hand only do so within the body of existing method and function
// implementations. See the translator.README.txt file in the tools directory
// for more information.
//

#ifndef CEF_LIBCEF_DLL_CPPTOC_WEB_PLUGIN_INFO_VISITOR_CPPTOC_H_
#define CEF_LIBCEF_DLL_CPPTOC_WEB_PLUGIN_INFO_VISITOR_CPPTOC_H_
#pragma once

#ifndef USING_CEF_SHARED
#pragma message("Warning: "__FILE__" may be accessed wrapper-side only")
#else  // USING_CEF_SHARED

#include "include/cef_web_plugin.h"
#include "include/capi/cef_web_plugin_capi.h"
#include "libcef_dll/cpptoc/cpptoc.h"

// Wrap a C++ class with a C structure.
// This class may be instantiated and accessed wrapper-side only.
class CefWebPluginInfoVisitorCppToC
    : public CefCppToC<CefWebPluginInfoVisitorCppToC, CefWebPluginInfoVisitor,
        cef_web_plugin_info_visitor_t> {
 public:
  explicit CefWebPluginInfoVisitorCppToC(CefWebPluginInfoVisitor* cls);
  virtual ~CefWebPluginInfoVisitorCppToC() {}
};

#endif  // USING_CEF_SHARED
#endif  // CEF_LIBCEF_DLL_CPPTOC_WEB_PLUGIN_INFO_VISITOR_CPPTOC_H_

