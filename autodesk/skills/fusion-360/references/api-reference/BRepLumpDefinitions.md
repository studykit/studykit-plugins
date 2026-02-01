# BRepLumpDefinitions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLumpDefinitions.h>

## Description

Provides access to the BRepLumpDefinition objects associated with the BRepBodyDefinition and it's through this object that you create new BRepLumpDefinition objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BRepLumpDefinitions_add.htm) | Creates a new empty BRepLumpDefinition associated with the parent BRepBodyDefinition object. |
| [classType](BRepLumpDefinitions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepLumpDefinitions_item.htm) | Function that returns the specified BRepLumpDefinition object using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepLumpDefinitions_count.htm) | The number of B-Rep lump definition objects in the collection. |
| [isValid](BRepLumpDefinitions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepLumpDefinitions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepBodyDefinition.lumpDefinitions](BRepBodyDefinition_lumpDefinitions.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |