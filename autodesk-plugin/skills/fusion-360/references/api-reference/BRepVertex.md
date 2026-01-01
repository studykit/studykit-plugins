# BRepVertex Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertex.h>

## Description

A 0-dimensional topological entity that bounds a BRepEdge.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepVertex_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](BRepVertex_createForAssemblyContext.htm) | Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](BRepVertex_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepVertex object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [attributes](BRepVertex_attributes.htm) | Returns the collection of attributes associated with this face. |
| [body](BRepVertex_body.htm) | Returns the parent body. |
| [edges](BRepVertex_edges.htm) | Returns the BRepEdges bounded by this vertex |
| [entityToken](BRepVertex_entityToken.htm) | Returns a token for the BRepVertex object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same vertex. |
| [faces](BRepVertex_faces.htm) | Returns the BRepFaces that uses this vertex through BRepEdge |
| [geometry](BRepVertex_geometry.htm) | Returns the underlying geometry point |
| [isTolerant](BRepVertex_isTolerant.htm) | Returns if the vertex is tolerant. The tolerance used is available from the tolerance property. |
| [isValid](BRepVertex_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](BRepVertex_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](BRepVertex_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [shell](BRepVertex_shell.htm) | Returns the parent shell. |
| [tempId](BRepVertex_tempId.htm) | Returns the temporary ID of this vertex. This ID is only good while the document remains open and as long as the owning BRepBody is not modified in any way. The findByTempId method of the BRepBody will return the entity in the body with the given ID. |
| [tolerance](BRepVertex_tolerance.htm) | Returns the tolerance used by a tolerant vertex. This value is only useful when isTolerant is true. |

## Accessed From

[BRepEdge.endVertex](BRepEdge_endVertex.htm), [BRepEdge.startVertex](BRepEdge_startVertex.htm), [BRepVertex.createForAssemblyContext](BRepVertex_createForAssemblyContext.htm), [BRepVertex.nativeObject](BRepVertex_nativeObject.htm), [BRepVertices.item](BRepVertices_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |