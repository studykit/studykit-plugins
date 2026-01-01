# ConfigurationMaterialCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialCell.h>

## Description

Represents a single cell within a ConfigurationMaterialTable table that controls which material is assigned to a component or body.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationMaterialCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationMaterialCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [material](ConfigurationMaterialCell_material.htm) | Gets and sets the material associated with this cell. When setting this property, the material used must exist in the design. |
| [objectType](ConfigurationMaterialCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationMaterialCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationMaterialCell_parentRow.htm) | Returns the row this cell is in. |

## Accessed From

[ConfigurationMaterialColumn.getCell](ConfigurationMaterialColumn_getCell.htm), [ConfigurationMaterialColumn.getCellByRowId](ConfigurationMaterialColumn_getCellByRowId.htm), [ConfigurationMaterialColumn.getCellByRowName](ConfigurationMaterialColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |