# BRepLoopDefinitions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoopDefinitions.h>

## Description

Provides access to the BRepLoopDefinition objects associated with the parent BRepFaceDefinition object. It's through this object that you create new BRepLoopDefinition objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BRepLoopDefinitions_add.htm) | Creates a new empty loop associated with the parent face definition. |
| [classType](BRepLoopDefinitions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepLoopDefinitions_item.htm) | Function that returns the specified BRepLoopDefinition object using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepLoopDefinitions_count.htm) | The number of B-Rep loop definition objects in the collection. |
| [isValid](BRepLoopDefinitions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepLoopDefinitions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepFaceDefinition.loopDefinitions](BRepFaceDefinition_loopDefinitions.htm)

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