# MeshBodies Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodies.h>

## Description

Provides access to the MeshBodies in the parent Component and supports the creation of new mesh bodies.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](MeshBodies_add.htm) | Creates a new mesh body by importing an STL, OBJ or 3MF file. |
| [addByTriangleMeshData](MeshBodies_addByTriangleMeshData.htm) | Creates a new mesh body using the mesh description provided. |
| [classType](MeshBodies_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](MeshBodies_item.htm) | Provides access to a mesh body within the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MeshBodies_count.htm) | Returns the number of mesh bodies in the collection. |
| [isValid](MeshBodies_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MeshBodies_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Component.meshBodies](Component_meshBodies.htm), [FlatPatternComponent.meshBodies](FlatPatternComponent_meshBodies.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |