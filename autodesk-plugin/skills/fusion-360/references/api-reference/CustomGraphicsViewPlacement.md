# CustomGraphicsViewPlacement Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsViewPlacement.h>

## Description

Positions custom graphics relative to one of the four corners of the view. Graphics positioned this way will always appear on top of the model graphics. This is typically used to display legends are small interactive tools.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomGraphicsViewPlacement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](CustomGraphicsViewPlacement_create.htm) | Creates a new CustomGraphicsViewPlacement object that can be used when setting the viewPlacement property of a custom graphics entity to specify the billboarding behavior. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [anchorPoint](CustomGraphicsViewPlacement_anchorPoint.htm) | Gets and sets the position within the defined graphics that serves as the anchor. This is the location on the graphics that is positioned at the specified view point. |
| [isValid](CustomGraphicsViewPlacement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomGraphicsViewPlacement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [viewCorner](CustomGraphicsViewPlacement_viewCorner.htm) | Gets and sets which corner the graphics are positioned relative to. |
| [viewPoint](CustomGraphicsViewPlacement_viewPoint.htm) | A 2D point in the view that defines the position of the graphics. This is relative to the corner and is in pixels. The x and y directions vary for each of the corners. These directions are only used to position the 2D point and do not affect the standard coordinate system the graphics were drawn in.   upperLeftViewCorner - The x direction is to the right and y is down.   upperRightViewCorner - The x direction is to the left and y is down.   lowerLeftViewCorner - The x direction is to the right and y is up.   lowerRightViewCorner - The x direction is to the left and y is up. |

## Accessed From

[CustomGraphicsBRepBody.viewPlacement](CustomGraphicsBRepBody_viewPlacement.htm), [CustomGraphicsCurve.viewPlacement](CustomGraphicsCurve_viewPlacement.htm), [CustomGraphicsEntity.viewPlacement](CustomGraphicsEntity_viewPlacement.htm), [CustomGraphicsGroup.viewPlacement](CustomGraphicsGroup_viewPlacement.htm), [CustomGraphicsLines.viewPlacement](CustomGraphicsLines_viewPlacement.htm), [CustomGraphicsMesh.viewPlacement](CustomGraphicsMesh_viewPlacement.htm), [CustomGraphicsPointSet.viewPlacement](CustomGraphicsPointSet_viewPlacement.htm), [CustomGraphicsText.viewPlacement](CustomGraphicsText_viewPlacement.htm), [CustomGraphicsViewPlacement.create](CustomGraphicsViewPlacement_create.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |