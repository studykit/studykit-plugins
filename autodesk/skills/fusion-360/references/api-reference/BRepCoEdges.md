# BRepCoEdges Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdges.h>

## Description

BRepCoEdge Collection.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepCoEdges_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepCoEdges_item.htm) | Function that returns the specified co-edge using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepCoEdges_count.htm) | The number of co-edges in the collection. |
| [isValid](BRepCoEdges_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepCoEdges_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepEdge.coEdges](BRepEdge_coEdges.htm), [BRepLoop.coEdges](BRepLoop_coEdges.htm), [BRepWire.coEdges](BRepWire_coEdges.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |