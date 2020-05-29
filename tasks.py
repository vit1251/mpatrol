
from invoke import task

@task
def prepare(c):
    c.run('meson builddir', echo=True, pty=True)

@task(default=True, pre=[prepare])
def build(c):
    c.run('ninja -C builddir', echo=True, pty=True)

@task(pre=[prepare])
def check(c):
    c.run('ninja -C builddir test', echo=True, pty=True)
