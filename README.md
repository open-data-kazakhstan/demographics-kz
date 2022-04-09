Demographics in Kazakhstan by region, age and sex.

## Data

Data is in CSV format and synced with upstream source monthly. It is sourced from https://data.egov.kz/datasets/view?index=kazakstan_respublikasy_halkyny1.

**Note:** Since data.egov.kz requested for a signed key for authorization, we just downloaded and put in directory *archive*. It is temporary solution

We have processed the source data to make it normalized and derived from it several aggregated datasets:

* `data/regions-age-sex.csv` - data by region, age and sex.
* `data/regions-total.csv` - aggregated by region.
* `data/regions-by-sex.csv` - aggregated by region and sex.

We have also added some metadata such as column descriptions and [data packaged it][dp].

[dp]: https://frictionlessdata.io/data-package/

## Preparation

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
![.github/workflows/actions.yml](https://github.com/anuveyatsu/demographics-kz/workflows/.github/workflows/actions.yml/badge.svg?branch=master)

This repository uses [dataflows](https://github.com/datahq/dataflows) to process and normalize the data.

You first need to install the dependencies:

```
pip install -r scripts/requirements.txt
```

Then run the script

```
python scripts/process.py
```

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/
