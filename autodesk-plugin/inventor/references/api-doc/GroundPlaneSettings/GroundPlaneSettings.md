# GroundPlaneSettings Object

## Description

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetSize](../GroundPlaneSettings/GroundPlaneSettings_GetSize.md) | Method that gets the current size of the displayed graphics for the ground plane. The plane is functionally infinite but has a plane that is displayed to allow the user to visualize it. |
| [SetSize](../GroundPlaneSettings/GroundPlaneSettings_SetSize.md) | Method that sets the current size of the displayed graphics for the ground plane. The plane is functionally infinite but has a plane that is displayed to allow the user to visualize it. This method will fail if the AutoResize property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GroundPlaneSettings/GroundPlaneSettings_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutoResize](../GroundPlaneSettings/GroundPlaneSettings_AutoResize.md) | Gets or sets whether the ground plane should be resized automatically based on the component size. |
| [Color](../GroundPlaneSettings/GroundPlaneSettings_Color.md) | Read-write property that gets and sets the color for the ground plane for the area inside the margin. |
| [DisplayGridLines](../GroundPlaneSettings/GroundPlaneSettings_DisplayGridLines.md) | Read-write property that specifies whether to display grid lines. |
| [FrontDirection](../GroundPlaneSettings/GroundPlaneSettings_FrontDirection.md) | Gets front directon of the ground plane. |
| [HeightOffset](../GroundPlaneSettings/GroundPlaneSettings_HeightOffset.md) | Gets and sets the offset of the ground plane from the specified position. |
| [MinorGridLineSpacing](../GroundPlaneSettings/GroundPlaneSettings_MinorGridLineSpacing.md) | Gets and sets the spacing between minor grid lines in centimeters. |
| [MinorLinesPerMajorGridLine](../GroundPlaneSettings/GroundPlaneSettings_MinorLinesPerMajorGridLine.md) | Gets and sets the number of minor lines to appear between major lines. |
| [Opacity](../GroundPlaneSettings/GroundPlaneSettings_Opacity.md) | Gets and sets the opacity of the ground plane. |
| [Plane](../GroundPlaneSettings/GroundPlaneSettings_Plane.md) | Property that returns the geometry of the ground plane. The returned Plane object provides information about the position and normal of the work plane. |
| [Position](../GroundPlaneSettings/GroundPlaneSettings_Position.md) | Gets and sets the position of the ground plane. |
| [ReflectionBlur](../GroundPlaneSettings/GroundPlaneSettings_ReflectionBlur.md) | Gets and sets the reflection’s blurriness, specifying the amount of blur the ground plane surface will produce. |
| [ReflectionBlurFalloff](../GroundPlaneSettings/GroundPlaneSettings_ReflectionBlurFalloff.md) | Gets and sets where the model reflection seems to fade away. |
| [Reflectivity](../GroundPlaneSettings/GroundPlaneSettings_Reflectivity.md) | Gets and sets the reflectivity of the ground plane. |
| [Type](../GroundPlaneSettings/GroundPlaneSettings_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpDirection](../GroundPlaneSettings/GroundPlaneSettings_UpDirection.md) | Gets up directon of the ground plane. |

## Accessed From

[DisplaySettings.GroundPlaneSettings](../DisplaySettings/DisplaySettings_GroundPlaneSettings.md)

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |