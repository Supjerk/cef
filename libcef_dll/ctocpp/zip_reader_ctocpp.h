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

#ifndef CEF_LIBCEF_DLL_CTOCPP_ZIP_READER_CTOCPP_H_
#define CEF_LIBCEF_DLL_CTOCPP_ZIP_READER_CTOCPP_H_
#pragma once

#ifndef USING_CEF_SHARED
#pragma message("Warning: "__FILE__" may be accessed wrapper-side only")
#else  // USING_CEF_SHARED

#include "include/cef_zip_reader.h"
#include "include/capi/cef_zip_reader_capi.h"
#include "libcef_dll/ctocpp/ctocpp.h"

// Wrap a C structure with a C++ class.
// This class may be instantiated and accessed wrapper-side only.
class CefZipReaderCToCpp
    : public CefCToCpp<CefZipReaderCToCpp, CefZipReader, cef_zip_reader_t> {
 public:
  explicit CefZipReaderCToCpp(cef_zip_reader_t* str)
      : CefCToCpp<CefZipReaderCToCpp, CefZipReader, cef_zip_reader_t>(str) {}
  virtual ~CefZipReaderCToCpp() {}

  // CefZipReader methods
  virtual bool MoveToFirstFile() OVERRIDE;
  virtual bool MoveToNextFile() OVERRIDE;
  virtual bool MoveToFile(const CefString& fileName,
      bool caseSensitive) OVERRIDE;
  virtual bool Close() OVERRIDE;
  virtual CefString GetFileName() OVERRIDE;
  virtual int64 GetFileSize() OVERRIDE;
  virtual time_t GetFileLastModified() OVERRIDE;
  virtual bool OpenFile(const CefString& password) OVERRIDE;
  virtual bool CloseFile() OVERRIDE;
  virtual int ReadFile(void* buffer, size_t bufferSize) OVERRIDE;
  virtual int64 Tell() OVERRIDE;
  virtual bool Eof() OVERRIDE;
};

#endif  // USING_CEF_SHARED
#endif  // CEF_LIBCEF_DLL_CTOCPP_ZIP_READER_CTOCPP_H_

