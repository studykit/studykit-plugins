# ConfigurationVisibilityCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityCell.h>

## Description

Represents a single cell within a configuration table that controls whether an entity is visible. Get the parent column to get the entity.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationVisibilityCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationVisibilityCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](ConfigurationVisibilityCell_isVisible.htm) | Specifies if the entity is visible or not. This property behaves as read-only when the table is obtained from a DataFile. |
| [objectType](ConfigurationVisibilityCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationVisibilityCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationVisibilityCell_parentRow.htm) | Returns the row this cell is in. |

## Accessed From

[ConfigurationVisibilityColumn.getCell](ConfigurationVisibilityColumn_getCell.htm), [ConfigurationVisibilityColumn.getCellByRowId](ConfigurationVisibilityColumn_getCellByRowId.htm), [ConfigurationVisibilityColumn.getCellByRowName](ConfigurationVisibilityColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |