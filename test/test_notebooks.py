import glob
import os
import shutil
from pathlib import Path

import pytest


def included_notebooks():
    include = ['.']
    files = []
    for folder in include:
        files += glob.glob(os.path.join(folder, '*.ipynb'))
    return sorted(files)


@pytest.fixture(params=included_notebooks(), scope='module')
def notebook(request):
#    reset_folders = ('examples/pleasant_lgr',
#                     )
#    for folder in reset_folders:
#        root = Path(project_root_path)
#        abspath = os.path.normpath(os.path.join(project_root_path, folder))
#        # make double sure the path is within the project before deleting it
#        if os.path.isdir(abspath) and root in Path(abspath).parents:
#            print('removing output folder {}'.format(abspath))
#            shutil.rmtree(abspath)
    return request.param


@pytest.fixture(scope='session')
def kernel_name():
    """Pick a Jupyter Notebook kernel from the ones available.
    """
    import jupyter_client
    M = jupyter_client.kernelspec.KernelSpecManager()
    specs = M.find_kernel_specs()

    # try using the first one of these kernels that is found
    try_kernel_names = ['flopy_example', 'gis']
    for name in try_kernel_names:
        if name in specs:
            return name
    # otherwise use the first kernel listed in specs
    return list(specs.keys())[0]

def test_notebook(kernel_name, notebook):
    # run autotest on each notebook
    #notebook = os.path.join('.', notebook)
    path, fname = os.path.split(notebook)

    # save the rendered notebook to the documentation folder
    # so that nbsphinx can render it in the docs
    # the docs get built when the tests are run on travis
    # so successful execution of this test will build the notebooks for the docs
    output_folder = 'docs/source/notebooks'

    cmd = ('jupyter ' + 'nbconvert '
           '--ExecutePreprocessor.timeout=600 '
           '--ExecutePreprocessor.kernel_name={} '.format(kernel_name) +
           '--to ' + 'notebook '
           '--execute ' + '{} '.format(notebook) +
           '--output-dir ' + '{} '.format(output_folder) +
           '--output ' + '{}'.format(fname))
    ival = os.system(cmd)
    assert ival == 0, 'could not run {}'.format(os.path.abspath(notebook))
