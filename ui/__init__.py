#coding=utf-8
from PyQt5    import QtCore, QtGui, QtWidgets
from enum     import Enum
from typing   import Any, List, Dict, Tuple, Iterator, Union
from json     import load
from glob     import glob

from greenyy      import GreenyyComponent, GreenyyDirectDict
from greenyy      import deepget
from greenyy      import a, ui, options, hardware


class GreenyyUiTheme(GreenyyDirectDict):
    'Тема интерфейса.'
    def __init__(self, name) -> None:
        super().__init__({'name': name})

        self.read()

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        return iter(zip(
            self.componentList, 
            [self.__dict__[ck] for ck in self.componentList]))

    def read(self) -> None:
        'Чтение темы'
        self.componentList: List[str] = []

        try:
            load(open(f'theme/{self.name}/manifest.json', 'r', encoding = 'utf-8'))
        except:
            raise FileNotFoundError(f'Тема {self.name} не имеет файла manifest.json'
                'или он повреждён')

        with open(f'theme/{self.name}/manifest.json', 'r', encoding = 'utf-8') as f:
            #Прочесть displayName, style
            self.update(load(f))

        for styleSheetFile in glob(f'theme/{self.name}/*.qss'):
            targetName = styleSheetFile.split('\\')[-1][:-4]
            self.componentList.append(targetName)

            with open(styleSheetFile, 'r', encoding = 'utf-8') as f:
                self.update({targetName: f.read()})


class GreenyyUiComponentType(Enum):
    Window = 0
    Dialog = 1
    Widget = 2


class GreenyyUiComponent(GreenyyComponent):
    'Создание униформизма между всеми компонентами интерфейса.'
    def __init__(
            self,
            name: str,
            cmType: GreenyyUiComponentType,
            *args,
            displayName: str = '',
            loggerName: str = '',
            **kwargs
        ):
        super().__init__(
            name, 
            *args,
            displayName = displayName,
            loggerName = loggerName,
            **kwargs
        )

        self.cmType = cmType

        ui().add(self)

        self.setupUi(self)
        self.defaultSize = QtCore.QSize(
            *deepget(
                options().ui,
                f'{self.name}.size',                
                default = (self.minimumSize().width(), self.minimumSize().height())
            )
        )
        self.resize(self.defaultSize)

        self.theme = deepget(options().ui, f'{self.name}.theme', default = 'default')

    def setupUi(self, *args):
        super().setupUi(*args)

    def interconnect(self):
        super().interconnect()

    def bind(self):
        super().bind()

    def updateUi(self):
        super().updateUi()

    def show(self, **kwargs):
        super().show(**kwargs)

    def close(self):
        super().close()

    def isVisible(self) -> bool:
        return super().isVisible()


from .window.general          import GreenyyGeneralWindow
from .window.log              import GreenyyLogWindow
from .window.settings         import GreenyySettingsWindow

from .dialog.deviceProperties import GreenyyDeviceDialog
from .dialog.plantProperties  import GreenyyPlantDialog
from .dialog.ruleItem         import GreenyyRuleItemDialog
from .dialog.ruleProperties   import GreenyyRuleDialog

from .widget.plantWidget      import GreenyyPlantWidget


class GreenyyUi(GreenyyComponent):
    def __init__(self) -> None:
        super().__init__('ui')

        self.components: List[GreenyyUiComponent] = []

    def __getitem__(self, name: str) -> GreenyyUiComponent:
        try:
            return [c for c in self.components if (c.name == name)][0]
        except IndexError:
            raise KeyError(f'Компонент GUI {name} не найден или не зарегистрирован')

    def __iter__(self) -> Iterator[GreenyyUiComponent]:
        return iter(self.components)

    def setupUi(self):
        GreenyyGeneralWindow()
        GreenyySettingsWindow()
        GreenyyLogWindow()

        for c in self: 
            self.logger.debug(f'{c.name} size: {c.size()}')

        self.interconnect()
        self.bind()
        self.loadThemes()
        self.themize()

    def interconnect(self):
        for component in self:
            component.interconnect()

        self.logger.debug(
            'Взаимосвязывание сигналов в интерфейсе выполнено'
        )
        
    def bind(self):
        for component in self:
            component.bind()

        self.logger.debug(
            'Глобальная привязка сочетаний клавиш выполнена'
        )

    def updateUi(self):
        for component in self:
            component.updateUi()

        self.logger.debug(
            'Интерфейс полностью обновлён'
        )

    def show(self):
        for component in self:
            if (component.name in options().ui.keys()):
                self.showComponent(component)

    def showComponent(self, component: GreenyyUiComponent):
        if (options().ui[component.name].get('onLaunch', False)):
            component.show()

            self.logger.debug(
                f'Компонент {component.name} отображён согласно настройкам'
            )

    def add(self, component: GreenyyUiComponent):
        self.components.append(component)
        setattr(self, component.name, component)

        self.logger.debug(
            f'Компонент {component.name} зарегистрирован'
        )

    def remove(self, component: Union[GreenyyUiComponent, str]):
        if (isinstance(component, GreenyyUiComponent)):
            self.components.remove(component)
            delattr(self, component.name)

        if (isinstance(component, str)):
            self.components.remove(self[component.name])
            delattr(self, component)

        self.logger.debug(
            f'Компонент {component.name} недоступен'
        )

    def deviceIntegration(self):
        'todo: убрать'
        self.logWindow.allDevicesAction = QtWidgets.QAction('Все устройства', self.logWindow)
        self.logWindow.allDevicesAction.setCheckable(True)
        self.logWindow.allDevicesAction.setChecked(all(d.logWindow for d in hardware()))
        self.logWindow.allDevicesAction.setData('device')
        self.logWindow.setLoggingSourceActions.addAction(self.logWindow.allDevicesAction)

        self.logWindow.allASCIIAction = QtWidgets.QAction('Все', self.logWindow)
        self.logWindow.allASCIIAction.setCheckable(True)
        self.logWindow.allASCIIAction.setChecked(all(d.decodeASCIIMode for d in hardware()))
        self.logWindow.setASCIIModeActions.addAction(self.logWindow.allASCIIAction)

        for d in hardware():
            self.generalWindow.meiWindow.addAction(d.address)

            self.logWindow.cbbPort.addItem(d.address)
            self.logWindow.cbbPort.setCurrentText(d.address)

            setASCIIModeAction = QtWidgets.QAction(d.address.upper(), self.logWindow)
            setASCIIModeAction.setCheckable(True)
            setASCIIModeAction.setChecked(d.decodeASCII)
            self.logWindow.setASCIIModeActions.addAction(setASCIIModeAction)

            setLoggerVisibilityAction = QtWidgets.QAction(d.address.upper(), self.logWindow)
            setLoggerVisibilityAction.setCheckable(True)
            setLoggerVisibilityAction.setChecked(d.logWindow)
            setLoggerVisibilityAction.setData('device')
            self.logWindow.setLoggingSourceActions.addAction(setLoggerVisibilityAction)

            self.settingsWindow.treeDevices.addTopLevelItem(d.liwDevicesItem)
            
            d.port.readyRead.connect(lambda: self.logWindow.writeDeviceMessage(d))
    
    def loadThemes(self):
        self.themes: List[GreenyyUiTheme] = []

        for themePath in glob('theme/*'):
            themeName = themePath.split('\\')[-1]
            theme = GreenyyUiTheme(themeName)
            self.themes.append(theme)

            self.logger.debug(
                f'Загружена тема {theme.displayName} ({themeName}, '
                f'{len(theme.componentList)} QSS)'
            )

    def getTheme(self, name: str) -> GreenyyUiTheme:
        return [t for t in self.themes if (t.name == name)][0]

    def themize(self):
        appTheme = self.getTheme(
            deepget(options().ui, 'app.theme', 'default')
        )
        
        a().setStyle(appTheme.style)
        a().setStyleSheet(appTheme.app)

        self.logger.debug(f'Тема {appTheme.name}: установлен глобальный QSS длиной {len(appTheme.app)}')
        self.logger.debug(f'Тема {appTheme.name}: установлен глобальный QStyle {appTheme.style}')

        for c in self:
            theme = self.getTheme(
                deepget(options().ui, f'{c.name}.theme', 'default')
            )

            self.logger.debug(f'Тема {theme.name} обнаружена для компонента {c.name}')

            cQss = theme.get(c.name, '')
            c.setStyleSheet(cQss)
            if (cQss):
                self.logger.debug(f'Тема {theme.name}: установлен QSS для {c.name} длиной {len(cQss)}')

            for target, styleSheet in theme:
                subName = '.'.join(target.split('.')[1:])

                if (len(target.split('.')) > 1 and 
                    hasattr(c, subName)):
                    getattr(c, subName).setStyleSheet(styleSheet)

                    self.logger.debug(f'Тема {theme.name}: '
                        f'установлен QSS для {target} длиной {len(theme[target])}'
                    )


    def isVisible(self) -> bool:
        return any(c.isVisible() for c in self.components)
