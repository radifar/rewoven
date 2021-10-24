"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Rewoven."""


if __name__ == "__main__":
    main(prog_name="rewoven")  # pragma: no cover
