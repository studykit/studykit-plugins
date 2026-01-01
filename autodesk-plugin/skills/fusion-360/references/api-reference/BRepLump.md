# BRepLump Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLump.h>

## Description

Represents an entirely connected set of entities. A BRepBody consists of BRepLumps.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepLump_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](BRepLump_createForAssemblyContext.htm) | Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [pointContainment](BRepLump_pointContainment.htm) | Determines the relationship of the input point with respect to this lump. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [area](BRepLump_area.htm) | Returns the area in cm ^ 2. |
| [assemblyContext](BRepLump_assemblyContext.htm) | Returns the assembly context that is directly referencing this object in an assembly. This is only valid in the case where this BRepLump object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [body](BRepLump_body.htm) | Returns the immediate owner BRepBody of the lump |
| [boundingBox](BRepLump_boundingBox.htm) | Returns the bounding box of the lump |
| [edges](BRepLump_edges.htm) | Returns the BRepEdges owned by the lump |
| [entityToken](BRepLump_entityToken.htm) | Returns a token for the BRepLump object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same lump. |
| [faces](BRepLump_faces.htm) | Returns the BRepFaces owned by the lump |
| [isClosed](BRepLump_isClosed.htm) | Returns true of the lump is closed |
| [isValid](BRepLump_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [meshManager](BRepLump_meshManager.htm) | Returns the mesh manager object for this lump. |
| [nativeObject](BRepLump_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](BRepLump_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [shells](BRepLump_shells.htm) | Returns the BRepShells owned by the lump |
| [vertices](BRepLump_vertices.htm) | Returns the BRepVertices owned by the lump |
| [volume](BRepLump_volume.htm) | Returns the volume in cm ^ 3. Returns 0 in the case the lump is not solid. |

## Accessed From

[BRepLump.createForAssemblyContext](BRepLump_createForAssemblyContext.htm), [BRepLump.nativeObject](BRepLump_nativeObject.htm), [BRepLumps.item](BRepLumps_item.htm), [BRepShell.lump](BRepShell_lump.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |