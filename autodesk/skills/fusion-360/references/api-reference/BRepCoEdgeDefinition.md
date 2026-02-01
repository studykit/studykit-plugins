# BRepCoEdgeDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinition.h>

## Description

Represents the definition of a B-Rep co-edge that can be used as input to create a BRepBody that includes this co-edge.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepCoEdgeDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [edgeDefinition](BRepCoEdgeDefinition_edgeDefinition.htm) | Gets and sets the BRepEdgeDefinition object associated with this BrepCoEdgeDefinition object. |
| [isOpposedToEdge](BRepCoEdgeDefinition_isOpposedToEdge.htm) | Gets and sets if the orientation of this BRepCoEdgeDefinition object is reversed with respect to the associated BRepEdgeDefinition object. |
| [isValid](BRepCoEdgeDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepCoEdgeDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepCoEdgeDefinitions.add](BRepCoEdgeDefinitions_add.htm), [BRepCoEdgeDefinitions.item](BRepCoEdgeDefinitions_item.htm)

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