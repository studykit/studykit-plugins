# CustomGraphicsBillBoard Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBillBoard.h>

## Description

Used to specify if the orientation of custom graphics are defined relative to the screen instead of model space. This is commonly used for legends and symbols that you want to always face the user, even as the camera is rotated.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomGraphicsBillBoard_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](CustomGraphicsBillBoard_create.htm) | Creates a new CustomGraphicsBillBoard object that can be used when calling the billBoarding property of the CustomGraphicsEntity object to specify the billboarding behavior of some custom graphics. Once created you can assign it to a custom graphics entity using its billBoarding property. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [anchorPoint](CustomGraphicsBillBoard_anchorPoint.htm) | RETIRED - This property has been retired. It is not needed since the matrix defined for the CustomGraphicsText object defines the position and anchor for the billboarded text. Getting the value of this property will return a point at the origin. Setting this property will be ignored.  Specifies the coordinate in model or view space that the graphics will anchor to. For graphics that represent a label, this will typically be the point where the label attaches to the model. A CustomGraphicsAnchorPoint can be created using the static create method on the CustomGraphicsAnchorPoint object. |
| [axis](CustomGraphicsBillBoard_axis.htm) | When the billBoardStyle property is set to AxialBillBoardStyle, this is used to control the direction of the graphics. Otherwise it uses the x axis of the view. |
| [billBoardStyle](CustomGraphicsBillBoard_billBoardStyle.htm) | Specifies the type of billboarding to use. When a new CustomGraphicsBillBoard object is created this defaults to ScreenBillBoardStyle so the graphics will all be facing the view plane. It can also be set to an arbitrary plane by setting this to AxialBillBoardStyle and can be defined so that it never appear backwards by setting it to RightReadingBillBoardStyle. |
| [isValid](CustomGraphicsBillBoard_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomGraphicsBillBoard_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CustomGraphicsBillBoard.create](CustomGraphicsBillBoard_create.htm), [CustomGraphicsBRepBody.billBoarding](CustomGraphicsBRepBody_billBoarding.htm), [CustomGraphicsCurve.billBoarding](CustomGraphicsCurve_billBoarding.htm), [CustomGraphicsEntity.billBoarding](CustomGraphicsEntity_billBoarding.htm), [CustomGraphicsGroup.billBoarding](CustomGraphicsGroup_billBoarding.htm), [CustomGraphicsLines.billBoarding](CustomGraphicsLines_billBoarding.htm), [CustomGraphicsMesh.billBoarding](CustomGraphicsMesh_billBoarding.htm), [CustomGraphicsPointSet.billBoarding](CustomGraphicsPointSet_billBoarding.htm), [CustomGraphicsText.billBoarding](CustomGraphicsText_billBoarding.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |