# CustomGraphicsViewPlacement.create Method

Parent Object: [CustomGraphicsViewPlacement](CustomGraphicsViewPlacement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewPlacement.h>

## Description

Creates a new CustomGraphicsViewPlacement object that can be used when setting the viewPlacement property of a custom graphics entity to specify the billboarding behavior.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomGraphicsViewPlacement](CustomGraphicsViewPlacement.htm) | Returns the newly created CustomGraphicsViewPlacement object or null in the case of failure. This can then be assigned to any custom graphics entity using its viewPlacement property. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| anchorPoint | [Point3D](Point3D.htm) | The position within the defined graphics that will serve as the anchor. This is the location on the graphics that will be positioned at the specified view point. |
| viewCorner | [ViewCorners](ViewCorners.htm) | Defines which of the four corners of the view the graphics are drawn relative to. |
| viewPoint | [Point2D](Point2D.htm) | A 2D point in the view that defines the position of the graphics. This is relative to the corner and is in pixels. The x and y directions vary for each of the corners. These directions are only used to position the 2D point and do not affect the standard coordinate system the graphics were drawn in.   upperLeftViewCorner - The x direction is to the right and y is down.   upperRightViewCorner - The x direction is to the left and y is down.   lowerLeftViewCorner - The x direction is to the right and y is up.   lowerRightViewCorner - The x direction is to the left and y is up. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |