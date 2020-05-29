
from invoke import task

@task(default=True)
def build(c):
    c.run('meson builddir', echo=True, pty=True)
    c.run('ninja -C builddir', echo=True, pty=True)
