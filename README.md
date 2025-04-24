# DBD Page Parser
Script for parsing a web page so that I don't have to physically insert perk text.

## Setup

### Windows (Powershell)
Start by creating a virtual environment for Python:
```powershell
python -m venv venv
```

Then activate the virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

Then install requirements:
```powershell
pip install -r requirements.txt
```

## Running Program

All data can be exported via the `export-all` command:
```powershell
python .\DBDParser-CLI.py export-all
```

## Commands

- `export-all` Exports all data.
- `export_perk_icons` Exports all perks icon images.
- `export-survivor-names` Exports the survivors names to an Android strings file.
- `export-survivor-perk-names` Exports the survivor perks names to an Android strings file.
- `export-survivor-perk-descriptions` Exports the survivor perks descriptions to an Android strings file.
- `export-survivor-enum-class` Exports the survivors to a Kotlin enum class.
- `export-survivor-perk-list` Exports all survivor perks to a Kotlin list.
- `export-survivor-perk-icons` Exports all survivor perks icon images.
- `export-killer-names` Exports the killers names to an Android strings file.
- `export-killer-perk-names` Exports the killer perks names to an Android strings file.
- `export-killer-perk-descriptions` Exports the killer perks descriptions to an Android strings file.
- `export-killer-enum-class` Exports the killers to a Kotlin enum class.
- `export-killer-perk-list` Exports all killer perks to a Kotlin list.
- `export-killer-perk-icons` Exports all killer perks icon images.

## Links

[Perk website being parsed](https://deadbydaylight.fandom.com/wiki/Perks)
