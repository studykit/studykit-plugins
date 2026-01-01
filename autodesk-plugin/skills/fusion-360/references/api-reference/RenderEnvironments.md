# RenderEnvironments Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEnvironments.h>

## Description

The list of available render environments. This represents the list of environments shown in the "Scene Settings" dialog as being in the "Fusion Library". It does not include a custom environment, if one has been loaded.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RenderEnvironments_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](RenderEnvironments_item.htm) | Method that returns the specified render environment using an index into the collection. |
| [itemById](RenderEnvironments_itemById.htm) | Returns the render environment with the specified ID. |
| [itemByName](RenderEnvironments_itemByName.htm) | Returns the specified render environment using the name as seen in the user interface. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RenderEnvironments_count.htm) | The number of render environments in the collection. |
| [isValid](RenderEnvironments_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RenderEnvironments_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[RenderManager.renderEnvironments](RenderManager_renderEnvironments.htm)

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |