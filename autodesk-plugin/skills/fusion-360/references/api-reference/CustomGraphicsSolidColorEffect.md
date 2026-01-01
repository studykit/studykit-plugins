# CustomGraphicsSolidColorEffect Object

Derived from: [CustomGraphicsColorEffect](CustomGraphicsColorEffect.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsSolidColorEffect.h>

## Description

One of the types of color effects that can be applied to a custom graphics entity. With this type of effect, the graphics entity will display as the single color without any lighting effects. For example, a sphere will display as a solid filled circle without any shading indicating it is actually spherical.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomGraphicsSolidColorEffect_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](CustomGraphicsSolidColorEffect_create.htm) | Statically creates a new CustomGraphicsSolidColorEffect object. This can be used as input when creating various color related custom graphics attributes. A solid color effect, colors the entity with a single color without any lighting effects. With this coloring effect, a sphere will display as a solid filled circle. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [color](CustomGraphicsSolidColorEffect_color.htm) | The color to use for the solid color display. The opacity component of the color is ignored because the opacity of custom graphics is controlled separately using an opacity attribute. |
| [isValid](CustomGraphicsSolidColorEffect_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomGraphicsSolidColorEffect_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CustomGraphicsSolidColorEffect.create](CustomGraphicsSolidColorEffect_create.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |