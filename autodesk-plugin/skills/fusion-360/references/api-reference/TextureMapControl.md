# TextureMapControl Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Materials/TextureMapControl.h>

## Description

Provides access to the various settings that control how a texture is applied to a body or mesh. This is the base class for the various texture mapping techniques.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TextureMapControl_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [reset](TextureMapControl_reset.htm) | Resets the texture map back to its original default settings. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](TextureMapControl_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](TextureMapControl_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepBody.textureMapControl](BRepBody_textureMapControl.htm), [MeshBody.textureMapControl](MeshBody_textureMapControl.htm), [TSplineBody.textureMapControl](TSplineBody_textureMapControl.htm)

## Derived Classes

[ProjectedTextureMapControl](ProjectedTextureMapControl.htm), [TextureMapControl3D](TextureMapControl3D.htm)

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |