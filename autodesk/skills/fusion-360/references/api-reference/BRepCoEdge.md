# BRepCoEdge Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdge.h>

## Description

Represents the use of a BRepEdge by a BRepFace.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepCoEdge_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](BRepCoEdge_createForAssemblyContext.htm) | Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](BRepCoEdge_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepCoEdge object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [body](BRepCoEdge_body.htm) | Returns the body this co-edge is part of. |
| [edge](BRepCoEdge_edge.htm) | Returns the edge this co-edge is associated with. |
| [entityToken](BRepCoEdge_entityToken.htm) | Returns a token for the BRepCoEdge object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same co-edge. |
| [evaluator](BRepCoEdge_evaluator.htm) | Returns a curve evaluator that can be used to perform geometric evaluations on the co-edge. |
| [geometry](BRepCoEdge_geometry.htm) | Returns a geometry object that represents the shape of this co-edge in parameter space of the parent face's surface. |
| [isOpposedToEdge](BRepCoEdge_isOpposedToEdge.htm) | Indicates if the orientation of this co-edge is in the same direction or opposed to its associated edge. |
| [isParamReversed](BRepCoEdge_isParamReversed.htm) | Returns if the parametric direction of this co-edge is reversed from the parametric direction of the underlying curve obtained from the geometry property. A co-edge's parametric direction is from the start vertex to the end vertex. But the underlying curve geometry may have the opposite parameterization. This property indicates if the parameterization order of the evaluator obtained from this co-edge is reversed from the order of the geometry curve's evaluator. |
| [isValid](BRepCoEdge_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [loop](BRepCoEdge_loop.htm) | Returns the loop this co-edge is part of. |
| [nativeObject](BRepCoEdge_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [next](BRepCoEdge_next.htm) | Returns the next co-edge in the loop. |
| [objectType](BRepCoEdge_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [partner](BRepCoEdge_partner.htm) | Returns the co-edge on the adjacent face |
| [previous](BRepCoEdge_previous.htm) | Returns the previous co-edge in the loop. |

## Accessed From

[BRepCoEdge.createForAssemblyContext](BRepCoEdge_createForAssemblyContext.htm), [BRepCoEdge.nativeObject](BRepCoEdge_nativeObject.htm), [BRepCoEdge.next](BRepCoEdge_next.htm), [BRepCoEdge.partner](BRepCoEdge_partner.htm), [BRepCoEdge.previous](BRepCoEdge_previous.htm), [BRepCoEdges.item](BRepCoEdges_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |