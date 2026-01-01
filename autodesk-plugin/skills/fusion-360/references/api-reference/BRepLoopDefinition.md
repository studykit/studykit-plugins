# BRepLoopDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoopDefinition.h>

## Description

Represents the definition of a B-Rep loop that can be used as input to create a BRepBody that includes this loop.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepLoopDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [bRepCoEdgeDefinitions](BRepLoopDefinition_bRepCoEdgeDefinitions.htm) | Provides access to the BRepCoEdgeDefinitions object associated with the parent BRepFaceDefinition object. It's through the returned collection that you can create new BRepCoEdgeDefinition objects. |
| [isValid](BRepLoopDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepLoopDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepLoopDefinitions.add](BRepLoopDefinitions_add.htm), [BRepLoopDefinitions.item](BRepLoopDefinitions_item.htm)

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