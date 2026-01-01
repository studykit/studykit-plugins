# RenderEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEventArgs.h>

## Description

The RenderEventArgs provides information associated with the render process. Render events happen when there's a change in state of the rendering process. The most typical is when the rendering process has reached a predefined quality.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RenderEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [firingEvent](RenderEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](RenderEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RenderEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [viewport](RenderEventArgs_viewport.htm) | Returns the viewport that the rendering was performed in when the render is an in-canvas rendering. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |