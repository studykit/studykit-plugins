# ConfigurationTable Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTable.h>

## Description

The base class of all configuration tables.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationTable_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getCell](ConfigurationTable_getCell.htm) | Returns the cell at the specified row and column. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](ConfigurationTable_id.htm) | Returns the unique ID of this table. |
| [isValid](ConfigurationTable_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationTable_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [rows](ConfigurationTable_rows.htm) | Returns the rows (configurations) defined for this table and provides the functionality to create new rows. |

## Accessed From

[ConfigurationFeatureAspectColumn.parentTable](ConfigurationFeatureAspectColumn_parentTable.htm), [ConfigurationInsertColumn.parentTable](ConfigurationInsertColumn_parentTable.htm), [ConfigurationInsertStandardDesignColumn.parentTable](ConfigurationInsertStandardDesignColumn_parentTable.htm), [ConfigurationJointSnapColumn.parentTable](ConfigurationJointSnapColumn_parentTable.htm), [ConfigurationParameterColumn.parentTable](ConfigurationParameterColumn_parentTable.htm), [ConfigurationPropertyColumn.parentTable](ConfigurationPropertyColumn_parentTable.htm), [ConfigurationRow.parentTable](ConfigurationRow_parentTable.htm), [ConfigurationSuppressColumn.parentTable](ConfigurationSuppressColumn_parentTable.htm), [ConfigurationThemeColumn.parentTable](ConfigurationThemeColumn_parentTable.htm), [ConfigurationThemeColumn.referencedTable](ConfigurationThemeColumn_referencedTable.htm), [ConfigurationVisibilityColumn.parentTable](ConfigurationVisibilityColumn_parentTable.htm)

## Derived Classes

[ConfigurationAppearanceTable](ConfigurationAppearanceTable.htm), [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm), [ConfigurationMaterialTable](ConfigurationMaterialTable.htm), [ConfigurationPlasticRuleTable](ConfigurationPlasticRuleTable.htm), [ConfigurationSheetMetalRuleTable](ConfigurationSheetMetalRuleTable.htm), [ConfigurationTopTable](ConfigurationTopTable.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |