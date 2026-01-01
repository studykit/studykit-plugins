# BRepEdges Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdges.h>

## Description

BRepEdge collection.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepEdges_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepEdges_item.htm) | Function that returns the specified edge using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepEdges_count.htm) | The number of edges in the collection. |
| [isValid](BRepEdges_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepEdges_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepBody.concaveEdges](BRepBody_concaveEdges.htm), [BRepBody.convexEdges](BRepBody_convexEdges.htm), [BRepBody.edges](BRepBody_edges.htm), [BRepFace.edges](BRepFace_edges.htm), [BRepLoop.edges](BRepLoop_edges.htm), [BRepLump.edges](BRepLump_edges.htm), [BRepShell.edges](BRepShell_edges.htm), [BRepVertex.edges](BRepVertex_edges.htm), [BRepWire.edges](BRepWire_edges.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |