# AppearanceTextureProperty Object

Derived from: [Property](Property.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTextureProperty.h>

## Description

A texture value property associated with a material or appearance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](AppearanceTextureProperty_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](AppearanceTextureProperty_id.htm) | Returns the unique ID of this property. |
| [isReadOnly](AppearanceTextureProperty_isReadOnly.htm) | Indicates if this property is read-only. If True any attempted edits will fail. |
| [isUsed](AppearanceTextureProperty_isUsed.htm) | Specifies if this AppearanceTexture is being used. This is the equivalent of the check box in the Appearance dialog to enable the use of a text for an appearance or not. if this is False, then the value property should not be used because there isn't an associated. AppearanceTexture. |
| [isValid](AppearanceTextureProperty_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](AppearanceTextureProperty_name.htm) | Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language |
| [objectType](AppearanceTextureProperty_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](AppearanceTextureProperty_parent.htm) | Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in. |
| [value](AppearanceTextureProperty_value.htm) | Gets and sets this property value. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |