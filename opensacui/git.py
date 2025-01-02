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
        TODO: OSError: If there is an error creating the local directory or cloning the repository.

    Example:
        git.CloneProject(
            "https://github.com/natebass/opensac-ui",
            "../_build/natebass-opensac-ui"
        )
    """
    try:
        subprocess.run(["mkdir", "-p", local_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nError creating directory:\n{e}")

    try:
        subprocess.run(["git", "clone", url, local_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nError cloning repository:\n{e}")
