# ConfigurationAppearanceTable Object

Derived from: [ConfigurationTable](ConfigurationTable.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceTable.h>

## Description

Represents a configuration table that defines the appearances assigned to bodies and components.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationAppearanceTable_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clear](ConfigurationAppearanceTable_clear.htm) | Clears the content of the appearance table, removes the reference from the top table, and hides it in the user interface. |
| [getCell](ConfigurationAppearanceTable_getCell.htm) | Returns the cell at the specified row and column. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [columns](ConfigurationAppearanceTable_columns.htm) | Returns the collection that provides access to this table's columns and the ability to create new columns. |
| [id](ConfigurationAppearanceTable_id.htm) | Returns the unique ID of this table. |
| [isValid](ConfigurationAppearanceTable_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ConfigurationAppearanceTable_name.htm) | Returns the name of the table as seen in the user interface. |
| [objectType](ConfigurationAppearanceTable_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentTableColumn](ConfigurationAppearanceTable_parentTableColumn.htm) | Returns the column in the top table that references this appearance table. |
| [rows](ConfigurationAppearanceTable_rows.htm) | Returns the rows (configurations) defined for this table and provides the functionality to create new rows. |

## Accessed From

[ConfigurationAppearanceColumn.parentAppearanceTable](ConfigurationAppearanceColumn_parentAppearanceTable.htm), [ConfigurationTopTable.appearanceTable](ConfigurationTopTable_appearanceTable.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |