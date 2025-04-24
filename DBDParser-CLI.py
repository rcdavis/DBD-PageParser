import typer
from DBDParser import DBDParser
from pathlib import Path

app = typer.Typer()

@app.command()
def export_survivor_names(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported strings"),
    output_file: str = typer.Option("survivor_name_strings.xml", help="File for exported strings")
):
    """Export survivor names to an Android strings.xml file."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting survivor names to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_survivor_names(strFile)

@app.command()
def export_survivor_perk_names(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported strings"),
    output_file: str = typer.Option("survivor_perk_name_strings.xml", help="File for exported strings")
):
    """Export survivor perk names to an Android strings.xml file."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting survivor perk names to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_survivor_perk_names(strFile)

@app.command()
def export_survivor_perk_descriptions(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported strings"),
    output_file: str = typer.Option("survivor_perk_description_strings.xml", help="File for exported strings")
):
    """Export survivor perk descriptions to an Android strings.xml file."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting survivor perk descriptions to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_survivor_perk_descriptions(strFile)

@app.command()
def export_survivor_enum_class(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported enum class"),
    output_file: str = typer.Option("Survivor.kt", help="File for exported enum class")
):
    """Export survivor enum class."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting survivor enum class to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_survivor_enum_class(strFile)

@app.command()
def export_survivor_perk_list(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported enum class"),
    output_file: str = typer.Option("SurvivorPerksList.kt", help="File for exported enum class")
):
    """Export survivor perk list data class."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting survivor perk list data class to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_survivor_perk_list(strFile)

@app.command()
def export_killer_names(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported strings"),
    output_file: str = typer.Option("killer_name_strings.xml", help="File for exported strings")
):
    """Export killer names to an Android strings.xml file."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting killer names to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_killer_names(strFile)

@app.command()
def export_killer_perk_names(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported strings"),
    output_file: str = typer.Option("killer_perk_name_strings.xml", help="File for exported strings")
):
    """Export killer perk names to an Android strings.xml file."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting killer perk names to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_killer_perk_names(strFile)

@app.command()
def export_killer_perk_descriptions(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported strings"),
    output_file: str = typer.Option("killer_perk_description_strings.xml", help="File for exported strings")
):
    """Export killer perk descriptions to an Android strings.xml file."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting killer perk descriptions to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_killer_perk_descriptions(strFile)

@app.command()
def export_killer_enum_class(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported enum class"),
    output_file: str = typer.Option("Killer.kt", help="File for exported enum class")
):
    """Export killer enum class."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting killer enum class to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_killer_enum_class(strFile)

@app.command()
def export_killer_perk_list(
    output_dir: str = typer.Option("OutputFiles", help="Directory for exported enum class"),
    output_file: str = typer.Option("KillerPerksList.kt", help="File for exported enum class")
):
    """Export killer perk list data class."""
    strFile = Path(output_dir) / output_file
    typer.echo(f"Exporting killer perk list data class to {strFile}")

    parser = DBDParser()
    parser.parse_from_url("https://deadbydaylight.fandom.com/wiki/Perks")
    parser.export_killer_perk_list(strFile)

if __name__ == "__main__":
    app()
