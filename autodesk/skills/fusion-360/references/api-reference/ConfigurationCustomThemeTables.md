# ConfigurationCustomThemeTables Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTables.h>

## Description

Provides access to the custom theme tables associated with a configuration table and provides the functionality to create new custom theme tables.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ConfigurationCustomThemeTables_add.htm) | Creates a new custom theme table using the specified columns. |
| [classType](ConfigurationCustomThemeTables_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ConfigurationCustomThemeTables_item.htm) | A method that returns the specified custom theme table using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ConfigurationCustomThemeTables_count.htm) | Returns the number of custom theme tables associated with the top table. |
| [isValid](ConfigurationCustomThemeTables_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationCustomThemeTables_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ConfigurationTopTable.customThemeTables](ConfigurationTopTable_customThemeTables.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |