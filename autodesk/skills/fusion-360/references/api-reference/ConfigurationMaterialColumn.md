# ConfigurationMaterialColumn Object

Derived from: [ConfigurationColumn](ConfigurationColumn.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumn.h>

## Description

Represents a material column in the material table. This defines the material to use for a specific component.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationMaterialColumn_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ConfigurationMaterialColumn_deleteMe.htm) | Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail. |
| [getCell](ConfigurationMaterialColumn_getCell.htm) | Gets the cell in this column at the specified row. The first row has an index of 0 and does not include the header row. |
| [getCellByRowId](ConfigurationMaterialColumn_getCellByRowId.htm) | Gets the cell in this column at the row specified by its ID. |
| [getCellByRowName](ConfigurationMaterialColumn_getCellByRowName.htm) | Gets the cell in this column at the row specified by its name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [entity](ConfigurationMaterialColumn_entity.htm) | Returns the Component or BRepBody being modified by this column. This property returns null when the table being queried was obtained from a DataFile object. |
| [id](ConfigurationMaterialColumn_id.htm) | The id of the column. This is constant and cannot be changed by the user. |
| [index](ConfigurationMaterialColumn_index.htm) | The index position of this column within the table. The first column is at index 0 and does not include the "Name" column. |
| [isValid](ConfigurationMaterialColumn_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationMaterialColumn_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentMaterialTable](ConfigurationMaterialColumn_parentMaterialTable.htm) | Returns the parent material table this column is in. |
| [rowCount](ConfigurationMaterialColumn_rowCount.htm) | Returns the number of rows in this column. |
| [title](ConfigurationMaterialColumn_title.htm) | The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.   If the table was obtained from a DataFile, this property behaves as read-only for all the columns. |

## Accessed From

[ConfigurationMaterialCell.parentColumn](ConfigurationMaterialCell_parentColumn.htm), [ConfigurationMaterialColumns.add](ConfigurationMaterialColumns_add.htm), [ConfigurationMaterialColumns.item](ConfigurationMaterialColumns_item.htm), [ConfigurationMaterialColumns.itemById](ConfigurationMaterialColumns_itemById.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |