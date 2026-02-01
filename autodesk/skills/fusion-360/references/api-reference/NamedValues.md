# NamedValues Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/NamedValues.h>

## Description

Wraps a list of named values.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](NamedValues_add.htm) | Adds a name value pair to the NamedValues object |
| [classType](NamedValues_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](NamedValues_create.htm) | Creates a transient NamedValues object. |
| [getByIndex](NamedValues_getByIndex.htm) | Function that returns the name and ValueInput object of a name value pair by specifying an index number |
| [getValueByName](NamedValues_getValueByName.htm) | Function that returns the ValueInput object of a name value pair by specifying its name |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](NamedValues_count.htm) | Returns the number of name value pairs in this object. |
| [isValid](NamedValues_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](NamedValues_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[NamedValues.create](NamedValues_create.htm), [PostProcessInput.postProperties](PostProcessInput_postProperties.htm), [ToolQuery.criteria](ToolQuery_criteria.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |