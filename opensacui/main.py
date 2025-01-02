from git import CloneProject
import typer

app = typer.Typer()


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def repo(
    name: str = "https://github.com/natebass/opensac-ui",
    name2: str = "../_build/natebass-opensac-ui",
):
    CloneProject(name, name2)


@app.callback()
def callback():
    """
    A CLI for Open Sacramento UI documentation.
    """


def main(ctx: typer.Context):
    for extra_arg in ctx.args:
        print(f"Got extra arg: {extra_arg}")


if __name__ == "__main__":
    app()
