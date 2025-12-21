# View Object

## Description

The View object represents a view in a document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../View/View_Activate.md) | Method that causes this view to become the active view (i.e. receive user-focus). |
| [Close](../View/View_Close.md) | Method that closes the view. If only one view exists for a document and the Close method is called it will also cause the Document to close. |
| [Fit](../View/View_Fit.md) | Method that fits all of the contents of the document within the view. Can optionally cause the display of the view to be updated. |
| [GetWindowExtents](../View/View_GetWindowExtents.md) | Method that returns the current size and position of the view's window. |
| [GoHome](../View/View_GoHome.md) | Method that sets the view to the default view of the model. |
| [Move](../View/View_Move.md) | Method that moves the window this view is contained within. |
| [ResetFront](../View/View_ResetFront.md) | Method that resets the front view to the factory default. |
| [SaveAsBitmap](../View/View_SaveAsBitmap.md) | Method that saves the view as a bitmap. |
| [SaveAsBitmapWithOptions](../View/View_SaveAsBitmapWithOptions.md) | Method that saves the view as a bitmap with more options. The width and height arguments define the aspect ratio and the number of pixels in the output image. The Options argument allow you to define more effects for the bitmap. |
| [SaveAsBitmapWithRayTracing](../View/View_SaveAsBitmapWithRayTracing.md) | Method that saves the view with ray tracing on as a bitmap in one of the following types: bmp, jpg, png, tiff, and gif. |
| [SetCurrentAsFront](../View/View_SetCurrentAsFront.md) | Method that sets the current view as the front view. |
| [SetCurrentAsHome](../View/View_SetCurrentAsHome.md) | Method that sets the current view as the home view. |
| [SetCurrentAsTop](../View/View_SetCurrentAsTop.md) | Method that sets the current view as the top view. |
| [StartRenderingRateRecord](../View/View_StartRenderingRateRecord.md) | Method that starts a rendering rate record for the graphics window. |
| [StopRenderingRateRecord](../View/View_StopRenderingRateRecord.md) | Method that stops the rendering rate record for the graphics window and gets the results. |
| [Update](../View/View_Update.md) | Method that causes the view to update. In some cases, changes made to a model or to the view will not immediately be shown in the view and the Update method must be called to cause the view to refresh. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../View/View_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AreTexturesOn](../View/View_AreTexturesOn.md) | Gets and sets whether to turn textures on. |
| [Camera](../View/View_Camera.md) | Property that returns a Camera object which contains the information that defines the current contents of the view. |
| [Caption](../View/View_Caption.md) | Gets/Sets the caption on this View's window. |
| [DisplayMode](../View/View_DisplayMode.md) | Gets/Sets the Display Mode on this View's window. |
| [DisplaySeparateColorsType](../View/View_DisplaySeparateColorsType.md) | Read-write property that gets and sets which type of display separate colors will be applied. |
| [Document](../View/View_Document.md) | Property that returns the  the view is associated with. |
| [Height](../View/View_Height.md) | Gets/Sets the Height of the view window. |
| [HWND](../View/View_HWND.md) | Property that returns the hWnd for the window. This provides convenient access to the window's hWnd. Having the hWnd allows you to use various Windows API calls with the window. |
| [IsRayTracingPaused](../View/View_IsRayTracingPaused.md) | Gets and sets whether the current ray tracing process is paused. If this property returns true then set it to false will continue the current ray tracing. |
| [Left](../View/View_Left.md) | Gets/Sets the distance between the left edge of the view window and left edge of the frame window. |
| [NoiseReductionEnabled](../View/View_NoiseReductionEnabled.md) | Read-write property that gets and sets whether the noise reduction is enabled or not when ray tracing is enabled. |
| [Parent](../View/View_Parent.md) | Property that returns the parent  object from whom this object can logically be reached. |
| [RayTracing](../View/View_RayTracing.md) | Gets and sets whether to enable ray tracing for the view. |
| [RayTracingProgress](../View/View_RayTracingProgress.md) | Gets the progress in percentage of the ray tracing process. |
| [RayTracingQuality](../View/View_RayTracingQuality.md) | Gets and sets the quality used when ray tracing is enabled. |
| [ShowAmbientShadows](../View/View_ShowAmbientShadows.md) | Gets and sets whether to display ambient shadows. |
| [ShowGroundPlane](../View/View_ShowGroundPlane.md) | Gets and sets whether to display the ground plane. |
| [ShowGroundReflections](../View/View_ShowGroundReflections.md) | Gets and sets whether to display ground reflections. |
| [ShowGroundShadows](../View/View_ShowGroundShadows.md) | Gets and sets whether to display ground shadows. |
| [ShowObjectShadows](../View/View_ShowObjectShadows.md) | Gets and sets whether to display object shadows. |
| [Top](../View/View_Top.md) | Gets/Sets the distance between the top of the view window and top of the frame window. |
| [Type](../View/View_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [ViewFrame](../View/View_ViewFrame.md) | Read-only property that returns the ViewFrame this view is located in. |
| [ViewTab](../View/View_ViewTab.md) | Read-only property that returns the ViewTab of this view. |
| [Visible](../View/View_Visible.md) | Gets/Sets the visibility of this View. |
| [Width](../View/View_Width.md) | Gets/Sets the Width of the view window. |
| [WindowState](../View/View_WindowState.md) | Gets/Sets this windows state. |

## Accessed From

[Application.ActiveView](../Application/Application_ActiveView.md), [ViewList.Item](../ViewList/ViewList_Item.md), [Views.Add](../Views/Views_Add.md), [Views.Item](../Views/Views_Item.md), [ViewsEnumerator.Item](../ViewsEnumerator/ViewsEnumerator_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drive the camera](../../sample-programs/DriveCamera_Sample.md) | This sample will fly the camera around the model. To simplify the code, the target is hard coded at the origin and the up vector is the positive Z. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |
| [Cancel a double click](../../sample-programs/UserInputEventsSink_OnDoubleClick_Sample.md) | Demonstrates how to receive (and in this case, cancel) a double click from a user. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |