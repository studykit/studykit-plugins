# ConfigurationPropertyCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyCell.h>

## Description

Represents an individual cell within a configuration table that defines the value of a property.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationPropertyCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationPropertyCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationPropertyCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationPropertyCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationPropertyCell_parentRow.htm) | Returns the row this cell is in. |
| [value](ConfigurationPropertyCell_value.htm) | Gets and sets the value of the property associated with the parent column of this cell. |

## Accessed From

[ConfigurationPropertyColumn.getCell](ConfigurationPropertyColumn_getCell.htm), [ConfigurationPropertyColumn.getCellByRowId](ConfigurationPropertyColumn_getCellByRowId.htm), [ConfigurationPropertyColumn.getCellByRowName](ConfigurationPropertyColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |