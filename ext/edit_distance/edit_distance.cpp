//===- edit_distance.c - Ruby Edit Distance Native Extension ------*- C -*-===//
//
// This source file is part of the edit_distance open source project.
//
// Copyright (c) 2018 J. Morgan Lieberthal
// Licensed under Apache License, Version 2.0
//
//===----------------------------------------------------------------------===//

#include <ruby.h>

#include <algorithm>
#include <memory>

static VALUE mEditDistance;

static VALUE
f_compute_edit_distance(VALUE self, VALUE v_str1, VALUE v_str2,
                        VALUE v_allow_replacements, VALUE v_max)
{
  bool AllowReplacements = RTEST(v_allow_replacements);
  unsigned MaxEditDistance = NUM2UINT(v_max);

  // Get the length of each string
  size_t m = RSTRING_LEN(v_str1);
  size_t n = RSTRING_LEN(v_str2);

  // Get pointers to the string data
  const char *FromStr = RSTRING_PTR(v_str1);
  const char *ToStr = RSTRING_PTR(v_str2);

  // Set up other variables
  const unsigned SmallBufferSize = 64;
  unsigned SmallBuffer[SmallBufferSize];
  std::unique_ptr<unsigned[]> Allocated;
  unsigned *Row = SmallBuffer;

  // allocate storage if we need more than 64 chars
  if (n + 1 > SmallBufferSize) {
    Row = new unsigned[n + 1];
    Allocated.reset(Row);
  }

  // Fill in the row
  for (unsigned i = 1; i <= n; ++i)
    Row[i] = i;

  for (size_t y = 1; y <= m; ++y) {
    Row[0] = static_cast<unsigned>(y);
    unsigned BestThisRow = Row[0];

    unsigned Previous = static_cast<unsigned>(y - 1);
    for (size_t x = 1; x <= n; ++x) {
      int OldRow = Row[x];
      if (AllowReplacements) {
        Row[x] = std::min(Previous + (FromStr[y - 1] == ToStr[x - 1] ? 0u : 1u),
                          std::min(Row[x - 1], Row[x]) + 1);
      } else {
        if (FromStr[y - 1] == ToStr[x - 1])
          Row[x] = Previous;
        else
          Row[x] = std::min(Row[x - 1], Row[x]) + 1;
      }
      Previous = OldRow;
      BestThisRow = std::min(BestThisRow, Row[x]);
    }

    if (MaxEditDistance && BestThisRow > MaxEditDistance)
      return UINT2NUM(MaxEditDistance + 1);
  }

  unsigned Result = Row[n];
  return UINT2NUM(Result);
}

extern "C" void
Init_edit_distance(void)
{
  mEditDistance = rb_define_module("EditDistance");
  rb_define_module_function(mEditDistance, "_compute_edit_distance",
                            (VALUE(*)(...))f_compute_edit_distance, 4);
}
