# MeshManager Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/MeshManager.h>

## Description

Provides access to meshes that approximate a B-Rep and T-Spline.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshManager_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createMeshCalculator](MeshManager_createMeshCalculator.htm) | Creates a new MeshCalculator which is used to calculate new triangular meshes based on various parameters that control the calculation. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [displayMeshes](MeshManager_displayMeshes.htm) | Returns a collection that provides access to all of the existing display meshes. |
| [isValid](MeshManager_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MeshManager_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](MeshManager_parent.htm) | Returns the parent BRepBody, BRepFace, BRepLump, BRepShell, SculptBody, or SculptFace object. |

## Accessed From

[BRepBody.meshManager](BRepBody_meshManager.htm), [BRepFace.meshManager](BRepFace_meshManager.htm), [BRepLump.meshManager](BRepLump_meshManager.htm), [BRepShell.meshManager](BRepShell_meshManager.htm), [TriangleMeshCalculator.parentMeshManager](TriangleMeshCalculator_parentMeshManager.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |