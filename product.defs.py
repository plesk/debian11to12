# Copyright 2023-2024. WebPros International GmbH. All rights reserved.
# vim:ft=python:

include_defs('//buck.defs.py')


# Function is necessary, because Buck won't allow
# get_git_revision_description() to be called at the top level of an
# included file due to get_base_path() call inside (so, you can't just
# do REVISION = get_git_revision_description())
def get_deb11to12_revision():
    return get_git_revision_description(dirty=False)


def get_deb11to12_version():
    rev = get_deb11to12_revision()
    return rev.lstrip('v').split('-', 1)[0] if '-' in rev else ''
