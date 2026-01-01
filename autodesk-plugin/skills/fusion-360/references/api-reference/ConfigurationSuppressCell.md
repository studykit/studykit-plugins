# ConfigurationSuppressCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSuppressCell.h>

## Description

Represents a single cell within a configuration table that controls if a feature is suppressed. Get the parent column to get the feature being suppressed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationSuppressCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isSuppressed](ConfigurationSuppressCell_isSuppressed.htm) | Specifies if the feature is suppressed or not. This property behaves as read-only when the table is obtained from a DataFile. |
| [isValid](ConfigurationSuppressCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationSuppressCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationSuppressCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationSuppressCell_parentRow.htm) | Returns the row this cell is in. |

## Accessed From

[ConfigurationSuppressColumn.getCell](ConfigurationSuppressColumn_getCell.htm), [ConfigurationSuppressColumn.getCellByRowId](ConfigurationSuppressColumn_getCellByRowId.htm), [ConfigurationSuppressColumn.getCellByRowName](ConfigurationSuppressColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |