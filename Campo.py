class Campo:
    def __init__(self, dataType, fieldName, fieldSize):
        self.dataType = dataType
        self.fieldName = fieldName
        self.fieldSize = fieldSize
        self.isRadio = False
        self.isSecondaryKey = False

    def setSecondaryKey(self, key):
        self.isSecondaryKey = key

    def getSecondaryKey(self, key):
        return self.isSecondaryKey
    def setKey(self, radio):
        self.isRadio = radio

    def isKey(self):
        return self.isRadio
    def setDataType(self, dataType):
        self.dataType = dataType

    def getDataType(self):
        return self.dataType

    def setFieldName(self, fieldName):
        self.fieldName = fieldName

    def getFieldName(self):
        return self.fieldName

    def setFieldSize(self, fieldSize):
        self.fieldSize = fieldSize

    def getFieldSize(self):
        return self.fieldSize

    def __str__(self):
        return self.fieldName