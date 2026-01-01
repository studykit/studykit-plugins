# TriangleMeshList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshList.h>

## Description

Provides access to a set of triangle meshes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TriangleMeshList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](TriangleMeshList_item.htm) | Returns the specified triangle meshes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [bestMesh](TriangleMeshList_bestMesh.htm) | Returns the mesh with the tightest surface tolerance. This can return null in the case the list is empty, i.e. Count is 0. |
| [count](TriangleMeshList_count.htm) | Returns the number of meshes in the collection. |
| [isValid](TriangleMeshList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](TriangleMeshList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[MeshManager.displayMeshes](MeshManager_displayMeshes.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |