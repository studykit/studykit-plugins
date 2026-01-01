# CustomGraphicsAppearanceColorEffect Object

Derived from: [CustomGraphicsColorEffect](CustomGraphicsColorEffect.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsAppearanceColorEffect.h>

## Description

One of the types of color effects that can be applied to a custom graphics entity. With this type of effect, the graphics entity will display using a Fusion appearance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomGraphicsAppearanceColorEffect_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](CustomGraphicsAppearanceColorEffect_create.htm) | Statically creates a new CustomGraphicsAppearanceColorEffect object. This can be used when setting the color property of the various custom graphics objects. With this coloring effect, an existing appearance is used. The appearance must be available in the design where the graphics will be drawn. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [appearance](CustomGraphicsAppearanceColorEffect_appearance.htm) | Gets and sets the appearance to use. The appearance assigned must be available in the design where the graphics will be drawn. |
| [isValid](CustomGraphicsAppearanceColorEffect_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomGraphicsAppearanceColorEffect_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CustomGraphicsAppearanceColorEffect.create](CustomGraphicsAppearanceColorEffect_create.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |