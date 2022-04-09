from dataflows import Flow, load, dump_to_path, add_metadata, printer, update_resource, join_with_self
from dataflows import find_replace, delete_fields, set_type, unpivot, update_schema, duplicate


unpivoting_fields = [
    { 'name': '(women|men)_(\d+(-|\+)\d*)', 'keys': {'sex': r'\1', 'age': r'\2'} }
]
extra_keys = [{'name': 'sex', 'type': 'string'}, {'name': 'age', 'type': 'string'}]
extra_value = {'name': 'value', 'type': 'integer'}

def remove_empty(rows):
    for row in rows:
        if row:
            yield row

def demographics():
    flow = Flow(
        # Load inputs
        load("archive/kazakhstan_respublikasy_halkyny1-v4.csv", format='csv', name='regions-age-sex'),
        # Remove empty rows
        remove_empty,
        unpivot(unpivoting_fields, extra_keys, extra_value),
        update_resource('regions-age-sex', path='data/regions-age-sex.csv'),
        # Create total data
        duplicate(
            source='regions-age-sex',
            target_name='regions-total',
            target_path='data/regions-total.csv'
        ),
        join_with_self(
            resource_name='regions-total',
            join_key=['region'],
            fields=dict(
                region={
                    'name': 'region'
                },
                value={
                    'name': 'value',
                    'aggregate': 'sum'
                }
            )
        ),
        # Create data by sex
        duplicate(
            source='regions-age-sex',
            target_name='regions-by-sex',
            target_path='data/regions-by-sex.csv'
        ),
        join_with_self(
            resource_name='regions-by-sex',
            join_key=['region', 'sex'],
            fields=dict(
                region={
                    'name': 'region'
                },
                sex={
                    'name': 'sex'
                },
                value={
                    'name': 'value',
                    'aggregate': 'sum'
                }
            )
        ),
        # Save the results
        add_metadata(name='demographics-kz', title='''Demographics in Kazakhstan by region, age and sex.'''),
        printer(),
        dump_to_path(),
    )
    flow.process()


if __name__ == '__main__':
    demographics()
