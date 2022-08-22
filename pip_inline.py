
## Inline pip examples


## Example 1
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])




## Example 2
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


if __name__ == '__main__':
    install('argh')




## Example 3
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", package])




## Example 4
import sys
import subprocess
import pkg_resources

required  = {'numpy', 'pandas', '<etc>'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])



#### FINAL VERSION
# Try import and install inline if module import fails.
def inline_import(module):
  try:
    return getattr(__import__(module, fromlist=[module]), module)
  except ModuleNotFoundError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])
    return getattr(__import__(module, fromlist=[module]), module)
  except Exception as e:
    print(e)


def inline_from_import(package, module):
  try:
    return getattr(__import__(package, fromlist=[module]), module)
  except ModuleNotFoundError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    return getattr(__import__(package, fromlist=[module]), module)
  except Exception as e:
    print(e)

pandas = inline_import('pandas')
sleep = inline_from_import('time','sleep')