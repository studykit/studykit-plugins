# ConfigurationInsertCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertCell.h>

## Description

Represents a single cell within a top or custom theme configuration table that controls which configuration is used for an inserted configured design. Use the parent column to get the feature being suppressed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationInsertCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationInsertCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationInsertCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationInsertCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationInsertCell_parentRow.htm) | Returns the row this cell is in. |
| [row](ConfigurationInsertCell_row.htm) | Gets and sets which row of the configured design is used for this cell. When setting this property, the row must come from the configured design used by the occurrence associated with the parent column of this cell. |

## Accessed From

[ConfigurationInsertColumn.getCell](ConfigurationInsertColumn_getCell.htm), [ConfigurationInsertColumn.getCellByRowId](ConfigurationInsertColumn_getCellByRowId.htm), [ConfigurationInsertColumn.getCellByRowName](ConfigurationInsertColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |