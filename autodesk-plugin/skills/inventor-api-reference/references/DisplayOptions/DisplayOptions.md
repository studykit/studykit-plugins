# DisplayOptions Object

## Description

The DisplayOptions object provides access to properties that provide read and write access of the display related application options. This is somewhat equivalent to the Display tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DisplayOptions/DisplayOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AreTexturesOn](../DisplayOptions/DisplayOptions_AreTexturesOn.md) | Gets and sets whether to turn textures on. |
| [AutoUpdateReferringDocuments](../DisplayOptions/DisplayOptions_AutoUpdateReferringDocuments.md) | Enable/Disable automatically update referring documents. |
| [DefaultOrbitType](../DisplayOptions/DisplayOptions_DefaultOrbitType.md) | Gets/sets the default behavior for the orbit command. |
| [DepthDimming](../DisplayOptions/DisplayOptions_DepthDimming.md) | Read-write property that enables or disables the depth dimming effect that displays entities that are nearer with a brighter light to better convey the depth of the model. Setting this property to True enables the depth dimming effect. |
| [DisplayQuality](../DisplayOptions/DisplayOptions_DisplayQuality.md) | Specifies the resolution quality to apply to the display of the model. |
| [DisplaySilhouettes](../DisplayOptions/DisplayOptions_DisplaySilhouettes.md) | Read-write property that specifies whether to display silhouette edges for active components. |
| [EdgeColor](../DisplayOptions/DisplayOptions_EdgeColor.md) | Read-write property that gets and sets the color for the edge display (including silhouettes) for active components. |
| [EnableSmoothSketchLines](../DisplayOptions/DisplayOptions_EnableSmoothSketchLines.md) | Gets/sets whether to use the smooth sketch line. |
| [HiddenLineDimmingPercent](../DisplayOptions/DisplayOptions_HiddenLineDimmingPercent.md) | Gets/sets the dimming factor (expressed as a percentage) applied to the display of hidden lines in the model. |
| [InactiveComponentsEdgeColor](../DisplayOptions/DisplayOptions_InactiveComponentsEdgeColor.md) | Read-write property that gets and sets the color for the edge display (including silhouettes) for inactive components. |
| [InactiveComponentsEdgeDisplay](../DisplayOptions/DisplayOptions_InactiveComponentsEdgeDisplay.md) | Read-write property that specifies whether edges should be displayed for inactive components. |
| [InactiveComponentsEdgeDisplayFollowVisibility](../DisplayOptions/DisplayOptions_InactiveComponentsEdgeDisplayFollowVisibility.md) | Read-write property that specifies whether inactive component edges display should follow the visibility setting of visual styles. |
| [InactiveComponentsShaded](../DisplayOptions/DisplayOptions_InactiveComponentsShaded.md) | Read-write property that enables or disables contrasting shading for the display of inactive components. |
| [InactiveComponentsShadeOpacity](../DisplayOptions/DisplayOptions_InactiveComponentsShadeOpacity.md) | Read-write property that gets and sets the opacity level (expressed as a percentage) for the shading of inactive components. |
| [MinimumFrameRate](../DisplayOptions/DisplayOptions_MinimumFrameRate.md) | Gets/sets the number of frames to display for the model during interactive viewing operations like Rotate, Pan and Zoom. |
| [NewWindowDisplayMode](../DisplayOptions/DisplayOptions_NewWindowDisplayMode.md) | Gets/sets the default display mode for new windows. |
| [NewWindowProjectionType](../DisplayOptions/DisplayOptions_NewWindowProjectionType.md) | Gets/sets the default projection type for new windows. |
| [NewWindowShowAmbientShadows](../DisplayOptions/DisplayOptions_NewWindowShowAmbientShadows.md) | Gets and sets whether to display ambient shadows (occlusions) for new windows. |
| [NewWindowShowGroundPlane](../DisplayOptions/DisplayOptions_NewWindowShowGroundPlane.md) | Read-write property that gets and sets whether to display ground planes for new windows. |
| [NewWindowShowGroundReflections](../DisplayOptions/DisplayOptions_NewWindowShowGroundReflections.md) | Read-write property that gets and sets whether to display ground plane reflections for new windows. |
| [NewWindowShowGroundShadows](../DisplayOptions/DisplayOptions_NewWindowShowGroundShadows.md) | Gets and sets whether to display ground shadows for new windows. |
| [NewWindowShowObjectShadows](../DisplayOptions/DisplayOptions_NewWindowShowObjectShadows.md) | Gets and sets whether to display object shadows for new windows. |
| [RayTracingQuality](../DisplayOptions/DisplayOptions_RayTracingQuality.md) | Gets and sets the quality used when ray tracing is enabled. |
| [ReverseZoomDirection](../DisplayOptions/DisplayOptions_ReverseZoomDirection.md) | Gets/sets the zoom direction with respect to the movement of the mouse cursor or mouse wheel. |
| [Show3DIndicator](../DisplayOptions/DisplayOptions_Show3DIndicator.md) | Show/Hide 3D indicator. |
| [ShowXYZAxisLabels](../DisplayOptions/DisplayOptions_ShowXYZAxisLabels.md) | Gets and sets whether to show axis labels for the 3D indicator (triad). |
| [SolidLinesForHiddenEdges](../DisplayOptions/DisplayOptions_SolidLinesForHiddenEdges.md) | Gets/sets whether the hidden model edges should be displayed as solid lines. |
| [TransparentComponentsEdgeColor](../DisplayOptions/DisplayOptions_TransparentComponentsEdgeColor.md) | Read-write property that gets and sets the color for the edge display (including silhouettes) for transparent components. |
| [TransparentComponentsEdgeDisplay](../DisplayOptions/DisplayOptions_TransparentComponentsEdgeDisplay.md) | Read-write property that specifies whether edges should be displayed for transparent components. |
| [TransparentComponentsEdgeDisplayFollowVisibility](../DisplayOptions/DisplayOptions_TransparentComponentsEdgeDisplayFollowVisibility.md) | Read-write property that specifies whether transparent component edges display should follow the visibility setting of visual styles. |
| [TransparentComponentsShaded](../DisplayOptions/DisplayOptions_TransparentComponentsShaded.md) | Read-write property that enables or disables contrasting shading for the display of transparent components. |
| [TransparentComponentsShadeOpacity](../DisplayOptions/DisplayOptions_TransparentComponentsShadeOpacity.md) | Read-write property that gets and sets the opacity level (expressed as a percentage) for the shading of transparent components. |
| [Type](../DisplayOptions/DisplayOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseDocumentDisplaySettings](../DisplayOptions/DisplayOptions_UseDocumentDisplaySettings.md) | Read-write property that gets and sets whether to use the display appearance settings defined in the document. If set to False, the application level display settings are used. |
| [UseNearestModelPointForOrbit](../DisplayOptions/DisplayOptions_UseNearestModelPointForOrbit.md) | Gets/sets whether to use the nearest model point to the mouse position as orbit pivot. |
| [UseRayTracingForRealisticDisplay](../DisplayOptions/DisplayOptions_UseRayTracingForRealisticDisplay.md) | Gets and sets whether to enable ray tracing in realistic visual styles for new windows. |
| [ViewTransitionTime](../DisplayOptions/DisplayOptions_ViewTransitionTime.md) | Gets/sets the time taken to transition between views of a model. |
| [ZoomToCursor](../DisplayOptions/DisplayOptions_ZoomToCursor.md) | Gets/sets whether the cursor position is the focus point for the zoom operation. |

## Accessed From

[Application.DisplayOptions](../Application/Application_DisplayOptions.md), [ApprenticeServer.DisplayOptions](../ApprenticeServer/ApprenticeServer_DisplayOptions.md), [ApprenticeServerComponent.DisplayOptions](../ApprenticeServerComponent/ApprenticeServerComponent_DisplayOptions.md), [InventorServer.DisplayOptions](InventorServer_DisplayOptions.md), [InventorServerObject.DisplayOptions](InventorServerObject_DisplayOptions.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |