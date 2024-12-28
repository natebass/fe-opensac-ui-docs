from opensacui import git


def test_clone_project():
    git.CloneProject(
        "https://github.com/natebass/opensac-ui",
        "/home/nwb/Source/Repos/opensac-ui-docs/_build/natebass-opensac-ui",
    )
