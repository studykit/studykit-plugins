# CustomGraphicsBillBoard.create Method

Parent Object: [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBillBoard.h>

## Description

Creates a new CustomGraphicsBillBoard object that can be used when calling the billBoarding property of the CustomGraphicsEntity object to specify the billboarding behavior of some custom graphics. Once created you can assign it to a custom graphics entity using its billBoarding property.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm) | Returns the newly created CustomGraphicsBillBoard object or null in the case of failure. This can be assigned to a custom graphics entity using its billBoarding property. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| anchorPoint | [Point3D](Point3D.htm) | The parameter must be input and can be null but the value is ignored. Use of the anchor point has been retired and it is no longer used. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |