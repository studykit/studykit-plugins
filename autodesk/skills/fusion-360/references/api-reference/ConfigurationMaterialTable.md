# ConfigurationMaterialTable Object

Derived from: [ConfigurationTable](ConfigurationTable.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialTable.h>

## Description

Represents a configuration table that defines materials assigned to bodies and components.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationMaterialTable_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clear](ConfigurationMaterialTable_clear.htm) | Clears the content of the material table, removes the reference from the top table, and hides it in the user interface. |
| [getCell](ConfigurationMaterialTable_getCell.htm) | Returns the cell at the specified row and column. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [columns](ConfigurationMaterialTable_columns.htm) | Returns the collection that provides access to the columns in this table. |
| [id](ConfigurationMaterialTable_id.htm) | Returns the unique ID of this table. |
| [isValid](ConfigurationMaterialTable_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ConfigurationMaterialTable_name.htm) | Returns the name of the table as seen in the user interface. |
| [objectType](ConfigurationMaterialTable_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentTableColumn](ConfigurationMaterialTable_parentTableColumn.htm) | Returns the column in the top table that references this material table. |
| [rows](ConfigurationMaterialTable_rows.htm) | Returns the rows (configurations) defined for this table and provides the functionality to create new rows. |

## Accessed From

[ConfigurationMaterialColumn.parentMaterialTable](ConfigurationMaterialColumn_parentMaterialTable.htm), [ConfigurationTopTable.materialTable](ConfigurationTopTable_materialTable.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |