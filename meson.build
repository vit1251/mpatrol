project('mpatrol', 'c', version: '1.4.8')

src_dir = include_directories('src')

c_args = [
    '-O3', '-fno-inline-functions', '-DMP_THREADS_SUPPORT', '-DTARGET=TARGET_UNIX',
]

# Dependency

c_compiler = meson.get_compiler('c')

bfd_dep = c_compiler.find_library('bfd')

pthread_dep = c_compiler.find_library('pthread')

# Library

sources = [
    'src/list.c',
    'src/tree.c',
    'src/slots.c',
    'src/utils.c',
    'src/memory.c',
    'src/heap.c',
    'src/alloc.c',
    'src/info.c',
    'src/stack.c',
    'src/addr.c',
    'src/strtab.c',
    'src/symbol.c',
    'src/signals.c',
    'src/diag.c',
    'src/option.c',
    'src/leaktab.c',
    'src/profile.c',
    'src/trace.c',
    'src/inter.c',
    'src/malloc.c',
    'src/cplus.c',
    'src/version.c',
    'src/mutex.c'
]

mpatrol = static_library('mpatrol', sources,
        c_args: c_args,
    )
mpatrol_dep = declare_dependency(
        link_with : mpatrol,
        include_directories : src_dir,
    )

#MPAOBJS = mpalloc.o mpfailure.o mpsetfail.o mpmalloc.o mpcalloc.o mpstrdup.o
#   mprealloc.o

#MPLOBJS = dbmalloc.o dmalloc.o heapdiff.o mgauge.o mtrace.o

# Tools

executable('mpatrol', ['src/mpatrol.c', 'src/getopt.c', 'src/version.c'],
        dependencies : [ mpatrol_dep, bfd_dep, pthread_dep, ],
    )

executable('mprof', ['src/mprof.c', 'src/graph.c', 'src/getopt.c', 'src/list.c', 'src/tree.c', 'src/version.c'],
        dependencies : [ mpatrol_dep, bfd_dep, pthread_dep, ],
    )

executable('mptrace', ['src/mptrace.c', 'src/getopt.c', 'src/tree.c', 'src/slots.c', 'src/utils.c', 'src/version.c'],
        dependencies : [ mpatrol_dep, bfd_dep, pthread_dep, ],
    )

executable('mleak', ['src/mleak.c', 'src/getopt.c', 'src/tree.c', 'src/version.c'],
        dependencies : [ mpatrol_dep, bfd_dep, pthread_dep, ],
    )

# Tests

test('Test 1', executable('test1', ['tests/fail/test1.c'],
            include_directories: src_dir,
            dependencies : [ mpatrol_dep, bfd_dep, pthread_dep, ],
        ),
        should_fail: true
    )
