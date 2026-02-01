# ConfigurationThemeCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationThemeCell.h>

## Description

Represents an individual cell within a top configuration table that specifies which row in the custom theme table should be used.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationThemeCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationThemeCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationThemeCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationThemeCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationThemeCell_parentRow.htm) | Returns the row this cell is in. |
| [referencedTableRow](ConfigurationThemeCell_referencedTableRow.htm) | Gets and sets the row to use from the referenced table. |

## Accessed From

[ConfigurationThemeColumn.getCell](ConfigurationThemeColumn_getCell.htm), [ConfigurationThemeColumn.getCellByRowId](ConfigurationThemeColumn_getCellByRowId.htm), [ConfigurationThemeColumn.getCellByRowName](ConfigurationThemeColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |