APJ_BOARD_ID = '9'
APJ_BOARD_TYPE = 'STM32F427xx'
APJ_TOOL = '/home/mike/Documents/haggis-aero-2019/pixhawk/Tools/scripts/apj_tool.py'
AP_HAL_REL = '../../libraries/AP_HAL_ChibiOS'
AP_HAL_ROOT = '/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/AP_HAL_ChibiOS'
AP_LIBRARIES = ['AP_HAL_ChibiOS', 'AP_UAVCAN', 'modules/uavcan/libuavcan/src/**/*.cpp', 'modules/uavcan/libuavcan_drivers/stm32/driver/src/*.cpp']
AP_LIBRARIES_OBJECTS_KW = {'features': ['ch_ap_library']}
AP_PROGRAM_FEATURES = ['ch_ap_program']
AR = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/bin'
BOARD = 'CubeBlack'
BOARD_MK = '/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/AP_HAL_ChibiOS/hwdef/common/chibios_board.mk'
BOOTLOADER = False
BOOTLOADER_OPTION = ''
BUILDDIR = '/home/mike/Documents/haggis-aero-2019/pixhawk/build/CubeBlack/modules/ChibiOS'
BUILDDIR_REL = 'modules/ChibiOS'
BUILDROOT = '/home/mike/Documents/haggis-aero-2019/pixhawk/build/CubeBlack'
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o', '']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '9', '3')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-Werror=shadow', '-Werror=return-type', '-Werror=unused-result', '-Werror=narrowing', '-Werror=attributes', '-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-u_printf_float', '-Wno-cast-align', '-Wlogical-op', '-Wframe-larger-than=1300', '-fsingle-precision-constant', '-Wno-attributes', '-Wno-error=double-promotion', '-Wno-error=missing-declarations', '-Wno-error=float-equal', '-Wno-error=undef', '-Wno-error=cpp', '-fno-exceptions', '-Wall', '-Wextra', '-Wno-sign-compare', '-Wfloat-equal', '-Wpointer-arith', '-Wmissing-declarations', '-Wno-unused-parameter', '-Werror=array-bounds', '-Wfatal-errors', '-Werror=uninitialized', '-Werror=init-self', '-Wframe-larger-than=1024', '-Werror=unused-but-set-variable', '-Wno-missing-field-initializers', '-Wno-trigraphs', '-fno-strict-aliasing', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-fno-strength-reduce', '-fno-builtin-printf', '-fno-builtin-fprintf', '-fno-builtin-vprintf', '-fno-builtin-vfprintf', '-fno-builtin-puts', '-mno-thumb-interwork', '-mthumb', '--specs=nano.specs', '-specs=nosys.specs', '-DCHIBIOS_BOARD_NAME="CubeBlack"', '-MMD', '-DUAVCAN_STM32_CHIBIOS=1', '-DUAVCAN_STM32_NUM_IFACES=2', '-O3']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CHIBIOS_BOARD_NAME = 'HAL_BOARD_NAME="CubeBlack"'
CHIBIOS_BUILD_FLAGS = 'USE_FATFS=yes CHIBIOS_STARTUP_MK=os/common/startup/ARMCMx/compilers/GCC/mk/startup_stm32f4xx.mk MCU=cortex-m4 ENV_UDEFS=-DCHPRINTF_USE_FLOAT=1 CHIBIOS_PLATFORM_MK=os/hal/ports/STM32/STM32F4xx/platform.mk USE_COPT=-O3'
CHIBIOS_SCRIPTS = '/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/AP_HAL_ChibiOS/hwdef/scripts'
CH_ROOT = '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/ChibiOS'
CH_ROOT_REL = '../../modules/ChibiOS'
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CONFIGURE_FILES = ['/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/extras/c_emscripten.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/c_osx.py', '/usr/lib/python3.5/sitecustomize.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/waf_unit_test.py', '/usr/lib/python3.5/encodings/hex_codec.py', '/usr/lib/python3.5/importlib/_bootstrap.py', '/usr/lib/python3.5/importlib/util.py', '/usr/lib/python3.5/encodings/aliases.py', '/usr/lib/python3.5/collections/abc.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/TaskGen.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/compiler_cxx.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Errors.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Options.py', '/usr/lib/python3.5/pickle.py', '/usr/lib/python3.5/token.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/cxx.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/extras/clang_compilation_database.py', '/usr/lib/python3.5/sre_compile.py', '/usr/lib/python3.5/shutil.py', '/usr/lib/python3.5/_sitebuiltins.py', '/usr/lib/python3.5/weakref.py', '/usr/lib/python3.5/functools.py', '/usr/lib/python3.5/enum.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/icc.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Scripting.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/icpc.py', '/usr/lib/python3.5/abc.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Context.py', '/usr/lib/python3.5/bz2.py', '/usr/lib/python3.5/json/scanner.py', '/usr/lib/python3.5/collections/__init__.py', '/usr/lib/python3.5/json/encoder.py', '/usr/lib/python3.5/re.py', '/usr/lib/python3.5/lib-dynload/_opcode.cpython-35m-x86_64-linux-gnu.so', '/usr/lib/python3.5/ast.py', '/usr/lib/python3.5/signal.py', '/usr/lib/python3.5/io.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Build.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Utils.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/c_preproc.py', '/usr/lib/python3.5/threading.py', '/usr/lib/python3.5/lib-dynload/termios.cpython-35m-x86_64-linux-gnu.so', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waf-light', '/usr/lib/python3.5/platform.py', '/usr/lib/python3.5/os.py', '/usr/lib/python3.5/inspect.py', '/usr/lib/python3.5/dis.py', '/usr/lib/python3.5/lzma.py', '/usr/lib/python3.5/lib-dynload/_bz2.cpython-35m-x86_64-linux-gnu.so', '/usr/lib/python3.5/subprocess.py', '/usr/lib/python3.5/optparse.py', '/usr/lib/python3.5/logging/__init__.py', '/usr/lib/python3.5/traceback.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/extras/__init__.py', '/usr/lib/python3.5/importlib/__init__.py', '/usr/lib/python3.5/locale.py', 'Tools/ardupilotwaf/cxx_checks.py', '/usr/lib/python3.5/xml/__init__.py', '/usr/lib/python3.5/hashlib.py', '/usr/lib/python3.5/fnmatch.py', 'Tools/ardupilotwaf/build_summary.py', '/usr/lib/python3.5/genericpath.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/extras/c_nec.py', '/usr/lib/python3.5/ctypes/_endian.py', '/usr/lib/python3.5/linecache.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/c.py', '/usr/lib/python3.5/tokenize.py', '/usr/lib/python3.5/textwrap.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/ar.py', '/usr/lib/python3.5/encodings/cp437.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Logs.py', '/usr/lib/python3.5/sre_parse.py', 'Tools/ardupilotwaf/git_submodule.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/gxx.py', '/usr/lib/python3.5/encodings/__init__.py', '/usr/lib/python3.5/_sysconfigdata.py', '/usr/lib/python3.5/datetime.py', '/usr/lib/python3.5/xml/etree/ElementPath.py', '/usr/lib/python3.5/imp.py', '/usr/lib/python3.5/copy.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/clangxx.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/compiler_c.py', '/usr/lib/python3.5/sysconfig.py', '/usr/lib/python3.5/importlib/machinery.py', 'Tools/ardupilotwaf/mavgen.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/extras/gccdeps.py', '/usr/lib/python3.5/importlib/_bootstrap_external.py', 'Tools/ardupilotwaf/ap_library.py', '/usr/lib/python3.5/xml/etree/__init__.py', '/usr/lib/python3.5/_compat_pickle.py', '/usr/lib/python3.5/copyreg.py', '/usr/lib/python3.5/reprlib.py', '/usr/lib/python3.5/tarfile.py', 'Tools/ardupilotwaf/boards.py', '/usr/lib/python3.5/gettext.py', '/usr/lib/python3.5/posixpath.py', '/usr/lib/python3.5/lib-dynload/_ctypes.cpython-35m-x86_64-linux-gnu.so', '/usr/lib/python3.5/_bootlocale.py', 'Tools/ardupilotwaf/ap_persistent.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/gcc.py', '/usr/lib/python3.5/struct.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/clang.py', '/usr/lib/python3.5/codecs.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/ConfigSet.py', '/usr/lib/python3.5/shlex.py', '/usr/lib/python3.5/warnings.py', '/usr/lib/python3.5/sre_constants.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/c_aliases.py', '/usr/lib/python3.5/json/decoder.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Configure.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/__init__.py', '/usr/lib/python3.5/ctypes/__init__.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/c_tests.py', '/usr/lib/python3.5/operator.py', '/usr/lib/python3.5/opcode.py', '/usr/lib/python3.5/heapq.py', '/usr/lib/python3.5/site.py', 'Tools/ardupilotwaf/gtest.py', '/usr/lib/python3.5/queue.py', '/usr/lib/python3.5/contextlib.py', 'Tools/ardupilotwaf/toolchain.py', '/usr/lib/python3.5/lib-dynload/_hashlib.cpython-35m-x86_64-linux-gnu.so', '/usr/lib/python3.5/lib-dynload/_lzma.cpython-35m-x86_64-linux-gnu.so', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Node.py', '/usr/lib/python3.5/importlib/abc.py', 'Tools/ardupilotwaf/uavcangen.py', '/usr/lib/python3.5/plat-x86_64-linux-gnu/_sysconfigdata_m.py', '/usr/lib/python3.5/keyword.py', '/usr/lib/python3.5/__future__.py', '/usr/lib/python3.5/random.py', '/usr/lib/python3.5/string.py', '/usr/lib/python3.5/stat.py', 'Tools/ardupilotwaf/static_linking.py', '/usr/lib/python3.5/base64.py', '/usr/lib/python3.5/_compression.py', '/usr/lib/python3.5/_collections_abc.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Runner.py', '/usr/lib/python3.5/encodings/latin_1.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Task.py', 'Tools/ardupilotwaf/chibios.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/c_config.py', '/usr/lib/python3.5/tempfile.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/ccroot.py', '/usr/lib/python3.5/pipes.py', '/usr/lib/python3.5/types.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/ansiterm.py', '/usr/lib/python3.5/xml/etree/ElementTree.py', '/usr/lib/python3.5/encodings/utf_8.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/xlc.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/__init__.py', 'Tools/ardupilotwaf/ardupilotwaf.py', '/usr/lib/python3.5/_weakrefset.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/Tools/python.py', '/usr/lib/python3.5/selectors.py', '/usr/lib/python3.5/json/__init__.py', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/waf/waflib/extras/c_bgxlc.py', '/usr/lib/python3.5/lib-dynload/_json.cpython-35m-x86_64-linux-gnu.so', '/home/mike/Documents/haggis-aero-2019/pixhawk/wscript']
CONFIGURE_HASH = b'@\xd7.\xce\xfe\xf4e*!Bl%B\xbd\x8c\xdd'
CPPPATH_ST = '-I%s'
CPU_FLAGS = ['-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-u_printf_float']
CXX = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-g++']
CXXFLAGS = ['-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Werror=attributes', '-Werror=format-security', '-Werror=enum-compare', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=narrowing', '-Werror=return-type', '-Werror=switch', '-Werror=sign-compare', '-Werror=type-limits', '-Werror=unused-result', '-Werror=shadow', '-Werror=unused-variable', '-Wfatal-errors', '-Wno-trigraphs', '-Werror=unused-but-set-variable', '-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-Werror=shadow', '-Werror=return-type', '-Werror=unused-result', '-Werror=narrowing', '-Werror=attributes', '-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-u_printf_float', '-Wno-cast-align', '-Wlogical-op', '-Wframe-larger-than=1300', '-fsingle-precision-constant', '-Wno-attributes', '-Wno-error=double-promotion', '-Wno-error=missing-declarations', '-Wno-error=float-equal', '-Wno-error=undef', '-Wno-error=cpp', '-fno-exceptions', '-Wall', '-Wextra', '-Wno-sign-compare', '-Wfloat-equal', '-Wpointer-arith', '-Wmissing-declarations', '-Wno-unused-parameter', '-Werror=array-bounds', '-Wfatal-errors', '-Werror=uninitialized', '-Werror=init-self', '-Wframe-larger-than=1024', '-Werror=unused-but-set-variable', '-Wno-missing-field-initializers', '-Wno-trigraphs', '-fno-strict-aliasing', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-fno-strength-reduce', '-fno-builtin-printf', '-fno-builtin-fprintf', '-fno-builtin-vprintf', '-fno-builtin-vfprintf', '-fno-builtin-puts', '-mno-thumb-interwork', '-mthumb', '--specs=nano.specs', '-specs=nosys.specs', '-DCHIBIOS_BOARD_NAME="CubeBlack"', '-fno-rtti', '-fno-threadsafe-statics', '-MMD', '-Wno-error=cast-align', '-DUAVCAN_STM32_CHIBIOS=1', '-DUAVCAN_STM32_NUM_IFACES=2', '-O3']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o', '']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFAULT_PARAMETERS = '/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/AP_HAL_ChibiOS/hwdef/CubeBlack/defaults.parm'
DEFINES = ['SKETCHBOOK="/home/mike/Documents/haggis-aero-2019/pixhawk"', 'AP_SCRIPTING_CHECKS=1', 'CONFIG_HAL_BOARD=HAL_BOARD_CHIBIOS', 'HAVE_OCLOEXEC=0', 'HAVE_STD_NULLPTR_T=0', 'UAVCAN_CPP_VERSION=UAVCAN_CPP03', 'UAVCAN_NO_ASSERTIONS=1', 'UAVCAN_NULLPTR=nullptr']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'HAVE_CMATH_ISNAN': '', 'HAVE_ENDIAN_H': '', '__STDC_FORMAT_MACROS': '', '_GNU_SOURCE': '', 'HAVE_CMATH_ISINF': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', 'WAF_BUILD': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'HAVE_MEMRCHR': '', 'HAVE_BYTESWAP_H': '', 'PYTHONARCHDIR': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'PYTHONDIR': '', 'HAVE_CMATH_ISFINITE': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
DSDL_COMPILER = '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/uavcan/libuavcan/dsdl_compiler'
ENABLE_ASSERTS = False
ENABLE_GCCDEPS = ['c', 'cxx']
ENABLE_HEADER_CHECKS = False
FLASH_RESERVE_START_KB = '16'
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['ChibiOS', 'mavlink']
HAL_WITH_UAVCAN = '1'
HAS_GTEST = False
HAVE_CMATH_ISFINITE = 1
HAVE_CMATH_ISINF = 1
HAVE_CMATH_ISNAN = 1
HAVE_INTEL_HEX = False
HAVE_MEMRCHR = 1
HWDEF = '/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/AP_HAL_ChibiOS/hwdef/CubeBlack/hwdef.dat'
INCLUDES = ['/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/', '/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/AP_Common/missing', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/uavcan/libuavcan/include', '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/uavcan/libuavcan_drivers/stm32/driver/include']
IOMCU_FW = 0
LIB = ['gcc', 'm']
LIBDIR = '/usr/lib'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m4', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-u_printf_float', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-u_port_lock', '-u_port_unlock', '-u_exit', '-u_kill', '-u_getpid', '-u_errno', '-uchThdExit', '-fno-common', '-nostartfiles', '-mno-thumb-interwork', '-mthumb', '-specs=nano.specs', '-specs=nosys.specs', '-L/home/mike/Documents/haggis-aero-2019/pixhawk/build/CubeBlack', '-L/home/mike/Documents/haggis-aero-2019/pixhawk/modules/ChibiOS/os/common/startup/ARMCMx/compilers/GCC/ld', '-L/home/mike/Documents/haggis-aero-2019/pixhawk/libraries/AP_HAL_ChibiOS/hwdef/common', '-Wl,--gc-sections,--no-warn-mismatch,--library-path=/ld,--script=ldscript.ld,--defsym=__process_stack_size__=0x2000,--defsym=__main_stack_size__=0x400']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-gcc']
LINK_CXX = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-g++']
MAIN_STACK = '0x400'
MAKE = ['/usr/bin/make']
MAVLINK_DIR = '/home/mike/Documents/haggis-aero-2019/pixhawk/modules/mavlink'
MKFW_TOOLS = '/home/mike/Documents/haggis-aero-2019/pixhawk/Tools/ardupilotwaf'
NEED_CMATH_ISFINITE_STD_NAMESPACE = 1
NEED_CMATH_ISINF_STD_NAMESPACE = 1
NEED_CMATH_ISNAN_STD_NAMESPACE = 1
OBJCOPY = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-objcopy']
OPTIMIZE = '-O3'
OPTIONS = {'all_tests': False, 'pyc': 1, 'bootloader': False, 'program_group': [], 'default_parameters': None, 'no_lock_in_top': '', 'static': False, 'enable_header_checks': False, 'clear_failed_tests': False, 'rsync_dest': '', 'enable_sfml': False, 'files': '', 'progress_bar': 0, 'whelp': 0, 'clean_all_sigs': None, 'colors': 'auto', 'dump_test_scripts': False, 'autoconfig': True, 'testcmd': False, 'toolchain': None, 'enable_lttng': False, 'lcov_report': False, 'pythondir': None, 'check_c_compiler': None, 'prefix': '/usr', 'submodule_update': True, 'no_lock_in_run': '', 'jobs': 8, 'upload': None, 'enable_math_check_indexes': False, 'nopycache': None, 'debug': False, 'pdb': 0, 'sitl_flash_storage': False, 'disable_libiio': False, 'enable_gcov': False, 'verbose': 0, 'bindir': None, 'apstatedir': '', 'enable_sfml_audio': False, 'use_nuttx_iofw': False, 'libdir': None, 'python': None, 'destdir': '', 'keep': 0, 'pyo': 1, 'top': '', 'scripting_checks': True, 'disable_gccdeps': False, 'targets': '', 'enable_asserts': False, 'check_verbose': None, 'board': 'CubeBlack', 'check_cxx_compiler': None, 'no_tests': False, 'profile': 0, 'enable_scripting': False, 'enable_benchmarks': False, 'force': False, 'distcheck_args': None, 'zones': '', 'summary_all': None, 'no_lock_in_out': '', 'out': '', 'pythonarchdir': None, 'disable_tests': False}
PREFIX = '/usr'
PROCESS_STACK = '0x2000'
PT_DIR = '/home/mike/Documents/haggis-aero-2019/pixhawk/Tools/ardupilotwaf/chibios/image'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-35'
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/lib/python3/dist-packages'
PYTHONDIR = '/usr/lib/python3/dist-packages'
PYTHON_VERSION = '3.5'
ROMFS_FILES = [('io_firmware.bin', 'Tools/IO_Firmware/fmuv2_IO.bin'), ('bootloader.bin', '/home/mike/Documents/haggis-aero-2019/pixhawk/Tools/bootloaders/CubeBlack_bl.bin')]
RPATH_ST = '-Wl,-rpath,%s'
RSYNC = ['/usr/bin/rsync']
SERIAL_PORT = '/home/mike/Documents/haggis-aero-2019/pixhawk/dev/serial/by-id/*_STLink*'
SHLIB_MARKER = '-Wl,-Bdynamic'
SIZE = ['/opt/gcc-arm-none-eabi-4_9-2015q3/bin/arm-none-eabi-size']
SONAME_ST = '-Wl,-h,%s'
SRCROOT = '/home/mike/Documents/haggis-aero-2019/pixhawk'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = True
TOOLCHAIN = 'arm-none-eabi'
TOOLS_SCRIPTS = '/home/mike/Documents/haggis-aero-2019/pixhawk/Tools/scripts'
UPLOAD_TOOLS = '/home/mike/Documents/haggis-aero-2019/pixhawk/Tools/scripts'
USE_NUTTX_IOFW = False
cfg_files = ['/home/mike/Documents/haggis-aero-2019/pixhawk/build/CubeBlack/ap_config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
macbundle_PATTERN = '%s.bundle'
