# DisplaySettings Object

## Description

The DisplaySettings object provides access to properties that provide read and write access of the display appearance related document settings. This is somewhat equivalent to the Display Appearance tab of the Document Settings dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DisplaySettings/DisplaySettings_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AreTexturesOn](../DisplaySettings/DisplaySettings_AreTexturesOn.md) | Gets and sets whether to turn textures on. |
| [DepthDimming](../DisplaySettings/DisplaySettings_DepthDimming.md) | Enables or disables the depth dimming effect that displays entities that are nearer with a brighter light to better convey the depth of the model. |
| [DisplaySilhouettes](../DisplaySettings/DisplaySettings_DisplaySilhouettes.md) | Read-write property that specifies whether to display silhouette edges for active components. |
| [EdgeColor](../DisplaySettings/DisplaySettings_EdgeColor.md) | Gets and sets the color for the edge display (including silhouettes) for active components. |
| [GroundPlaneSettings](../DisplaySettings/DisplaySettings_GroundPlaneSettings.md) | Property that returns the GroundPlaneSettings object. The GroundPlaneSettings object provides access to various settings that define the ground plane. |
| [HiddenLineDimmingPercent](../DisplaySettings/DisplaySettings_HiddenLineDimmingPercent.md) | Gets and sets the dimming factor (expressed as a percentage) applied to the display of hidden lines in the model. |
| [NewWindowDisplayMode](../DisplaySettings/DisplaySettings_NewWindowDisplayMode.md) | Gets and sets the default display mode for new windows. |
| [NewWindowProjectionType](../DisplaySettings/DisplaySettings_NewWindowProjectionType.md) | Gets and sets the default projection type for new windows. |
| [NewWindowShowAmbientShadows](../DisplaySettings/DisplaySettings_NewWindowShowAmbientShadows.md) | Gets and sets whether to display ambient shadows (occlusions) for new windows. |
| [NewWindowShowGroundPlane](../DisplaySettings/DisplaySettings_NewWindowShowGroundPlane.md) | Gets and sets whether to display ground planes for new windows. |
| [NewWindowShowGroundReflections](../DisplaySettings/DisplaySettings_NewWindowShowGroundReflections.md) | Gets and sets whether to display ground plane reflections for new windows. |
| [NewWindowShowGroundShadows](../DisplaySettings/DisplaySettings_NewWindowShowGroundShadows.md) | Gets and sets whether to display ground shadows for new windows. |
| [NewWindowShowObjectShadows](../DisplaySettings/DisplaySettings_NewWindowShowObjectShadows.md) | Gets and sets whether to display object shadows for new windows. |
| [Parent](../DisplaySettings/DisplaySettings_Parent.md) | Property that returns the parent Document object. |
| [RayTracingQuality](../DisplaySettings/DisplaySettings_RayTracingQuality.md) | Gets and sets the quality used when ray tracing is enabled. |
| [SolidLinesForHiddenEdges](../DisplaySettings/DisplaySettings_SolidLinesForHiddenEdges.md) | Gets and sets whether the hidden model edges should be displayed as solid lines. |
| [Type](../DisplaySettings/DisplaySettings_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseRayTracingForRealisticDisplay](../DisplaySettings/DisplaySettings_UseRayTracingForRealisticDisplay.md) | Gets and sets whether to enable ray tracing in realistic visual styles for new windows. |

## Accessed From

[AssemblyDocument.DisplaySettings](../AssemblyDocument/AssemblyDocument_DisplaySettings.md), [PartDocument.DisplaySettings](../PartDocument/PartDocument_DisplaySettings.md), [PresentationDocument.DisplaySettings](../PresentationDocument/PresentationDocument_DisplaySettings.md)

## Version

Introduced in version 2011
