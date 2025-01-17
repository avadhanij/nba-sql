import requests

from utils import get_rowset_mapping, column_names_from_table
from constants import headers


class GenericRequester:

    def __init__(self, settings, url, table):
        """
        Constructor.
        """
        self.settings = settings
        self.url = url
        self.table = table
        self.settings.db.bind([self.table])
        # Okay without this variables bleed inbetween requesters that inherit
        # this base class. Why does that happen?
        self.rows = []

    def create_ddl(self):
        """
        Initialize the table schema.
        """
        self.settings.db.create_tables([self.table], safe=True)

    def generate_rows(self, input_id, params):
        """
        Build GET REST request and fill the table.
        """

        # json response
        response = requests.get(url=self.url, headers=headers, params=params).json()

        result_sets = response['resultSets'][0]
        rowset = result_sets['rowSet']

        column_names = column_names_from_table(self.settings.db, self.table._meta.table_name)

        column_mapping = get_rowset_mapping(result_sets, column_names)

        for row in rowset:
            new_row = {column_name: row[row_index] for column_name, row_index in column_mapping.items()}
            self.rows.append(new_row)

    def populate(self):
        """
        Bulk insert.
        """
        self.table.insert_many(self.rows).execute()
