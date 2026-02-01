# ConfigurationVisibilityColumn Object

Derived from: [ConfigurationColumn](ConfigurationColumn.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityColumn.h>

## Description

Represents a visibility column in a top or custom theme configuration table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationVisibilityColumn_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ConfigurationVisibilityColumn_deleteMe.htm) | Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail. |
| [getCell](ConfigurationVisibilityColumn_getCell.htm) | Gets the cell in this column at the specified row. The first row has an index of 0 and does not include the header row. |
| [getCellByRowId](ConfigurationVisibilityColumn_getCellByRowId.htm) | Gets the cell in this column at the row specified by its ID. |
| [getCellByRowName](ConfigurationVisibilityColumn_getCellByRowName.htm) | Gets the cell in this column at the row specified by its name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [entity](ConfigurationVisibilityColumn_entity.htm) | Returns the entity whose visibility is being controlled by this column. |
| [id](ConfigurationVisibilityColumn_id.htm) | The id of the column. This is constant and cannot be changed by the user. |
| [index](ConfigurationVisibilityColumn_index.htm) | The index position of this column within the table. The first column is at index 0 and does not include the "Name" column. |
| [isValid](ConfigurationVisibilityColumn_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationVisibilityColumn_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentTable](ConfigurationVisibilityColumn_parentTable.htm) | Returns the parent table, either top or custom theme table, this column is in. |
| [rowCount](ConfigurationVisibilityColumn_rowCount.htm) | Returns the number of rows in this column. |
| [title](ConfigurationVisibilityColumn_title.htm) | The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.   If the table was obtained from a DataFile, this property behaves as read-only for all the columns. |

## Accessed From

[ConfigurationColumns.addVisibilityColumn](ConfigurationColumns_addVisibilityColumn.htm), [ConfigurationVisibilityCell.parentColumn](ConfigurationVisibilityCell_parentColumn.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |