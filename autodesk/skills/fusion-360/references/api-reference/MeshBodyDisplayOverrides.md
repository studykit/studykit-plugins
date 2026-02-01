# MeshBodyDisplayOverrides Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodyDisplayOverrides.h>

## Description

Container for overrides that control how the mesh is displayed in the interactive 3D view.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshBodyDisplayOverrides_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isSuppressFaceGroupColors](MeshBodyDisplayOverrides_isSuppressFaceGroupColors.htm) | Controls whether the mesh body face group colors are shown. If set to true, the face groups will be shown with the assigned appearance, ignoring the current display settings. |
| [isSuppressTriangleEdges](MeshBodyDisplayOverrides_isSuppressTriangleEdges.htm) | Controls whether the edges of the triangles of the mesh body are shown. If set to true, individual triangles will not be visible, edges of face groups (if any) will be shown instead. |
| [isValid](MeshBodyDisplayOverrides_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MeshBodyDisplayOverrides_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[MeshBody.displayOverrides](MeshBody_displayOverrides.htm)

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |