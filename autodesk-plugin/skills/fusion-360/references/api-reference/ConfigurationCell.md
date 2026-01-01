# ConfigurationCell Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCell.h>

## Description

Represents a single cell within a configuration table. This is the base class for the type-specific cell objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentRow](ConfigurationCell_parentRow.htm) | Returns the row this cell is in. |

## Accessed From

[ConfigurationAppearanceTable.getCell](ConfigurationAppearanceTable_getCell.htm), [ConfigurationCustomThemeTable.getCell](ConfigurationCustomThemeTable_getCell.htm), [ConfigurationFeatureAspectColumn.getCell](ConfigurationFeatureAspectColumn_getCell.htm), [ConfigurationFeatureAspectColumn.getCellByRowId](ConfigurationFeatureAspectColumn_getCellByRowId.htm), [ConfigurationFeatureAspectColumn.getCellByRowName](ConfigurationFeatureAspectColumn_getCellByRowName.htm), [ConfigurationJointSnapColumn.getCell](ConfigurationJointSnapColumn_getCell.htm), [ConfigurationJointSnapColumn.getCellByRowId](ConfigurationJointSnapColumn_getCellByRowId.htm), [ConfigurationJointSnapColumn.getCellByRowName](ConfigurationJointSnapColumn_getCellByRowName.htm), [ConfigurationMaterialTable.getCell](ConfigurationMaterialTable_getCell.htm), [ConfigurationPlasticRuleTable.getCell](ConfigurationPlasticRuleTable_getCell.htm), [ConfigurationRow.getCellByColumnId](ConfigurationRow_getCellByColumnId.htm), [ConfigurationRow.getCellByColumnIndex](ConfigurationRow_getCellByColumnIndex.htm), [ConfigurationSheetMetalRuleTable.getCell](ConfigurationSheetMetalRuleTable_getCell.htm), [ConfigurationTable.getCell](ConfigurationTable_getCell.htm), [ConfigurationTopTable.getCell](ConfigurationTopTable_getCell.htm)

## Derived Classes

[ConfigurationAppearanceCell](ConfigurationAppearanceCell.htm), [ConfigurationFeatureAspectBooleanCell](ConfigurationFeatureAspectBooleanCell.htm), [ConfigurationFeatureAspectStringCell](ConfigurationFeatureAspectStringCell.htm), [ConfigurationInsertCell](ConfigurationInsertCell.htm), [ConfigurationInsertStandardDesignCell](ConfigurationInsertStandardDesignCell.htm), [ConfigurationJointSnapCell](ConfigurationJointSnapCell.htm), [ConfigurationMaterialCell](ConfigurationMaterialCell.htm), [ConfigurationParameterCell](ConfigurationParameterCell.htm), [ConfigurationPlasticRuleCell](ConfigurationPlasticRuleCell.htm), [ConfigurationPropertyCell](ConfigurationPropertyCell.htm), [ConfigurationSheetMetalRuleCell](ConfigurationSheetMetalRuleCell.htm), [ConfigurationSuppressCell](ConfigurationSuppressCell.htm), [ConfigurationThemeCell](ConfigurationThemeCell.htm), [ConfigurationVisibilityCell](ConfigurationVisibilityCell.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |