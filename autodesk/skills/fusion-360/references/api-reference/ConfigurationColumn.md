# ConfigurationColumn Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumn.h>

## Description

Represents a column in a configuration table. This is the base class for the more specific column types. The "Name" column is not considered a standard column but is a value associated with each table row.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationColumn_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ConfigurationColumn_deleteMe.htm) | Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](ConfigurationColumn_id.htm) | The id of the column. This is constant and cannot be changed by the user. |
| [index](ConfigurationColumn_index.htm) | The index position of this column within the table. The first column is at index 0 and does not include the "Name" column. |
| [isValid](ConfigurationColumn_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationColumn_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [rowCount](ConfigurationColumn_rowCount.htm) | Returns the number of rows in this column. |
| [title](ConfigurationColumn_title.htm) | The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.   If the table was obtained from a DataFile, this property behaves as read-only for all the columns. |

## Accessed From

[ConfigurationColumns.item](ConfigurationColumns_item.htm), [ConfigurationColumns.itemById](ConfigurationColumns_itemById.htm), [ConfigurationCustomThemeTable.moveColumns](ConfigurationCustomThemeTable_moveColumns.htm), [ConfigurationTopTable.moveColumns](ConfigurationTopTable_moveColumns.htm)

## Derived Classes

[ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm), [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm), [ConfigurationInsertColumn](ConfigurationInsertColumn.htm), [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm), [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm), [ConfigurationParameterColumn](ConfigurationParameterColumn.htm), [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm), [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm), [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm), [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm), [ConfigurationThemeColumn](ConfigurationThemeColumn.htm), [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |