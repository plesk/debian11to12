# Copyright 2023-2024. WebPros International GmbH. All rights reserved.
# vim:ft=python:

include_defs('//product.defs.py')


python_binary(
    name = 'debian11to12.pex',
    platform = 'py3',
    build_args = ['--python-shebang', '/usr/bin/env python3'],
    main_module = 'debian11to12.main',
    deps = [
        'dist-upgrader//pleskdistup:lib',
        '//debian11to12:lib',
    ],
)

genrule(
    name = 'debian11to12',
    srcs = [':debian11to12.pex'],
    out = 'debian11to12',
    cmd = 'cp $(location :debian11to12.pex) $OUT && chmod +x $OUT',
)
