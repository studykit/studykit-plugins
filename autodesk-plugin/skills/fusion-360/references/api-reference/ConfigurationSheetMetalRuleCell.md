# ConfigurationSheetMetalRuleCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleCell.h>

## Description

Represents a single cell within a configuration table that controls which sheet metal rule is assigned to a component.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationSheetMetalRuleCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationSheetMetalRuleCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationSheetMetalRuleCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationSheetMetalRuleCell_parentColumn.htm) | Returns the column this cell is in. |
| [parentRow](ConfigurationSheetMetalRuleCell_parentRow.htm) | Returns the row this cell is in. |
| [sheetMetalRule](ConfigurationSheetMetalRuleCell_sheetMetalRule.htm) | Gets and sets the sheet metal rule defined for this cell. |

## Accessed From

[ConfigurationSheetMetalRuleColumn.getCell](ConfigurationSheetMetalRuleColumn_getCell.htm), [ConfigurationSheetMetalRuleColumn.getCellByRowId](ConfigurationSheetMetalRuleColumn_getCellByRowId.htm), [ConfigurationSheetMetalRuleColumn.getCellByRowName](ConfigurationSheetMetalRuleColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |