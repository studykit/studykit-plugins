# ConfigurationRows Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRows.h>

## Description

Returns a collection of the rows in the table. The header row is not included in this list.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ConfigurationRows_add.htm) | Adds a new row to the table. For the top table, this creates a new configuration. For theme tables, this creates a new theme. The new row is added to the bottom of the table, and the cell values are copied from the row above it. You can also use the ConfigurationRow.copy method to create a new row by copying any existing row. |
| [classType](ConfigurationRows_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ConfigurationRows_item.htm) | A method that returns the specified row using an index into the collection. These are returned in the same order as in the table; the first row is the default row. |
| [itemById](ConfigurationRows_itemById.htm) | A method that returns the row with the specified ID. |
| [itemByName](ConfigurationRows_itemByName.htm) | A method that returns the row with the specified name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ConfigurationRows_count.htm) | Returns the number of rows in the table where the header row is not included. |
| [isValid](ConfigurationRows_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationRows_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ConfigurationAppearanceTable.rows](ConfigurationAppearanceTable_rows.htm), [ConfigurationCustomThemeTable.rows](ConfigurationCustomThemeTable_rows.htm), [ConfigurationMaterialTable.rows](ConfigurationMaterialTable_rows.htm), [ConfigurationPlasticRuleTable.rows](ConfigurationPlasticRuleTable_rows.htm), [ConfigurationSheetMetalRuleTable.rows](ConfigurationSheetMetalRuleTable_rows.htm), [ConfigurationTable.rows](ConfigurationTable_rows.htm), [ConfigurationTopTable.rows](ConfigurationTopTable_rows.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |