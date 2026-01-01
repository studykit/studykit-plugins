# SaveImageFileOptions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/SaveImageFileOptions.h>

## Description

Class that defines the various options that can be used when saving a viewport as an image. This object is created by using the static create method on the class and is then used as input to the Viewport.saveAsImageFileWithOptions method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SaveImageFileOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](SaveImageFileOptions_create.htm) | Creates a new SaveImageFileOptions object. The returned object can be used to define the various options to use when saving a viewport as an image. The object is passed into the ViewPort.saveAsImageFileWithOptions method to create an image of the viewport. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](SaveImageFileOptions_filename.htm) | Gets and sets the full filename, including the path, of the image file. The type of image file to be created is inferred from the extension of the filename. |
| [height](SaveImageFileOptions_height.htm) | Gets and set the height of the image to be created in pixels. A value of zero is valid and indicates the current height of the viewport is to be used. When the SaveImageFileOptions object is initially created, this is initialized to 0. |
| [isAntiAliased](SaveImageFileOptions_isAntiAliased.htm) | Gets and sets if the rendered image should be anti-aliased or not. If false, there is no anti-aliasing. |
| [isBackgroundTransparent](SaveImageFileOptions_isBackgroundTransparent.htm) | Gets and sets if the background should be rendered as transparent. If false, the background will be the same as seen in Fusion.   When the SaveImageFileOptions object is initially created, this is initialized to false. |
| [isValid](SaveImageFileOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SaveImageFileOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [width](SaveImageFileOptions_width.htm) | Gets and set the width of the image to be created in pixels. A value of zero is valid and indicates the current width of the viewport is to be used. When the SaveImageFileOptions object is initially created, this is initialized to 0. |

## Accessed From

[SaveImageFileOptions.create](SaveImageFileOptions_create.htm)

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |