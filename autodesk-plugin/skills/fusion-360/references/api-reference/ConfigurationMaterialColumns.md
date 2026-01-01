# ConfigurationMaterialColumns Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumns.h>

## Description

Provides access to the columns in a material table. This collection can be empty when no columns have been created. When the table is empty, it is not displayed in the user interface, and adding a column causes the table to be displayed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ConfigurationMaterialColumns_add.htm) | Adds a new column to the material table. If you are adding the first column to the table and it is anything other than the root component, an additional column for the root component will automatically be created as the first column. |
| [classType](ConfigurationMaterialColumns_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ConfigurationMaterialColumns_item.htm) | A method that returns the specified column using an index into the collection. These are returned in the same order as they appear in the table. |
| [itemById](ConfigurationMaterialColumns_itemById.htm) | A method that returns the column with the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ConfigurationMaterialColumns_count.htm) | Returns the number of columns in the table where the name column is not included. |
| [isValid](ConfigurationMaterialColumns_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationMaterialColumns_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ConfigurationMaterialTable.columns](ConfigurationMaterialTable_columns.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |