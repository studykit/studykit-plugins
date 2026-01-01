# BRepWireEdgeDefinitions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinitions.h>

## Description

A collection of BRepWireEdgeDefinition objects. Using this collection you can create new BRepWireDefinition objects to full define a wire body.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BRepWireEdgeDefinitions_add.htm) | Creates a new BRepWireEdgeDefinition object associated with the parent BRepWireDefinition object. |
| [classType](BRepWireEdgeDefinitions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepWireEdgeDefinitions_item.htm) | Function that returns the specified BRepWireEdgeDefinition object using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepWireEdgeDefinitions_count.htm) | The number of B-Rep wire edge definition objects in the collection. |
| [isValid](BRepWireEdgeDefinitions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepWireEdgeDefinitions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepWireDefinition.wireEdgeDefinitions](BRepWireDefinition_wireEdgeDefinitions.htm)

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