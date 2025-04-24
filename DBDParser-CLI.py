import typer
from DBDParser import DBDParser
from pathlib import Path

app = typer.Typer()

@app.command()
def export_survivor_perk_names(
    input_name: str,
    output_dir: str = typer.Option("OutputStrings", help="Directory for exported strings"),
    output_file: str = typer.Option("survivor_perk_name_strings.xml", help="File for exported strings")
):
    """Export survivor perk names to an Android strings.xml file."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting survivor perk names to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_survivor_perk_names(strFile)

if __name__ == "__main__":
    app()
