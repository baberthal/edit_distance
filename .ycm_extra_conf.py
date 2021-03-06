# Generated by YCM Generator at 2017-10-20 01:27:37.246835

# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RVM_RUBY_DIR = '/Users/morgan/.rvm/rubies/ruby-2.5.1/include/ruby-2.5.0'
XCTOOLCHAIN_DIR = '/Applications/Xcode.app/Contents/Developer' \
        '/Toolchains/XcodeDefault.xctoolchain'

BASE_FLAGS = [
    '-D_DARWIN_C_SOURCE',
    '-D_DARWIN_UNLIMITED_SELECT',
    '-D_REENTRANT',
    '-D_XOPEN_SOURCE',
    '-I{0}/tmp/x86_64-darwin16/edit_distance/2.5.1'.format(PROJECT_ROOT_DIR),
    '-I{0}/ext/edit_distance'.format(PROJECT_ROOT_DIR),
    '-I{0}'.format(RVM_RUBY_DIR),
    '-I{0}/ruby/backward'.format(RVM_RUBY_DIR),
    '-I{0}/x86_64-darwin16'.format(RVM_RUBY_DIR),
    '-I/usr/local/opt/libksba/include',
    '-I/usr/local/opt/libyaml/include',
    '-I/usr/local/opt/openssl@1.1/include',
    '-I/usr/local/opt/readline/include',
    '-isystem',
    '{0}/usr/include/c++/v1'.format(XCTOOLCHAIN_DIR),
    '-isystem',
    '/usr/local/include'.format(XCTOOLCHAIN_DIR),
    '-isystem',
    '{0}/usr/lib/clang/9.1.0/include'.format(XCTOOLCHAIN_DIR),
    '-isystem',
    '{0}/usr/include'.format(XCTOOLCHAIN_DIR),
    '-isystem',
    '/usr/include',
    '-Wall',
    '-Wdeclaration-after-statement',
    '-Wdeprecated-declarations',
    '-Wdivision-by-zero',
    '-Wextra',
    '-Wextra-tokens',
    '-Wimplicit-function-declaration',
    '-Wimplicit-int',
    '-Wno-constant-logical-operand',
    '-Wno-long-long',
    '-Wno-missing-field-initializers',
    '-Wno-parentheses',
    '-Wno-parentheses-equality',
    '-Wno-self-assign',
    '-Wno-tautological-compare',
    '-Wno-unused-parameter',
    '-Wpointer-arith',
    '-Wshorten-64-to-32',
    '-Wunused-variable',
    '-Wwrite-strings',
]


def DirectoryOfThisScript():
    return os.path.dirname(os.path.abspath(__file__))


# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'BASE_FLAGS'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'BASE_FLAGS' list of compilation flags. Notice that YCM itself uses that
# approach.
compilation_database_folder = os.path.join(DirectoryOfThisScript(), 'tmp')

SOURCE_EXTENSIONS = ['.cpp', '.cxx', '.cc', '.c', '.m', '.mm']

if os.path.exists(compilation_database_folder):
    database = ycm_core.CompilationDatabase(compilation_database_folder)
else:
    database = None


def IsHeaderFile(filename):
    extension = os.path.splitext(filename)[1]
    return extension in ['.h', '.hxx', '.hpp', '.hh']


def GetLanguageAndStandardFlagsForFile(filename):
    extension = os.path.splitext(filename)[1]

    if IsHeaderFile(filename) or extension in ['.cpp', '.cxx', '.cc']:
        return (['-x', 'c++'], ['-std=c++14'])
    elif extension == '.m':
        return (['-ObjC'], [])
    elif extension == '.mm':
        return (['-ObjC++'], [])
    else:
        return (['-x', 'c'], ['-std=gnu11'])


def BuildFlagListForFile(filename):
    (lang_flags, std_flags) = GetLanguageAndStandardFlagsForFile(filename)
    final_flags = lang_flags + BASE_FLAGS + std_flags
    return final_flags


def GetCompilationInfoForFile(filename):
    # The compilation_commands.json file generated by CMake does not have
    # entries for header files. So we do our best by asking the db for flags
    # for a corresponding source file, if any. If one exists, the flags for
    # that file should be good enough.
    if IsHeaderFile(filename):
        basename = os.path.splitext(filename)[0]
        for extension in SOURCE_EXTENSIONS:
            replacement_file = basename + extension
            if os.path.exists(replacement_file):
                compilation_info = database.GetCompilationInfoForFile(
                    replacement_file)
                if compilation_info.compiler_flags_:
                    return compilation_info
        return None
    return database.GetCompilationInfoForFile(filename)


def FlagsForFile(filename, **kwargs):
    if not database:
        return {
            'flags': BuildFlagListForFile(filename),
            'include_paths_relative_to_dir': DirectoryOfThisScript()
        }

    compilation_info = GetCompilationInfoForFile(filename)
    if not compilation_info:
        return {
            'flags': BuildFlagListForFile(filename),
            'include_paths_relative_to_dir': DirectoryOfThisScript()
        }

    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object.
    final_flags = list(compilation_info.compiler_flags_)

    return {
        'flags': final_flags,
        'include_paths_relative_to_dir': compilation_info.compiler_working_dir_
    }
