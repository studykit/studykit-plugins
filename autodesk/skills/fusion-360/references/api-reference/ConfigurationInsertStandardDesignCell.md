# ConfigurationInsertStandardDesignCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertStandardDesignCell.h>

## Description

Represents a single cell within a top or custom theme configuration table that controls which design is used for an inserted standard design. Use the parent column to get the occurrence being modified.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationInsertStandardDesignCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationInsertStandardDesignCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationInsertStandardDesignCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationInsertStandardDesignCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationInsertStandardDesignCell_parentRow.htm) | Returns the row this cell is in. |
| [replaceDesign](ConfigurationInsertStandardDesignCell_replaceDesign.htm) | Gets and sets which ConfigurationReplaceDesign object will be used when the row this cell is in is active. When setting this property, only ConfigurationReplaceDesign objects defined for the parent column of this cell can be used. |

## Accessed From

[ConfigurationInsertStandardDesignColumn.getCell](ConfigurationInsertStandardDesignColumn_getCell.htm), [ConfigurationInsertStandardDesignColumn.getCellByRowId](ConfigurationInsertStandardDesignColumn_getCellByRowId.htm), [ConfigurationInsertStandardDesignColumn.getCellByRowName](ConfigurationInsertStandardDesignColumn_getCellByRowName.htm)

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |