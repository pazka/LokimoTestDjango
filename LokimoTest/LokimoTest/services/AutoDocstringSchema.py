import yaml
from rest_framework.schemas.openapi import AutoSchema


class AutoDocstringSchema(AutoSchema):
    @property
    def documentation(self):
        if not hasattr(self, "_documentation"):
            try:
                self._documentation = yaml.safe_load(self.view.__doc__)
            except yaml.scanner.ScannerError:
                self._documentation = {}
        return self._documentation

    def get_components(self, path, method):
        components = super().get_components(path, method)
        doc_components = self.documentation.get("components", {})
        components.update(doc_components)
        return components

    def get_operation(self, path, method):
        operation = super().get_operation(path, method)
        doc_operation = self.documentation.get(method.lower(), {})
        operation.update(doc_operation)
        return operation
