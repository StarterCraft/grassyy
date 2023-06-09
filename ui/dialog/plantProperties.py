from PySide6 import QtWidgets

from ui    import GreenyyUiComponent, GreenyyUiComponentType
from uidef.dialog.plantProperties import Ui_PlantPropertiesDialog


class GreenyyPlantDialog(
    GreenyyUiComponent, 
    QtWidgets.QMainWindow,
    Ui_PlantPropertiesDialog):
    def __init__(self):
        super().__init__(f'plantDialog ({id(self)})', GreenyyUiComponentType.Dialog)
        
        self.logger.debug(f'Инициализирован диалог {self.name}')
