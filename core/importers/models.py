import json

from ocldev.oclfleximporter import OclFlexImporter

from core.common.utils import get_base_url
from core.users.models import UserProfile


class ImportResults:  # pragma: no cover
    def __init__(self, importer):
        self.json = json.loads(importer.import_results.to_json())
        self.detailed_summary = importer.import_results.get_detailed_summary()
        self.report = importer.import_results.display_report()


class BulkImport:  # pragma: no cover
    def __init__(self, content, username, update_if_exists):
        self.input_list = []
        self.user = None
        self.result = None
        self.importer = None
        self.content = content
        self.username = username
        self.update_if_exists = update_if_exists
        self.populate_input_list()
        self.set_user()
        self.initialize_importer()

    def populate_input_list(self):
        for line in self.content.splitlines():
            self.input_list.append(json.loads(line))

    def set_user(self):
        self.user = UserProfile.objects.get(username=self.username)

    def initialize_importer(self):
        self.importer = OclFlexImporter(
            input_list=self.input_list,
            api_url_root=get_base_url(),
            api_token=self.user.get_token(),
            do_update_if_exists=self.update_if_exists
        )

    def run(self):
        self.importer.process()
        self.result = ImportResults(self.importer)
