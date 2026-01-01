# Canvas Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Represents a Canvas within a component.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Canvas_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](Canvas_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](Canvas_deleteMe.htm) | Deletes the canvas from the component. |
| [flipHorizontal](Canvas_flipHorizontal.htm) | Flips the image along the horizontal axis. This is a convenience method that flips the direction of the X axis of the transform. |
| [flipVertical](Canvas_flipVertical.htm) | Flips the image along the vertical axis. This is a convenience method that flips the direction of the Y axis of the transform. |
| [saveImage](Canvas_saveImage.htm) | Saves the image associated with the canvas to the specified file. This is useful in cases where the original image file is no longer available but you need the image for some other purpose. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](Canvas_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [entityToken](Canvas_entityToken.htm) | Returns a token for the Canvas object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same canvas. |
| [imageFilename](Canvas_imageFilename.htm) | Gets and sets the filename of the image used for the canvas. When getting this property, the filename returned is the file that was used when the canvas was initially created. it's possible the file may no longer exist.   When setting this property, it is the full filename to the image to use for the canvas. PNG, JPEG, and TIFF files are supported. |
| [isDisplayedThrough](Canvas_isDisplayedThrough.htm) | Controls if the image is visible through the model or not. |
| [isLightBulbOn](Canvas_isLightBulbOn.htm) | Gets and sets if the light bulb of this canvas as displayed in the browser is on or off.   A canvas will only be visible if the light bulb is switched on. However, the light bulb can be on and the canvas still invisible if the visibility of a higher level occurrence has its light bulb off or if the light bulb for Canvases folder is off to turn off all canvases in a component. |
| [isRenderable](Canvas_isRenderable.htm) | Controls if the canvas will be rendered when ray tracing within the Render workspace. |
| [isSelectable](Canvas_isSelectable.htm) | Controls if the canvas is selectable or not within the graphics window. |
| [isValid](Canvas_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](Canvas_isVisible.htm) | Returns if the canvas is currently visible in the graphics window. The isLightBulbOn property of the canvas controls if the canvas should be displayed or not, but even when true, the canvas may not be visible because the occurrence that references the component may not be visible. It's also possible to turn off the visibility of all canvases for a component. This property takes all of that into account when reporting if the canvas is visible or not. |
| [name](Canvas_name.htm) | Gets and sets the name of the canvas. This is the name seen in the browser and timeline. |
| [nativeObject](Canvas_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](Canvas_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [opacity](Canvas_opacity.htm) | Gets and sets the opacity of the canvas where 0 is completely transparent and 100 is completely opaque. Setting this property to a value outside the range of 0-100 will result in the value being set to the closest valid value. |
| [planarEntity](Canvas_planarEntity.htm) | Gets and sets the plane the canvas is associated with. This can be either a planar Face or a construction plane. In a direct modeling design or the canvas is being created in a base feature, this can be a Plane object. |
| [plane](Canvas_plane.htm) | Returns a Plane object that represents the position and orientation of the canvas in model space. |
| [timelineObject](Canvas_timelineObject.htm) | Returns the timeline object associated with the creation of this canvas. |
| [transform](Canvas_transform.htm) | Gets and sets the transform of the canvas. This allows you to control the position, rotation, scaling, and flipping. The X and Y axes defined by the matrix and must be perpendicular to one another.   This is a 3x3 matrix where the third column controls the position of the canvas and defines the position using 2D coordinates in the model space. |

## Accessed From

[Canvas.createForAssemblyContext](Canvas_createForAssemblyContext.htm), [Canvas.nativeObject](Canvas_nativeObject.htm), [Canvases.add](Canvases_add.htm), [Canvases.item](Canvases_item.htm), [Canvases.itemByName](Canvases_itemByName.htm)

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |