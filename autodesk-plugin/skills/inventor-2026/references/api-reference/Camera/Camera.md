# Camera Object

## Description

The Camera defines the view of the model shown within the window.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Apply](../Camera/Camera_Apply.md) | Method that causes the changes made to the Camera object to be applied to the actual camera of the view. This will also cause the view to update. |
| [ApplyWithoutTransition](../Camera/Camera_ApplyWithoutTransition.md) | Method that applies the current camera to the View without transition. |
| [ComputeWithMouseInput](../Camera/Camera_ComputeWithMouseInput.md) | Method that changes the view according mouse movement and view operation. |
| [CreateImage](../Camera/Camera_CreateImage.md) | Creates an image based on the current camera view. |
| [CreateImageWithOptions](../Camera/Camera_CreateImageWithOptions.md) | Creates an image based on the current camera view with options. |
| [Fit](../Camera/Camera_Fit.md) | Method that fits all the contents of the Document into the view. |
| [GetExtents](../Camera/Camera_GetExtents.md) | Method that gets the current extents of the camera. The camera extents define the area within the model that is visible in the view. |
| [ModelToViewSpace](../Camera/Camera_ModelToViewSpace.md) | Method that converts a point in model space to the equivalent point on the view. |
| [SaveAsBitmap](../Camera/Camera_SaveAsBitmap.md) | Method that saves the current camera view to the specified file. The width and height arguments define the aspect ratio and the number of pixels in the output image.  The CreateImage method is similar to this but instead of writing the image to a file it creates it in memory, which is more efficient than writing and reading if from disk if you need to use the image immediately. |
| [SetExtents](../Camera/Camera_SetExtents.md) | Method that sets the current extents of the camera. The camera extents define the area within the model that is visible in the view. Setting the extents results in the camera zooming in or out. The Apply method of the camera must be called before any changes are shown in the view. |
| [ViewToModelSpace](../Camera/Camera_ViewToModelSpace.md) | Method that converts a point in view space to the equivalent point in the model. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Eye](../Camera/Camera_Eye.md) | Specifies the position of the observer's 'Eye' (View's center). |
| [ModelToViewTransformation](../Camera/Camera_ModelToViewTransformation.md) | Read-only property that returns the transformation matrix from model space to view space. |
| [Parent](../Camera/Camera_Parent.md) | Property that returns the parent object of the camera. |
| [Perspective](../Camera/Camera_Perspective.md) | Gets/Sets a boolean flag indicating whether Perpspective viewing is on/off. |
| [PerspectiveAngle](../Camera/Camera_PerspectiveAngle.md) | Gets/Sets the Perspective Angle. |
| [SceneObject](../Camera/Camera_SceneObject.md) | Get/Set the contents of the scene for a camera. This is applicable only when the Camera is created from the TransientObjects.CreateCamera. Valid objects that can be set to this property are: ComponentDefinition, Sheet, and PresentationScene. |
| [Target](../Camera/Camera_Target.md) | Specifies the position of the Target point the observer's viewing in the scene (View's Z-axis). |
| [Type](../Camera/Camera_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpVector](../Camera/Camera_UpVector.md) | Specifies the vector defining what is 'up' for the observer. |
| [ViewOrientationType](../Camera/Camera_ViewOrientationType.md) | Gets/Sets the type of orientation of the camera (Top, Iso, etc. or arbitrary). |

## Accessed From

[ClientView.Camera](../ClientView/ClientView_Camera.md), [DesignViewRepresentation.Camera](../DesignViewRepresentation/DesignViewRepresentation_Camera.md), [DetailDrawingView.Camera](../DetailDrawingView/DetailDrawingView_Camera.md), [DrawingView.Camera](../DrawingView/DrawingView_Camera.md), [PresentationSequence.Camera](PresentationSequence_Camera.md), [PresentationSnapshotView.SavedCamera](../PresentationSnapshotView/PresentationSnapshotView_SavedCamera.md), [Publication.InitialCamera](Publication_InitialCamera.md), [PublicationMarkedView.Camera](PublicationMarkedView_Camera.md), [SectionDrawingView.Camera](../SectionDrawingView/SectionDrawingView_Camera.md), [TransientObjects.CreateCamera](../TransientObjects/TransientObjects_CreateCamera.md), [View.Camera](../View/View_Camera.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drive the camera](../../sample-programs/DriveCamera_Sample.md) | This sample will fly the camera around the model. To simplify the code, the target is hard coded at the origin and the up vector is the positive Z. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4
