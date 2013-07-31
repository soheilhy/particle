#
# Copyright (C) 2013, The Packet project authors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# The GNU General Public License is contained in the file LICENSE.
#

{
  'targets': [
    {
      'target_name': 'particle',
      'type': 'none',
      'variables': {
        'particle_home': '<(cpp_src_dir)/particle',
      },
      'all_dependent_settings': {
        'include_dirs': [
          '<(particle_home)',
        ],
      },
      'dependencies': [
        '<(particle_home)/particle.gyp:headers',
        '<(particle_home)/particle.gyp:signal',
        '<(particle_home)/particle.gyp:typename',
        '<(cpp_src_dir)/third_party/folly.gyp:folly',
        '<(cpp_src_dir)/third_party/sparsehash.gyp:sparsehash',
      ],
      'sources': [
        'commons.gypi',
      ],
    },
    {
      'target_name': 'particle_testlib',
      'type': 'none',
      'dependencies': [
        '<(cpp_src_dir)/third_party/gtest.gyp:gtest',
        '<(cpp_src_dir)/third_party/gmock.gyp:gmock',
      ],
    },
    {
      'target_name': 'particle_testrunner',
      'type': 'none',
      'dependencies': [
        '<(cpp_src_dir)/third_party/gtest.gyp:gtest_main',
      ],
    },
    {
      'target_name': 'particle_tests',
      'type': 'none',
      'variables': {
        'particle_home': '<(cpp_src_dir)/particle',
      },
      'dependencies': [
        '<(particle_home)/particle.gyp:particle_unittests',
      ],
    },
  ]
}

