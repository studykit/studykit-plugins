# MeshBodyList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodyList.h>

## Description

Provides access to a list of MeshBody objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshBodyList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](MeshBodyList_item.htm) | Provides access to a mesh body within the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MeshBodyList_count.htm) | Returns the number of mesh bodies in the collection. |
| [isValid](MeshBodyList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MeshBodyList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[MeshBodies.add](MeshBodies_add.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |