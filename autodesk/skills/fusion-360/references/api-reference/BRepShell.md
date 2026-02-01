# BRepShell Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShell.h>

## Description

Represents an entirely connected set of BRepFaces. A BRepLump may contain multiple BRepShells.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepShell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](BRepShell_createForAssemblyContext.htm) | Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [pointContainment](BRepShell_pointContainment.htm) | Determines the relationship of the input point with respect to this shell. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [area](BRepShell_area.htm) | Returns the area in cm ^ 2. |
| [assemblyContext](BRepShell_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepShell object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [body](BRepShell_body.htm) | Returns the parent body of the shell. |
| [boundingBox](BRepShell_boundingBox.htm) | Returns the bounding box of this shell |
| [edges](BRepShell_edges.htm) | returns the BRepEdges owned by this shell |
| [entityToken](BRepShell_entityToken.htm) | Returns a token for the BRepShell object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same shell. |
| [faces](BRepShell_faces.htm) | Returns the BRepFaces directly owned by this shell |
| [isClosed](BRepShell_isClosed.htm) | Returns true if this shell is closed |
| [isValid](BRepShell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVoid](BRepShell_isVoid.htm) | Returns true if the faces of this shell bound a void or an empty space within an outer shell. |
| [lump](BRepShell_lump.htm) | Returns the parent lump of this shell. |
| [meshManager](BRepShell_meshManager.htm) | Returns the mesh manager object for this shell. |
| [nativeObject](BRepShell_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](BRepShell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [vertices](BRepShell_vertices.htm) | Returns the BRepVertices owned by this shell |
| [volume](BRepShell_volume.htm) | Returns the volume in cm ^ 3. Returns 0 in the case the shell is not solid. |
| [wire](BRepShell_wire.htm) | Returns the wire body, if any, that exists in this shell. Returns null if the shell doesn't have a wire body. |

## Accessed From

[BRepEdge.shell](BRepEdge_shell.htm), [BRepFace.shell](BRepFace_shell.htm), [BRepShell.createForAssemblyContext](BRepShell_createForAssemblyContext.htm), [BRepShell.nativeObject](BRepShell_nativeObject.htm), [BRepShells.item](BRepShells_item.htm), [BRepVertex.shell](BRepVertex_shell.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |