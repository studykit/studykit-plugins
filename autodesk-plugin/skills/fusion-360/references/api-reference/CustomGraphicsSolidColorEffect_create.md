# CustomGraphicsSolidColorEffect.create Method

Parent Object: [CustomGraphicsSolidColorEffect](CustomGraphicsSolidColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsSolidColorEffect.h>

## Description

Statically creates a new CustomGraphicsSolidColorEffect object. This can be used as input when creating various color related custom graphics attributes. A solid color effect, colors the entity with a single color without any lighting effects. With this coloring effect, a sphere will display as a solid filled circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomGraphicsSolidColorEffect](CustomGraphicsSolidColorEffect.htm) | Returns the created CustomGraphicsSolidColorEffect or null in case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| color | [Color](Color.htm) | The color to use for the solid color display. The opacity component of the color is ignored because the opacity of custom graphics is controlled separately using an opacity attribute. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |