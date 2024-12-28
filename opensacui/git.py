import subprocess


def CloneProject(
    url,
    local_dir,
):
    """Git clone project into sphinx build folder.

    Args:
        url (str): The URL of the repository to clone.
        local_dir (str): The local directory to clone the repository into.

    Returns:
        None

    Raises:
        OSError: If there is an error creating the local directory or cloning the repository.

    Example:
        git.CloneProject(
            "https://github.com/natebass/opensac-ui",
            "../_build/natebass-opensac-ui"
        )
    """
    subprocess.run(["mkdir", "-p", local_dir], check=True)
    subprocess.run(["git", "clone", url, local_dir], check=True)
    print(f"Successfully cloned {url} into {local_dir}")
