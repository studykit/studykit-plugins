# ConfigurationParameterCell Object

Derived from: [ConfigurationCell](ConfigurationCell.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterCell.h>

## Description

Represents a single cell within a configuration table that controls the value of a parameter. Get the parent column to get the parameter being controlled.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationParameterCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [expression](ConfigurationParameterCell_expression.htm) | Gets and sets the expression that defines the value of the associated parameter when the parent row is active. This property behaves as read-only when the table is obtained from a DataFile object. |
| [isValid](ConfigurationParameterCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationParameterCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentColumn](ConfigurationParameterCell_parentColumn.htm) | Returns the column this cell is in. From the column, you can get the parameter object being controlled. |
| [parentRow](ConfigurationParameterCell_parentRow.htm) | Returns the row this cell is in. |
| [value](ConfigurationParameterCell_value.htm) | Gets and sets the value of the parameter in database units. You can use the units property of the associated Parameter object, which you can get from the column, to determine the type of units this parameter is defined in. Setting this property will overwrite any existing expression. This property behaves as read-only when the table is obtained from a DataFile object. |

## Accessed From

[ConfigurationParameterColumn.getCell](ConfigurationParameterColumn_getCell.htm), [ConfigurationParameterColumn.getCellByRowId](ConfigurationParameterColumn_getCellByRowId.htm), [ConfigurationParameterColumn.getCellByRowName](ConfigurationParameterColumn_getCellByRowName.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |