# AppearanceTexture Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTexture.h>

## Description

Provides access to a list of properties that define a texture.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [changeTextureImage](AppearanceTexture_changeTextureImage.htm) | Changes the image of this texture. |
| [classType](AppearanceTexture_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](AppearanceTexture_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](AppearanceTexture_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [properties](AppearanceTexture_properties.htm) | Returns a collection of the properties associated with this texture. |
| [textureType](AppearanceTexture_textureType.htm) | Gets the type of texture this appearance currently is. |

## Accessed From

[AppearanceTextureProperty.value](AppearanceTextureProperty_value.htm), [ColorProperty.connectedTexture](ColorProperty_connectedTexture.htm), [FloatProperty.connectedTexture](FloatProperty_connectedTexture.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |